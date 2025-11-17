# Quick Start Guide

## Installation

1. **Install dependencies:**
```bash
cd D:\Git\virtual457-projects\job-application-automator
pip install -r requirements.txt
```

2. **Initialize the project:**
```bash
cd src
python main.py init
```

3. **Copy your base resume:**
   - Take your current resume (Chandan_Resume_Base.docx)
   - Copy it to: `templates/base_resume.docx`

## Usage

### Generate a Single Resume

```bash
# Backend role at Salesforce
python main.py generate-resume --company Salesforce --role backend

# ML role at ByteDance
python main.py generate-resume --company ByteDance --role ml

# Algorithms role at IBM
python main.py generate-resume --company IBM --role algorithms
```

### Generate Multiple Resumes at Once

```bash
# Generate all 15 Week 1 applications
python main.py batch-generate ../config/week1_applications.yaml
```

### List Available Role Types

```bash
python main.py list-roles
```

**Output:**
```
📋 Available Role Types:

  • backend
  • ml
  • data
  • algorithms
  • general
```

### View Statistics

```bash
python main.py stats
```

**Output:**
```
📊 Resume Generation Statistics

Total Resumes Generated: 15

By Role Type:
  • backend       : 9
  • ml            : 4
  • algorithms    : 2

Top Companies:
  • Salesforce    : 1
  • Intuit        : 1
  • ByteDance     : 1
  ...
```

## Configuration

### Customize Role Templates

Edit `config/resume_config.yaml` to modify:
- Headers
- Summary templates
- Technical skills ordering
- Project preferences

### Create Custom Batch Files

Create new YAML files in `config/` directory:

```yaml
# config/my_applications.yaml
applications:
  - company: CompanyName
    role_type: backend
  
  - company: AnotherCompany
    role_type: ml
```

Then run:
```bash
python main.py batch-generate ../config/my_applications.yaml
```

## Output

All generated resumes are saved to:
```
output/resumes/Chandan_Resume_[Company]_[RoleType].docx
```

Generation log:
```
output/generation_log.txt
```

## Tips

1. **Always review generated resumes** before submitting
2. **Manually reorder projects** in Word if needed (automation handles skills/summary)
3. **Keep your base template clean** - no company-specific content
4. **Track applications** separately (we'll add tracking module soon)

## Troubleshooting

### Error: Template not found
```
❌ Error: Template not found at templates/base_resume.docx
💡 Create a base resume template first!
```

**Solution:** Copy your resume to `templates/base_resume.docx`

### Error: Unknown role type
```
ValueError: Unknown role type: xyz. Available: ['backend', 'ml', 'data', 'algorithms', 'general']
```

**Solution:** Use one of the available role types listed by `python main.py list-roles`

## Next Steps

1. Generate first 15 resumes for Week 1
2. Manually review and adjust if needed
3. Apply to companies through career pages
4. Track applications (coming soon: application tracker module)

---

**Goal:** 75+ applications by November 30, 2025
**Progress tracking:** Check `output/generation_log.txt`
