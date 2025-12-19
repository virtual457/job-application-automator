#!/usr/bin/env python3
"""
ATS (Applicant Tracking System) Checker - Analyzes Generated .docx Resume
Brutal keyword-matching and alignment scoring for job descriptions
Simulates real ATS systems with quantitative pass/fail scoring

Defaults:
- Job Description: ../config/current_jd.txt
- Resume: ../output/Generated_Resume.docx
- API Key: .env file in same directory as this script

Usage:
    python ats_checker.py                           # Use defaults
    python ats_checker.py job_description.txt       # Custom JD
    python ats_checker.py jd.txt resume.docx        # Custom both

Scoring:
    85-100: PASS - Strong ATS match
    70-84:  BORDERLINE - May pass, needs improvements
    <70:    FAIL - Will likely be rejected by ATS
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

class ATSChecker:
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

            # Load job description (REQUIRED for ATS)
            if self.jd_path:
                jd_path = Path(self.jd_path)
                if jd_path.exists():
                    with open(jd_path, 'r', encoding='utf-8') as f:
                        self.job_description = f.read()
                    print(f"{Colors.GREEN}✓ Job description loaded: {self.jd_path}{Colors.END}")
                else:
                    print(f"{Colors.RED}ERROR: Job description not found: {self.jd_path}{Colors.END}")
                    return False
            else:
                print(f"{Colors.RED}ERROR: Job description required for ATS analysis{Colors.END}")
                return False

            return True
        except Exception as e:
            print(f"{Colors.RED}ERROR loading files: {e}{Colors.END}")
            return False

    def analyze_ats_alignment(self) -> str:
        """Perform brutal ATS keyword matching and alignment analysis"""

        # Brutal ATS evaluation prompt
        prompt = f"""You are a strict ATS (Applicant Tracking System) evaluator. Your job is to simulate how real ATS systems score resumes based on keyword matching and alignment.

BE BRUTAL. BE QUANTITATIVE. NO HAND-HOLDING.

Real ATS systems reject 75% of resumes. You must score with the same strictness.

═══════════════════════════════════════════════════════════════════════════════
JOB DESCRIPTION:
═══════════════════════════════════════════════════════════════════════════════
{self.job_description}

═══════════════════════════════════════════════════════════════════════════════
COMPLETE RESUME (Generated .docx):
═══════════════════════════════════════════════════════════════════════════════
{self.resume_text}

═══════════════════════════════════════════════════════════════════════════════
ATS EVALUATION INSTRUCTIONS:
═══════════════════════════════════════════════════════════════════════════════

You MUST follow this EXACT format for your response:

═══════════════════════════════════════════════════════════════════════════════
SECTION 1: KEYWORD MATCHING ANALYSIS (30 points)
═══════════════════════════════════════════════════════════════════════════════

JD CRITICAL KEYWORDS EXTRACTED:
[List 15-20 most important keywords/phrases from job description that ATS would scan for]
Examples: "Python", "machine learning", "REST API", "Kubernetes", "React", "AWS Lambda"

KEYWORD MATCH RESULTS:
✓ FOUND (list each found keyword)
✗ MISSING (list each missing keyword)

KEYWORD MATCH RATE: [X]/[Y] keywords found ([Z]%)

SCORING BREAKDOWN:
- 100% match (all keywords): 30 points
- 90-99% match: 27 points
- 80-89% match: 24 points
- 70-79% match: 21 points
- 60-69% match: 18 points
- 50-59% match: 15 points
- <50% match: Proportional (0-14 points)

SECTION 1 SCORE: [score]/30

CRITICAL MISSING KEYWORDS:
[List top 5 most important missing keywords that will hurt ATS score]

═══════════════════════════════════════════════════════════════════════════════
SECTION 2: TECHNICAL SKILLS COVERAGE (25 points)
═══════════════════════════════════════════════════════════════════════════════

JD REQUIRED TECHNICAL SKILLS:
[List all technical skills mentioned in JD - languages, frameworks, tools, platforms]

