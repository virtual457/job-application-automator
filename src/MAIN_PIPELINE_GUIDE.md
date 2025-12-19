# Main Pipeline - Complete Resume Workflow

## 🎯 **What It Does**

The `main.py` script orchestrates your entire resume generation and validation workflow in one command:

1. ✅ **Validate YAML** → Check constraints (chars, bold markers, structure)
2. ✅ **Generate Resume** → Create DOCX from YAML
3. ✅ **Quality Check** → Content quality + visual formatting (PDF)
4. ✅ **ATS Check** → Keyword matching + visual compatibility (PDF)

---

## 🚀 **Quick Start**

```bash
cd D:\Git\virtual457-projects\job-application-automator\src

# Run complete pipeline
python main.py
```

That's it! The script will:
- Validate `config/current_application.yaml`
- Generate `output/Generated_Resume.docx`
- Convert to `output/Generated_Resume.pdf`
- Run quality analysis
- Run ATS analysis
- Show final summary

---

## 📋 **Command Options**

```bash
# Run full pipeline (recommended)
python main.py

# Skip YAML validation (if you already validated)
python main.py --skip-validation

# Skip generation (if DOCX already exists)
python main.py --skip-generation

# Skip quality check (faster, skip content analysis)
python main.py --skip-quality

# Skip ATS check (faster, skip keyword analysis)
python main.py --skip-ats

# Only validate + generate (skip both checks)
python main.py --skip-quality --skip-ats

# Only run checks (skip validation + generation)
python main.py --skip-validation --skip-generation
```

---

## 🔄 **Complete Workflow**

### **Step 1: YAML Validation**
- Reads: `config/current_application.yaml`
- Checks: Character counts, bold markers, structure
- Status: **BLOCKING** (pipeline stops if fails)
- Output: Error list or ✓ PASS

### **Step 2: Resume Generation**
- Reads: `config/current_application.yaml`
- Creates: `output/Generated_Resume.docx`
- Status: **BLOCKING** (pipeline stops if fails)
- Output: Word document ready to review

### **Step 3: Quality Check**
- Reads: `output/Generated_Resume.docx`
- Converts: → `output/Generated_Resume.pdf`
- Sends: PDF to Gemini for visual analysis
- Status: **NON-BLOCKING** (pipeline continues even if issues)
- Output: Scores + suggestions for improvement

### **Step 4: ATS Check**
- Reads: `output/Generated_Resume.docx` + `config/current_jd.txt`
- Converts: → PDF (if not already done)
- Sends: PDF + JD to Gemini for brutal analysis
- Status: **NON-BLOCKING** (pipeline continues even if issues)
- Output: Score/100 + pass/fail verdict

---

## 📊 **Expected Output**

```
================================================================================
RESUME GENERATION & VALIDATION PIPELINE
================================================================================

================================================================================
STEP 1: YAML CONSTRAINT VALIDATION
================================================================================

Running: YAML Validation...

   Length: 561 chars (Required: 520-570)
   ✓ PASS
   
   Bold markers: 8 (Required: 5-8)
   ✓ PASS

✓ YAML Validation completed successfully

================================================================================
STEP 2: RESUME GENERATION
================================================================================

Running: Resume Generation...

✓ Generated: output/Generated_Resume.docx

✓ Resume Generation completed successfully

================================================================================
STEP 3: QUALITY CHECK (PDF Visual Analysis)
================================================================================

Using PDF visual analysis checker

Running: Quality Check...

Converting DOCX to PDF...
✓ PDF created successfully

Sending PDF to Gemini for analysis...
[Quality analysis results...]

✓ Quality Check completed successfully

================================================================================
STEP 4: ATS CHECK (Keyword Matching + Visual Compatibility)
================================================================================

Using PDF visual compatibility checker

Running: ATS Check...

Running brutal ATS analysis...
[ATS analysis results...]

✓ ATS Check completed successfully

================================================================================
PIPELINE SUMMARY
================================================================================

Step 1 - YAML Validation:    ✓ PASSED
Step 2 - Resume Generation:  ✓ PASSED
Step 3 - Quality Check:      ✓ PASSED
Step 4 - ATS Check:          ✓ PASSED

✅ PIPELINE COMPLETED SUCCESSFULLY

Generated Resume:
  DOCX: D:\Git\virtual457-projects\job-application-automator\output\Generated_Resume.docx
  PDF:  D:\Git\virtual457-projects\job-application-automator\output\Generated_Resume.pdf

✓ Ready to apply!

================================================================================
```

