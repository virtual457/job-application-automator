#!/usr/bin/env python3
"""
Resume Quality Checker - Analyzes Generated .docx Resume
Uses Google Gemini API with one comprehensive evaluation for all sections
Provides detailed scoring, refinements, and feedback for each section

Defaults:
- Job Description: ../config/current_jd.txt
- Resume: ../output/Generated_Resume.docx
- API Key: .env file in same directory as this script

Usage:
    python quality_checker.py                           # Use defaults
    python quality_checker.py job_description.txt       # Custom JD
    python quality_checker.py jd.txt resume.docx        # Custom both
"""

import os
import sys
import google.generativeai as genai
from pathlib import Path
from docx import Document

# ANSI colors
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

class ResumeQualityChecker:
    def __init__(self, resume_path: str, jd_path: str = None):
        self.resume_path = resume_path
        self.jd_path = jd_path
        self.resume_text = ""
        self.job_description = ""
        self.model = None

        self._setup_gemini()

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
                print(f"{Colors.GREEN}✓ API key loaded from: {env_file}{Colors.END}")
            else:
                print(f"{Colors.YELLOW}⚠ .env file not found at: {env_file}{Colors.END}")

        if not api_key:
            print(f"{Colors.RED}ERROR: GEMINI_API_KEY not found!{Colors.END}")
            sys.exit(1)

        try:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.5-flash')
            print(f"{Colors.GREEN}✓ Gemini 2.5 Flash configured{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}ERROR configuring Gemini: {e}{Colors.END}")
            sys.exit(1)

    def _extract_text_from_docx(self, docx_path: str) -> str:
        """Extract all text from .docx file"""
        try:
            doc = Document(docx_path)
            full_text = []

            for paragraph in doc.paragraphs:
                text = paragraph.text.strip()
                if text:
                    full_text.append(text)

            return '\n'.join(full_text)
        except Exception as e:
            print(f"{Colors.RED}ERROR reading .docx: {e}{Colors.END}")
            return ""

    def load_files(self) -> bool:
        """Load resume and job description"""
        try:
            # Load resume (.docx)
            resume_path = Path(self.resume_path)
            if not resume_path.exists():
                print(f"{Colors.RED}ERROR: Resume not found: {self.resume_path}{Colors.END}")
                return False

            self.resume_text = self._extract_text_from_docx(str(resume_path))
            if not self.resume_text:
                print(f"{Colors.RED}ERROR: Could not extract text from resume{Colors.END}")
                return False

            print(f"{Colors.GREEN}✓ Resume loaded: {self.resume_path}{Colors.END}")
            print(f"{Colors.BLUE}  Extracted {len(self.resume_text)} characters{Colors.END}")

            # Load job description
            if self.jd_path:
                jd_path = Path(self.jd_path)
                if jd_path.exists():
                    with open(jd_path, 'r', encoding='utf-8') as f:
                        self.job_description = f.read()
                    print(f"{Colors.GREEN}✓ Job description loaded: {self.jd_path}{Colors.END}")
                else:
                    print(f"{Colors.YELLOW}⚠ JD not found, using general evaluation{Colors.END}")
            else:
                print(f"{Colors.YELLOW}⚠ No JD provided, using general evaluation{Colors.END}")

            return True
        except Exception as e:
            print(f"{Colors.RED}ERROR loading files: {e}{Colors.END}")
            return False

    def evaluate_complete_resume(self) -> str:
        """Single comprehensive evaluation of entire resume"""

        # Comprehensive evaluation prompt
        prompt = f"""You are an expert resume reviewer conducting a comprehensive quality assessment of a resume for a software engineering internship.

═══════════════════════════════════════════════════════════════════════════════
JOB DESCRIPTION:
═══════════════════════════════════════════════════════════════════════════════
{self.job_description if self.job_description else "General software engineering internship position"}

═══════════════════════════════════════════════════════════════════════════════
COMPLETE RESUME (Generated .docx):
═══════════════════════════════════════════════════════════════════════════════
{self.resume_text}

═══════════════════════════════════════════════════════════════════════════════
EVALUATION INSTRUCTIONS:
═══════════════════════════════════════════════════════════════════════════════

Provide a comprehensive evaluation with detailed scores, feedback, and actionable refinements for each section.

Your response MUST follow this EXACT format:

═══════════════════════════════════════════════════════════════════════════════
SECTION 1: SUMMARY EVALUATION
═══════════════════════════════════════════════════════════════════════════════

GRAMMAR & LANGUAGE: [score]/10
[2-3 sentences: Specific grammar issues, awkward phrasing, clarity problems. Flag nonsensical constructions like "Built production experience engineering"]

FLOW & COHERENCE: [score]/10
[2-3 sentences: How well does it flow? Transition quality? Story clarity?]

JOB RELEVANCE: [score]/10
[2-3 sentences: Match to JD? Right skills highlighted? Company-specific positioning?]

IMPACT & METRICS: [score]/10
[2-3 sentences: Are metrics compelling? Quantified achievements? Demonstrates value?]

PROFESSIONALISM: [score]/10
[2-3 sentences: Appropriate tone? Company-specific ending? Professional language?]

SECTION SCORE: [average]/10

CRITICAL ISSUES:
- [List specific problems that MUST be fixed, or "None"]

REFINEMENTS:
- [2-3 specific, actionable improvements with examples]

═══════════════════════════════════════════════════════════════════════════════
SECTION 2: SKILLS EVALUATION
═══════════════════════════════════════════════════════════════════════════════

JOB RELEVANCE: [score]/10
[2-3 sentences: Do skills match JD? Priority order correct? Most important skills first?]

COMPREHENSIVENESS: [score]/10
[2-3 sentences: Good coverage? Any gaps? Too cluttered or too sparse?]

ORGANIZATION: [score]/10
[2-3 sentences: Logical categories? Well-structured? Easy to scan?]

ACCURACY: [score]/10
[2-3 sentences: Skills appear genuine? Any keyword stuffing? Believable proficiency levels?]

SECTION SCORE: [average]/10

MISSING SKILLS FROM JD:
- [List 2-3 key skills from job description not present, or "None"]

REFINEMENTS:
- [2-3 specific improvements: reordering, additions, removals with reasoning]

═══════════════════════════════════════════════════════════════════════════════
SECTION 3: WORK EXPERIENCE EVALUATION (Sample bullets)
═══════════════════════════════════════════════════════════════════════════════

OVERALL EXPERIENCE RELEVANCE: [score]/10
[3-4 sentences: How well does work experience align with JD? Are the right projects/achievements highlighted? Do metrics demonstrate impact?]

BULLET QUALITY (Grammar, Impact, Clarity): [score]/10
[3-4 sentences: Are bullets well-written? Strong action verbs? Quantified results? Clear technical depth?]

SECTION SCORE: [average]/10

CRITICAL ISSUES:
- [Specific problems in bullets, or "None"]

REFINEMENTS:
- [2-3 specific improvements for experience bullets with examples]

═══════════════════════════════════════════════════════════════════════════════
SECTION 4: PROJECTS EVALUATION
═══════════════════════════════════════════════════════════════════════════════

PROJECT RELEVANCE: [score]/10
[3-4 sentences: Do projects align with JD? Right technologies showcased? Demonstrate required skills?]

PROJECT DESCRIPTIONS QUALITY: [score]/10
[3-4 sentences: Are project bullets clear and impactful? Technical depth appropriate? Metrics included?]

SECTION SCORE: [average]/10

REFINEMENTS:
- [2-3 specific improvements for project bullets]

═══════════════════════════════════════════════════════════════════════════════
SECTION 5: EDUCATION & OVERALL PRESENTATION
═══════════════════════════════════════════════════════════════════════════════

EDUCATION CLARITY: [score]/10
[2 sentences: Is education clearly stated? GPA highlighted? Relevant coursework if needed?]

OVERALL FORMATTING & READABILITY: [score]/10
[2-3 sentences: Is resume easy to scan? Good use of whitespace? Professional appearance?]

SECTION SCORE: [average]/10

═══════════════════════════════════════════════════════════════════════════════
OVERALL ASSESSMENT
═══════════════════════════════════════════════════════════════════════════════

SECTION SCORES:
- Summary: [score]/10
- Skills: [score]/10
- Work Experience: [score]/10
- Projects: [score]/10
- Education & Presentation: [score]/10

OVERALL RESUME SCORE: [weighted average]/10

RATING: [EXCELLENT 9-10 | VERY GOOD 8-9 | GOOD 7-8 | ACCEPTABLE 6-7 | NEEDS WORK <6]

TOP 3 STRENGTHS:
1. [Specific strength with example]
2. [Specific strength with example]
3. [Specific strength with example]

TOP 3 IMPROVEMENTS NEEDED:
1. [Specific, actionable improvement with priority]
2. [Specific, actionable improvement]
3. [Specific, actionable improvement]

READINESS ASSESSMENT:
[2-3 sentences: Is this resume ready to submit? What's the risk of submitting as-is? What must be fixed before applying?]
"""

        try:
            print(f"{Colors.BLUE}Sending comprehensive evaluation request to Gemini...{Colors.END}")
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error during evaluation: {e}"

    def run_quality_check(self):
        """Run complete quality assessment with single API call"""
        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")
        print(f"{Colors.BOLD}COMPREHENSIVE RESUME QUALITY ASSESSMENT{Colors.END}")
        print(f"{Colors.BOLD}{'=' * 80}{Colors.END}\n")

        if not self.load_files():
            return

        # Single comprehensive evaluation
        print(f"{Colors.BOLD}Running comprehensive evaluation...{Colors.END}")
        print(f"{Colors.BLUE}This may take 10-20 seconds...{Colors.END}\n")

        evaluation_result = self.evaluate_complete_resume()

        # Print results with formatting
        self._print_formatted_results(evaluation_result)

    def _print_formatted_results(self, results: str):
        """Print evaluation results with color formatting"""
        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")
        print(f"{Colors.BOLD}EVALUATION RESULTS{Colors.END}")
        print(f"{Colors.BOLD}{'=' * 80}{Colors.END}\n")

        # Parse and colorize scores
        lines = results.split('\n')
        for line in lines:
            # Color section headers
            if 'SECTION' in line and '════' not in line:
                print(f"{Colors.BOLD}{Colors.BLUE}{line}{Colors.END}")
            # Color scores
            elif '/10' in line:
                # Extract score
                try:
                    score_str = line.split('/10')[0].split(':')[-1].strip()
                    score = int(float(score_str))

                    if score >= 9:
                        color = Colors.GREEN
                    elif score >= 7:
                        color = Colors.YELLOW
                    else:
                        color = Colors.RED

                    print(f"{color}{line}{Colors.END}")
                except:
                    print(line)
            # Color critical issues
            elif 'CRITICAL ISSUES' in line or 'TOP 3 IMPROVEMENTS' in line:
                print(f"{Colors.BOLD}{Colors.RED}{line}{Colors.END}")
            # Color strengths
            elif 'TOP 3 STRENGTHS' in line:
                print(f"{Colors.BOLD}{Colors.GREEN}{line}{Colors.END}")
            # Color overall score
            elif 'OVERALL RESUME SCORE' in line or 'OVERALL ASSESSMENT' in line:
                print(f"{Colors.BOLD}{Colors.BLUE}{line}{Colors.END}")
            # Color rating
            elif 'RATING:' in line:
                if 'EXCELLENT' in line or 'VERY GOOD' in line:
                    print(f"{Colors.GREEN}{Colors.BOLD}{line}{Colors.END}")
                elif 'GOOD' in line or 'ACCEPTABLE' in line:
                    print(f"{Colors.YELLOW}{Colors.BOLD}{line}{Colors.END}")
                else:
                    print(f"{Colors.RED}{Colors.BOLD}{line}{Colors.END}")
            # Color readiness
            elif 'READINESS ASSESSMENT' in line:
                print(f"{Colors.BOLD}{Colors.BLUE}{line}{Colors.END}")
            # Color separator lines
            elif '═══' in line or '───' in line:
                print(f"{Colors.BOLD}{line}{Colors.END}")
            # Regular lines
            else:
                print(line)

        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")

