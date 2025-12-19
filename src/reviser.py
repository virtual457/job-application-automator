#!/usr/bin/env python3
"""
YAML Resume Reviser
Revises current_application.yaml based on feedback while maintaining constraints

Takes:
- Current YAML (config/current_application.yaml)
- Job Description (config/current_jd.txt)
- Feedback (user input or from quality/ATS checkers)
- Constraints (config/constraints.yaml)
- User Profile (optional - docs/user_profile/CHANDAN_PROFILE_MASTER.md)

Outputs:
- Revised YAML that addresses feedback while staying within constraints

Usage:
    python reviser.py
    python reviser.py --feedback "Summary too generic, needs more specific metrics"
    python reviser.py --feedback-file feedback.txt
    python reviser.py --use-profile  # Include user profile data
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

class YAMLReviser:
    def __init__(self, use_profile=False):
        self.script_dir = Path(__file__).parent.resolve()
        self.project_root = self.script_dir.parent
        
        self.current_yaml_path = self.project_root / 'config' / 'current_application.yaml'
        self.jd_path = self.project_root / 'config' / 'current_jd.txt'
        self.constraints_path = self.project_root / 'config' / 'constraints.yaml'
        self.profile_path = self.project_root / 'docs' / 'user_profile' / 'CHANDAN_PROFILE_MASTER.md'
        
        self.current_yaml = None
        self.jd_text = None
        self.constraints = None
        self.profile_data = None
        self.use_profile = use_profile
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
    
    def load_files(self) -> bool:
        """Load all required files"""
        print(f"\n{Colors.BOLD}Loading files...{Colors.END}")
        
        # Load current YAML
        try:
            with open(self.current_yaml_path, 'r', encoding='utf-8') as f:
                self.current_yaml = f.read()
            print(f"{Colors.GREEN}✓ Current YAML loaded{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}ERROR loading YAML: {e}{Colors.END}")
            return False
        
        # Load JD
        try:
            with open(self.jd_path, 'r', encoding='utf-8') as f:
                self.jd_text = f.read()
            print(f"{Colors.GREEN}✓ Job description loaded{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}ERROR loading JD: {e}{Colors.END}")
            return False
        
        # Load constraints
        try:
            with open(self.constraints_path, 'r', encoding='utf-8') as f:
                self.constraints = f.read()
            print(f"{Colors.GREEN}✓ Constraints loaded{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}ERROR loading constraints: {e}{Colors.END}")
            return False
        
        # Load profile (optional)
        if self.use_profile:
            try:
                with open(self.profile_path, 'r', encoding='utf-8') as f:
                    self.profile_data = f.read()
                print(f"{Colors.GREEN}✓ User profile loaded{Colors.END}")
            except Exception as e:
                print(f"{Colors.YELLOW}⚠ Could not load profile: {e}{Colors.END}")
                self.profile_data = None
        
        return True
    
    def revise_yaml(self, feedback: str) -> str:
        """Generate revised YAML based on feedback"""
        
        # Build comprehensive prompt
        prompt = f"""You are an expert resume YAML generator. Your task is to revise a resume YAML configuration based on feedback while maintaining all constraints.

═══════════════════════════════════════════════════════════════════════════════
CURRENT YAML:
═══════════════════════════════════════════════════════════════════════════════
```yaml
{self.current_yaml}
```

═══════════════════════════════════════════════════════════════════════════════
JOB DESCRIPTION:
═══════════════════════════════════════════════════════════════════════════════
{self.jd_text}

═══════════════════════════════════════════════════════════════════════════════
CONSTRAINTS (MUST FOLLOW):
═══════════════════════════════════════════════════════════════════════════════
{self.constraints}

CRITICAL CONSTRAINT RULES:
- Summary: 450-520 characters (excluding ** markers), 5-8 bold markers
- Skills: Exactly 7 categories, items 35-95 characters each
- Experience bullets: 150-250 characters (excluding ** markers), 3-5 bold markers each
- LSEG: Exactly 5 bullets
- Infosys: Exactly 4 bullets
- Projects: Exactly 3 projects
- Project bullets: Max 250 characters (excluding ** markers), 3-5 bold markers each
- Tech line: Max 80 characters

