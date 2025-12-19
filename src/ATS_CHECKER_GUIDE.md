# ATS Checker - Brutal Mode Guide

## 🎯 What This Does

**ATS Checker simulates real Applicant Tracking Systems** that auto-reject 75% of resumes based on keyword matching.

**Key Difference:**
- `quality_checker.py` = Content quality (grammar, flow, readability)
- `ats_checker.py` = **Keyword matching (will you pass the robots?)**

---

## 🚀 Quick Start

```bash
cd src

# Run ATS check (requires job description)
python ats_checker.py
```

**Requires:**
- Job description: `../config/current_jd.txt` (MUST exist)
- Resume YAML: `../config/current_application.yaml`
- API key: `.env` in src folder

---

## 📊 Scoring System (Out of 100)

### Section Breakdown:
1. **Keyword Matching** (30 pts) - Are JD keywords in your resume?
2. **Technical Skills** (25 pts) - Required skills in skills section?
3. **Experience Alignment** (20 pts) - Work bullets match JD requirements?
4. **Project Relevance** (15 pts) - Projects demonstrate required tech?
5. **Hard Requirements** (10 pts) - Education, GPA, availability met?

### Pass/Fail Thresholds:
- **85-100**: ✓ PASS - Strong ATS match, will reach human review
- **70-84**: ⚠ BORDERLINE - May pass, competitive but risky
- **Below 70**: ✗ FAIL - AUTO-REJECTED by ATS, don't waste time applying

---

## 🔥 Brutal Mode Rules

This checker is STRICT by design:

1. **Exact keyword matching** - "React" ≠ "React.js" unless ATS recognizes synonym
2. **Skills section required** - Mentioning Python in experience doesn't count if not in skills
3. **Hard requirements = Auto-fail** - Missing degree/GPA = 0 points in section 5
4. **Quantitative only** - No partial credit for "related" skills
5. **No hand-holding** - If score < 70, you're told "Do not submit"

---

## 📋 Usage Examples

### Default (Current JD)
```bash
cd src
python ats_checker.py
# Uses: ../config/current_jd.txt and ../config/current_application.yaml
```

### Custom Job Description
```bash
python ats_checker.py path/to/waymo_jd.txt
# Uses: waymo_jd.txt and ../config/current_application.yaml
```

### Custom Both
```bash
python ats_checker.py jd.txt path/to/resume.yaml
```

---

## 🔄 Recommended Workflow

```
1. Get JD → Save to config/current_jd.txt
2. Generate YAML → Claude creates config/current_application.yaml
3. Format validation → python validate_yaml.py
4. ATS check → python ats_checker.py
5. Quality check → python quality_checker.py
6. Score ≥ 85? → Generate resume and apply
7. Score < 85? → Fix critical issues, re-run ATS check
```

**NEVER submit if ATS score < 70** - guaranteed rejection

---

## 📈 What Gets Scored

### 1. Keyword Matching (30 pts)
- Extracts 15-20 critical keywords from JD
- Checks if keywords appear ANYWHERE in resume
- Calculates match percentage
- **Brutal:** Missing 5+ keywords = likely fail

### 2. Technical Skills Coverage (25 pts)
- Required skills MUST be in skills section
- Partial credit if mentioned elsewhere
- **Brutal:** -2 pts per completely missing skill

### 3. Experience Alignment (20 pts)
- Maps JD requirements to work experience bullets
- Generic bullets = no credit
- **Brutal:** Uncovered requirements hurt score

### 4. Project Relevance (15 pts)
- Each project scored 0-5 based on tech overlap
- **Brutal:** Irrelevant projects = 0 points

### 5. Hard Requirements (10 pts)
- Degree, GPA, availability, years of experience
- **Brutal:** Missing ANY hard requirement = AUTO-FAIL

---

## 🎯 Score Interpretation

### 95-100: Perfect ATS Match
- All keywords present
- All required skills in skills section
- Strong experience alignment
- Highly relevant projects
- All hard requirements met

### 85-94: Strong Pass
- 85%+ keyword match
- Most required skills present
- Good experience coverage
- Relevant projects
- Hard requirements met

### 70-84: Borderline
- 70-84% keyword match
- Some missing skills
- Gaps in experience coverage
- May pass, may not - competitive field = reject

### Below 70: Auto-Reject
- <70% keyword match
- Critical skills missing
- Poor JD alignment
- DO NOT SUBMIT - waste of time

---

## 🔧 Common Issues & Fixes

### Issue: Low Keyword Score (<24/30)
**Fix:** Add missing keywords to:
1. Skills section (highest priority)
2. Work experience bullets
3. Project descriptions
4. Summary (if natural fit)

### Issue: Low Skills Coverage (<20/25)
**Fix:**
1. Add missing tech to skills section
2. Reorder categories to match JD priority
3. Remove irrelevant skills to make room

### Issue: Low Experience Alignment (<16/20)
**Fix:**
1. Rewrite bullets to match JD requirements
2. Emphasize relevant technologies
3. Add metrics that align with JD needs

### Issue: Low Project Relevance (<12/15)
**Fix:**
1. Swap irrelevant project for more relevant one
2. Highlight technologies that match JD
3. Rewrite project bullets to emphasize JD tech

