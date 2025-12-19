# LaTeX PDF Generation System

**NEW FEATURE:** Professional LaTeX-to-PDF resume generation! 🎉

## Quick Start

### 1. Install LaTeX Distribution

**Windows (MiKTeX - Recommended):**
```bash
winget install MiKTeX.MiKTeX
```

**Mac:**
```bash
brew install --cask mactex-no-gui
```

**Linux:**
```bash
sudo apt-get install texlive-latex-base texlive-latex-extra
```

### 2. Install Python Packages

```bash
pip install latex jinja2 pyyaml
```

### 3. Test Your Installation

```bash
python test_latex_install.py
```

Expected output:
```
✅ pdflatex is installed and working!
✅ 'latex' package installed
✅ 'jinja2' package installed
✅ 'pyyaml' package installed
✅ LaTeX compilation successful!
```

### 4. Generate Your Resume

```bash
python src/latex_generator.py
```

Output: `output/Generated_Resume.pdf`

---

## How It Works

```
config/current_application.yaml  →  Jinja2 Template  →  LaTeX  →  PDF
                                     (escapes special chars,
                                      converts **bold** to \textbf{})
```

**Workflow:**
1. Reads your YAML config (same as Word generation)
2. Escapes LaTeX special characters (&, %, $, #, _, {, }, ~, ^, \)
3. Converts `**text**` markdown bold to `\textbf{text}` LaTeX
4. Renders Jinja2 template with processed data
5. Compiles with pdflatex
6. Saves professional PDF

---

## Files Added

**New Files:**
- `templates/resume_latex_template.tex` - Jinja2 LaTeX template
- `src/latex_generator.py` - PDF generation script
- `test_latex_install.py` - Installation verification
- `LATEX_SETUP.md` - Detailed installation guide
- `LATEX_README.md` - This file

**Modified:**
- None! LaTeX generation works alongside existing Word generation

---

## Advantages of LaTeX

✅ **Professional typesetting** - Superior to Word for technical documents
✅ **Consistent formatting** - Pixel-perfect output every time
✅ **Version control friendly** - Text-based templates
✅ **ATS-compatible** - Clean, parseable PDF structure
✅ **Portable** - Same output on all platforms
✅ **Fast compilation** - 2-3 seconds typical

---

## Comparison: Word vs LaTeX

| Feature | Word (`simple_generator.py`) | LaTeX (`latex_generator.py`) |
|---------|------------------------------|------------------------------|
| **Setup** | Python only | Python + MiKTeX (4GB) |
| **Speed** | ~1 second | ~3 seconds |
| **Quality** | Good | Excellent (professional) |
| **Compatibility** | Windows Word required | Cross-platform |
| **ATS Parsing** | Good | Excellent |
| **Manual editing** | Easy (Word UI) | Requires LaTeX knowledge |

**Recommendation:** Use LaTeX for final submissions, Word for quick iterations.

---

## Troubleshooting

### "pdflatex not found"

**Windows:**
1. Install MiKTeX: `winget install MiKTeX.MiKTeX`
2. Restart terminal
3. Run `pdflatex --version` to verify

**Mac/Linux:**
- Restart terminal after installation
- Check PATH includes TeX binaries

### "Missing package" errors

**MiKTeX (Windows):**
1. Open MiKTeX Console
2. Settings → Always install missing packages
3. Try compiling again

**TeX Live (Mac/Linux):**
```bash
sudo tlmgr install <package-name>
```

### Compilation hangs

- Check for infinite loops in LaTeX code
- The script has 60-second timeout built-in
- See `output/debug_resume.tex` for problematic code

### LaTeX syntax errors

1. Check `output/debug_resume.tex` (auto-generated on errors)
2. Compile manually: `pdflatex output/debug_resume.tex`
3. See full error output

---

## Advanced Usage

### Custom Templates

Edit `templates/resume_latex_template.tex` to customize:
- Fonts
- Colors
- Spacing
- Section order
- Additional sections

**Example - Add color:**
```latex
\usepackage{xcolor}
\definecolor{myblue}{RGB}{0,102,204}

% In section headers:
\titleformat{\section}{\large\bfseries\color{myblue}}{}{0em}{}[\titlerule]
```

### Multiple Templates

Create different templates:
- `resume_latex_creative.tex` - For design roles
- `resume_latex_technical.tex` - For engineering roles
- `resume_latex_academic.tex` - For research positions

Update `src/latex_generator.py` template_path to switch.

---

## Integration with Existing Workflow

**Your current workflow (unchanged):**
```bash
# Generate YAML (manual or via Claude)
# Edit config/current_application.yaml

# Generate Word doc
python src/simple_generator.py
# Output: output/Generated_Resume.docx
```

**New LaTeX workflow (parallel):**
```bash
# Same YAML config (no changes needed)

# Generate PDF
python src/latex_generator.py
# Output: output/Generated_Resume.pdf
```

**Both use the same YAML!** No duplicate work.

---

## Next Steps

1. ✅ Run `python test_latex_install.py` to verify setup
2. ✅ Run `python src/latex_generator.py` to generate first PDF
3. ✅ Compare with Word output for quality
4. 📝 Customize `templates/resume_latex_template.tex` if needed
5. 🚀 Use LaTeX for all final submissions

---

## Support

**Issues?**
1. Check `LATEX_SETUP.md` for detailed installation steps
2. Run `test_latex_install.py` for diagnostics
3. See `output/debug_resume.tex` for LaTeX errors
4. Verify MiKTeX settings allow auto-package installation

**Questions about LaTeX syntax?**
- [Overleaf Documentation](https://www.overleaf.com/learn)
- [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX)

---

## Performance

**Typical generation times:**
- YAML parsing: <0.1s
- Template rendering: <0.1s
- LaTeX compilation: 2-3s
- **Total: ~3 seconds**

**Disk usage:**
- MiKTeX installation: ~4 GB
- TinyTeX (minimal): ~100 MB
- Template files: <10 KB
- Generated PDFs: ~50-100 KB

---

**Enjoy professional LaTeX resumes! 🎓✨**
