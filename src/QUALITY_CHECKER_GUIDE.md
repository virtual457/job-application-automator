# Quality Checker - Quick Start Guide

## ✅ Setup Complete!

All files are configured and ready to use:

```
job-application-automator/
├── src/
│   ├── quality_checker.py     ✅ AI quality evaluator
│   ├── validate_yaml.py       ✅ Format validator
│   └── .env                   ✅ Gemini API key configured
├── config/
│   ├── current_application.yaml    ✅ Your resume YAML
│   └── current_jd.txt              ✅ Current job description (UPDATE THIS)
```

---

## 🚀 How to Use

### Step 1: Update Job Description
```bash
# Edit this file with the actual JD you're applying to:
notepad config\current_jd.txt
```

### Step 2: Run Validators
```bash
cd src

# Format validation (fast, no API)
python validate_yaml.py

# Quality check (AI-powered)
python quality_checker.py
```

**Both use defaults automatically!**
- Job description: `../config/current_jd.txt`
- Resume YAML: `../config/current_application.yaml`
- API key: `.env` in src folder

---

## 📋 Usage Examples

### Default (No Arguments)
```bash
cd src
python quality_checker.py
# Uses: ../config/current_jd.txt and ../config/current_application.yaml
```

### Custom Job Description
```bash
python quality_checker.py waymo_jd.txt
# Uses: waymo_jd.txt and ../config/current_application.yaml
```

### Custom Both
```bash
python quality_checker.py jd.txt path/to/resume.yaml
```

---

## 🔄 Typical Workflow

1. **Get job description** → Copy/paste to `config/current_jd.txt`
2. **Generate YAML** → Claude creates `config/current_application.yaml`
3. **Validate format** → `python validate_yaml.py`
4. **Check quality** → `python quality_checker.py`
5. **Both pass** → `cd .. && generate.bat`
6. **Apply!**

---

## ⚙️ What Gets Checked

### validate_yaml.py (Format)
- Character limits (summary, bullets, skills)
- Bold marker counts
- Required sections
- Structure compliance

### quality_checker.py (Quality)
- Grammar & language
- Flow & coherence
- Job relevance
- Impact & metrics
- Professionalism

---

## 📊 Score Interpretation

**9-10:** Excellent - Production ready ⭐⭐⭐  
**8-9:** Very good - Minor tweaks ⭐⭐  
**7-8:** Good - Some improvements ⭐  
**6-7:** Acceptable - Significant work needed ⚠  
**<6:** Needs major revisions ❌

---

## 🔧 Troubleshooting

**"GEMINI_API_KEY not found"**
- Check `.env` file exists in `src/` folder
- Verify API key is correct

**"File not found"**
- Make sure you're in `src/` directory when running
- Or use absolute paths

**"Error evaluating"**
- Check internet connection
- Verify Gemini API quota

---

## 💡 Pro Tips

1. **Always update current_jd.txt** before quality check
2. **Run validate_yaml.py first** (catches format issues fast)
3. **Then run quality_checker.py** (AI gives content feedback)
4. **Focus on lowest scores** when improving

---

## API Key Setup

Your Gemini API key is already configured in `src/.env`

If you need to update it:
1. Get new key: https://aistudio.google.com/app/apikey
2. Edit `src/.env`
3. Update `GEMINI_API_KEY=your-new-key`

**Never commit .env to git!**

---

**Your quality checker is ready to use!** 🚀
