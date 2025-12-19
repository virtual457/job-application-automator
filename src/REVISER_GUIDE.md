# YAML Reviser - Usage Guide

**Created:** November 27, 2025

## 🎯 **What It Does**

The reviser takes feedback and automatically updates your `current_application.yaml` while maintaining all constraints.

**Magic:** You give it feedback → It generates revised YAML → You review & save

---

## 🚀 **Quick Start**

### **Method 1: Interactive Mode (Recommended)**

```bash
cd src
python reviser.py
```

**Prompts you for feedback:**
```
Enter feedback for revision (press Enter twice when done):

Summary is too generic, add more specific LSEG metrics
Skills section missing Kotlin which is in the JD
Experience bullets don't emphasize AI integration enough

[Press Enter]
[Press Enter again to submit]
```

**Then:**
- ✅ Reviser generates improved YAML
- ✅ Shows preview
- ✅ Asks to save or discard

---

### **Method 2: Command Line Feedback**

```bash
python reviser.py --feedback "Summary needs more AI keywords from JD"
```

**Quick one-liner revision!**

---

### **Method 3: Feedback from File**

```bash
# Create feedback.txt with your notes
python reviser.py --feedback-file feedback.txt
```

**Useful for:** Quality checker output, ATS checker suggestions, reviewer notes

---

### **Method 4: With User Profile Data**

```bash
python reviser.py --use-profile --feedback "Add more metrics from LSEG experience"
```

**Includes:** Full user profile database for factual accuracy
**Use when:** Feedback requires deep knowledge of your background

---

## 📋 **What the Reviser Knows:**

**Always loaded:**
1. ✅ `config/current_application.yaml` - Current resume
2. ✅ `config/current_jd.txt` - Job description
3. ✅ `config/constraints.yaml` - Character limits, structure rules

**Optionally loaded (with --use-profile):**
4. ⚠️ `docs/user_profile/CHANDAN_PROFILE_MASTER.md` - Your complete background

---

## 💡 **Example Feedback:**

### **Good Feedback (Specific):**

```
Summary:
- Too long (currently 540 chars, need 450-520)
- Missing ServiceNow's AI integration focus
- Should mention React for web UI development

Skills:
- Add "Kotlin" to Programming Languages (in JD)
- Reorder to put "Full-Stack Development" before "AI & Machine Learning"

Experience:
- LSEG B3: Remove mention of "CloudWatch", not in JD
- Add bullet about cross-functional collaboration (JD emphasizes this)

Projects:
- Swap Calendly for Kambaz LMS (need more full-stack emphasis)
```

### **Okay Feedback (Less Specific):**

```
- Summary doesn't match JD well
- Skills section could be better organized
- Need more emphasis on full-stack capabilities
```

### **Bad Feedback (Too Vague):**

```
- Make it better
- Fix the summary
- Improve everything
```

---

## 🔄 **Complete Workflow:**

```bash
# Step 1: Generate initial YAML (manual or via Claude)
# Edit: config/current_application.yaml

# Step 2: Validate
python validate_yaml.py

# Step 3: Generate resume
python simple_generator.py

# Step 4: Run quality check
python quality_checker_pdf.py

# Step 5: Get feedback from quality checker output

# Step 6: Revise based on feedback
python reviser.py --feedback "Add more AI keywords, summary too long"

# Step 7: Validate revised version
python validate_yaml.py

# Step 8: If passes, generate again
python simple_generator.py
```

---

## ⚙️ **How It Works:**

**Reviser sends to Gemini:**

```
Here's the current YAML, the JD, the constraints, and the feedback.
Generate a revised YAML that:
1. Addresses all the feedback
2. Stays within all constraints
3. Maintains factual accuracy
4. Keeps the same structure

Output ONLY valid YAML, nothing else.
```

**Gemini returns:**
- Complete revised YAML
- Already validated against constraints
- Feedback applied

**You review and save!**

---

## 📊 **What Gets Revised:**

**Based on feedback, reviser can update:**
- ✅ Summary text, length, bold markers
- ✅ Skills categories, ordering, items
- ✅ Experience bullets (LSEG, Infosys)
- ✅ Project selection and bullets
- ✅ Header title (keywords)