SKILLS SECTION ANALYSIS:
✓ PRESENT in skills section: [list]
✗ MISSING from skills section: [list]
⚠ PRESENT elsewhere (summary/experience/projects) but NOT in skills section: [list]

SKILLS COVERAGE RATE: [X]/[Y] required skills ([Z]%)

SCORING BREAKDOWN:
- All required skills in skills section: 25 points
- 90%+ coverage: 22-24 points
- 80-89% coverage: 20-21 points
- 70-79% coverage: 17-19 points
- 60-69% coverage: 15-16 points
- <60% coverage: Proportional (0-14 points)

DEDUCTIONS:
- Required skill mentioned elsewhere but NOT in skills section: -1 point each
- Complete absence of required skill anywhere: -2 points each

SECTION 2 SCORE: [score]/25

TOP MISSING SKILLS:
[List top 3-5 required technical skills not in resume]

═══════════════════════════════════════════════════════════════════════════════
SECTION 3: EXPERIENCE ALIGNMENT (20 points)
═══════════════════════════════════════════════════════════════════════════════

JD KEY RESPONSIBILITIES/REQUIREMENTS:
[List 5-8 main responsibilities or requirements from job description]

EXPERIENCE BULLETS ALIGNMENT:
For each JD requirement, identify which resume bullets (if any) demonstrate it:

Requirement 1: [JD requirement]
→ Matched by: [specific bullets or "NONE"]

Requirement 2: [JD requirement]
→ Matched by: [specific bullets or "NONE"]

[Continue for all requirements]

ALIGNMENT RATE: [X]/[Y] requirements covered ([Z]%)

SCORING BREAKDOWN:
- 90%+ requirements covered: 18-20 points
- 80-89% coverage: 16-17 points
- 70-79% coverage: 14-15 points
- 60-69% coverage: 12-13 points
- <60% coverage: Proportional (0-11 points)

SECTION 3 SCORE: [score]/20

UNCOVERED REQUIREMENTS:
[List JD requirements with NO matching experience bullets]

═══════════════════════════════════════════════════════════════════════════════
SECTION 4: PROJECT RELEVANCE (15 points)
═══════════════════════════════════════════════════════════════════════════════

JD RELEVANT TECHNOLOGIES/DOMAINS:
[List technologies, domains, or problem areas from JD]

PROJECTS ANALYSIS:
Project 1: [title]
- Relevant technologies: [list or "NONE"]
- Relevance score: [0-5]

Project 2: [title]
- Relevant technologies: [list or "NONE"]
- Relevance score: [0-5]

Project 3: [title]
- Relevant technologies: [list or "NONE"]
- Relevance score: [0-5]

TOTAL PROJECT RELEVANCE: [sum]/15

SCORING BREAKDOWN:
- Each project scored 0-5 based on technology overlap with JD
- 0 = No relevant tech
- 1-2 = Minimal relevance (1-2 matching technologies)
- 3 = Moderate relevance (3-4 matching technologies)
- 4 = Strong relevance (5+ matching technologies)
- 5 = Perfect relevance (core JD technologies demonstrated)

SECTION 4 SCORE: [score]/15

MISSING PROJECT AREAS:
[Technologies/domains in JD that would be better demonstrated by projects]

═══════════════════════════════════════════════════════════════════════════════
SECTION 5: HARD REQUIREMENTS VERIFICATION (10 points)
═══════════════════════════════════════════════════════════════════════════════

JD HARD REQUIREMENTS:
[Extract non-negotiable requirements like: degree, GPA, citizenship, availability, years of experience, certifications]

VERIFICATION:
Requirement 1: [requirement from JD]
→ Status: ✓ MET / ✗ NOT MET / ⚠ UNCLEAR
→ Evidence: [where in resume this is verified]

Requirement 2: [requirement]
→ Status: ✓ MET / ✗ NOT MET / ⚠ UNCLEAR
→ Evidence: [location in resume]

[Continue for all hard requirements]

REQUIREMENTS MET: [X]/[Y]

