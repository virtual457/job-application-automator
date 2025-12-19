# LaTeX PDF Generation Setup Guide

**Last Updated:** December 15, 2025

This guide helps you set up LaTeX-to-PDF generation for professional resumes.

---

## Windows Installation (Choose ONE)

### Option 1: MiKTeX (Recommended for Windows)

**Download & Install:**
```bash
# Using winget (Windows 11/10)
winget install MiKTeX.MiKTeX

# OR download installer from: https://miktex.org/download
```

**Configure for automatic package installation:**
1. Open MiKTeX Console
2. Go to Settings → General
3. Set "Install missing packages" to "Always"

**Install required packages:**
```bash
# Open MiKTeX Console → Packages → Search and install:
# - geometry
# - enumitem
# - hyperref
# - titlesec
# - tabularx
```

### Option 2: TinyTeX (Lighter weight - 100MB)

```bash
pip install pytinytex
python -c "import pytinytex; pytinytex.download_tinytex()"
```

---

## Mac Installation

```bash
# Using Homebrew
brew install --cask mactex-no-gui

# OR minimal version
brew install --cask basictex
```

---

## Linux Installation

```bash
# Ubuntu/Debian
sudo apt-get install texlive-latex-base texlive-latex-extra

# Fedora
sudo dnf install texlive-scheme-basic texlive-collection-latexextra
```

---

## Python Package Installation

```bash
# Install LaTeX compilation library
pip install latex

# Install Jinja2 for templating (if not already installed)
pip install jinja2
```

---

## Verify Installation

Run this to test your LaTeX installation:

```python
# test_latex.py
import subprocess
import sys

try:
    result = subprocess.run(['pdflatex', '--version'], 
                          capture_output=True, text=True, timeout=5)
    if result.returncode == 0:
        print("✅ pdflatex is installed and working!")
        print(result.stdout.split('\n')[0])
    else:
        print("❌ pdflatex returned an error")
        sys.exit(1)
except FileNotFoundError:
    print("❌ pdflatex not found. Please install MiKTeX or TeX Live.")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
```

Run: `python test_latex.py`

---

## Troubleshooting

### "pdflatex not found"
- **Windows:** Add MiKTeX to PATH: `C:\Program Files\MiKTeX\miktex\bin\x64\`
- **Mac/Linux:** Restart terminal after installation

### "Missing package" errors
- **MiKTeX:** Should auto-install packages (check Console settings)
- **TeX Live:** Run `tlmgr install <package-name>`

### Compilation hangs
- Check for infinite loops in LaTeX code
- Use `-interaction=nonstopmode` flag

### Permission errors (Windows)
- Run MiKTeX Console as Administrator once
- Allow automatic package installation

---

## Next Steps

Once installation is verified:
```bash
python src/latex_generator.py
```

This will generate `output/Generated_Resume.pdf` from `config/current_application.yaml`

---

## Disk Space Requirements

- **MiKTeX (full):** ~4 GB
- **MiKTeX (basic + packages):** ~500 MB
- **TinyTeX:** ~100 MB
- **TeX Live:** ~5 GB
