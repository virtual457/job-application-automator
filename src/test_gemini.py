#!/usr/bin/env python3
"""
Gemini API Tester
Tests your Gemini API key and basic functionality

Usage:
    python test_gemini.py
"""

import os
import sys
from pathlib import Path

# ANSI colors
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

def load_api_key():
    """Load API key from .env file"""
    script_dir = Path(__file__).parent.resolve()
    env_file = script_dir / '.env'
    
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key and env_file.exists():
        print(f"{Colors.BLUE}Reading API key from: {env_file}{Colors.END}")
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line.startswith('GEMINI_API_KEY='):
                    api_key = line.split('=', 1)[1].strip()
                    break
    
    return api_key

def test_gemini_api():
    """Test Gemini API connection and functionality"""
    print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")
    print(f"{Colors.BOLD}GEMINI API TESTER{Colors.END}")
    print(f"{Colors.BOLD}{'=' * 80}{Colors.END}\n")
    
    # Test 1: Load API key
    print(f"{Colors.BOLD}TEST 1: Loading API Key{Colors.END}")
    api_key = load_api_key()
    
    if not api_key:
        print(f"{Colors.RED}✗ FAILED: API key not found{Colors.END}")
        print(f"\nCreate .env file in src/ directory with:")
        print(f"  GEMINI_API_KEY=your-key-here")
        return False
    
    print(f"{Colors.GREEN}✓ PASSED: API key loaded{Colors.END}")
    print(f"  Key: {api_key[:20]}...{api_key[-10:]}")
    
    # Test 2: Import google-generativeai
    print(f"\n{Colors.BOLD}TEST 2: Importing google-generativeai{Colors.END}")
    try:
        import google.generativeai as genai
        print(f"{Colors.GREEN}✓ PASSED: Package imported successfully{Colors.END}")
    except ImportError as e:
        print(f"{Colors.RED}✗ FAILED: {e}{Colors.END}")
        print(f"\nInstall with:")
        print(f"  pip install google-generativeai")
        return False
    
    # Test 3: Configure API
    print(f"\n{Colors.BOLD}TEST 3: Configuring Gemini API{Colors.END}")
    try:
        genai.configure(api_key=api_key)
        print(f"{Colors.GREEN}✓ PASSED: API configured{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}✗ FAILED: {e}{Colors.END}")
        return False
    
    # Test 4: Create model
    print(f"\n{Colors.BOLD}TEST 4: Creating Gemini Model{Colors.END}")
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        print(f"{Colors.GREEN}✓ PASSED: Model created (gemini-2.5-flash){Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}✗ FAILED: {e}{Colors.END}")
        return False
    
    # Test 5: Simple generation test
    print(f"\n{Colors.BOLD}TEST 5: Testing Content Generation{Colors.END}")
    print(f"{Colors.BLUE}Sending test prompt...{Colors.END}")
    
    try:
        response = model.generate_content("Say 'Hello! API is working!' in exactly 5 words.")
        response_text = response.text.strip()
        
        print(f"{Colors.GREEN}✓ PASSED: Content generated successfully{Colors.END}")
        print(f"\n{Colors.BOLD}Response:{Colors.END}")
        print(f"  {response_text}")
        
    except Exception as e:
        print(f"{Colors.RED}✗ FAILED: {e}{Colors.END}")
        print(f"\nPossible issues:")
        print(f"  - Invalid API key")
        print(f"  - API quota exceeded")
        print(f"  - Network connection issue")
        return False
    
    # Test 6: Resume evaluation test
    print(f"\n{Colors.BOLD}TEST 6: Testing Resume Evaluation{Colors.END}")
    print(f"{Colors.BLUE}Testing resume evaluation prompt...{Colors.END}")
    
    test_summary = """MS Computer Science student at Northeastern (**3.89 GPA**) with production experience building **scalable backend systems** at **London Stock Exchange Group**. Proficient in **Python (4+ years), Java**, with expertise in AWS, Kubernetes. Engineered systems processing **7.5M+ records daily** with **99.9% reliability**. Excited to build innovative products at Amazon."""
    
    prompt = f"""Evaluate this resume summary on grammar quality (0-10):

{test_summary}

Respond with just:
GRAMMAR: [score]/10
[One sentence feedback]"""
    
    try:
        response = model.generate_content(prompt)
        response_text = response.text.strip()
        
        print(f"{Colors.GREEN}✓ PASSED: Resume evaluation working{Colors.END}")
        print(f"\n{Colors.BOLD}Sample Evaluation:{Colors.END}")
        print(f"  {response_text}")
        
    except Exception as e:
        print(f"{Colors.RED}✗ FAILED: {e}{Colors.END}")
        return False
    
    # Final summary
    print(f"\n{Colors.BOLD}{'=' * 80}{Colors.END}")
    print(f"{Colors.GREEN}{Colors.BOLD}✅ ALL TESTS PASSED{Colors.END}")
    print(f"{Colors.BOLD}{'=' * 80}{Colors.END}\n")
    
    print(f"{Colors.BOLD}Your Gemini API is fully configured and working!{Colors.END}")
    print(f"\n{Colors.BOLD}Next steps:{Colors.END}")
    print(f"  1. Update config/current_jd.txt with actual job description")
    print(f"  2. Run: python quality_checker.py")
    print(f"  3. Review quality scores and suggestions")
    
    print(f"\n{Colors.GREEN}✓ Ready to evaluate resumes!{Colors.END}\n")
    return True

if __name__ == "__main__":
    success = test_gemini_api()
    sys.exit(0 if success else 1)
