# Resume Validation Tools

Two Python scripts for comprehensive resume validation:

1. **validate_yaml.py** - Format & constraint validation
2. **quality_checker.py** - AI-powered content quality assessment

---

## Quick Start

### Install Dependencies
```bash
pip install google-generativeai pyyaml
```

### Run Both Validators
```bash
cd D:\Git\virtual457-projects\job-application-automator\src

# Step 1: Check formatting constraints
python validate_yaml.py

# Step 2: Check content quality with AI
python quality_checker.py ../job_descriptions/waymo.txt
```

---

## 1. validate_yaml.py - Format Validator

**Checks:**
- ✅ Summary: 520-570 chars, 5-8 bold markers
- ✅ Skills: Exactly 7 categories, each 70-95 chars
- ✅ LSEG: Exactly 5 bullets, 150-200 chars, 3-5 bold each
- ✅ Infosys: Exactly 4 bullets, 150-200 chars, 3-5 bold each
- ✅ Projects: Exactly 3, tech max 80 chars, bullets max 200 chars

**Usage:**
```bash
python validate_yaml.py
python validate_yaml.py path/to/resume.yaml
```

**Output:**
- Green ✓ = Pass
- Red ✗ = Fail with fix instructions
- Exit code 0 = success, 1 = errors

---

## 2. quality_checker.py - AI Quality Assessment

**Requires:** Gemini API key (already configured in .env)

**Checks:**
- ✅ Grammar & language quality
- ✅ Flow & coherence
- ✅ Job relevance to JD
- ✅ Impact & metrics
- ✅ Professionalism
- ✅ Skills organization
- ✅ Bullet point effectiveness

**Usage:**
```bash
# Without job description
python quality_checker.py

# With job description (recommended)
python quality_checker.py job_description.txt

# Custom YAML path
python quality_checker.py jd.txt path/to/resume.yaml
```

**Output:**
```
SUMMARY EVALUATION
★★★ Score: 9/10

GRAMMAR: 9/10
FLOW: 9/10
RELEVANCE: 10/10
...

OVERALL QUALITY SCORE: 8.7/10
RATING: VERY GOOD - Minor tweaks recommended
```

---

## Recommended Workflow

**Complete validation in 2 steps:**

```bash
# Terminal 1: Format check (fast, no API calls)
python validate_yaml.py

# Terminal 2: Quality check (uses Gemini API)
python quality_checker.py waymo_jd.txt
```

**Both scripts pass → Resume is production-ready!**

---

## Files in This Directory

- `validate_yaml.py` - Format/constraint validator
- `quality_checker.py` - AI-powered quality checker
- `.env` - Gemini API key (DO NOT COMMIT TO GIT)
- `README.md` - This file

---

## API Key Setup

API key is already configured in `.env` file.

If you need to change it:
1. Get key from: https://aistudio.google.com/app/apikey
2. Edit `.env` file
3. Update `GEMINI_API_KEY=your-new-key`

**Never commit .env to git!**

---

## Cost

**validate_yaml.py:** Free (local checks)  
**quality_checker.py:** ~$0.0005 per resume (6-8 API calls)

Gemini free tier: 15 requests/minute, 1500/day

---

## Troubleshooting

**"File not found"**
- Check YAML path is correct
- Run from src directory or use absolute paths

**"GEMINI_API_KEY not found"**
- Verify .env file exists in src folder
- Check API key is valid

**"Error evaluating"**
- Check internet connection
- Verify API quota not exceeded
- Try again (API can have temporary issues)

---

## Example Complete Validation

```bash
# Format validation
$ python validate_yaml.py
✅✅✅ ZERO ERRORS - PERFECT - PRODUCTION READY ✅✅✅

# Quality validation
$ python quality_checker.py waymo_jd.txt
OVERALL QUALITY SCORE: 8.9/10
RATING: VERY GOOD - Minor tweaks recommended
✓ Resume quality is excellent - ready to submit

# All checks pass → Generate resume
$ cd ..
$ generate.bat
```

**Your life depends on these internships - use both validators!** 💯
