#!/usr/bin/env python3
"""
YAML Resume Generator
Generates complete resume YAML from job description

Inputs:
- Job Description (interactive, file, or command line)
- Constraints (config/constraints.yaml)
- User Profile (docs/user_profile/CHANDAN_PROFILE_MASTER.md)
- Generation Guide (docs/LLM_GUIDE_YAML_CREATION_v3.md)

Outputs:
- Complete current_application.yaml ready to validate and generate

Usage:
    python generator.py                                    # Interactive mode (auto-detects company)
    python generator.py --jd-file job_description.txt      # From file (auto-detects company)
    python generator.py --jd "Job description text..."     # Direct text (auto-detects company)
    python generator.py --company "ServiceNow"             # Override auto-detected company name
"""

import os
import sys
import yaml
import argparse
import google.generativeai as genai
from pathlib import Path

# ANSI colors
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

class YAMLGenerator:
    def __init__(self, company_name: str = None):
        self.script_dir = Path(__file__).parent.resolve()
        self.project_root = self.script_dir.parent
        
        self.output_path = self.project_root / 'config' / 'current_application.yaml'
        self.jd_output_path = self.project_root / 'config' / 'current_jd.txt'
        self.constraints_path = self.project_root / 'config' / 'constraints.yaml'
        self.profile_path = self.project_root / 'docs' / 'user_profile' / 'CHANDAN_PROFILE_MASTER.md'
        self.guide_path = self.project_root / 'docs' / 'LLM_GUIDE_YAML_CREATION_v3.md'
        
        self.company_name = company_name
        self.jd_text = None
        self.constraints = None
        self.profile_data = None
        self.generation_guide = None
        self.model = None
        
        self._setup_gemini()
    
    def _setup_gemini(self):
        """Initialize Gemini API"""
        api_key = os.getenv('GEMINI_API_KEY')
        
        if not api_key:
            env_file = self.script_dir / '.env'
            if env_file.exists():
                with open(env_file) as f:
                    for line in f:
                        if line.strip().startswith('GEMINI_API_KEY='):
                            api_key = line.split('=', 1)[1].strip()
                            break
        
        if not api_key:
            print(f"{Colors.RED}ERROR: GEMINI_API_KEY not found!{Colors.END}")
            sys.exit(1)
        
        try:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.5-flash')
            print(f"{Colors.GREEN}✓ Gemini 2.5 Flash configured{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}ERROR: {e}{Colors.END}")
            sys.exit(1)
    
    def load_reference_files(self) -> bool:
        """Load constraints, profile, and generation guide"""
        print(f"\n{Colors.BOLD}Loading reference files...{Colors.END}")
        
        # Load constraints (REQUIRED)
        try:
            with open(self.constraints_path, 'r', encoding='utf-8') as f:
                self.constraints = f.read()
            print(f"{Colors.GREEN}✓ Constraints loaded{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}ERROR loading constraints: {e}{Colors.END}")
            return False
        
        # Load user profile (REQUIRED)
        try:
            with open(self.profile_path, 'r', encoding='utf-8') as f:
                self.profile_data = f.read()
            print(f"{Colors.GREEN}✓ User profile loaded{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}ERROR loading profile: {e}{Colors.END}")
            return False
        
        # Load generation guide (OPTIONAL but helpful)
        try:
            with open(self.guide_path, 'r', encoding='utf-8') as f:
                self.generation_guide = f.read()
            print(f"{Colors.GREEN}✓ Generation guide loaded{Colors.END}")
        except Exception as e:
            print(f"{Colors.YELLOW}⚠ Generation guide not found (continuing without){Colors.END}")
            self.generation_guide = None
        
        return True
    
    def get_job_description(self, jd_text: str = None, jd_file: str = None) -> bool:
        """Get job description from various sources"""
        
        if jd_text:
            # JD provided as text
            self.jd_text = jd_text
            print(f"{Colors.GREEN}✓ Job description provided{Colors.END}")
            return True
        
        elif jd_file:
            # JD provided as file
            try:
                with open(jd_file, 'r', encoding='utf-8') as f:
                    self.jd_text = f.read()
                print(f"{Colors.GREEN}✓ Job description loaded from: {jd_file}{Colors.END}")
                return True
            except Exception as e:
                print(f"{Colors.RED}ERROR loading JD file: {e}{Colors.END}")
                return False
        
        else:
            # Interactive mode - paste JD
            print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")
            print(f"{Colors.BOLD}PASTE JOB DESCRIPTION{Colors.END}")
            print(f"{Colors.BOLD}{'=' * 80}{Colors.END}\n")
            print(f"{Colors.YELLOW}Paste the complete job description below.{Colors.END}")
            print(f"{Colors.YELLOW}Press Enter twice when done:{Colors.END}\n")
            
            lines = []
            empty_count = 0
            
            while True:
                line = input()
                if line == "":
                    empty_count += 1
                    if empty_count >= 2:
                        break
                else:
                    empty_count = 0
                    lines.append(line)
            
            self.jd_text = '\n'.join(lines)
            
            if not self.jd_text.strip():
                print(f"{Colors.RED}No job description provided. Exiting.{Colors.END}")
                return False
            
            print(f"{Colors.GREEN}✓ Job description received ({len(self.jd_text)} characters){Colors.END}")
            return True
    
    def generate_yaml(self) -> str:
        """Generate complete YAML from JD using Gemini"""
        
        # Build comprehensive prompt
        prompt = f"""You are an expert resume YAML generator. Generate a complete, tailored resume YAML for this job description.

═══════════════════════════════════════════════════════════════════════════════
JOB DESCRIPTION:
═══════════════════════════════════════════════════════════════════════════════
{self.jd_text}

═══════════════════════════════════════════════════════════════════════════════
CONSTRAINTS (MUST FOLLOW EXACTLY):
═══════════════════════════════════════════════════════════════════════════════
{self.constraints}

CRITICAL RULES:
- Summary: 450-520 characters (EXCLUDING ** markers), 5-8 bold markers
- Skills: EXACTLY 7 categories, items 35-95 characters each
- LSEG: EXACTLY 5 bullets, 150-250 characters each (EXCLUDING **), 3-5 bold each
- Infosys: EXACTLY 4 bullets, 150-250 characters each (EXCLUDING **), 3-5 bold each
- Projects: EXACTLY 3 projects
- Project bullets: Max 250 characters each (EXCLUDING **), 3-5 bold each
- Tech line: Max 80 characters

═══════════════════════════════════════════════════════════════════════════════
USER PROFILE DATABASE (For Factual Accuracy):
═══════════════════════════════════════════════════════════════════════════════
{self.profile_data}

{'═══════════════════════════════════════════════════════════════════════════════' if self.generation_guide else ''}
{'GENERATION GUIDE (Best Practices):' if self.generation_guide else ''}
{'═══════════════════════════════════════════════════════════════════════════════' if self.generation_guide else ''}
{self.generation_guide if self.generation_guide else ''}

═══════════════════════════════════════════════════════════════════════════════
GENERATION INSTRUCTIONS:
═══════════════════════════════════════════════════════════════════════════════

STEP 1: ANALYZE JOB DESCRIPTION
- Extract primary role type (Backend/ML/Full-Stack/DevOps/Data)
- Identify top 15-20 keywords/technologies
- Understand key focus areas
- Note company mission/values

STEP 2: GENERATE HEADER
- title: "[Role from JD] | MS CS @ Northeastern | [Top 3-5 JD keywords]"
- Max 100 characters

STEP 3: GENERATE SUMMARY (450-520 chars, 5-8 bold)
Required format:
"MS Computer Science student at Northeastern (**3.89 GPA**, Graduating **May 2027**), **F-1 CPT/OPT** eligible, available for **Summer 2026** internship. [Experience focus at **London Stock Exchange Group**]. [2-3 technical highlights matching JD]. [1 key achievement with metric]. Excited to [company-specific value proposition at **COMPANY**]."

STEP 4: GENERATE SKILLS (EXACTLY 7 categories)
- Order categories by JD priority (most important first)
- Include all critical JD keywords
- Each category 35-95 characters
- Use actual skills from user profile only

STEP 5: GENERATE EXPERIENCE BULLETS
LSEG (5 bullets, fresh generation based on JD):
- Use real metrics from profile: 7.5M+ records, 180+ countries, 40 records/sec, 99.9% uptime, 35-40% improvements, 5 engineers, 7 teams
- Technologies: Python, Java, AWS Lambda/SQS/API Gateway, microservices, event-driven
- Match JD keywords naturally
- 150-250 chars each (excluding **), 3-5 bold each

Infosys (4 bullets, complement LSEG):
- Use real metrics: 3x throughput, 50% reduction, 35% latency, 20% accuracy
- Technologies: Python, ETL, microservices, APIs, databases
- Fill gaps in JD coverage
- 150-250 chars each (excluding **), 3-5 bold each

STEP 6: SELECT 3 MOST RELEVANT PROJECTS
From available projects in profile, choose based on:
- Tech stack match with JD
- Role type alignment
- Demonstrates required skills

STEP 7: GENERATE PROJECT BULLETS
- Each project gets 2 bullets (bullet1, bullet2)
- Emphasize JD-relevant aspects
- Use real metrics from profile
- Max 250 chars each (excluding **), 3-5 bold each
- Tech line max 80 chars

CRITICAL REQUIREMENTS:
1. ALL facts must come from user profile (no fabrication)
2. ALL constraints must be met (character limits, bold counts)
3. Generate content FRESH for this JD (not copy-paste from database)
4. Use natural language (not keyword-stuffed)
5. Bold markers: Use ** syntax around key terms

YOUR RESPONSE MUST BE:
- ONLY the complete YAML (no explanations)
- Start with "header:"
- End with last project bullet2
- Valid YAML syntax
- All constraints met

OUTPUT THE YAML NOW:
```yaml
[YOUR COMPLETE YAML HERE]
```
"""

        try:
            print(f"\n{Colors.BLUE}Analyzing job description and generating YAML...{Colors.END}")
            print(f"{Colors.BLUE}This may take 60-90 seconds...{Colors.END}\n")
            
            response = self.model.generate_content(prompt)
            generated_yaml = response.text
            
            # Strip markdown code blocks if present
            if '```yaml' in generated_yaml:
                generated_yaml = generated_yaml.split('```yaml')[1].split('```')[0].strip()
            elif '```' in generated_yaml:
                # Try to find yaml block
                parts = generated_yaml.split('```')
                for i, part in enumerate(parts):
                    if 'header:' in part:
                        generated_yaml = part.strip()
                        break
            
            return generated_yaml
            
        except Exception as e:
            print(f"{Colors.RED}ERROR during generation: {e}{Colors.END}")
            return None
    
    def _extract_company_name(self) -> str:
        """Extract company name from JD using AI"""
        if not self.jd_text or not self.model:
            return None

        prompt = f"""Extract ONLY the company name from this job description.

Job Description:
{self.jd_text[:1000]}

Instructions:
- Return ONLY the company name (e.g., "Google", "Amazon", "Meta")
- Do NOT include "Inc", "LLC", "Corporation" suffixes
- Do NOT include additional text or explanation
- If multiple companies mentioned, return the hiring company

Company name:"""

        try:
            response = self.model.generate_content(prompt)
            company_name = response.text.strip().strip('"').strip("'")

            # Clean up common suffixes
            for suffix in [' Inc', ' LLC', ' Corporation', ' Corp', ' Ltd', ' Limited']:
                if company_name.endswith(suffix):
                    company_name = company_name[:-len(suffix)].strip()

            return company_name if company_name and len(company_name) < 50 else None
        except Exception as e:
            print(f"{Colors.YELLOW}⚠ Error extracting company name: {e}{Colors.END}")
            return None

    def save_yaml(self, generated_yaml: str, save_jd: bool = True):
        """Save the generated YAML and optionally the JD"""
        try:
            # Validate it's proper YAML first
            yaml.safe_load(generated_yaml)

            # Save YAML
            with open(self.output_path, 'w', encoding='utf-8') as f:
                f.write(generated_yaml)
            print(f"\n{Colors.GREEN}✓ YAML saved to: {self.output_path}{Colors.END}")

            # Save JD
            if save_jd and self.jd_text:
                with open(self.jd_output_path, 'w', encoding='utf-8') as f:
                    f.write(self.jd_text)
                print(f"{Colors.GREEN}✓ JD saved to: {self.jd_output_path}{Colors.END}")

            return True

        except yaml.YAMLError as e:
            print(f"\n{Colors.RED}ERROR: Generated YAML has syntax errors!{Colors.END}")
            print(f"{Colors.YELLOW}Error: {e}{Colors.END}")
            print(f"\n{Colors.YELLOW}Generated YAML (with errors):{Colors.END}")
            print(generated_yaml)
            return False
    
    def run(self, jd_text: str = None, jd_file: str = None, auto_save: bool = False):
        """Run the complete generation process

        Args:
            jd_text: Job description text
            jd_file: Path to JD file
            auto_save: If True, save without prompting (for automated pipelines)
        """
        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")
        print(f"{Colors.BOLD}YAML RESUME GENERATOR{Colors.END}")
        if self.company_name:
            print(f"{Colors.BOLD}Company: {self.company_name}{Colors.END}")
        print(f"{Colors.BOLD}{'=' * 80}{Colors.END}")
        
        # Load reference files
        if not self.load_reference_files():
            return False
        
        # Get job description
        if not self.get_job_description(jd_text, jd_file):
            return False
        
        # If company name not provided, extract from JD using AI
        if not self.company_name:
            print(f"\n{Colors.BLUE}Extracting company name from JD...{Colors.END}")
            self.company_name = self._extract_company_name()
            if self.company_name:
                print(f"{Colors.GREEN}✓ Detected company: {self.company_name}{Colors.END}")
            else:
                print(f"{Colors.YELLOW}⚠ Could not auto-detect company name{Colors.END}")
                print(f"{Colors.YELLOW}Enter company name manually: {Colors.END}", end='')
                self.company_name = input().strip()
                if not self.company_name:
                    print(f"{Colors.RED}Company name required for summary generation{Colors.END}")
                    return False
        
        # Generate YAML
        generated_yaml = self.generate_yaml()
        
        if not generated_yaml:
            print(f"{Colors.RED}Failed to generate YAML{Colors.END}")
            return False
        
        # Show preview
        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")
        print(f"{Colors.BOLD}GENERATED YAML PREVIEW{Colors.END}")
        print(f"{Colors.BOLD}{'=' * 80}{Colors.END}\n")
        
        # Show first 600 chars
        preview_length = min(600, len(generated_yaml))
        print(generated_yaml[:preview_length])
        if len(generated_yaml) > 600:
            print(f"\n{Colors.BLUE}... ({len(generated_yaml) - 600} more characters){Colors.END}")

        # Save (auto or prompt)
        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")

        if auto_save:
            # Auto-save for automated pipeline
            print(f"{Colors.BLUE}Auto-saving to config/current_application.yaml...{Colors.END}")
            if self.save_yaml(generated_yaml):
                print(f"\n{Colors.GREEN}{Colors.BOLD}✅ GENERATION COMPLETE{Colors.END}")
                return True
            else:
                print(f"\n{Colors.RED}Failed to save YAML{Colors.END}")
                return False
        else:
            # Interactive mode - ask user
            response = input(f"{Colors.YELLOW}Save to config/current_application.yaml? (y/n): {Colors.END}")

            if response.lower() in ['y', 'yes']:
                if self.save_yaml(generated_yaml):
                    print(f"\n{Colors.GREEN}{Colors.BOLD}✅ GENERATION COMPLETE{Colors.END}")
                    print(f"\n{Colors.BOLD}Next steps:{Colors.END}")
                    print(f"  1. Run: python validate_yaml.py")
                    print(f"  2. If passes: python main.py")
                    print(f"  3. Review generated resume")
                    print(f"  4. Apply!")
                    return True
            else:
                print(f"{Colors.YELLOW}YAML not saved{Colors.END}")

                # Offer to save to different file
                save_alt = input(f"{Colors.YELLOW}Save to generated_application.yaml instead? (y/n): {Colors.END}")
                if save_alt.lower() in ['y', 'yes']:
                    alt_path = self.project_root / 'config' / 'generated_application.yaml'
                    if self.save_yaml(generated_yaml, save_jd=False):
                        print(f"{Colors.GREEN}✓ Saved to: {alt_path}{Colors.END}")
                        return True
        
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Generate complete resume YAML from job description',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generator.py                                    # Interactive mode
  python generator.py --jd-file job_description.txt      # From file
  python generator.py --jd "ServiceNow seeks..."         # Direct text
  python generator.py --company "ServiceNow"             # Interactive with company
        """
    )
    
    parser.add_argument('--jd', type=str,
                       help='Job description text directly')
    parser.add_argument('--jd-file', type=str,
                       help='Path to job description file')
    parser.add_argument('--company', type=str,
                       help='Company name (for summary generation)')
    
    args = parser.parse_args()
    
    # Run generator
    generator = YAMLGenerator(company_name=args.company)
    success = generator.run(jd_text=args.jd, jd_file=args.jd_file)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
