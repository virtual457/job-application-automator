# Quick Reference: Using the Resume Generator

## 🚀 Basic Workflow

1. **Paste JD to Claude/LLM**
2. **Get YAML content** (optimized for that role)
3. **Copy YAML to:** `config/current_application.yaml`
4. **Run:** `python simple_generator.py` (or double-click `generate.bat`)
5. **Review** in Word (opens automatically)
6. **Save as PDF** and apply!

---

## 📝 What to Tell the LLM

**Simple prompt:**
```
Here's a job description for [Company] [Role]. 

Create optimized YAML content for my resume generator following the guide in LLM_GUIDE_YAML_CREATION.md

[PASTE JD HERE]
```

**The LLM will give you:**
- Tailored header
- Optimized summary (540-590 chars with bold markers)
- Reordered skills (7 categories)
- Best 3 projects for this role (with bold markers)

---

## 🎯 Character Limits Quick Reference

| Section | Max Limit | Notes |
|---------|-----------|-------|
| Header title | 100 chars | Role \| School \| Skills |
| Summary | 580 chars | Reduced for bold formatting |
| Skill category | 35 chars | Category name |
| Skill items | ~100 chars | After tab alignment |
| Project tech | 80 chars | Bold-italic formatted |
| Project bullet | 200 chars | ~2 lines, use bold markers |

---

## ⚡ Bold Markers

**Use `**text**` to bold important terms:**

```yaml
summary: "Experience at **LSEG** processing **7.5M+ records**"
bullet1: "Built **AWS Lambda** achieving **40% improvement**"
```

**What to bold:**
- Metrics: `**7.5M+**`, `**40%**`, `**99.9%**`
- Technologies: `**Python**`, `**Kubernetes**`, `**AWS Lambda**`
- Scale: `**180+ countries**`, `**52 source files**`
- Company/School: `**LSEG**`, `**Northeastern**`

---

## 🎨 Project Name Must Match

**Use exact names from this list:**
- `Dino Game Deep RL Agent`
- `Orion PaaS` or `Orion Platform`
- `Calendly - Calendar Management System` or `Calendly`
- `Maritime Logistics Platform`
- `Large Scale Data Analysis`
- `Face Recognition & Validation System`
- `Online Examination System`

**These are pre-configured with GitHub URLs for auto-hyperlinking.**

---

## 🔧 Generated Resume Features

**Automatic formatting:**
- ✅ Hyperlinked email, LinkedIn, Portfolio, GitHub
- ✅ Hyperlinked project titles and GitHub links
- ✅ Bold skill categories, regular items
- ✅ Bold project titles, bold-italic tech stacks
- ✅ Bold markers rendered correctly
- ✅ Aligned skills section
- ✅ Font size 10 throughout
- ✅ Opens in Word automatically

---

## 📊 Application Tracking

After generating resume:
1. Review formatting in Word
2. Save as PDF: `Chandan_Resume_[Company].pdf`
3. Apply through company career page
4. Send 3 referral requests on LinkedIn
5. Log in tracking sheet

---

## 🎯 Target: 75+ Applications by Nov 30

**Week 1:** 15 applications (Nov 16-17)
**Week 2:** 30 applications (Nov 18-24)
**Week 3:** 30 applications (Nov 25-30)

**Each application:** 12-15 minutes total
- Get YAML from LLM: 2 mins
- Generate resume: 1 min
- Review: 3 mins
- Apply: 5 mins
- Request referral: 4 mins

---

**System is production-ready. Start applying! 🚀**