═══════════════════════════════════════════════════════════════════════════════
FEEDBACK TO ADDRESS:
═══════════════════════════════════════════════════════════════════════════════
{feedback}

{'═══════════════════════════════════════════════════════════════════════════════' if self.profile_data else ''}
{'USER PROFILE DATA (For Factual Accuracy):' if self.profile_data else ''}
{'═══════════════════════════════════════════════════════════════════════════════' if self.profile_data else ''}
{self.profile_data if self.profile_data else ''}

═══════════════════════════════════════════════════════════════════════════════
REVISION INSTRUCTIONS:
═══════════════════════════════════════════════════════════════════════════════

1. READ the current YAML carefully
2. READ the feedback and identify what needs to change
3. READ the constraints and ensure all limits are met
4. REVISE only the sections mentioned in feedback
5. MAINTAIN factual accuracy:
   - ONLY use projects, skills, and experiences from USER PROFILE DATA above
   - DO NOT invent or add projects not listed in the profile
   - DO NOT suggest skills or technologies not mentioned in the profile
   - ONLY use real metrics from LSEG/Infosys as documented in the profile
   - If something isn't in the profile, DO NOT include it
6. STAY within all character limits (excluding ** markers)
7. ENSURE bold marker counts are within limits
8. KEEP the same overall structure

YOUR RESPONSE MUST BE:
- ONLY the complete revised YAML (no explanations before or after)
- Valid YAML syntax
- All constraints met
- Feedback addressed
- ALL content factually accurate per user profile

OUTPUT FORMAT:
```yaml
header:
  name: "Chandan Gowda K S"
  title: "..."
  contact: "..."

summary: "..."

skills:
  - category: "..."
    items: "..."
  # ... exactly 7 categories

experience:
  - company: "London Stock Exchange Group (LSEG)"
    role: "Senior Software Engineer"
    location: "Bengaluru"
    duration: "08-2022 to 12-2024"
    bullets:
      - "..."
      # ... exactly 5 bullets
  
  - company: "Infosys"
    role: "Senior Systems Engineer"
    location: "Bengaluru"
    duration: "10-2020 to 07-2022"
    bullets:
      - "..."
      # ... exactly 4 bullets

projects:
  - title: "..."
    tech: "..."
    github: "GitHub"
    bullet1: "..."
    bullet2: "..."
  # ... exactly 3 projects
```