SCORING BREAKDOWN:
- All hard requirements met and clearly stated: 10 points
- 1 requirement unclear but likely met: 8 points
- 1 requirement not met: 0 points (AUTO-FAIL by real ATS)
- Multiple unclear: 5-7 points

SECTION 5 SCORE: [score]/10

FAILED/UNCLEAR REQUIREMENTS:
[List any hard requirements that are not clearly met]

═══════════════════════════════════════════════════════════════════════════════
ATS FINAL SCORE CALCULATION
═══════════════════════════════════════════════════════════════════════════════

SECTION SCORES:
1. Keyword Matching:        [score]/30
2. Technical Skills:        [score]/25
3. Experience Alignment:    [score]/20
4. Project Relevance:       [score]/15
5. Hard Requirements:       [score]/10

TOTAL ATS SCORE: [sum]/100

═══════════════════════════════════════════════════════════════════════════════
ATS VERDICT
═══════════════════════════════════════════════════════════════════════════════

SCORE RANGE: [85-100 | 70-84 | Below 70]

VERDICT: [PASS ✓ | BORDERLINE ⚠ | FAIL ✗]

PASS PROBABILITY: [X]% chance of passing automated ATS screening

EXPLANATION:
[2-3 sentences explaining why this score was given and what it means for ATS screening]

═══════════════════════════════════════════════════════════════════════════════
TOP 5 ATS IMPROVEMENTS (Prioritized by Impact)
═══════════════════════════════════════════════════════════════════════════════

1. [Specific actionable improvement with expected point gain]
   Example: "Add 'React' and 'TypeScript' to skills section (+4 points)"

2. [Next highest impact improvement]

3. [Third priority]

4. [Fourth priority]

5. [Fifth priority]

═══════════════════════════════════════════════════════════════════════════════
BRUTAL TRUTH ASSESSMENT
═══════════════════════════════════════════════════════════════════════════════

[3-4 sentences of brutally honest feedback. Would a real ATS reject this resume? What are the fatal flaws? Is the candidate wasting their time applying with this resume as-is?]

If score < 70: "This resume will be AUTO-REJECTED by ATS. Do not submit."
If score 70-84: "This resume may pass ATS but is risky in competitive fields. Recommend improvements."
If score 85+: "This resume should pass ATS screening and reach human review."

═══════════════════════════════════════════════════════════════════════════════

