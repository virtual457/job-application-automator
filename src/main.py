#!/usr/bin/env python3
"""
Master Resume Generation & Validation Pipeline

Orchestrates the complete workflow (auto-generates YAML from JD by default):
0. Generate YAML from JD (auto-detects company from JD)
1. Validate YAML constraints (with auto-revision if validation fails)
2. Generate DOCX + PDF resume
3. Run quality checker (PDF visual analysis)
4. Run ATS checker (PDF compatibility + keyword matching)

Usage:
    python main.py                          # Full pipeline (uses config/current_jd.txt)
    python main.py --jd-file path.txt       # Custom JD file
    python main.py --company "Google"       # Override company detection
    python main.py --skip-quality --skip-ats  # Quick generation only
    python main.py --skip-yaml-generation   # Use existing YAML (skip auto-gen)
"""

import sys
import subprocess
from pathlib import Path
import argparse
import time
import os

# Import YAML generator and reviser
try:
    from generator import YAMLGenerator
except ImportError:
    YAMLGenerator = None

try:
    from reviser import YAMLReviser
except ImportError:
    YAMLReviser = None

# ANSI colors
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

def close_all_word_applications():
    """Close all Microsoft Word instances (Windows only)"""
    if os.name != 'nt':
        return
    try:
        subprocess.run(['taskkill', '/F', '/IM', 'WINWORD.EXE'],
                      capture_output=True, check=False)
    except Exception:
        pass

