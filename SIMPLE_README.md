# Simple Resume Generator - Quick Start

## 🚀 How It Works

1. Edit content in `config/current_application.yaml`
2. Run `generate.bat` (or `python src/simple_generator.py`)
3. Get your tailored resume in `output/Generated_Resume.docx`

## 📝 Step-by-Step

### Step 1: Edit the YAML file

Open `config/current_application.yaml` and edit:

```yaml
header:
  name: "Your Name"
  title: "Software Engineer | MS CS @ Northeastern | Your Key Skills"
  contact: "phone; email; LinkedIn; Portfolio; GitHub;"

summary: "Your summary paragraph mentioning the company..."

skills:
  - category: "Programming Language"
    items: "Python, Java, C++"
  # ... more skills

projects:
  - title: "Project Name"
    tech: "Tech1, Tech2, Tech3"
    github: "GitHub"
    bullet1: "First achievement bullet point..."
    bullet2: "Second achievement bullet point..."
```

### Step 2: Generate Resume

**Windows:**
```
generate.bat
```

**Or directly:**
```
cd src
python simple_generator.py
```

### Step 3: Review Output

Open `output/Generated_Resume.docx` and review:
- ✅ Header (name, title, contact)
- ✅ Summary paragraph
- ✅ Technical Skills (7 categories)
- ✅ Projects (3 projects with 2 bullets each)
- ✅ Work Experience (unchanged from template)

## 📋 Character Limits

Based on your resume format:

- **Header title:** ~100 characters
- **Summary:** ~600 characters (~100 words)
- **Skills items:** ~100 characters after category name
- **Project bullet:** ~200 characters (fits in 2 lines)

## 🎯 Workflow

**For each job application:**

1. Get the job description
2. Edit `current_application.yaml` with optimized content
3. Run `generate.bat`
4. Review `output/Generated_Resume.docx`
5. Save as PDF and apply!

## ⚠️ Important

- The template must be at: `templates/Chandan_Resume_Format.docx`
- Work experience section is NOT modified (stays from template)
- Education section is NOT modified (stays from template)
- Only updates: header, summary, skills, projects

## 🔧 Troubleshooting

**Error: Template not found**
- Make sure `Chandan_Resume_Format.docx` is in `templates/` folder

**Formatting looks wrong**
- Open template and generated file side-by-side
- Check if paragraph structure matches
- May need to adjust script's paragraph indices

**Skills not updating**
- Make sure you have exactly 7 skill categories in YAML
- Check that template has "TECHNICAL SKILLS" heading

## 📌 Next Steps

After testing with one application:
1. Refine the YAML content format
2. Add JD analysis to auto-generate YAML
3. Batch process multiple applications