def main():
    print(f"\n{Colors.BOLD}Resume Quality Checker{Colors.END}")
    print(f"{Colors.BOLD}Powered by Google Gemini 2.5 Flash (Analyzes Generated .docx){Colors.END}\n")

    # Get script directory for relative paths
    script_dir = Path(__file__).parent.resolve()
    config_dir = script_dir.parent / 'config'
    output_dir = script_dir.parent / 'output'

    # Default paths
    default_jd = config_dir / 'current_jd.txt'
    default_resume = output_dir / 'Generated_Resume.docx'

    # Parse arguments
    if len(sys.argv) == 1:
        # No arguments - use defaults
        jd_path = str(default_jd) if default_jd.exists() else None
        resume_path = str(default_resume)
        print(f"{Colors.BLUE}Using defaults:{Colors.END}")
        print(f"  JD: {jd_path if jd_path else 'None (general evaluation)'}")
        print(f"  Resume: {resume_path}\n")
    elif len(sys.argv) == 2:
        # Only JD provided
        jd_path = sys.argv[1]
        resume_path = str(default_resume)
    else:
        # Both provided
        jd_path = sys.argv[1]
        resume_path = sys.argv[2]

    # Run quality check
    checker = ResumeQualityChecker(resume_path, jd_path)
    checker.run_quality_check()

if __name__ == "__main__":
    main()
