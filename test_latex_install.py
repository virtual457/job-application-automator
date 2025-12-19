"""
Test LaTeX Installation

Quick script to verify pdflatex is installed and working.
Run this before attempting to generate resumes.

Usage:
    python test_latex_install.py
"""

import subprocess
import sys
from pathlib import Path


def test_pdflatex():
    """Test if pdflatex is accessible."""
    print("🔍 Testing pdflatex installation...")
    
    try:
        result = subprocess.run(
            ['pdflatex', '--version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            print("✅ pdflatex is installed and working!")
            version_line = result.stdout.split('\n')[0]
            print(f"   Version: {version_line}")
            return True
        else:
            print("❌ pdflatex returned an error")
            print(result.stderr)
            return False
            
    except FileNotFoundError:
        print("❌ pdflatex not found in PATH")
        print("\n📋 Installation needed:")
        print("   Windows: Install MiKTeX from https://miktex.org/")
        print("   Mac:     brew install --cask mactex-no-gui")
        print("   Linux:   sudo apt-get install texlive-latex-base")
        print("\n📖 See LATEX_SETUP.md for detailed instructions")
        return False
        
    except subprocess.TimeoutExpired:
        print("❌ pdflatex timed out")
        return False
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def test_python_packages():
    """Test if required Python packages are installed."""
    print("\n🔍 Testing Python packages...")
    
    packages_ok = True
    
    # Test latex package
    try:
        import latex
        print("✅ 'latex' package installed")
    except ImportError:
        print("❌ 'latex' package not found")
        print("   Install: pip install latex")
        packages_ok = False
    
    # Test jinja2
    try:
        import jinja2
        print("✅ 'jinja2' package installed")
    except ImportError:
        print("❌ 'jinja2' package not found")
        print("   Install: pip install jinja2")
        packages_ok = False
    
    # Test pyyaml
    try:
        import yaml
        print("✅ 'pyyaml' package installed")
    except ImportError:
        print("❌ 'pyyaml' package not found")
        print("   Install: pip install pyyaml")
        packages_ok = False
    
    return packages_ok


def test_simple_compilation():
    """Test a simple LaTeX compilation."""
    print("\n🔍 Testing LaTeX compilation...")
    
    simple_tex = r"""
\documentclass{article}
\begin{document}
Hello, LaTeX!
\end{document}
"""
    
    try:
        from latex import build_pdf
        
        pdf = build_pdf(simple_tex)
        print("✅ LaTeX compilation successful!")
        print(f"   Generated {len(bytes(pdf))} bytes PDF")
        return True
        
    except Exception as e:
        print(f"❌ Compilation failed: {e}")
        return False


def main():
    print("=" * 60)
    print("LaTeX Installation Test")
    print("=" * 60)
    
    # Test 1: pdflatex binary
    pdflatex_ok = test_pdflatex()
    
    # Test 2: Python packages
    packages_ok = test_python_packages()
    
    # Test 3: Simple compilation (only if previous tests pass)
    compilation_ok = False
    if pdflatex_ok and packages_ok:
        compilation_ok = test_simple_compilation()
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    print(f"pdflatex binary:       {'✅ OK' if pdflatex_ok else '❌ FAILED'}")
    print(f"Python packages:       {'✅ OK' if packages_ok else '❌ FAILED'}")
    print(f"LaTeX compilation:     {'✅ OK' if compilation_ok else '❌ FAILED' if pdflatex_ok and packages_ok else '⏭️  SKIPPED'}")
    
    if pdflatex_ok and packages_ok and compilation_ok:
        print("\n🎉 All tests passed! You're ready to generate resumes.")
        print("   Run: python src/latex_generator.py")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please fix issues above before continuing.")
        print("   See LATEX_SETUP.md for installation instructions.")
        return 1


if __name__ == '__main__':
    sys.exit(main())