class ResumePipeline:
    def __init__(self, jd_file=None, company=None, skip_yaml_generation=False,
                 skip_validation=False, skip_generation=False, skip_quality=False, skip_ats=False,
                 max_revision_attempts=5):
        self.script_dir = Path(__file__).parent.resolve()
        self.project_root = self.script_dir.parent

        self.jd_file = jd_file
        self.company = company
        self.skip_yaml_generation = skip_yaml_generation
        self.max_revision_attempts = max_revision_attempts

        self.skip_validation = skip_validation
        self.skip_generation = skip_generation
        self.skip_quality = skip_quality
        self.skip_ats = skip_ats

        self.yaml_generation_passed = False
        self.validation_passed = False
        self.generation_passed = False
        self.quality_passed = False
        self.ats_passed = False
        self.revision_count = 0
        self.validation_errors = []

    def print_header(self, text):
        """Print section header"""
        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")
        print(f"{Colors.BOLD}{text}{Colors.END}")
        print(f"{Colors.BOLD}{'=' * 80}{Colors.END}\n")

    def run_command(self, command, description):
        """Run a command and return success status"""
        print(f"{Colors.BLUE}Running: {description}...{Colors.END}\n")
        
        try:
            result = subprocess.run(
                command,
                cwd=str(self.script_dir),
                capture_output=False,
                text=True,
                check=False
            )
            
            if result.returncode == 0:
                print(f"\n{Colors.GREEN}✓ {description} completed successfully{Colors.END}")
                return True
            else:
                print(f"\n{Colors.RED}✗ {description} failed with exit code {result.returncode}{Colors.END}")
                return False
                
        except Exception as e:
            print(f"\n{Colors.RED}✗ Error running {description}: {e}{Colors.END}")
            return False

    def step_0_generate_yaml(self):
        """Step 0: Auto-generate YAML from JD (default behavior)"""
        if self.skip_yaml_generation:
            print(f"{Colors.YELLOW}⚠ Skipping YAML generation (--skip-yaml-generation flag){Colors.END}")
            print(f"{Colors.YELLOW}Using existing config/current_application.yaml{Colors.END}")
            self.yaml_generation_passed = True
            return True

        if YAMLGenerator is None:
            print(f"{Colors.RED}ERROR: generator.py not found!{Colors.END}")
            print(f"{Colors.YELLOW}Cannot auto-generate YAML. Please create YAML manually.{Colors.END}")
            return False

        self.print_header("STEP 0: YAML AUTO-GENERATION (from Job Description)")

        try:
            # Initialize generator
            generator = YAMLGenerator(company_name=self.company)

            # Determine JD file path
            jd_path = self.jd_file
            if not jd_path:
                # Default to config/current_jd.txt
                default_jd = self.project_root / 'config' / 'current_jd.txt'
                if default_jd.exists():
                    print(f"{Colors.BLUE}Using default JD file: {default_jd}{Colors.END}")
                    jd_path = str(default_jd)

            # Run generation with auto-save (no prompts in automated pipeline)
            success = generator.run(jd_file=jd_path, auto_save=True)

            if success:
                self.yaml_generation_passed = True
                print(f"\n{Colors.GREEN}✓ YAML generation completed successfully{Colors.END}")
                print(f"{Colors.GREEN}✓ Output: config/current_application.yaml{Colors.END}")
                return True
            else:
                print(f"\n{Colors.RED}✗ YAML generation failed{Colors.END}")
                return False

        except Exception as e:
            print(f"\n{Colors.RED}✗ Error during YAML generation: {e}{Colors.END}")
            return False

    def step_1_validate_yaml_with_restart(self):
        """Step 1: Validate YAML with revision, returns (success, needs_restart)"""
        if self.skip_validation:
            print(f"{Colors.YELLOW}⚠ Skipping YAML validation (--skip-validation flag){Colors.END}")
            self.validation_passed = True
            return (True, False)

        self.print_header("STEP 1: YAML CONSTRAINT VALIDATION")

        # Run validation
        result = subprocess.run(
            [sys.executable, "validate_yaml.py"],
            cwd=str(self.project_root),
            capture_output=True,
            text=True,
            check=False
        )

        self.validation_passed = (result.returncode == 0)

        if self.validation_passed:
            print(f"\n{Colors.GREEN}✓ YAML Validation completed successfully{Colors.END}")
            return (True, False)

        # Validation failed - print errors
        print(f"\n{Colors.RED}{Colors.BOLD}❌ VALIDATION ERRORS:{Colors.END}")
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)

        # Try auto-revision (single attempt, then restart pipeline)
        print(f"\n{Colors.YELLOW}⚠ Attempting auto-revision...{Colors.END}")
        validation_feedback = result.stdout if result.stdout else "Validation failed"
        if self.step_1a_revise_yaml(validation_feedback):
            self.revision_count += 1
            print(f"\n{Colors.GREEN}✓ YAML revised - restarting pipeline from validation{Colors.END}")
            return (True, True)  # Success with restart
        else:
            print(f"\n{Colors.RED}❌ Auto-revision failed{Colors.END}")
            return (False, False)  # Failed

    def step_1_validate_yaml(self):
        """Step 1: Validate YAML constraints with auto-revision loop"""
        if self.skip_validation:
            print(f"{Colors.YELLOW}⚠ Skipping YAML validation (--skip-validation flag){Colors.END}")
            self.validation_passed = True
            return True

        self.print_header("STEP 1: YAML CONSTRAINT VALIDATION")

        # Validation loop with auto-revision
        for attempt in range(self.max_revision_attempts + 1):
            if attempt > 0:
                print(f"\n{Colors.BLUE}Revision attempt {attempt}/{self.max_revision_attempts}{Colors.END}")

            # Run validation and capture output
            result = subprocess.run(
                [sys.executable, "validate_yaml.py"],
                cwd=str(self.project_root),
                capture_output=True,
                text=True,
                check=False
            )

            self.validation_passed = (result.returncode == 0)

            if self.validation_passed:
                print(f"\n{Colors.GREEN}✓ YAML Validation completed successfully{Colors.END}")
                return True

            # Validation failed - print ALL output for user to see
            print(f"\n{Colors.RED}{Colors.BOLD}❌ VALIDATION ERRORS:{Colors.END}")
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(result.stderr)

            # If max attempts reached, fail
            if attempt >= self.max_revision_attempts:
                print(f"\n{Colors.RED}{Colors.BOLD}❌ VALIDATION FAILED after {self.max_revision_attempts} revision attempts{Colors.END}")
                print(f"{Colors.YELLOW}Please fix errors manually in config/current_application.yaml{Colors.END}")
                return False

            # Try to auto-revise (pass captured output as feedback)
            print(f"\n{Colors.YELLOW}⚠ Attempting auto-revision using AI...{Colors.END}")
            validation_feedback = result.stdout if result.stdout else "Validation failed"
            if not self.step_1a_revise_yaml(validation_feedback):
                print(f"\n{Colors.RED}❌ Auto-revision failed{Colors.END}")
                return False

            self.revision_count += 1

        return False

    def step_1a_revise_yaml(self, validation_errors):
        """Step 1a: Auto-revise YAML based on validation errors using AI"""
        if YAMLReviser is None:
            print(f"{Colors.RED}ERROR: reviser.py not found!{Colors.END}")
            return False

        try:
            print(f"{Colors.BLUE}Initializing YAML Reviser...{Colors.END}")
            reviser = YAMLReviser(use_profile=True)

            print(f"{Colors.BLUE}Loading files (profile, constraints, current YAML)...{Colors.END}")
            if not reviser.load_files():
                print(f"{Colors.RED}Failed to load files for revision{Colors.END}")
                return False

            print(f"{Colors.BLUE}Sending to AI for revision...{Colors.END}")
            revised_yaml = reviser.revise_yaml(validation_errors)

            if not revised_yaml:
                print(f"{Colors.RED}AI reviser returned empty result{Colors.END}")
                return False

            # Save directly without prompting (automated pipeline)
            print(f"{Colors.BLUE}Saving revised YAML automatically...{Colors.END}")
            yaml_path = self.project_root / 'config' / 'current_application.yaml'

            import yaml
            # Validate YAML syntax first
            try:
                yaml.safe_load(revised_yaml)
            except yaml.YAMLError as e:
                print(f"{Colors.RED}Generated YAML has syntax errors: {e}{Colors.END}")
                return False

            # Save to file
            with open(yaml_path, 'w', encoding='utf-8') as f:
                f.write(revised_yaml)

            print(f"{Colors.GREEN}✓ Revised YAML saved to: {yaml_path}{Colors.END}")
            return True

        except Exception as e:
            print(f"{Colors.RED}Error during auto-revision: {e}{Colors.END}")
            return False

    def step_2_generate_resume(self):
        """Step 2: Generate DOCX resume"""
        if self.skip_generation:
            print(f"{Colors.YELLOW}⚠ Skipping resume generation (--skip-generation flag){Colors.END}")
            self.generation_passed = True
            return True

        self.print_header("STEP 2: RESUME GENERATION")

        # Run from src/ directory (where simple_generator.py is)
        # But simple_generator.py uses relative paths from project root
        generator_path = self.script_dir / "simple_generator.py"
        result = subprocess.run(
            [sys.executable, str(generator_path)],
            cwd=str(self.project_root),  # Run from project root, not src/
            capture_output=False,
            text=True,
            check=False
        )

        self.generation_passed = (result.returncode == 0)

        if self.generation_passed:
            print(f"\n{Colors.GREEN}✓ Resume Generation completed successfully{Colors.END}")
            # Wait for Word to fully open and finish saving files
            print(f"\n{Colors.BLUE}Waiting 10 seconds for Word to complete operations...{Colors.END}")
            time.sleep(10)
            print(f"{Colors.GREEN}✓ Wait complete{Colors.END}")
        else:
            print(f"\n{Colors.RED}✗ Resume Generation failed with exit code {result.returncode}{Colors.END}")

        if not self.generation_passed:
            print(f"\n{Colors.RED}{Colors.BOLD}❌ GENERATION FAILED{Colors.END}")
            print(f"{Colors.YELLOW}Check simple_generator.py output for errors{Colors.END}")
            return False

        return True

    def step_3_quality_check_with_restart(self):
        """Step 3: Quality check with restart on revision, returns (success, needs_restart)"""
        if self.skip_quality:
            print(f"{Colors.YELLOW}⚠ Skipping quality check (--skip-quality flag){Colors.END}")
            self.quality_passed = True
            return (True, False)

        self.print_header("STEP 3: QUALITY CHECK (PDF Visual Analysis)")

        # Close Word and wait
        print(f"{Colors.BLUE}Closing Word instances...{Colors.END}")
        close_all_word_applications()
        time.sleep(2)
        print(f"{Colors.GREEN}✓ Word cleanup complete{Colors.END}\n")

        # Check if PDF checker exists
        pdf_checker = self.script_dir / "quality_checker_pdf.py"
        text_checker = self.script_dir / "quality_checker.py"

        if pdf_checker.exists():
            checker = "quality_checker_pdf.py"
        elif text_checker.exists():
            checker = "quality_checker.py"
        else:
            print(f"{Colors.RED}No quality checker found!{Colors.END}")
            return (False, False)

        # Run quality checker
        result = subprocess.run(
            [sys.executable, checker],
            cwd=str(self.script_dir),
            capture_output=True,
            text=True,
            check=False
        )

        # Print output and errors
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(f"\n{Colors.RED}Quality checker errors:{Colors.END}")
            print(result.stderr)

        # Check if quality checker failed
        if result.returncode != 0:
            print(f"\n{Colors.RED}✗ Quality checker failed with exit code {result.returncode}{Colors.END}")
            self.quality_passed = False
            return (True, False)  # Non-blocking, continue

        # Parse score
        score = self._parse_quality_score(result.stdout)
        quality_threshold = 9.5  # 95%

        if score >= quality_threshold:
            print(f"\n{Colors.GREEN}✓ Quality score {score}/10 meets threshold ({quality_threshold}/10){Colors.END}")
            self.quality_passed = True
            return (True, False)

        print(f"\n{Colors.YELLOW}⚠ Quality score {score}/10 below threshold ({quality_threshold}/10){Colors.END}")

        # Try auto-revision
        print(f"\n{Colors.YELLOW}⚠ Attempting quality-based revision...{Colors.END}")
        if self.step_1a_revise_yaml(result.stdout):
            self.revision_count += 1
            print(f"\n{Colors.GREEN}✓ YAML revised - restarting pipeline from validation{Colors.END}")
            return (True, True)  # Success with restart
        else:
            print(f"\n{Colors.YELLOW}⚠ Quality revision failed, continuing anyway{Colors.END}")
            self.quality_passed = False
            return (True, False)  # Non-blocking

    def step_3_quality_check(self):
        """Step 3: Quality check with PDF visual analysis and auto-revision loop"""
        if self.skip_quality:
            print(f"{Colors.YELLOW}⚠ Skipping quality check (--skip-quality flag){Colors.END}")
            self.quality_passed = True
            return True

        self.print_header("STEP 3: QUALITY CHECK (PDF Visual Analysis)")

        # Check if PDF checker exists
        pdf_checker = self.script_dir / "quality_checker_pdf.py"
        text_checker = self.script_dir / "quality_checker.py"

        if pdf_checker.exists():
            checker = "quality_checker_pdf.py"
        elif text_checker.exists():
            checker = "quality_checker.py"
        else:
            print(f"{Colors.RED}No quality checker found!{Colors.END}")
            return False

        # Quality check loop with auto-revision
        quality_attempts = 0
        max_quality_attempts = 3
        quality_threshold = 9.5  # 95% score threshold

        while quality_attempts < max_quality_attempts:
            if quality_attempts > 0:
                print(f"\n{Colors.BLUE}Quality improvement attempt {quality_attempts}/{max_quality_attempts}{Colors.END}")

            # Close Word and wait
            print(f"{Colors.BLUE}Closing Word instances...{Colors.END}")
            close_all_word_applications()
            time.sleep(2)
            print(f"{Colors.GREEN}✓ Word cleanup complete{Colors.END}\n")

            # Run quality checker and capture output
            result = subprocess.run(
                [sys.executable, checker],
                cwd=str(self.script_dir),
                capture_output=True,
                text=True,
                check=False
            )

            # Print quality check output
            print(result.stdout)

            # Parse score from output (look for "OVERALL CONTENT SCORE: X/10")
            score = self._parse_quality_score(result.stdout)

            if score >= quality_threshold:
                print(f"\n{Colors.GREEN}✓ Quality score {score}/10 meets threshold ({quality_threshold}/10){Colors.END}")
                self.quality_passed = True
                return True

            print(f"\n{Colors.YELLOW}⚠ Quality score {score}/10 below threshold ({quality_threshold}/10){Colors.END}")

            if quality_attempts >= max_quality_attempts - 1:
                print(f"\n{Colors.YELLOW}⚠ Max quality improvement attempts reached{Colors.END}")
                self.quality_passed = False
                return True  # Non-blocking

            # Extract improvements and revise
            print(f"\n{Colors.YELLOW}⚠ Attempting quality-based revision...{Colors.END}")
            if not self.step_1a_revise_yaml(result.stdout):
                print(f"\n{Colors.YELLOW}⚠ Quality revision failed, continuing anyway{Colors.END}")
                self.quality_passed = False
                return True  # Non-blocking

            # Regenerate resume
            print(f"\n{Colors.BLUE}Regenerating resume after quality revision...{Colors.END}")
            if not self.step_2_generate_resume():
                print(f"\n{Colors.RED}Failed to regenerate resume{Colors.END}")
                return False

            quality_attempts += 1

        self.quality_passed = False
        return True  # Non-blocking

    def _parse_quality_score(self, output: str) -> float:
        """Parse quality score from checker output"""
        try:
            # Look for "OVERALL CONTENT SCORE: X/10"
            import re
            match = re.search(r'OVERALL CONTENT SCORE:\s*(\d+(?:\.\d+)?)/10', output)
            if match:
                return float(match.group(1))
            return 0.0
        except Exception:
            return 0.0

    def step_4_ats_check(self):
        """Step 4: ATS check with keyword matching"""
        if self.skip_ats:
            print(f"{Colors.YELLOW}⚠ Skipping ATS check (--skip-ats flag){Colors.END}")
            self.ats_passed = True
            return True

        self.print_header("STEP 4: ATS CHECK (Keyword Matching + Visual Compatibility)")

        # Close all Word instances and wait for cleanup
        print(f"{Colors.BLUE}Closing Word instances...{Colors.END}")
        close_all_word_applications()
        time.sleep(2)  # Wait 2 seconds for Word to fully close
        print(f"{Colors.GREEN}✓ Word cleanup complete{Colors.END}\n")

        # Check if PDF checker exists
        pdf_checker = self.script_dir / "ats_checker_pdf.py"
        text_checker = self.script_dir / "ats_checker.py"
        
        if pdf_checker.exists():
            print(f"{Colors.BLUE}Using PDF visual compatibility checker{Colors.END}")
            checker = "ats_checker_pdf.py"
        elif text_checker.exists():
            print(f"{Colors.YELLOW}PDF checker not found, using text-only checker{Colors.END}")
            checker = "ats_checker.py"
        else:
            print(f"{Colors.RED}No ATS checker found!{Colors.END}")
            return False
        
        self.ats_passed = self.run_command(
            [sys.executable, checker],
            "ATS Check"
        )
        
        # ATS check is informational, don't fail pipeline
        if not self.ats_passed:
            print(f"\n{Colors.YELLOW}⚠ ATS check encountered issues (non-blocking){Colors.END}")
        
        return True

    def print_final_summary(self):
        """Print final pipeline summary"""
        self.print_header("PIPELINE SUMMARY")

        print(f"Step 0 - YAML Generation:    {self._status(self.yaml_generation_passed, not self.skip_yaml_generation)}")
        print(f"Step 1 - YAML Validation:    {self._status(self.validation_passed, not self.skip_validation)}")
        print(f"Step 2 - Resume Generation:  {self._status(self.generation_passed, not self.skip_generation)}")
        print(f"Step 3 - Quality Check:      {self._status(self.quality_passed, not self.skip_quality)}")
        print(f"Step 4 - ATS Check:          {self._status(self.ats_passed, not self.skip_ats)}")

        # Show revision count if any revisions were made
        if self.revision_count > 0:
            print(f"\n{Colors.BLUE}Auto-Revisions: {self.revision_count} attempt(s){Colors.END}")

        # Overall status (check validation & generation, yaml gen is optional)
        all_passed = self.validation_passed and self.generation_passed
        
        if all_passed:
            print(f"\n{Colors.GREEN}{Colors.BOLD}✅ PIPELINE COMPLETED SUCCESSFULLY{Colors.END}")
            print(f"\n{Colors.BOLD}Generated Resume:{Colors.END}")
            print(f"  DOCX: {self.project_root / 'output' / 'Generated_Resume.docx'}")
            print(f"  PDF:  {self.project_root / 'output' / 'Generated_Resume.pdf'}")
            print(f"\n{Colors.GREEN}✓ Ready to apply!{Colors.END}")
        else:
            print(f"\n{Colors.RED}{Colors.BOLD}❌ PIPELINE FAILED{Colors.END}")
            print(f"{Colors.YELLOW}Fix errors above and re-run{Colors.END}")
        
        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}\n")
        
        return all_passed

    def _status(self, passed, ran):
        """Return colored status string"""
        if not ran:
            return f"{Colors.YELLOW}⊘ SKIPPED{Colors.END}"
        elif passed:
            return f"{Colors.GREEN}✓ PASSED{Colors.END}"
        else:
            return f"{Colors.RED}✗ FAILED{Colors.END}"

    def run(self):
        """Run the complete pipeline with full restart loop"""
        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")
        print(f"{Colors.BOLD}RESUME GENERATION & VALIDATION PIPELINE{Colors.END}")
        print(f"{Colors.BOLD}{'=' * 80}{Colors.END}")

        # Step 0: Generate YAML (runs once at start)
        if not self.step_0_generate_yaml():
            self.print_final_summary()
            return False

        # Main pipeline loop - restarts from validation after ANY revision
        # No global limit - each step has its own retry limit
        pipeline_restart_count = 0

        while True:
            if pipeline_restart_count > 0:
                print(f"\n{Colors.BOLD}{Colors.BLUE}{'=' * 80}{Colors.END}")
                print(f"{Colors.BOLD}{Colors.BLUE}PIPELINE RESTART #{pipeline_restart_count} (after revision){Colors.END}")
                print(f"{Colors.BOLD}{Colors.BLUE}{'=' * 80}{Colors.END}\n")

            # Step 1: Validate YAML (max 5 retries per validation failure)
            validation_result, needs_restart = self.step_1_validate_yaml_with_restart()
            if not validation_result:
                self.print_final_summary()
                return False
            if needs_restart:
                pipeline_restart_count += 1
                continue

            # Step 2: Generate Resume
            if not self.step_2_generate_resume():
                self.print_final_summary()
                return False

            # Step 3: Quality Check (max 3 retries per quality issue)
            quality_result, needs_restart = self.step_3_quality_check_with_restart()
            if needs_restart:
                pipeline_restart_count += 1
                continue

            # Step 4: ATS Check (non-blocking for now)
            self.step_4_ats_check()

            # All checks passed, exit loop
            break

        # Final Summary
        return self.print_final_summary()