---

## ⚙️ **Pipeline Behavior**

### **Blocking Steps (Must Pass)**
1. **YAML Validation** → If fails, pipeline stops
2. **Resume Generation** → If fails, pipeline stops

### **Non-Blocking Steps (Informational)**
3. **Quality Check** → If fails, pipeline continues (shows warnings)
4. **ATS Check** → If fails, pipeline continues (shows warnings)

**Why non-blocking?**
- Quality and ATS checks are subjective/informational
- You might want to apply even with minor quality issues
- You can review feedback and decide if acceptable

---

## 🎯 **Typical Workflows**

### **First Time (Full Pipeline)**
```bash
python main.py
```
Review all results, fix any issues, regenerate.

### **After Fixing YAML Issues**
```bash
python main.py
```
Re-run full pipeline to verify fixes.

### **Quick Regeneration (Already Validated)**
```bash
python main.py --skip-validation
```
Skip validation if you know YAML is good.

### **Just Quality Check (DOCX Already Generated)**
```bash
python main.py --skip-validation --skip-generation
```
Only run quality + ATS checks on existing DOCX.

### **Fast Generation (Skip All Checks)**
```bash
python main.py --skip-quality --skip-ats
```
Just validate + generate, skip analysis.

---

## 🔧 **Troubleshooting**

### **"YAML Validation Failed"**
```bash
# Fix errors shown in output
# Then re-run
python main.py
```

### **"Resume Generation Failed"**
- Check if template exists: `templates/Chandan_Resume_Format.docx`
- Check YAML syntax is valid
- Run generator directly: `python simple_generator.py`

### **"Quality/ATS Check Failed"**
- Check if `docx2pdf` installed: `pip install docx2pdf`
- Check if Microsoft Word installed
- Check Gemini API key in `.env`

### **"File Not Found" Errors**
- Make sure you're in `src/` directory
- Check paths: `config/current_application.yaml` exists
- Check paths: `config/current_jd.txt` exists

---

## 💡 **Pro Tips**

1. **Always run full pipeline first** to catch all issues
2. **Use skip flags** for faster iteration after initial run
3. **Review quality/ATS feedback carefully** even if non-blocking
4. **Fix ATS score < 70** before applying (likely rejection)
5. **Keep generated PDFs** for your records

---

## 📈 **Performance**

| Step | Time | Blocking |
|------|------|----------|
| YAML Validation | ~1 sec | ✅ Yes |
| Resume Generation | ~2 sec | ✅ Yes |
| Quality Check | ~30 sec | ❌ No |
| ATS Check | ~40 sec | ❌ No |
| **Total** | **~75 sec** | - |

**Fast Mode (skip checks):** ~3 seconds  
**Full Pipeline:** ~75 seconds

---

## 🎯 **Exit Codes**

- **0** = Success (validation + generation passed)
- **1** = Failure (validation or generation failed)

Quality/ATS check failures don't affect exit code.

---

## 📝 **Files Used**

**Input:**
- `config/current_application.yaml` → Resume configuration
- `config/current_jd.txt` → Job description (for ATS)
- `templates/Chandan_Resume_Format.docx` → Word template
- `src/.env` → Gemini API key

**Output:**
- `output/Generated_Resume.docx` → Generated Word document
- `output/Generated_Resume.pdf` → Converted PDF (if checks run)

---

**Your complete pipeline is ready to use!** 🚀

Run `python main.py` to start.
