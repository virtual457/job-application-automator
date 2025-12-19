#!/usr/bin/env python3
"""
Resume Quality Checker - Content Analysis Only
Converts DOCX to PDF and sends to Gemini API for content quality evaluation

Requirements:
- pip install docx2pdf google-generativeai
- Microsoft Word must be installed (Windows)

Defaults:
- Job Description: ../config/current_jd.txt
- Resume: ../output/Generated_Resume.docx
- API Key: .env file in same directory as this script

Usage:
    python quality_checker_pdf.py                       # Use defaults
    python quality_checker_pdf.py job_description.txt   # Custom JD
    python quality_checker_pdf.py jd.txt resume.docx    # Custom both
"""

import os
import sys
import google.generativeai as genai
from pathlib import Path

# PDF conversion
try:
    from docx2pdf import convert
    PDF_CONVERSION_AVAILABLE = True
except ImportError:
    PDF_CONVERSION_AVAILABLE = False

# ANSI colors
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

def safe_print(text):
    """Print text with encoding error handling for Windows console"""
    try:
        print(text)
    except UnicodeEncodeError:
        # Replace problematic Unicode characters
        safe_text = text.encode('ascii', 'replace').decode('ascii')
        print(safe_text)

class ResumeQualityChecker:
    def __init__(self, resume_path: str, jd_path: str = None):
        self.resume_path = resume_path
        self.jd_path = jd_path
        self.pdf_path = None
        self.job_description = ""
        self.profile_data = ""
        self.model = None

        self._setup_gemini()
        self._load_user_profile()

    def _setup_gemini(self):
        """Initialize Gemini API - reads .env from script's directory"""
        api_key = os.getenv('GEMINI_API_KEY')

        if not api_key:
            script_dir = Path(__file__).parent.resolve()
            env_file = script_dir / '.env'

            if env_file.exists():
                with open(env_file) as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith('GEMINI_API_KEY='):
                            api_key = line.split('=', 1)[1].strip()
                            break
                print(f"{Colors.GREEN}[OK] API key loaded from: {env_file}{Colors.END}")
            else:
                print(f"{Colors.YELLOW}⚠ .env file not found at: {env_file}{Colors.END}")

        if not api_key:
            print(f"{Colors.RED}ERROR: GEMINI_API_KEY not found!{Colors.END}")
            sys.exit(1)

        try:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.5-flash')
            print(f"{Colors.GREEN}[OK] Gemini 2.5 Flash configured{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}ERROR configuring Gemini: {e}{Colors.END}")
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
                print(f"{Colors.YELLOW}⚠ User profile not found at: {profile_path}{Colors.END}")
                self.profile_data = ""
        except Exception as e:
            print(f"{Colors.YELLOW}⚠ Could not load user profile: {e}{Colors.END}")
            self.profile_data = ""

    def _convert_to_pdf(self, docx_path: str) -> str:
        """Convert DOCX to PDF using docx2pdf"""
        if not PDF_CONVERSION_AVAILABLE:
            print(f"{Colors.RED}ERROR: docx2pdf not installed!{Colors.END}")
            print(f"Install with: pip install docx2pdf")
            sys.exit(1)

        try:
            docx_path = Path(docx_path)
            pdf_path = docx_path.parent / f"{docx_path.stem}.pdf"
            
            print(f"{Colors.BLUE}Converting DOCX to PDF...{Colors.END}")
            print(f"  Input:  {docx_path}")
            print(f"  Output: {pdf_path}")
            
            convert(str(docx_path), str(pdf_path))
            
            print(f"{Colors.GREEN}[OK] PDF created successfully{Colors.END}")
            return str(pdf_path)
            
        except Exception as e:
            print(f"{Colors.RED}ERROR converting to PDF: {e}{Colors.END}")
            print(f"{Colors.YELLOW}Make sure Microsoft Word is installed{Colors.END}")
            sys.exit(1)

    def load_files(self) -> bool:
        """Load resume and convert to PDF"""
        try:
            # Check if resume exists
            resume_path = Path(self.resume_path)
            if not resume_path.exists():
                print(f"{Colors.RED}ERROR: Resume not found: {self.resume_path}{Colors.END}")
                return False

            print(f"{Colors.GREEN}[OK] Resume found: {self.resume_path}{Colors.END}")

            # Convert to PDF
            self.pdf_path = self._convert_to_pdf(str(resume_path))

            # Load job description
            if self.jd_path:
                jd_path = Path(self.jd_path)
                if jd_path.exists():
                    with open(jd_path, 'r', encoding='utf-8') as f:
                        self.job_description = f.read()
                    print(f"{Colors.GREEN}[OK] Job description loaded: {self.jd_path}{Colors.END}")
                else:
                    print(f"{Colors.YELLOW}⚠ JD not found, using general evaluation{Colors.END}")
            else:
                print(f"{Colors.YELLOW}⚠ No JD provided, using general evaluation{Colors.END}")

            return True
        except Exception as e:
            print(f"{Colors.RED}ERROR loading files: {e}{Colors.END}")
            return False

    def evaluate_complete_resume(self) -> str:
        """Send PDF to Gemini for content quality analysis"""
        
        # Read PDF file
        with open(self.pdf_path, 'rb') as f:
            pdf_data = f.read()

        # Create prompt for content analysis
        prompt = f"""You are an expert resume reviewer analyzing a PDF resume for CONTENT QUALITY.

═══════════════════════════════════════════════════════════════════════════════
JOB DESCRIPTION:
═══════════════════════════════════════════════════════════════════════════════
{self.job_description if self.job_description else "General software engineering internship position"}

═══════════════════════════════════════════════════════════════════════════════
USER PROFILE DATA (What candidate has actually done):
═══════════════════════════════════════════════════════════════════════════════
{self.profile_data if self.profile_data else "Profile not available"}

IMPORTANT INSTRUCTIONS:
- ONLY suggest skills/projects/technologies that appear in USER PROFILE DATA above
- DO NOT suggest adding things the candidate hasn't done (like Apache Kafka if not in profile)
- DO identify relevant items FROM THE PROFILE that are missing from the resume but should be highlighted for this JD
- Focus on reframing/improving what's already there based on profile facts

Evaluate the CONTENT quality of this resume. Focus on writing quality, job relevance, and impact.

Format your response EXACTLY as follows:

═══════════════════════════════════════════════════════════════════════════════
SECTION 1: SUMMARY EVALUATION
═══════════════════════════════════════════════════════════════════════════════

GRAMMAR & LANGUAGE: [score]/10
[2-3 sentences: Grammar issues, awkward phrasing, clarity problems]

FLOW & COHERENCE: [score]/10
[2-3 sentences: Does it flow well? Story clarity?]

JOB RELEVANCE: [score]/10
[2-3 sentences: Match to JD? Right skills highlighted?]

IMPACT & METRICS: [score]/10
[2-3 sentences: Metrics compelling? Demonstrates value?]

SECTION SCORE: [average]/10

CRITICAL ISSUES:
- [List problems that MUST be fixed, or "None"]

IMPROVEMENTS:
- [2-3 specific suggestions - reframe/improve based on user profile facts]

═══════════════════════════════════════════════════════════════════════════════
SECTION 2: SKILLS EVALUATION
═══════════════════════════════════════════════════════════════════════════════

JOB RELEVANCE: [score]/10
[Do skills match JD? Priority correct?]

COMPREHENSIVENESS: [score]/10
[Good coverage? Any gaps?]

ORGANIZATION: [score]/10
[Logical categories? Well-structured?]

SECTION SCORE: [average]/10

MISSING SKILLS FROM JD (that are IN USER PROFILE):
- [List 2-3 key skills from profile that should be added, or "None"]

IMPROVEMENTS:
- [2-3 suggestions - ONLY based on what's in user profile]

═══════════════════════════════════════════════════════════════════════════════
SECTION 3: WORK EXPERIENCE EVALUATION
═══════════════════════════════════════════════════════════════════════════════

RELEVANCE: [score]/10
[Work experience aligns with JD? Right projects highlighted?]

BULLET QUALITY: [score]/10
[Well-written? Strong verbs? Quantified results? Technical depth?]

SECTION SCORE: [average]/10

CRITICAL ISSUES:
- [Problems in bullets, or "None"]

IMPROVEMENTS:
- [2-3 suggestions - reframe/improve based on user profile facts]

═══════════════════════════════════════════════════════════════════════════════
SECTION 4: PROJECTS EVALUATION
═══════════════════════════════════════════════════════════════════════════════

PROJECT RELEVANCE: [score]/10
[Projects align with JD? Right tech showcased?]

DESCRIPTIONS QUALITY: [score]/10
[Clear and impactful? Technical depth?]

SECTION SCORE: [average]/10

MISSING RELEVANT PROJECTS (that are IN USER PROFILE):
- [List projects from profile that should replace current ones, or "None"]

IMPROVEMENTS:
- [2-3 suggestions - ONLY based on projects in user profile]

═══════════════════════════════════════════════════════════════════════════════
OVERALL ASSESSMENT
═══════════════════════════════════════════════════════════════════════════════

SECTION SCORES:
- Summary: [score]/10
- Skills: [score]/10
- Work Experience: [score]/10
- Projects: [score]/10

OVERALL CONTENT SCORE: [average]/10

RATING: [EXCELLENT 9-10 | VERY GOOD 8-9 | GOOD 7-8 | NEEDS WORK <7]

TOP 3 STRENGTHS:
1. [Specific strength]
2. [Specific strength]
3. [Specific strength]

TOP 3 IMPROVEMENTS:
1. [Specific, actionable improvement]
2. [Specific improvement]
3. [Specific improvement]

READINESS: [Ready to submit / Needs minor fixes / Needs major revisions]
[2-3 sentences explaining readiness]
"""

        try:
            print(f"{Colors.BLUE}Sending PDF to Gemini for content analysis...{Colors.END}")
            print(f"{Colors.BLUE}This may take 15-25 seconds...{Colors.END}\n")
            
            response = self.model.generate_content([
                {
                    'mime_type': 'application/pdf',
                    'data': pdf_data
                },
                prompt
            ])
            
            return response.text
        except Exception as e:
            return f"Error during evaluation: {e}"

    def run_quality_check(self):
        """Run complete quality assessment"""
        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")
        print(f"{Colors.BOLD}RESUME CONTENT QUALITY ASSESSMENT{Colors.END}")
        print(f"{Colors.BOLD}{'=' * 80}{Colors.END}\n")

        if not self.load_files():
            return

        evaluation_result = self.evaluate_complete_resume()
        self._print_formatted_results(evaluation_result)

    def _print_formatted_results(self, results: str):
        """Print results with color formatting"""
        safe_print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")
        safe_print(f"{Colors.BOLD}QUALITY ANALYSIS RESULTS{Colors.END}")
        safe_print(f"{Colors.BOLD}{'=' * 80}{Colors.END}\n")

        for line in results.split('\n'):
            if '/10' in line:
                try:
                    score = int(float(line.split('/10')[0].split(':')[-1].strip()))
                    color = Colors.GREEN if score >= 9 else Colors.YELLOW if score >= 7 else Colors.RED
                    safe_print(f"{color}{line}{Colors.END}")
                except:
                    safe_print(line)
            elif 'SECTION' in line and '═' not in line:
                safe_print(f"{Colors.BOLD}{Colors.BLUE}{line}{Colors.END}")
            elif 'RATING:' in line:
                if 'EXCELLENT' in line or 'VERY GOOD' in line:
                    color = Colors.GREEN
                elif 'GOOD' in line:
                    color = Colors.YELLOW
                else:
                    color = Colors.RED
                safe_print(f"{color}{Colors.BOLD}{line}{Colors.END}")
            elif 'CRITICAL ISSUES' in line or 'TOP 3 IMPROVEMENTS' in line:
                safe_print(f"{Colors.BOLD}{Colors.RED}{line}{Colors.END}")
            elif 'TOP 3 STRENGTHS' in line:
                safe_print(f"{Colors.BOLD}{Colors.GREEN}{line}{Colors.END}")
            elif '═══' in line:
                safe_print(f"{Colors.BOLD}{line}{Colors.END}")
            else:
                safe_print(line)

        safe_print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")

def main():
    print(f"\n{Colors.BOLD}Resume Quality Checker - Content Analysis{Colors.END}")
    print(f"{Colors.BOLD}Powered by Gemini 2.5 Flash{Colors.END}\n")

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
    elif len(sys.argv) == 2:
        jd_path = sys.argv[1]
        resume_path = str(default_resume)
    else:
        jd_path = sys.argv[1]
        resume_path = sys.argv[2]

    checker = ResumeQualityChecker(resume_path, jd_path)
    checker.run_quality_check()

if __name__ == "__main__":
    main()