def main():
    parser = argparse.ArgumentParser(
        description='Master resume generation and validation pipeline (auto-generates YAML from JD by default)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Default: Auto-generate everything from JD
  python main.py                                      # Uses config/current_jd.txt
  python main.py --jd-file path/to/jd.txt             # Custom JD file
  python main.py --company "Google"                   # Override company detection

  # Quick generation (skip checkers)
  python main.py --skip-quality --skip-ats            # Faster, no analysis

  # Use existing YAML (skip auto-generation)
  python main.py --skip-yaml-generation               # Use manual YAML

  # Skip other steps
  python main.py --skip-validation                    # Skip YAML validation
  python main.py --skip-generation                    # Use existing DOCX
        """
    )

    # Generation options
    parser.add_argument('--jd-file', type=str,
                       help='Job description file path (default: config/current_jd.txt)')
    parser.add_argument('--company', type=str,
                       help='Company name (auto-detected from JD if not provided)')

    # Skip options
    parser.add_argument('--skip-yaml-generation', action='store_true',
                       help='Skip YAML generation (use existing config/current_application.yaml)')
    parser.add_argument('--skip-validation', action='store_true',
                       help='Skip YAML validation step')
    parser.add_argument('--skip-generation', action='store_true',
                       help='Skip resume generation step')
    parser.add_argument('--skip-quality', action='store_true',
                       help='Skip quality check step')
    parser.add_argument('--skip-ats', action='store_true',
                       help='Skip ATS check step')

    args = parser.parse_args()

    # Run pipeline
    pipeline = ResumePipeline(
        jd_file=args.jd_file,
        company=args.company,
        skip_yaml_generation=args.skip_yaml_generation,
        skip_validation=args.skip_validation,
        skip_generation=args.skip_generation,
        skip_quality=args.skip_quality,
        skip_ats=args.skip_ats
    )

    success = pipeline.run()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