**What reviser does NOT change:**
- ❌ Name (always "Chandan Gowda K S")
- ❌ Contact info (fixed)
- ❌ Company names, roles, dates (factual data)
- ❌ Number of bullets (5 LSEG, 4 Infosys, 3 projects - fixed)

---

## 🎯 **Common Use Cases:**

### **Use Case 1: Quality Checker Found Issues**

**Quality checker says:**
> "Summary: Grammar issue 'building production experience' (6/10)
> Skills: Missing React and JavaScript from JD (7/10)
> Projects: LMARO not relevant for this backend role (6/10)"

**Revise:**
```bash
python reviser.py --feedback "Fix summary grammar, add React/JavaScript to skills, replace LMARO with Port Management System for backend focus"
```

---

### **Use Case 2: ATS Score Too Low**

**ATS checker says:**
> "Score: 72/100 - BORDERLINE
> Missing keywords: Kotlin, Agile, CI/CD
> Skills section doesn't have Kotlin (mentioned in JD)"

**Revise:**
```bash
python reviser.py --feedback "ATS score 72/100. Add Kotlin to Programming Languages. Add CI/CD to DevOps category. Emphasize Agile in experience bullets."
```

---

### **Use Case 3: Wrong Project Selection**

**You realize:**
> "This is a data engineering role, not ML. Need different projects."

**Revise:**
```bash
python reviser.py --feedback "Replace LMARO and Dino RL with Data Analysis on PUBG and Port Management System. This is a data engineering role, not ML."
```

---

### **Use Case 4: Summary Too Long**

**Validator says:**
> "Summary length: 547 chars (need 450-520)"

**Revise:**
```bash
python reviser.py --feedback "Summary is 547 characters, needs to be 450-520. Cut unnecessary words while keeping key metrics."
```

---

## ⚠️ **Important Notes:**

1. **Always validate after revision:**
   ```bash
   python validate_yaml.py
   ```

2. **Review before saving:**
   - Reviser shows preview before saving
   - Check it makes sense
   - Ensure feedback was addressed

3. **Factual accuracy:**
   - Without `--use-profile`, reviser uses only what's in current YAML
   - With `--use-profile`, reviser has access to all your projects/metrics
   - Use `--use-profile` when adding new content

4. **Iteration:**
   - You can run reviser multiple times
   - Each time it reads the current YAML
   - Feedback compounds if you save each time

---

## 🔧 **Troubleshooting:**

### **"Generated YAML has syntax errors"**
- Reviser will show the bad YAML
- Don't save it
- Try with simpler feedback
- Or manually fix the YAML

### **"Constraints not met after revision"**
- Run `python validate_yaml.py` on revised YAML
- If fails, run reviser again with more specific feedback
- Example: "Summary still 530 chars, must be under 520"

### **"Feedback not addressed"**
- Make feedback more specific
- Bad: "Fix summary"
- Good: "Summary: Remove mention of distributed pipelines, add React"

---

## 💡 **Pro Tips:**

1. **Be specific with feedback** - Tell it exactly what to change
2. **One section at a time** - Don't try to fix everything at once
3. **Use --use-profile** - When adding new content (metrics, projects)
4. **Always validate** - After saving, run validate_yaml.py
5. **Keep backups** - Reviser overwrites current_application.yaml

---

## 🎯 **Advanced Usage:**

### **Chain with Quality Checker:**

```bash
# Run quality check, save output
python quality_checker_pdf.py > quality_feedback.txt

# Revise based on quality feedback
python reviser.py --feedback-file quality_feedback.txt

# Validate
python validate_yaml.py

# Generate and check again
python main.py
```

### **Iterative Refinement:**

```bash
# Round 1
python reviser.py --feedback "Add more AI keywords"
python validate_yaml.py

# Round 2
python reviser.py --feedback "Summary still too long, cut to 500 chars"
python validate_yaml.py

# Round 3
python reviser.py --feedback "Replace project 3 with more relevant option"
python validate_yaml.py
```

---

**Your YAML reviser is ready to use!** 🎉

It's like having an AI assistant that edits your resume based on feedback while keeping everything within constraints.
