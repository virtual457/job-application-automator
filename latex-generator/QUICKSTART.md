# LaTeX Generator - Quick Start Guide

## ✅ System Ready!

Your LaTeX resume generation system is set up and ready to use.

---

## 📂 What You Have

```
latex-generator/
├── config/
│   └── sample_config.yaml          ← Example format
├── output/
│   └── (generated files appear here)
├── generate_latex.py               ← Run this!
└── README.md                       ← Full documentation
```

---

## 🚀 How to Use (3 Steps)

### Step 1: Create Your Config

```bash
cd latex-generator/config
# Copy sample to start
cp sample_config.yaml current_application.yaml

# Edit current_application.yaml with your data
```

### Step 2: Generate LaTeX

```bash
cd latex-generator
python generate_latex.py
```

**Output:**
```
============================================================
📄 LaTeX Resume Generator
============================================================

📖 Reading YAML: current_application.yaml
   Company: Luca IQ

🔧 Generating LaTeX sections...
   Generated 8,234 characters

✅ LaTeX generation complete!

💾 Saved LaTeX to: generated_resume.tex
   Full path: D:\...\output\generated_resume.tex

============================================================
🚀 Next Steps:
============================================================
1. Open Overleaf (https://overleaf.com)
2. Create new blank project
3. Copy-paste content from output/generated_resume.tex
4. Download PDF

✨ Done!
```

### Step 3: Use in Overleaf

1. Open `output/generated_resume.tex` in any text editor
2. Copy ALL content (Ctrl+A, Ctrl+C)
3. Go to Overleaf → New Project → Blank
4. Delete everything in Overleaf editor
5. Paste your LaTeX code
6. Wait 3 seconds for compilation
7. Download PDF!

---

## 🎯 YAML Format

**Required sections:**
- `header` (name, title, contact)
- `skills` (7 categories)
- `experience` (LSEG + Infosys)
- `projects` (3 projects)

**See `config/sample_config.yaml` for complete example.**

---

## 💡 Tips

### Bold Markers
```yaml
bullets:
  - "Built **scalable services** with **Python**"
```
Auto-converts to: `\textbf{scalable services}` and `\textbf{Python}`

### No Summary Section
Education comes first (after header) - saves space for one-page resume.

### Fixed Achievements
AWS certification and IEEE paper automatically included at the end.

---

## ⚡ Workflow

```
Edit YAML → Run Python → Copy to Overleaf → Download PDF
  (5 min)     (instant)      (2 min)          (instant)
```

**Total time: ~7 minutes from YAML to final PDF!**

---

## 🎓 What's Next?

**For your first resume:**
1. Use `sample_config.yaml` as starting point
2. Update with Luca IQ data (ML + Full-Stack template)
3. Generate and test in Overleaf
4. Download PDF and review

**For future resumes:**
1. Edit `current_application.yaml` for new company
2. Run generator
3. Done!

---

**System ready to use!** 🚀

See `README.md` for full documentation.
