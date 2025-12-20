# LaTeX Resume Generator

**Simple YAML → LaTeX converter for professional resumes**

Generate clean LaTeX code from YAML configs, ready to paste into Overleaf.

---

## 🚀 Quick Start (3 Steps)

### 1. Create your YAML config

```bash
cd latex-generator/config
cp sample_config.yaml current_application.yaml
# Edit current_application.yaml with your data
```

### 2. Generate LaTeX

```bash
cd latex-generator
python generate_latex.py
```

### 3. Use in Overleaf

```
Output: output/generated_resume.tex

1. Open the file in text editor
2. Copy all content (Ctrl+A, Ctrl+C)
3. Go to https://overleaf.com
4. New Project → Blank Project
5. Delete everything in editor
6. Paste your LaTeX code
7. Wait ~3 seconds for compilation
8. Download PDF!
```

---

## 📂 Folder Structure

```
latex-generator/
├── config/
│   ├── sample_config.yaml          ← Example YAML
│   └── current_application.yaml    ← Create this!
│
├── templates/
│   └── base_template.tex           ← Generic LaTeX template
│
├── output/
│   └── generated_resume.tex        ← Generated LaTeX
│
├── generate_latex.py               ← Generator script
├── README.md                       ← This file
└── CONSTRAINTS.md                  ← Field rules and limits
```

---

## ✨ How It Works

```
Your YAML → Python Generator → LaTeX Code → Overleaf → PDF
  (edit)    (escapes **bold**)   (paste)     (compile)
```

**Magic:**
- Converts `**text**` to `\textbf{text}`
- Escapes special chars (&, %, $, #, etc.)
- Uses ONE generic template
- Customize everything via YAML

---

## 🎯 Customizing for Different Roles

**All customization happens in YAML - ONE template fits all!**

### For ML Roles (Luca IQ):
```yaml
education:
  ms_coursework: "Machine Learning, NLP, Deep Learning, Database Management"

skills:
  - category: "AI & ML"  # Put AI first
    items: "PyTorch, TensorFlow, Deep Learning..."
  
  - category: "Backend Development"  # Backend second
    items: "FastAPI, Flask, REST APIs..."

projects:
  # LMARO, Dino RL, Kambaz (ML + Full-Stack)
```

### For Backend Roles:
```yaml
education:
  ms_coursework: "Advanced Algorithms & Data Structures, Database Management, Web Development"

skills:
  - category: "Backend Development"  # Backend first
    items: "Microservices, Spring Boot, REST APIs..."
  
  - category: "AI & ML"  # AI later
    items: "PyTorch, TensorFlow..."

projects:
  # Orion Platform, LMARO, Calendly (Backend focus)
```

### For Cloud/Infrastructure:
```yaml
skills:
  - category: "Cloud Platforms"  # Cloud first
    items: "AWS, Kubernetes, Docker..."
  
  - category: "Infrastructure & DevOps"  # DevOps second
    items: "Terraform, Jenkins, CI/CD..."

projects:
  # Orion Platform, LMARO (infra), Dino RL
```

**Same template, different YAML = different resume focus!**

---

## 📋 YAML Format

See `config/sample_config.yaml` for complete example.

**Required sections:**
1. `header` - Name, title, contact
2. `company_name` - Target company
3. `education` - MS and BE coursework
4. `skills` - 7 categories (exactly)
5. `experience` - LSEG (5 bullets) + Infosys (4 bullets)
6. `projects` - 3 projects with 2 bullets each

**Constraints:** See `CONSTRAINTS.md` for all field limits and rules.

---

## 💡 Pro Tips

### Bold Markers
```yaml
bullets:
  - "Built **scalable services** with **Python** processing **7.5M+ records**"
```
Auto-converts to LaTeX: `\textbf{scalable services}`

### Special Characters
Write normally in YAML:
```yaml
items: "C++, 50% improvement, R&D"
```
Generator escapes automatically: `C\+\+`, `50\%`, `R\&D`

### Contact Line
Use raw LaTeX (already formatted):
```yaml
contact: "+1 (123) 456-7890 \\textbar\\ \\href{mailto:email}{email}"
```

---

## ⚡ Workflow

```
1. Edit current_application.yaml (5 min)
   - Change skills order for role type
   - Update coursework
   - Select relevant projects

2. Generate LaTeX (instant)
   python generate_latex.py

3. Paste in Overleaf (2 min)
   - Copy output/generated_resume.tex
   - Paste in Overleaf
   - Download PDF

Total: ~7 minutes per application
```

---

## 🔧 Dependencies

```bash
pip install jinja2 pyyaml
```

---

## 🎓 Next Steps

1. ✅ Copy sample_config.yaml to current_application.yaml
2. ✅ Edit with your data for Luca IQ
3. ✅ Run: `python generate_latex.py`
4. ✅ Paste in Overleaf
5. ✅ Download professional PDF!

---

**Simple, clean, professional resumes in minutes!** 🚀

For detailed field requirements, see `CONSTRAINTS.md`.
