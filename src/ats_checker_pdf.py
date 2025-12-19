#!/usr/bin/env python3
"""
ATS Checker with PDF Visual Analysis
Brutal keyword matching + visual ATS compatibility check

Requirements:
- pip install docx2pdf google-generativeai
- Microsoft Word installed (Windows)

Usage:
    python ats_checker_pdf.py                    # Use defaults
    python ats_checker_pdf.py jd.txt             # Custom JD
    python ats_checker_pdf.py jd.txt resume.docx # Custom both
"""

import os
import sys
import google.generativeai as genai
from pathlib import Path

try:
    from docx2pdf import convert
    PDF_CONVERSION_AVAILABLE = True
except ImportError:
    PDF_CONVERSION_AVAILABLE = False

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

class ATSChecker:
    def __init__(self, resume_path: str, jd_path: str):
        self.resume_path = resume_path
        self.jd_path = jd_path
        self.pdf_path = None
        self.job_description = ""
        self.profile_data = ""
        self.model = None
        self._setup_gemini()
        self._load_user_profile()

    def _setup_gemini(self):
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            script_dir = Path(__file__).parent.resolve()
            env_file = script_dir / '.env'
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
            print(f"{Colors.GREEN}[OK] Gemini configured{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}ERROR: {e}{Colors.END}")
            sys.exit(1)

    def _load_user_profile(self):
        """Load user profile data for factual accuracy"""
        try:
            script_dir = Path(__file__).parent.resolve()
            profile_path = script_dir.parent / 'docs' / 'user_profile' / 'CHANDAN_PROFILE_MASTER.md'

            if profile_path.exists():
                with open(profile_path, 'r', encoding='utf-8') as f:
                    self.profile_data = f.read()
                print(f"{Colors.GREEN}[OK] User profile loaded{Colors.END}")
            else:
                print(f"{Colors.YELLOW}⚠ User profile not found{Colors.END}")
                self.profile_data = ""
        except Exception as e:
            print(f"{Colors.YELLOW}⚠ Could not load profile: {e}{Colors.END}")
            self.profile_data = ""

    def _convert_to_pdf(self, docx_path: str) -> str:
        if not PDF_CONVERSION_AVAILABLE:
            print(f"{Colors.RED}ERROR: docx2pdf not installed!{Colors.END}")
            sys.exit(1)

        try:
            docx_path = Path(docx_path)
            pdf_path = docx_path.parent / f"{docx_path.stem}.pdf"
            
            print(f"{Colors.BLUE}Converting to PDF...{Colors.END}")
            convert(str(docx_path), str(pdf_path))
            print(f"{Colors.GREEN}[OK] PDF created{Colors.END}")
            
            return str(pdf_path)
        except Exception as e:
            print(f"{Colors.RED}ERROR: {e}{Colors.END}")
            sys.exit(1)

    def load_files(self) -> bool:
        try:
            # Check resume
            if not Path(self.resume_path).exists():
                print(f"{Colors.RED}ERROR: Resume not found{Colors.END}")
                return False

            # Convert to PDF
            self.pdf_path = self._convert_to_pdf(self.resume_path)

            # Load JD
            if Path(self.jd_path).exists():
                with open(self.jd_path, 'r', encoding='utf-8') as f:
                    self.job_description = f.read()
                print(f"{Colors.GREEN}[OK] JD loaded{Colors.END}")
            else:
                print(f"{Colors.RED}ERROR: JD required{Colors.END}")
                return False

            return True
        except Exception as e:
            print(f"{Colors.RED}ERROR: {e}{Colors.END}")
            return False

    def analyze_ats(self) -> str:
        with open(self.pdf_path, 'rb') as f:
            pdf_data = f.read()

        prompt = f"""ATS BRUTAL ANALYSIS - Score /100

JOB DESCRIPTION:
{self.job_description}

USER PROFILE DATA (What candidate has actually done):
{self.profile_data if self.profile_data else "Profile not available"}

IMPORTANT: When suggesting missing keywords or improvements, ONLY suggest skills/technologies/projects that appear in the USER PROFILE DATA above. Do not suggest things the candidate hasn't done.

Analyze this PDF resume for ATS compatibility and keyword matching.

Response format:

VISUAL ATS COMPATIBILITY (/10):
- Table complexity: [Simple/Complex]
- Text extraction: [Easy/Hard]  
- Score: [X]/10

KEYWORD MATCHING (/30):
- Required keywords: [list 15-20]
- Found: [list]
- Missing: [list]
- Score: [X]/30

SKILLS COVERAGE (/25):
- Required skills: [list]
- Present in skills section: [list]
- Missing: [list]
- Score: [X]/25

EXPERIENCE ALIGNMENT (/20):
- JD requirements: [list 5-8]
- Covered: [list]
- Uncovered: [list]
- Score: [X]/20

PROJECT RELEVANCE (/10):
- Score: [X]/10

HARD REQUIREMENTS (/5):
- Degree/GPA/etc: [✓/✗]
- Score: [X]/5

TOTAL SCORE: [X]/100
VERDICT: [PASS ✓ 85+ | BORDERLINE ⚠ 70-84 | FAIL ✗ <70]

TOP 3 FIXES:
1. [Specific improvement]
2. [Specific improvement]
3. [Specific improvement]

BRUTAL TRUTH:
[Honest assessment - submit or not?]
"""

        try:
            print(f"{Colors.BLUE}Running ATS analysis...{Colors.END}\n")
            response = self.model.generate_content([
                {'mime_type': 'application/pdf', 'data': pdf_data},
                prompt
            ])
            return response.text
        except Exception as e:
            return f"Error: {e}"

    def run_check(self):
        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")
        print(f"{Colors.BOLD}BRUTAL ATS ANALYSIS (PDF){Colors.END}")
        print(f"{Colors.BOLD}{'=' * 80}{Colors.END}\n")

        if not self.load_files():
            return

        result = self.analyze_ats()
        self._print_results(result)

    def _print_results(self, results: str):
        print(f"\n{Colors.BOLD}RESULTS{Colors.END}\n")
        
        for line in results.split('\n'):
            if '/100' in line or '/30' in line or '/25' in line or '/20' in line or '/10' in line or '/5' in line:
                try:
                    score_str = line.split('/')[0].split(':')[-1].strip()
                    max_str = line.split('/')[1].split()[0]
                    pct = (float(score_str) / float(max_str)) * 100
                    color = Colors.GREEN if pct >= 85 else Colors.YELLOW if pct >= 70 else Colors.RED
                    print(f"{color}{line}{Colors.END}")
                except:
                    print(line)
            elif 'VERDICT:' in line:
                if 'PASS ✓' in line:
                    print(f"{Colors.GREEN}{Colors.BOLD}{line}{Colors.END}")
                elif 'BORDERLINE' in line:
                    print(f"{Colors.YELLOW}{Colors.BOLD}{line}{Colors.END}")
                elif 'FAIL ✗' in line:
                    print(f"{Colors.RED}{Colors.BOLD}{line}{Colors.END}")
                else:
                    print(line)
            else:
                print(line)

def main():
    print(f"\n{Colors.BOLD}ATS Checker (PDF){Colors.END}\n")

    if not PDF_CONVERSION_AVAILABLE:
        print(f"{Colors.RED}ERROR: docx2pdf not installed!{Colors.END}")
        print(f"Install: pip install docx2pdf\n")
        sys.exit(1)

    script_dir = Path(__file__).parent.resolve()
    config_dir = script_dir.parent / 'config'
    output_dir = script_dir.parent / 'output'

    default_jd = config_dir / 'current_jd.txt'
    default_resume = output_dir / 'Generated_Resume.docx'

    if len(sys.argv) == 1:
        jd_path = str(default_jd) if default_jd.exists() else None
        resume_path = str(default_resume)
        if not jd_path:
            print(f"{Colors.RED}ERROR: JD required for ATS{Colors.END}")
            sys.exit(1)
    elif len(sys.argv) == 2:
        jd_path = sys.argv[1]
        resume_path = str(default_resume)
    else:
        jd_path = sys.argv[1]
        resume_path = sys.argv[2]

    checker = ATSChecker(resume_path, jd_path)
    checker.run_check()

if __name__ == "__main__":
    main()
