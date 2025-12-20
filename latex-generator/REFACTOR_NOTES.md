# LaTeX Resume Generator - Template-Based System

**Refactored to use base template files with Jinja2!**

---

## ✅ **What Changed:**

### **Before (Hardcoded):**
```
Python script contains all LaTeX
→ Hard to modify formatting
→ One file does everything
```

### **After (Template-Based):**
```
Python script loads .tex templates
→ Easy to edit LaTeX formatting
→ Separation of concerns:
  - Python: Logic + escaping
  - Templates: LaTeX formatting
```

---

## 📂 **New Structure:**

```
latex-generator/
├── templates/              ← BASE TEMPLATES (edit these!)
│   ├── ml_fullstack.tex   ← ML + Full-Stack roles
│   ├── ml_backend.tex     ← ML Engineer with backend
│   └── backend_ml.tex     ← Backend with ML exposure
│
├── config/
│   ├── sample_config.yaml
│   └── current_application.yaml
│
├── output/
│   └── generated_resume.tex
│
└── generate_latex.py      ← Generator (loads templates)
```

---

## 🚀 **How to Use:**

### **Option 1: Default template (ml_fullstack)**
```bash
python generate_latex.py
```

### **Option 2: Specify template**
```bash
python generate_latex.py --template ml_backend
python generate_latex.py --template backend_ml
python generate_latex.py -t ml_fullstack
```

---

## 📝 **How Templates Work:**

### **Template Variables (Jinja2 syntax):**

**Variables:** `((( variable )))`
```latex
\textbf{((( header.name )))}  →  \textbf{Chandan Gowda K S}
```

**Conditionals:** `((* if ... *))`
```latex
((* if header.title *))
((( header.title ))) \\[-2pt]
((* endif *))
```

**Loops:** `((* for ... *))`
```latex
((* for skill in skills *))
\textbf{((( skill.category )))} & ((( skill.items ))) \\
((* endfor *))
```

---

## 🎨 **Customizing Templates:**

### **Edit Education Coursework:**

Open `templates/ml_fullstack.tex` and find:
```latex
\textit{Relevant Coursework:} Machine Learning, NLP, Web Development...
```

Change to whatever you want:
```latex
\textit{Relevant Coursework:} Deep Learning, Computer Vision, Databases
```

### **Change Spacing:**

```latex
% More space after header
\vspace{-10pt}  →  \vspace{-5pt}

% More space between skill categories
\\[3pt]  →  \\[5pt]
```

### **Different Font:**

Add to preamble:
```latex
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
```

---

## 🔧 **Template Differences:**

| Section | ml_fullstack | ml_backend | backend_ml |
|---------|-------------|-----------|-----------|
| **Education Courses** | ML, NLP, Web Dev | ML, Deep Learning, NLP | Algorithms, DB, Web Dev |
| **Skills Emphasis** | AI + Web balanced | AI first, Backend second | Backend first, AI second |
| **Typical Projects** | LMARO, Dino, Kambaz | LMARO, Dino, Face Recognition | Orion, LMARO, Calendly |

**All use same YAML structure - just different presentation!**

---

## 💡 **Workflow:**

```
1. Edit YAML (once per application)
   config/current_application.yaml

2. Choose template based on role
   python generate_latex.py --template ml_backend

3. Copy to Overleaf
   output/generated_resume.tex

4. Download PDF
```

---

## ✨ **Benefits:**

✅ **Easy customization** - Edit .tex templates directly
✅ **Multiple templates** - Switch with command flag
✅ **Same YAML** - One config works for all templates
✅ **Clean separation** - Python does escaping, templates do formatting
✅ **Version control** - Templates are text files

---

## 🎯 **Next Steps:**

1. **Test default template:**
   ```bash
   python generate_latex.py
   ```

2. **Try different template:**
   ```bash
   python generate_latex.py --template ml_backend
   ```

3. **Customize templates:**
   - Edit `templates/*.tex` files
   - Change coursework, spacing, fonts
   - Save and regenerate

---

**System refactored and ready!** 🚀

See `README.md` for full documentation.