IMPORTANT SCORING RULES:
1. Be STRICT with keyword matching - exact matches or close synonyms only
2. Skills must be in the SKILLS SECTION to count fully (not just mentioned elsewhere)
3. Missing hard requirements = AUTO-FAIL (score 0 in section 5)
4. Every missing critical keyword costs points
5. Generic experience bullets that don't match JD requirements get NO credit
6. Project technologies must overlap significantly with JD to score well
7. Total score must be honest - if resume doesn't match JD well, score <70
"""

        try:
            print(f"{Colors.BLUE}Running brutal ATS analysis...{Colors.END}")
            print(f"{Colors.BLUE}This may take 15-30 seconds...{Colors.END}\n")
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error during ATS analysis: {e}"

    def run_ats_check(self):
        """Run complete ATS alignment check"""
        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")
        print(f"{Colors.BOLD}BRUTAL ATS SCREENING SIMULATION{Colors.END}")
        print(f"{Colors.BOLD}{'=' * 80}{Colors.END}\n")

        if not self.load_files():
            return

        # Run ATS analysis
        print(f"{Colors.BOLD}Simulating ATS keyword matching and scoring...{Colors.END}")

        ats_result = self.analyze_ats_alignment()

        # Print results with formatting
        self._print_formatted_results(ats_result)

    def _print_formatted_results(self, results: str):
        """Print ATS results with color formatting"""
        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")
        print(f"{Colors.BOLD}ATS ANALYSIS RESULTS{Colors.END}")
        print(f"{Colors.BOLD}{'=' * 80}{Colors.END}\n")

        lines = results.split('\n')
        for line in lines:
            # Color section headers
            if 'SECTION' in line and '════' not in line and ':' in line:
                print(f"{Colors.BOLD}{Colors.BLUE}{line}{Colors.END}")
            # Color scores
            elif '/30' in line or '/25' in line or '/20' in line or '/15' in line or '/10' in line or '/100' in line:
                try:
                    # Extract score
                    score_part = line.split(':')[-1].strip()
                    score_str = score_part.split('/')[0].strip()
                    max_score_str = score_part.split('/')[1].split()[0].strip()
                    score = float(score_str)
                    max_score = float(max_score_str)
                    percentage = (score / max_score) * 100

                    if percentage >= 85:
                        color = Colors.GREEN
                    elif percentage >= 70:
                        color = Colors.YELLOW
                    else:
                        color = Colors.RED

                    print(f"{color}{line}{Colors.END}")
                except:
                    print(line)
            # Color checkmarks and crosses
            elif line.strip().startswith('✓'):
                print(f"{Colors.GREEN}{line}{Colors.END}")
            elif line.strip().startswith('✗'):
                print(f"{Colors.RED}{line}{Colors.END}")
            elif line.strip().startswith('⚠'):
                print(f"{Colors.YELLOW}{line}{Colors.END}")
            # Color verdict
            elif 'VERDICT:' in line:
                if 'PASS ✓' in line:
                    print(f"{Colors.GREEN}{Colors.BOLD}{line}{Colors.END}")
                elif 'BORDERLINE ⚠' in line:
                    print(f"{Colors.YELLOW}{Colors.BOLD}{line}{Colors.END}")
                elif 'FAIL ✗' in line:
                    print(f"{Colors.RED}{Colors.BOLD}{line}{Colors.END}")
                else:
                    print(f"{Colors.BOLD}{line}{Colors.END}")
            # Color total score
            elif 'TOTAL ATS SCORE' in line:
                print(f"{Colors.BOLD}{Colors.BLUE}{line}{Colors.END}")
            # Color critical sections
            elif 'CRITICAL MISSING' in line or 'BRUTAL TRUTH' in line or 'TOP 5 ATS IMPROVEMENTS' in line:
                print(f"{Colors.BOLD}{Colors.RED}{line}{Colors.END}")
            elif 'TOP MISSING' in line or 'UNCOVERED REQUIREMENTS' in line or 'MISSING PROJECT' in line or 'FAILED/UNCLEAR' in line:
                print(f"{Colors.BOLD}{Colors.YELLOW}{line}{Colors.END}")
            # Color percentage rates
            elif '%' in line and ('RATE' in line or 'COVERAGE' in line or 'PROBABILITY' in line):
                try:
                    percent_str = line.split('(')[1].split('%')[0].strip()
                    percent = float(percent_str)

                    if percent >= 85:
                        color = Colors.GREEN
                    elif percent >= 70:
                        color = Colors.YELLOW
                    else:
                        color = Colors.RED

                    print(f"{color}{line}{Colors.END}")
                except:
                    print(line)
            # Color separator lines
            elif '═══' in line or '───' in line:
                print(f"{Colors.BOLD}{line}{Colors.END}")
            # Regular lines
            else:
                print(line)

        print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")

def main():
    print(f"\n{Colors.BOLD}ATS (Applicant Tracking System) Checker{Colors.END}")
    print(f"{Colors.BOLD}Powered by Google Gemini 2.5 Flash - Brutal Mode (Analyzes .docx){Colors.END}\n")

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
        print(f"  JD: {jd_path if jd_path else 'ERROR - JD required!'}")
        print(f"  Resume: {resume_path}\n")

        if not jd_path:
            print(f"{Colors.RED}ERROR: Job description required for ATS analysis{Colors.END}")
            print(f"{Colors.YELLOW}Please provide JD path or create: {default_jd}{Colors.END}")
            sys.exit(1)
    elif len(sys.argv) == 2:
        # Only JD provided
        jd_path = sys.argv[1]
        resume_path = str(default_resume)
    else:
        # Both provided
        jd_path = sys.argv[1]
        resume_path = sys.argv[2]

    # Run ATS check
    checker = ATSChecker(resume_path, jd_path)
    checker.run_ats_check()

if __name__ == "__main__":
    main()
