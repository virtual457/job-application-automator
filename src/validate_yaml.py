#!/usr/bin/env python3
r"""
YAML Resume Validator - Dynamic Constraints (Excludes ** from character count)
Validates current_application.yaml against constraints.yaml
Zero-tolerance error checking for production-ready resumes

Usage:
    python validate_yaml.py [path_to_yaml]
    
If no path provided, defaults to:
    D:\Git\virtual457-projects\job-application-automator\config\current_application.yaml
"""

import yaml
import sys
from pathlib import Path
from typing import Dict

# ANSI color codes
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

class YAMLValidator:
    def __init__(self, yaml_path: str, constraints_path: str = None):
        self.yaml_path = yaml_path
        
        # Auto-detect constraints.yaml path
        if constraints_path is None:
            yaml_file = Path(yaml_path)
            self.constraints_path = yaml_file.parent / 'constraints.yaml'
        else:
            self.constraints_path = Path(constraints_path)
        
        self.errors = []
        self.warnings = []
        self.passes = []
        self.data = None
        self.constraints = None
    
    @staticmethod
    def _strip_bold_markers(text: str) -> str:
        """Remove ** markers from text for character counting"""
        return text.replace('**', '')
    
    @staticmethod
    def _count_bold_markers(text: str) -> int:
        """Count number of bold markers (pairs of **)"""
        return text.count('**') // 2
        
    def load_files(self) -> bool:
        """Load both YAML and constraints files"""
        # Load main YAML
        try:
            with open(self.yaml_path, 'r', encoding='utf-8') as f:
                self.data = yaml.safe_load(f)
        except FileNotFoundError:
            print(f"{Colors.RED}ERROR: File not found: {self.yaml_path}{Colors.END}")
            return False
        except yaml.YAMLError as e:
            print(f"{Colors.RED}ERROR: Invalid YAML syntax: {e}{Colors.END}")
            return False
        
        # Load constraints
        try:
            with open(self.constraints_path, 'r', encoding='utf-8') as f:
                self.constraints = yaml.safe_load(f)
            print(f"{Colors.BLUE}✓ Constraints loaded from: {self.constraints_path}{Colors.END}")
        except FileNotFoundError:
            print(f"{Colors.YELLOW}⚠ Constraints file not found: {self.constraints_path}{Colors.END}")
            print(f"{Colors.YELLOW}  Using default hardcoded values{Colors.END}")
            self.constraints = self._get_default_constraints()
        except yaml.YAMLError as e:
            print(f"{Colors.RED}ERROR: Invalid constraints YAML: {e}{Colors.END}")
            return False
        
        return True
    
    def _get_default_constraints(self) -> dict:
        """Fallback default constraints if file not found"""
        return {
            'summary': {
                'min_chars': 450,
                'max_chars': 520,
                'min_bold': 5,
                'max_bold': 8
            },
            'skills': {
                'exact_categories': 7,
                'items_min_chars': 35,
                'items_max_chars': 95
            },
            'experience': {
                'companies': {
                    'London Stock Exchange Group (LSEG)': {
                        'exact_bullets': 5,
                        'bullet_min_chars': 150,
                        'bullet_max_chars': 250,
                        'bullet_min_bold': 3,
                        'bullet_max_bold': 5
                    },
                    'Infosys': {
                        'exact_bullets': 4,
                        'bullet_min_chars': 150,
                        'bullet_max_chars': 250,
                        'bullet_min_bold': 3,
                        'bullet_max_bold': 5
                    }
                }
            },
            'projects': {
                'exact_count': 3,
                'tech_max_chars': 80,
                'bullet_max_chars': 250,
                'bullet_min_bold': 3,
                'bullet_max_bold': 5
            }
        }
    
    def validate_summary(self) -> None:
        """Validate summary section"""
        print(f"\n{Colors.BOLD}1. SUMMARY VALIDATION:{Colors.END}")
        
        if 'summary' not in self.data:
            self.errors.append("Summary section missing")
            print(f"   {Colors.RED}✗ Summary section missing{Colors.END}")
            return
        
        summary = self.data['summary'].strip()
        
        # Count characters WITHOUT ** markers
        summary_text_only = self._strip_bold_markers(summary)
        summary_len = len(summary_text_only)
        summary_bold = self._count_bold_markers(summary)
        
        # Get constraints
        min_chars = self.constraints['summary']['min_chars']
        max_chars = self.constraints['summary']['max_chars']
        min_bold = self.constraints['summary']['min_bold']
        max_bold = self.constraints['summary']['max_bold']

        # Length check (excluding ** markers)
        print(f"   Length: {summary_len} chars (excluding ** markers) (Required: {min_chars}-{max_chars})")
        if min_chars <= summary_len <= max_chars:
            self.passes.append("Summary length")
            print(f"   {Colors.GREEN}✓ PASS{Colors.END}")
        else:
            self.errors.append(f"Summary length: {summary_len} chars (need {min_chars}-{max_chars})")
            print(f"   {Colors.RED}✗ FAIL{Colors.END}")
            if summary_len < min_chars:
                print(f"      → Need to ADD {min_chars - summary_len} characters")
            else:
                print(f"      → Need to REMOVE {summary_len - max_chars} characters")

        # Bold markers check
        print(f"   Bold markers: {summary_bold} (Required: {min_bold}-{max_bold})")
        if min_bold <= summary_bold <= max_bold:
            self.passes.append("Summary bold markers")
            print(f"   {Colors.GREEN}✓ PASS{Colors.END}")
        else:
            self.errors.append(f"Summary bold markers: {summary_bold} (need {min_bold}-{max_bold})")
            print(f"   {Colors.RED}✗ FAIL{Colors.END}")
            if summary_bold < min_bold:
                print(f"      → Need to ADD {min_bold - summary_bold} bold markers")
            else:
                print(f"      → Need to REMOVE {summary_bold - max_bold} bold markers")
        
        # Content checks
        if "3.89 GPA" not in summary:
            self.warnings.append("Summary should include 3.89 GPA")
        
        if "London Stock Exchange Group" not in summary and "LSEG" not in summary:
            self.warnings.append("Summary should mention LSEG")
    
    def validate_skills(self) -> None:
        """Validate skills section"""
        print(f"\n{Colors.BOLD}2. SKILLS VALIDATION:{Colors.END}")
        
        if 'skills' not in self.data:
            self.errors.append("Skills section missing")
            print(f"   {Colors.RED}✗ Skills section missing{Colors.END}")
            return
        
        skills = self.data['skills']
        
        # Get constraints
        exact_count = self.constraints['skills']['exact_categories']
        max_chars = self.constraints['skills'].get('items_max_chars', 999)
        
        # Count check
        print(f"   Categories: {len(skills)} (Required: exactly {exact_count})")
        if len(skills) == exact_count:
            self.passes.append("Skills count")
            print(f"   {Colors.GREEN}✓ PASS{Colors.END}")
        else:
            self.errors.append(f"Skills: {len(skills)} categories (need exactly {exact_count})")
            print(f"   {Colors.RED}✗ FAIL - Need exactly {exact_count} categories{Colors.END}")
        
        # Check each category
        for i, skill in enumerate(skills, 1):
            if 'category' not in skill or 'items' not in skill:
                self.errors.append(f"Skill {i}: Missing 'category' or 'items' field")
                print(f"   {Colors.RED}✗ Skill {i}: Missing required fields{Colors.END}")
                continue
            
            category = skill['category']
            items = skill['items']
            length = len(items)

            # Only check max (no minimum)
            if length <= max_chars:
                self.passes.append(f"Skill {i}")
                print(f"   {Colors.GREEN}✓ {i}. {category}: {length} chars PASS{Colors.END}")
            else:
                self.errors.append(f"Skill {i} '{category}': {length} chars (max {max_chars})")
                print(f"   {Colors.RED}✗ {i}. {category}: {length} chars FAIL{Colors.END}")
                print(f"      → Need to REMOVE {length - max_chars} characters")
    
    def validate_experience(self) -> None:
        """Validate work experience section"""
        print(f"\n{Colors.BOLD}3. EXPERIENCE VALIDATION:{Colors.END}")
        
        if 'experience' not in self.data:
            self.errors.append("Experience section missing")
            print(f"   {Colors.RED}✗ Experience section missing{Colors.END}")
            return
        
        experience = self.data['experience']
        
        # Validate LSEG
        if len(experience) >= 1:
            lseg = experience[0]
            lseg_constraints = self.constraints['experience']['companies']['London Stock Exchange Group (LSEG)']
            self._validate_company(lseg, "LSEG", lseg_constraints, "London Stock Exchange Group")
        else:
            self.errors.append("LSEG experience missing")
        
        # Validate Infosys
        if len(experience) >= 2:
            infosys = experience[1]
            infosys_constraints = self.constraints['experience']['companies']['Infosys']
            self._validate_company(infosys, "Infosys", infosys_constraints, "Infosys")
        else:
            self.errors.append("Infosys experience missing")
    
    def _validate_company(self, company_data: Dict, company_name: str, 
                          constraints: Dict, expected_company: str) -> None:
        """Validate individual company experience using dynamic constraints"""
        print(f"\n   {Colors.BOLD}{company_name}:{Colors.END}")
        
        # Get constraints
        required_bullets = constraints['exact_bullets']
        min_chars = constraints['bullet_min_chars']
        max_chars = constraints['bullet_max_chars']
        min_bold = constraints['bullet_min_bold']
        max_bold = constraints['bullet_max_bold']
        
        # Check company name
        actual_company = company_data.get('company', '')
        if expected_company not in actual_company:
            self.warnings.append(f"{company_name}: Company name mismatch")
        
        # Check bullets count
        bullets = company_data.get('bullets', [])
        print(f"   Bullets: {len(bullets)} (Required: {required_bullets})")
        
        if len(bullets) == required_bullets:
            self.passes.append(f"{company_name} bullet count")
            print(f"   {Colors.GREEN}✓ Bullet count PASS{Colors.END}")
        else:
            self.errors.append(f"{company_name}: {len(bullets)} bullets (need {required_bullets})")
            print(f"   {Colors.RED}✗ Bullet count FAIL{Colors.END}")
        
        # Validate each bullet
        for i, bullet in enumerate(bullets, 1):
            # Count WITHOUT ** markers
            bullet_text_only = self._strip_bold_markers(bullet)
            length = len(bullet_text_only)
            bold = self._count_bold_markers(bullet)

            length_ok = min_chars <= length <= max_chars
            bold_ok = min_bold <= bold <= max_bold

            if length_ok and bold_ok:
                self.passes.append(f"{company_name} B{i}")
                print(f"   {Colors.GREEN}✓ Bullet {i}: {length} chars (excl. **), {bold} bold PASS{Colors.END}")
            else:
                status = []
                if not length_ok:
                    status.append(f"{length} chars (need {min_chars}-{max_chars})")
                    self.errors.append(f"{company_name} B{i}: {length} chars (need {min_chars}-{max_chars})")
                if not bold_ok:
                    status.append(f"{bold} bold (need {min_bold}-{max_bold})")
                    self.errors.append(f"{company_name} B{i}: {bold} bold (need {min_bold}-{max_bold})")

                print(f"   {Colors.RED}✗ Bullet {i}: {', '.join(status)}{Colors.END}")

                if length < min_chars:
                    print(f"      → ADD {min_chars - length} chars")
                elif length > max_chars:
                    print(f"      → REMOVE {length - max_chars} chars")

                if bold < min_bold:
                    print(f"      → ADD {min_bold - bold} bold markers")
                elif bold > max_bold:
                    print(f"      → REMOVE {bold - max_bold} bold markers")
    
    def validate_projects(self) -> None:
        """Validate projects section"""
        print(f"\n{Colors.BOLD}4. PROJECTS VALIDATION:{Colors.END}")
        
        if 'projects' not in self.data:
            self.errors.append("Projects section missing")
            print(f"   {Colors.RED}✗ Projects section missing{Colors.END}")
            return
        
        projects = self.data['projects']
        
        # Get constraints
        exact_count = self.constraints['projects']['exact_count']
        tech_max = self.constraints['projects']['tech_max_chars']
        bullet_max = self.constraints['projects']['bullet_max_chars']
        min_bold = self.constraints['projects']['bullet_min_bold']
        max_bold = self.constraints['projects']['bullet_max_bold']
        
        # Count check
        print(f"   Count: {len(projects)} (Required: exactly {exact_count})")
        if len(projects) == exact_count:
            self.passes.append("Project count")
            print(f"   {Colors.GREEN}✓ PASS{Colors.END}")
        else:
            self.errors.append(f"Projects: {len(projects)} projects (need exactly {exact_count})")
            print(f"   {Colors.RED}✗ FAIL - Need exactly {exact_count} projects{Colors.END}")
        
        # Validate each project
        for i, proj in enumerate(projects, 1):
            print(f"\n   {Colors.BOLD}Project {i}: {proj.get('title', 'MISSING TITLE')}{Colors.END}")
            
            # Check required fields
            required_fields = ['title', 'tech', 'github', 'bullet1', 'bullet2']
            for field in required_fields:
                if field not in proj:
                    self.errors.append(f"Project {i}: Missing '{field}' field")
                    print(f"   {Colors.RED}✗ Missing field: {field}{Colors.END}")
            
            # Validate tech line
            if 'tech' in proj:
                tech_len = len(proj['tech'])
                print(f"   Tech line: {tech_len} chars (Max: {tech_max})")
                if tech_len <= tech_max:
                    self.passes.append(f"Project {i} tech")
                    print(f"   {Colors.GREEN}✓ PASS{Colors.END}")
                else:
                    self.errors.append(f"Project {i} tech: {tech_len} chars (max {tech_max})")
                    print(f"   {Colors.RED}✗ FAIL - Remove {tech_len - tech_max} chars{Colors.END}")
            
            # Validate GitHub link
            if 'github' in proj:
                github = proj['github']
                if github != "GitHub" and not github.startswith('https://github.com/virtual457/'):
                    self.warnings.append(f"Project {i}: GitHub link may be incorrect")
                    print(f"   {Colors.YELLOW}⚠ Warning: GitHub should be 'GitHub' or URL{Colors.END}")
            
            # Validate bullet1
            if 'bullet1' in proj:
                b1 = proj['bullet1']
                b1_text_only = self._strip_bold_markers(b1)
                b1_len = len(b1_text_only)
                b1_bold = self._count_bold_markers(b1)

                len_ok = b1_len <= bullet_max
                bold_ok = min_bold <= b1_bold <= max_bold

                if len_ok and bold_ok:
                    self.passes.append(f"Project {i} bullet1")
                    print(f"   {Colors.GREEN}✓ Bullet 1: {b1_len} chars (excl. **), {b1_bold} bold PASS{Colors.END}")
                else:
                    if not len_ok:
                        self.errors.append(f"Project {i} bullet1: {b1_len} chars (max {bullet_max})")
                        print(f"   {Colors.RED}✗ Bullet 1: {b1_len} chars OVER - Remove {b1_len - bullet_max} chars{Colors.END}")
                    if not bold_ok:
                        self.errors.append(f"Project {i} bullet1: {b1_bold} bold (need {min_bold}-{max_bold})")
                        print(f"   {Colors.RED}✗ Bullet 1: {b1_bold} bold markers (need {min_bold}-{max_bold}){Colors.END}")

            # Validate bullet2
            if 'bullet2' in proj:
                b2 = proj['bullet2']
                b2_text_only = self._strip_bold_markers(b2)
                b2_len = len(b2_text_only)
                b2_bold = self._count_bold_markers(b2)

                len_ok = b2_len <= bullet_max
                bold_ok = min_bold <= b2_bold <= max_bold

                if len_ok and bold_ok:
                    self.passes.append(f"Project {i} bullet2")
                    print(f"   {Colors.GREEN}✓ Bullet 2: {b2_len} chars (excl. **), {b2_bold} bold PASS{Colors.END}")
                else:
                    if not len_ok:
                        self.errors.append(f"Project {i} bullet2: {b2_len} chars (max {bullet_max})")
                        print(f"   {Colors.RED}✗ Bullet 2: {b2_len} chars OVER - Remove {b2_len - bullet_max} chars{Colors.END}")
                    if not bold_ok:
                        self.errors.append(f"Project {i} bullet2: {b2_bold} bold (need {min_bold}-{max_bold})")
                        print(f"   {Colors.RED}✗ Bullet 2: {b2_bold} bold markers (need {min_bold}-{max_bold}){Colors.END}")
    
    def validate(self) -> bool:
        """Run all validations"""
        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")
        print(f"{Colors.BOLD}YAML RESUME VALIDATION (Excludes ** from Character Count){Colors.END}")
        print(f"{Colors.BOLD}{'=' * 80}{Colors.END}")
        print(f"\nResume: {self.yaml_path}")
        print(f"Constraints: {self.constraints_path}")
        
        if not self.load_files():
            return False
        
        # Run all validation checks
        self.validate_summary()
        self.validate_skills()
        self.validate_experience()
        self.validate_projects()
        
        # Print final report
        self._print_report()
        
        return len(self.errors) == 0
    
    def _print_report(self) -> None:
        """Print final validation report"""
        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")
        print(f"{Colors.BOLD}VALIDATION SUMMARY{Colors.END}")
        print(f"{Colors.BOLD}{'=' * 80}{Colors.END}")
        
        print(f"\n{Colors.GREEN}Passed: {len(self.passes)} checks{Colors.END}")
        
        if self.warnings:
            print(f"{Colors.YELLOW}Warnings: {len(self.warnings)}{Colors.END}")
            for w in self.warnings:
                print(f"  {Colors.YELLOW}⚠ {w}{Colors.END}")
        
        if self.errors:
            print(f"\n{Colors.RED}{Colors.BOLD}Errors: {len(self.errors)}{Colors.END}")
            for i, e in enumerate(self.errors, 1):
                print(f"  {Colors.RED}{i}. {e}{Colors.END}")
            
            print(f"\n{Colors.RED}{Colors.BOLD}❌ VALIDATION FAILED - DO NOT GENERATE ❌{Colors.END}")
            print(f"\n{Colors.YELLOW}Fix all errors above before generating{Colors.END}")
        else:
            print(f"\n{Colors.GREEN}{Colors.BOLD}✅ ZERO ERRORS - PRODUCTION READY ✅{Colors.END}")
            print(f"\n{Colors.BOLD}Ready to generate!{Colors.END}")
        
        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")

def main():
    # Default path
    default_path = r"D:\Git\virtual457-projects\job-application-automator\config\current_application.yaml"
    
    # Use provided path or default
    yaml_path = sys.argv[1] if len(sys.argv) > 1 else default_path
    
    # Run validation
    validator = YAMLValidator(yaml_path)
    success = validator.validate()
    
    # Exit with appropriate code (main.py reads this!)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