IMPORTANT:
- Output ONLY valid YAML
- NO explanations or commentary
- Start directly with "header:"
- End with last project bullet2
"""

        try:
            print(f"\n{Colors.BLUE}Generating revised YAML...{Colors.END}")
            print(f"{Colors.BLUE}This may take 30-60 seconds...{Colors.END}\n")
            
            response = self.model.generate_content(prompt)
            revised_yaml = response.text
            
            # Strip markdown code blocks if present
            if '```yaml' in revised_yaml:
                revised_yaml = revised_yaml.split('```yaml')[1].split('```')[0].strip()
            elif '```' in revised_yaml:
                revised_yaml = revised_yaml.split('```')[1].split('```')[0].strip()
            
            return revised_yaml
            
        except Exception as e:
            print(f"{Colors.RED}ERROR during revision: {e}{Colors.END}")
            return None
    
    def save_revised_yaml(self, revised_yaml: str, output_path: str = None):
        """Save the revised YAML"""
        if output_path is None:
            output_path = self.current_yaml_path
        
        try:
            # Validate it's proper YAML first
            yaml.safe_load(revised_yaml)
            
            # Save
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(revised_yaml)
            
            print(f"\n{Colors.GREEN}✓ Revised YAML saved to: {output_path}{Colors.END}")
            return True
            
        except yaml.YAMLError as e:
            print(f"\n{Colors.RED}ERROR: Generated YAML has syntax errors!{Colors.END}")
            print(f"{Colors.YELLOW}Error: {e}{Colors.END}")
            print(f"\n{Colors.YELLOW}Generated YAML (with errors):{Colors.END}")
            print(revised_yaml)
            return False
    
    def run(self, feedback: str):
        """Run the complete revision process"""
        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")
        print(f"{Colors.BOLD}YAML RESUME REVISER{Colors.END}")
        print(f"{Colors.BOLD}{'=' * 80}{Colors.END}")
        
        if not self.load_files():
            return False
        
        print(f"\n{Colors.BOLD}Feedback to address:{Colors.END}")
        print(f"{Colors.YELLOW}{feedback}{Colors.END}")
        
        # Generate revision
        revised_yaml = self.revise_yaml(feedback)
        
        if not revised_yaml:
            print(f"{Colors.RED}Failed to generate revision{Colors.END}")
            return False
        
        # Show preview
        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")
        print(f"{Colors.BOLD}REVISED YAML PREVIEW{Colors.END}")
        print(f"{Colors.BOLD}{'=' * 80}{Colors.END}\n")
        print(revised_yaml[:500] + "..." if len(revised_yaml) > 500 else revised_yaml)
        
        # Ask to save
        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")
        response = input(f"{Colors.YELLOW}Save this revision to current_application.yaml? (y/n): {Colors.END}")
        
        if response.lower() in ['y', 'yes']:
            if self.save_revised_yaml(revised_yaml):
                print(f"\n{Colors.GREEN}{Colors.BOLD}✅ REVISION COMPLETE{Colors.END}")
                print(f"\n{Colors.BOLD}Next steps:{Colors.END}")
                print(f"  1. Run: python validate_yaml.py")
                print(f"  2. If passes, run: python main.py")
                return True
        else:
            print(f"{Colors.YELLOW}Revision not saved{Colors.END}")
            
            # Offer to save to different file
            save_alt = input(f"{Colors.YELLOW}Save to revised_application.yaml instead? (y/n): {Colors.END}")
            if save_alt.lower() in ['y', 'yes']:
                alt_path = self.project_root / 'config' / 'revised_application.yaml'
                if self.save_revised_yaml(revised_yaml, str(alt_path)):
                    print(f"{Colors.GREEN}✓ Saved to: {alt_path}{Colors.END}")
                    return True
        
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Revise resume YAML based on feedback',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python reviser.py
  python reviser.py --feedback "Summary needs more AI/ML keywords"
  python reviser.py --feedback-file feedback.txt
  python reviser.py --use-profile --feedback "Add more LSEG metrics"
        """
    )
    
    parser.add_argument('--feedback', type=str,
                       help='Feedback text directly as argument')
    parser.add_argument('--feedback-file', type=str,
                       help='Path to file containing feedback')
    parser.add_argument('--use-profile', action='store_true',
                       help='Include user profile data for factual accuracy')
    
    args = parser.parse_args()
    
    # Get feedback
    feedback = None
    
    if args.feedback:
        feedback = args.feedback
    elif args.feedback_file:
        try:
            with open(args.feedback_file, 'r', encoding='utf-8') as f:
                feedback = f.read()
        except Exception as e:
            print(f"{Colors.RED}ERROR reading feedback file: {e}{Colors.END}")
            sys.exit(1)
    else:
        # Interactive mode - get feedback from user
        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")
        print(f"{Colors.BOLD}YAML RESUME REVISER - Interactive Mode{Colors.END}")
        print(f"{Colors.BOLD}{'=' * 80}{Colors.END}\n")
        
        print(f"{Colors.YELLOW}Enter feedback for revision (press Enter twice when done):{Colors.END}\n")
        
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
        
        feedback = '\n'.join(lines)
        
        if not feedback.strip():
            print(f"{Colors.RED}No feedback provided. Exiting.{Colors.END}")
            sys.exit(1)
    
    # Run reviser
    reviser = YAMLReviser(use_profile=args.use_profile)
    success = reviser.run(feedback)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