### Issue: Failed Hard Requirements (0/10)
**Fix:**
1. Make sure education/GPA clearly stated
2. Verify availability matches (8 months for co-op)
3. If you genuinely don't meet requirements, don't apply

---

## 💡 Pro Tips

1. **Run ATS check BEFORE quality check**
   - No point polishing grammar if ATS will reject you

2. **Focus on keyword score first**
   - 30 points = biggest section
   - Easy to fix (add missing keywords)

3. **Skills section is critical**
   - ATS scans skills section heavily
   - Make sure all JD-required tech is there

4. **Don't apply if score < 70**
   - You're wasting your time
   - Better to find better-fit roles

5. **85+ doesn't guarantee interview**
   - It means you pass ATS screening
   - Still need strong content (use quality_checker.py)

---

## 🆚 ATS vs Quality Checker

| Check | ATS Checker | Quality Checker |
|-------|-------------|-----------------|
| **Purpose** | Pass robot screening | Impress human reviewers |
| **Scoring** | Quantitative (0-100) | Qualitative (0-10 per section) |
| **Focus** | Keywords, skills, matching | Grammar, flow, impact |
| **Strictness** | Brutal, pass/fail | Constructive feedback |
| **When to use** | FIRST (before quality) | SECOND (after ATS pass) |

**Both must pass** for successful application:
1. ATS score ≥ 85 → Resume reaches humans
2. Quality score ≥ 8 → Humans impressed, interview granted

---

## 🚨 Critical Warnings

### DO NOT:
- ❌ Submit resume with ATS score < 70 (auto-reject)
- ❌ Keyword stuff to game ATS (quality_checker will catch it)
- ❌ Fabricate skills/keywords you don't have
- ❌ Ignore "CRITICAL MISSING KEYWORDS" section
- ❌ Apply to roles with <7/10 fit (waste of time)

### ALWAYS:
- ✅ Run ATS check before quality check
- ✅ Fix critical issues before re-checking
- ✅ Aim for 85+ before considering application
- ✅ Verify hard requirements are clearly met
- ✅ Update skills section based on ATS feedback

---

## 📝 Output Sections Explained

### Keyword Matching Analysis
- Lists all critical keywords from JD
- Shows which are ✓ found vs ✗ missing
- Calculates match percentage
- **Action:** Add missing keywords naturally

### Technical Skills Coverage
- Lists required technical skills
- Shows presence in skills section
- Flags skills mentioned elsewhere but not in skills section
- **Action:** Add to skills section, reorder by priority

### Experience Alignment
- Maps JD requirements to resume bullets
- Shows which requirements are uncovered
- **Action:** Rewrite bullets to cover requirements

### Project Relevance
- Scores each project 0-5 on tech overlap
- **Action:** Swap low-scoring projects for relevant ones

### Hard Requirements
- Verifies degree, GPA, availability, etc.
- **Action:** Make sure clearly stated in resume

### Top 5 Improvements
- Prioritized by point gain
- **Action:** Start with #1, work down the list

### Brutal Truth Assessment
- Honest verdict on submission readiness
- **Action:** If it says don't submit, don't submit

---

## 🔄 Iteration Loop

```
1. Run ATS check
2. Score < 85?
   YES → Fix top 3 improvements
   NO  → Run quality_checker.py
3. Re-run ATS check
4. Repeat until ≥ 85
5. Then run quality check
6. Both pass? → Generate and submit
```

Average iterations to reach 85+: **2-4 runs**

---

## 🎓 Understanding ATS Systems

Real ATS systems (Workday, Greenhouse, Lever, Taleo):
- Scan for exact keyword matches
- Rank candidates by match percentage
- Auto-reject bottom 50-75%
- Pass top 25% to human recruiters

**This checker simulates that process**

You're competing against:
- 200-500 applicants per role
- Top 25% = 50-125 resumes reach humans
- You need 85+ to be in that top 25%

---

## 📊 Score History Tracking

Keep track of your ATS scores:

```
Company          | Score | Applied? | Result
-----------------|-------|----------|--------
Waymo ML/RL      | 92/100| Yes      | Pending
Tesla Full Stack | 78/100| No       | Too low
Netflix Backend  | 88/100| Yes      | Interview
```

**Target:** 85+ average across all applications

---

## 🆘 Troubleshooting

**"Job description required for ATS analysis"**
- Create `config/current_jd.txt` with JD content
- Or provide JD path as argument

**"Score seems too low"**
- ATS is brutal by design
- Real systems reject 75% of resumes
- If score < 70, JD-resume fit is genuinely weak

**"All keywords present but score still low"**
- Check other sections (skills, experience, projects)
- Hard requirements might be failing
- Keywords alone ≠ high score (only 30%)

**"Can I game the system?"**
- Don't keyword stuff (quality_checker catches this)
- Don't add skills you don't have (interview will expose)
- Better to find better-fit roles than game ATS

---

**Your brutal ATS checker is ready!** 🤖

Remember: **85+ = Submit | 70-84 = Risky | <70 = Don't waste time**
