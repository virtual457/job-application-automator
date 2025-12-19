# CLAUDE.md - Resume Generation System Session Handoff

**Last Updated:** December 3, 2025
**System Version:** v2.1 (mandatory Guidelines document reading)
**Current Working Directory:** `D:\Git\virtual457-projects\job-application-automator`

---

## SYSTEM OVERVIEW

This is an automated resume generation system that creates tailored resumes for Spring/Summer 2026 co-op applications by merging YAML configuration files with a Word template.

**User:** Chandan Gowda K S
**Target:** Spring/Summer 2026 co-op positions (8-month availability)
**Institution:** Northeastern University, MS CS (3.89 GPA)
**Focus:** ML/AI, Backend Engineering, Full-Stack roles

---

## QUICK START - GENERATE RESUME

When user provides a job description:

```bash
# 1. Generate YAML (read docs FIRST in this order)
# - Read: docs/RESUME_GENERATION_GUIDELINES.md  ← START HERE (living document)
# - Read: docs/LLM_GUIDE_YAML_CREATION_v3.md
# - Read: docs/user_profile/CHANDAN_PROFILE_MASTER.md
# - Read: docs/user_profile/WORK_EXPERIENCE_DATABASE.md
# - Write to: config/current_application.yaml

# 2. Validate YAML
python validate_yaml.py

# 3. Generate resume (if validation passes)
python src/simple_generator.py

# 4. Output location
# output/Generated_Resume.docx (opens automatically in Word)
```

---

## FILE STRUCTURE

### Core Files

**Configuration:**
- `config/current_application.yaml` - Active YAML for current job (overwrite for each new application)
- `config/constraints.yaml` - Validation rules (character limits, bold markers, etc.)
- `config/templates/` - YAML templates for different role types

**User Profile Data:**
- `docs/user_profile/CHANDAN_PROFILE_MASTER.md` - ALL projects, skills, achievements (21 projects total)
- `docs/user_profile/WORK_EXPERIENCE_DATABASE.md` - LSEG & Infosys factual metrics
- `docs/LLM_GUIDE_YAML_CREATION_v3.md` - Complete YAML generation instructions
- `docs/RESUME_GENERATION_GUIDELINES.md` - Living document with iterative feedback and best practices (NEW)
- `docs/CONSTRAINTS.md` - Formatting rules and character limits

**Generation:**
- `templates/Chandan_Resume_Format.docx` - Base Word template (DO NOT MODIFY)
- `src/simple_generator.py` - Python script that merges YAML + template
- `validate_yaml.py` - Constraint validation script
- `output/Generated_Resume.docx` - Final generated resume

**Tracking:**
- `data/applications.csv` - Application tracking spreadsheet

---

## LIVING DOCUMENT WORKFLOW

### What is the Living Document?

**`docs/RESUME_GENERATION_GUIDELINES.md`** is a continuously updated document that captures:
- User feedback from every resume generation cycle
- Learned patterns and best practices
- Section-specific guidelines
- "What worked" and "what didn't" examples
- User preferences and corrections

### Why It Exists

**Problem it solves:**
- Without it: Same mistakes repeat across sessions
- Without it: User has to re-explain preferences each time
- Without it: No institutional memory of feedback

**With it:**
- ✅ Mistakes are documented and prevented
- ✅ User preferences persist across sessions
- ✅ Quality improves iteratively over time
- ✅ New Claude sessions can learn from past feedback

### When to Update Guidelines Document

**After EVERY user feedback/correction:**
1. User points out an error or preference
2. Document the feedback in relevant section's "User Feedback Log"
3. Update guidelines/templates if needed
4. Update examples to reflect new learning

**Examples of feedback to capture:**
- "Always include F1 CPT/OPT in header" → Update header guidelines
- "Don't use more than 5 bold markers" → Update constraints reminder
- "LMARO project works better for X roles" → Update project selection guide
- "This phrasing didn't work well" → Add to examples section

### How to Update

1. **Locate relevant section** in RESUME_GENERATION_GUIDELINES.md
2. **Add to User Feedback Log:**
   ```
   **Date:** 2025-12-03
   **Section:** Header
   **Feedback:** User emphasized reading Guidelines FIRST
   **Action Taken:** Updated CLAUDE.md to make Guidelines #1 priority
   **Example:** N/A
   ---
   ```
3. **Update guidelines/templates** if the feedback warrants a pattern change
4. **Commit changes** with descriptive message

### Reading Priority

**For EVERY resume generation:**
1. 📖 Read Guidelines FIRST (user-specific learned patterns)
2. 📖 Read LLM Guide (technical YAML instructions)
3. 📖 Read Profile Master (projects and skills)
4. 📖 Read Work Database (factual metrics)

**Guidelines is #1 because:**
- Contains user's specific preferences
- Prevents repeating past mistakes  
- Provides context for why rules exist
- Evolves with each feedback cycle

---

## CRITICAL CONSTRAINTS (MUST FOLLOW)

**📌 Source of Truth:** All constraints defined in `config/constraints.yaml`
**⚠️ Always validate with:** `python validate_yaml.py`

### Summary Section
- **Length:** 450-520 characters (STRICT)
- **Bold markers:** 5-8 using `**text**`
- **Required mentions:**
  - "MS Computer Science student at Northeastern"
  - "**3.89 GPA**" (bolded)
  - "London Stock Exchange Group" or "LSEG"
  - 2-3 real LSEG metrics (7.5M+, 180+, 40%, 99.9%, 35%, etc.)
- **NO "seeking internship"** or "looking for" language
- **Company-specific ending** mentioning target company

### Skills Section
- **Exactly 7 categories** (no more, no less)
- **Maximum:** 90 characters per category (no minimum - add only relevant skills)
- **Ordered by JD priority** (most important tech first)

### Experience Section
**LSEG:**
- **Exactly 5 bullets**
- **Each bullet:** 150-250 characters (see constraints.yaml)
- **Each bullet:** 3-5 bold markers using `**text**`
- **Use real metrics** from WORK_EXPERIENCE_DATABASE.md
- **Generate FRESH bullets** for each JD (don't copy verbatim)

**Infosys:**
- **Exactly 4 bullets**
- **Each bullet:** 150-250 characters (see constraints.yaml)
- **Each bullet:** 3-5 bold markers
- **Complement LSEG** story (don't duplicate focus)

### Projects Section
- **Exactly 3 projects**
- **Order by JD relevance** (most relevant first)
- **Tech line:** Max 80 characters
- **bullet1 & bullet2:** Max 250 characters each (see constraints.yaml), 3-5 bold markers each
- **Use field names:** `bullet1` and `bullet2` (NOT `bullets` array)
- **GitHub links:** Use exact URLs from CHANDAN_PROFILE_MASTER.md

---

## TOP PROJECTS BY ROLE TYPE

### ML/AI Engineering (Top 3)
1. **LMARO** - RAG, LangChain ReAct, Multi-Agent AI, Vector DB
2. **Dino Deep RL Agent** - PyTorch, Double DQN, 1.5M params, GPU training
3. **Face Recognition System** - TensorFlow, CNN, 88.2% accuracy

### Backend/Distributed Systems
1. **Orion Platform** - Kubernetes Operator, Go, CRDs, Cloud Native
2. **Port Management System** - Django, MySQL, 50+ stored procedures, Dijkstra in SQL
3. **LMARO** - FastAPI backend, 10 REST endpoints, WebSocket/SSE

### Full-Stack Development
1. **LMARO** - FastAPI + Next.js 15 + React 19 + ChromaDB
2. **Kambaz LMS** - Next.js 15 + React 19 + Node.js/Express
3. **Port Management System** - Django + MySQL full-stack

### Data Engineering
1. **PUBG Analysis** - 4.4M records, Pandas, NumPy, Statistical analysis
2. **Port Management** - 15+ tables, 50+ stored procedures
3. **LMARO** - Vector database, semantic search, data pipelines

---

## AVAILABLE PROJECTS (21 Total)

Full details in `docs/user_profile/CHANDAN_PROFILE_MASTER.md`

**Top Tier (Production-Grade):**
1. Orion Platform - Kubernetes Operator (Go)
2. Dino Game Deep RL Agent - PyTorch, Double DQN
3. **LMARO - LLM Multi-Agent Resume Optimizer** - RAG, LangChain, ReAct ← NEWLY ADDED
4. Kambaz LMS - Next.js 15 + React 19 (Live deployed)
5. Calendly - Java, 6+ design patterns, 98% coverage
6. Port Management - Django, MySQL, Advanced SQL

**ML/AI Projects:**
7. Face Recognition - TensorFlow, CNN, 88.2% accuracy
8. PUBG Analysis - 4.4M records, Pandas
9. Simple Neural Network - From-scratch backprop, 91.27% MNIST

**Other Projects (10-21):**
10. Online Examination System - Flask, MongoDB
11. Stocks Simulator - yfinance, Plotly
12. Pixel-Perfect - Image Processing, OpenCV
13. Quiz App - ASP.NET MVC
14. StuffyCare - Healthcare Management (.NET)
15. NS3 Network Simulation - C++
16. Cryptography Toolkit - RSA, Ciphers
17. Web Scraping - BeautifulSoup
18. Drive-Through - C++, Qt
19. Employee Admin - JavaScript
20. World Data Visualization - D3.js
21. Bingo Game - HTML/CSS/JS

---

## LSEG REAL METRICS (Use Accurately)

From `docs/user_profile/WORK_EXPERIENCE_DATABASE.md`:

- **7.5M+ records** processed
- **180+ countries** served
- **40 records/second** processing speed
- **99.9% data integrity**
- **35%** improvement in turnaround time
- **40%** latency reduction
- **50%** security incident reduction
- **5 engineers** mentored
- **7 cross-functional teams** collaborated
- **Zero-downtime** migrations

**Technologies:** Python, Java (Micronaut), AWS Lambda, SQS, API Gateway, CloudWatch

---

## INFOSYS REAL METRICS (Use Accurately)

- **3x throughput** improvement
- **50%** reduction in manual interventions
- **35%** latency reduction
- **20%** accuracy improvement

**Technologies:** Python, ETL pipelines, Microservices integration

---

## VALIDATION QUICK CHECKS

After generating YAML, run these Python checks:

```python
# Summary check
summary = '''[paste actual summary]'''
print(f'{len(summary)}c, {summary.count("**")//2}b')
# Expected: 520-570c, 5-8b

# Bullet check (sample)
bullet = '''[paste bullet]'''
print(f'{len(bullet)}c, {bullet.count("**")//2}b')
# Expected: 150-250c, 3-5b
```

Or use the validation script:
```bash
python validate_yaml.py
```

---

## CURRENT STATUS

### Latest Application
**Company:** NVIDIA
**Role:** Product Management Intern - AI Infrastructure
**YAML:** `config/current_application.yaml`
**Status:** Generated & validated (9.5/10 fit)

**Projects used:**
1. LMARO - Multi-Agent Resume Optimizer (RAG, LangChain, AI workflows)
2. Dino Game Deep RL Agent (PyTorch, GPU training)
3. Orion Platform (Kubernetes operator in Go)

**Key focus:** AI workflows, PyTorch, Kubernetes, product management, enterprise infrastructure

### Recent System Updates (Nov 26, 2025)
- ✅ Added LMARO project to CHANDAN_PROFILE_MASTER.md (#3)
- ✅ Updated all project numbering (now 21 projects total)
- ✅ Added RAG/LangChain/Multi-Agent keywords to ML section
- ✅ Updated positioning strategies to include LMARO for ML/AI roles
- ✅ Changed tab size from 2.45" to 2.2" in simple_generator.py
- ✅ Deleted generate.bat (use `python src/simple_generator.py` directly)

### Applications Submitted (Partial List)
- Tesla (4 roles), Tinder, Netflix, Nokia, IBM, NVIDIA, Two Sigma
- Cisco (Boston), Darby, InnoMat.AI, Amazon, C3Aero
- Roux Institute ML Engineer, Waymo ML/RL
- LLM Backend Systems (San Jose)

**High-priority targets:**
- Cisco (Boston local, 9/10 fit)
- Tinder (9.5/10 fit)
- LLM Backend Systems (9/10 fit, LMARO perfect match)
- InnoMat.AI (9/10 fit, Northeastern-aligned)

---

## YAML GENERATION WORKFLOW

### ⚠️ CRITICAL FIRST STEP - READ ALL DOCUMENTATION

**MANDATORY READING ORDER FOR EVERY RESUME GENERATION:**

1. **`docs/RESUME_GENERATION_GUIDELINES.md`** ← **LIVING DOCUMENT - READ FIRST!**
   - Contains iterative feedback from previous cycles
   - User preferences and learned patterns
   - Section-specific best practices
   - User Feedback Logs with corrections
   - **PURPOSE:** Prevent repeating mistakes, follow user preferences

2. **`docs/LLM_GUIDE_YAML_CREATION_v3.md`**
   - Complete YAML generation instructions
   - Dynamic generation philosophy
   - Bullet generation strategies

3. **`docs/user_profile/CHANDAN_PROFILE_MASTER.md`**
   - All 21 projects with details
   - Technical skills and keywords
   - Positioning strategies by role

4. **`docs/user_profile/WORK_EXPERIENCE_DATABASE.md`**
   - LSEG and Infosys factual metrics
   - Real technologies used
   - Example bullet variations

**WHY THIS ORDER MATTERS:**
- Guidelines captures USER-SPECIFIC preferences learned over time
- Contains "what worked" and "what didn't" from previous cycles
- Prevents making same mistake twice (e.g., forgetting F1 CPT/OPT in header)
- Provides context for why certain rules exist

---

### ⭐ NEW WORKFLOW - GENERATE FIRST, BOLD LATER (Dec 3, 2025)

**CRITICAL CHANGE:** Never write with bold markers during initial generation.

**Old Workflow (DEPRECATED):**
~~1. Write content with bold markers as you go~~
~~2. Often exceed 8 bold limit~~
~~3. Remove bold, recount, repeat~~

**New Workflow (CURRENT):**

**Step 1: Write Plain Text (No Bold)**
- Focus on narrative flow and grammar
- Get the story right
- Aim for target character count
- Don't worry about bold yet

**Step 2: Identify 5-8 Most Important Terms**
For Summary:
- **Required:** 3.89 GPA (always)
- **Technologies:** 2-3 JD-relevant terms
- **Metrics:** 1-2 key numbers (7.5M+, 40%)
- **Keywords:** 1-2 role-specific terms
- **Stop at 8 maximum**

For Experience/Project Bullets:
- **Technologies:** 2-3 key tech terms
- **Metrics:** 1-2 numbers
- **Actions:** 1-2 action terms
- **3-5 bold per bullet**

**Step 3: Add Bold Markers**
- Add `**term**` around selected terms
- Count as you go
- Verify still reads naturally

**Step 4: Verify Constraints**
- Character count: within range ✓
- Bold markers: within range ✓
- Flow still natural ✓

**Why This Works:**
- ✅ Never exceed limits
- ✅ Saves time (no recounting)
- ✅ Picks most important terms naturally
- ✅ Better quality writing (focus on content first)

---

### ⭐ CRITICAL QUALITY RULES (Dec 3, 2025)

**1. FACTUALITY IS NON-NEGOTIABLE**

**Never fabricate:**
- ❌ Technologies not used (e.g., Kubernetes at LSEG when only AWS)
- ❌ Metrics not real (verify every number against databases)
- ❌ Experiences that didn't happen

**Always verify:**
- ✅ Check WORK_EXPERIENCE_DATABASE.md for every LSEG/Infosys claim
- ✅ Check CHANDAN_PROFILE_MASTER.md for every project detail
- ✅ If unsure, ASK user, don't guess

**Example violations caught:**
- ❌ "Built Kubernetes at LSEG" - LSEG had ZERO Kubernetes (pure AWS)
- ❌ "180+ countries" in wrong context - implies ownership not had

---

**2. REMOVE WEAK LANGUAGE & NUMBERS**

**Never use:**
- ❌ "showcasing", "demonstrating", "highlighting" in bullets
- ❌ "lines of code" (1.5K+ lines, 2K LOC, etc.)
- ❌ Weak numbers that reduce credibility: "15+ tables", "10 endpoints", "50+ procedures"

**Why:**
- The work itself demonstrates the skill - don't SAY "showcasing"
- Lines of code is not resume-worthy
- Specific numbers look AI-generated and reduce credibility

**Examples:**
❌ "Built RESTful API (10 endpoints), showcasing backend engineering"
✅ "Built RESTful API for backend engineering and scalable architecture"

❌ "Custom Kubernetes operator (1.5K+ lines of Go)"
✅ "Custom Kubernetes operator in Go"

❌ "MySQL database (15+ tables, 50+ stored procedures)"
✅ "MySQL database with complex relational schema and stored procedures"

---

**3. PROJECTS MUST EXPLAIN PURPOSE FIRST**

**Structure:**
- **Bullet 1:** WHAT the project does (problem solved, purpose)
- **Bullet 2:** HOW it works (technical implementation)

**Examples:**
❌ "Built backend server with FastAPI framework (10 REST endpoints, WebSocket/SSE)"
✅ "Built AI-powered resume optimization platform that intelligently tailors resumes to job descriptions"

❌ "Implemented Dijkstra pathfinding algorithm in SQL with 50+ stored procedures"
✅ "Built maritime logistics platform with Django backend, implementing route optimization and workflow management"

**Principle:** Recruiters care about problem-solving, not just tech stack.

---

**4. ALL BULLETS MUST BE PROPER LENGTH**

**Requirement:** 150-250 characters (per constraints.yaml)

**Common mistake:** Writing bullets too short (120-140 chars)
- Infosys bullets were initially 105-134 chars (too short!)
- Every bullet needs full context and impact

**How to fix:**
- Add context: "for enterprise workloads", "in production environment"
- Add technical details: specific technologies, methods used
- Expand on impact: who benefited, scale of impact

**Example:**
❌ TOO SHORT (107 chars): "Optimized SQL queries, reducing processing latency by 35% for analytical workloads."
✅ PROPER (220 chars): "Optimized database query performance and ETL pipeline efficiency through strategic indexing and batch processing optimization, reducing data processing latency by 35% for high-volume enterprise workloads."

---

**5. PROFESSIONAL, CLEAR ENGLISH - EVERY SENTENCE MATTERS**

**User feedback:** "why is your english is so bad and you are not framing sentences correctly"

**Rules:**
- Each sentence must be well-thought-out
- Not just "writing for the sake of writing"
- Every point must be:
  - Factually correct
  - Aligned with JD
  - Having impact

**Grammar mistakes caught:**
❌ "processing 7.5M+ records with 40% latency reduction" (can't process WITH reduction)
✅ "processing 7.5M+ records and achieving 40% latency reduction"

**Weak writing caught:**
❌ "implementing cloud best practices for high-throughput systems" (meaningless filler)
✅ "reducing latency by 40% through batch processing optimization and monitoring"

**Principle:** Every bullet must have substance. If it's filler, remove it.

---

**6. PROJECT ORDERING BY JD SPIRIT, NOT JUST KEYWORDS**

**Rule:** When JD emphasizes something (like "AI/ML exposure"), prioritize projects demonstrating that, even if other projects match explicit framework names.

**Example:**
JD says: "Django, FastAPI, Express" + "AI/ML exposure"

❌ Wrong: Port Management first (has Django explicitly)
✅ Right: LMARO first (has AI/ML which JD emphasizes + FastAPI is still a server framework)

**Principle:** Match the SPIRIT of what they want, not just keywords.

---

### Step 1: Analyze JD
- Identify primary technologies (rank by importance)
- Determine role category (ML, backend, full-stack, etc.)
- Extract 15-20 keywords
- Calculate fit score (0-10)
- **If fit ≥ 7/10:** Generate YAML immediately

### Step 2: Read Required Documentation (MANDATORY)

**⚠️ READ ALL 4 DOCUMENTS IN ORDER BEFORE GENERATING:**

```bash
# 1. FIRST - Living document with user feedback and preferences
docs/RESUME_GENERATION_GUIDELINES.md  # ← START HERE!

# 2. YAML generation technical guide
docs/LLM_GUIDE_YAML_CREATION_v3.md

# 3. User profile and projects
docs/user_profile/CHANDAN_PROFILE_MASTER.md

# 4. Work experience factual database
docs/user_profile/WORK_EXPERIENCE_DATABASE.md
```

**Critical: Guidelines document is LIVING DOCUMENT**
- Updates after each user feedback
- Contains learned patterns and corrections
- Prevents repeating mistakes
- Read FIRST before every generation

### Step 3: Generate YAML Components

**Header:**
```yaml
header:
  name: "Chandan Gowda K S"
  title: "[Role | MS CS @ Northeastern | F1 CPT/OPT | Top 3-5 JD Keywords]"
  contact: "+1 (857) 421-7469; chandan.keelara@gmail.com; LinkedIn; Portfolio; GitHub;"

company_name: "[Company Name]"
```

**Summary:** 520-570c, 5-8b, mentions MS CS, 3.89 GPA, LSEG, 2-3 metrics, company-specific ending

**Skills:** 7 categories, 35-95c each (see constraints.yaml), ordered by JD priority

**Experience:** LSEG (5 bullets) + Infosys (4 bullets), 150-250c, 3-5b, fresh bullets per JD

**Projects:** 3 projects, ordered by relevance, tech max 80c, bullets max 250c with 3-5b

### Step 4: Validate
```bash
python validate_yaml.py
```

### Step 5: Generate Resume
```bash
python src/simple_generator.py
```

### Step 6: Review Output
```
output/Generated_Resume.docx (opens automatically)
```

---

## COMMON PATTERNS

### Backend-Heavy Resume
- **Summary focus:** Microservices, scale, AWS, distributed systems
- **Skills order:** Programming > Backend > Cloud > Databases > DevOps > ML > Software Eng
- **Projects:** Orion Platform, Port Management, LMARO (backend focus)
- **LSEG bullets:** Event-driven, Java microservices, AWS Lambda, performance

### ML/AI Resume
- **Summary focus:** Deep RL, RAG, agents, PyTorch, neural networks
- **Skills order:** Programming > AI/ML > ML Engineering > Software Eng > Cloud > Backend > DevOps
- **Projects:** LMARO, Dino RL, Face Recognition
- **LSEG bullets:** Data pipelines, 7.5M records, Python, automation, ML-ready data

### Full-Stack Resume
- **Summary focus:** Full-stack, React, Next.js, FastAPI, backend + frontend
- **Skills order:** Programming > Backend > Frontend > Databases > Cloud > DevOps > Software Eng
- **Projects:** LMARO (full-stack), Kambaz LMS, Port Management
- **LSEG bullets:** Microservices, APIs, workflows, collaboration

---

## CRITICAL RULES

### NEVER:
- ❌ Copy bullets verbatim from WORK_EXPERIENCE_DATABASE.md
- ❌ Fabricate metrics or technologies not in database
- ❌ Use "seeking internship" or "looking for" in summary
- ❌ Exceed character limits (summary, bullets, skills, tech)
- ❌ Use wrong bold marker counts
- ❌ Include projects not in CHANDAN_PROFILE_MASTER.md
- ❌ Use incorrect GitHub links (always verify from profile)
- ❌ Use `bullets` array in projects (use `bullet1` and `bullet2`)

### ALWAYS:
- ✅ **Read RESUME_GENERATION_GUIDELINES.md FIRST** (living document with user feedback)
- ✅ Read LLM_GUIDE_YAML_CREATION_v3.md before generating
- ✅ Read CHANDAN_PROFILE_MASTER.md and WORK_EXPERIENCE_DATABASE.md
- ✅ Generate FRESH bullets tailored to each JD
- ✅ Use ONLY real metrics from database
- ✅ Validate constraints before confirming ready
- ✅ Match JD keywords naturally (not keyword-stuffed)
- ✅ Tell coherent story across all sections
- ✅ Use exact GitHub URLs from CHANDAN_PROFILE_MASTER.md
- ✅ **Include "F1 CPT/OPT" in header title** (per Guidelines document)

---

## SYSTEM SETTINGS

### Tab Size (Skills Section)
**Current setting:** 2.2 inches
**Location:** `src/simple_generator.py:189`
```python
tab_position = 2.2  # 2.2 inches
```

### Template
**File:** `templates/Chandan_Resume_Format.docx`
**DO NOT MODIFY** - Generator overwrites content

### Output
**File:** `output/Generated_Resume.docx`
**Auto-opens in Word** after generation

---

## USER PREFERENCES

The user (Chandan):
- Values **direct, factual communication** (no fluff)
- Frequently validates character counts manually
- Corrects inaccuracies immediately (zero tolerance for errors)
- Prefers "give only what I ask" approach
- Gets frustrated with over-explanation
- Wants immediate YAML generation when fit ≥ 7/10
- Expects career-critical accuracy (his future depends on this)

**Communication style:** Concise, technical, no pleasantries

---

## TROUBLESHOOTING

### Validation Fails
1. Check character counts (summary 450-520, bullets 150-250, skills max 90, tech max 80) - See constraints.yaml
2. Check bold markers (summary 5-8, bullets 3-5)
3. Verify required keywords in summary (MS CS, 3.89 GPA, LSEG)
4. Ensure exactly 7 skill categories
5. Ensure exactly 5 LSEG bullets, 4 Infosys bullets
6. Ensure exactly 3 projects with bullet1 and bullet2 (not bullets array)

### Generator Fails
```bash
# Run from base directory
cd D:\Git\virtual457-projects\job-application-automator
python src/simple_generator.py
```

### Word Won't Open
- Generator auto-closes Word before generation
- Check if output/Generated_Resume.docx exists
- Manually open if auto-open fails

---

## EXAMPLE SESSION

```
User: [Pastes Waymo ML/RL job description]

Claude:
1. Analyzes JD → Identifies: PyTorch, Deep RL, reward models, Python, ML engineering
2. Calculates fit: 9/10 (strong ML/RL match)
3. Reads: LLM_GUIDE_YAML_CREATION_v3.md, CHANDAN_PROFILE_MASTER.md, WORK_EXPERIENCE_DATABASE.md
4. Generates YAML:
   - Summary: 538c, 8b, mentions Deep RL, RAG, PyTorch, LSEG, 7.5M records, 40%
   - Skills: Programming > AI/ML > ML Engineering > Software Eng > Cloud > Backend > DevOps
   - Projects: Dino RL, LMARO, Face Recognition (all ML-focused)
   - LSEG: 5 bullets emphasizing Python, 7.5M records, performance, algorithms
   - Infosys: 4 bullets complementing LSEG with data pipelines
5. Validates: python validate_yaml.py → ALL PASS
6. Generates: python src/simple_generator.py → output/Generated_Resume.docx
7. Confirms: "✅✅✅ WAYMO ML/RL - VALIDATED & READY ✅✅✅"
```

---

## IMPORTANT GITHUB LINKS

**Most Frequently Used:**
- LMARO: https://github.com/virtual457/llm-multi-agent-resume-optimizer
- Dino RL: https://github.com/virtual457/dino-game-AI
- Orion Platform: https://github.com/virtual457/Orion-platform
- Kambaz LMS: https://github.com/virtual457/kambaz-next-js
- Port Management: https://github.com/virtual457/Port-Management-System
- Face Recognition: https://github.com/virtual457/Recognition-and-Validation-of-Faces-using-Machine-Learning-and-Image-Processing
- PUBG Analysis: https://github.com/virtual457/Data-analysis-on-pubg
- Calendly: https://github.com/virtual457/Calendly

**Profile Links:**
- LinkedIn: https://www.linkedin.com/in/chandan-gowda-k-s-765194186/
- GitHub: https://github.com/virtual457
- Portfolio: https://virtual457.github.io/

---

## SUCCESS METRICS

**Good YAML produces:**
- ✅ All constraints met (see config/constraints.yaml for exact limits)
- ✅ 75%+ JD keyword match
- ✅ Natural flow (not keyword-stuffed)
- ✅ Factually accurate (all metrics verifiable)
- ✅ Appropriate tone (learning-focused if needed, production-proven when valuable)
- ✅ Working GitHub links
- ✅ Company-specific ending

**Expected callback rates:**
- 9-10/10 fit: 20-30%
- 8-8.5/10 fit: 15-20%
- 7-7.5/10 fit: 10-15%
- <7/10 fit: Skip (low ROI)

---

## POSITIONING FOR F1 VISA (CPT)

- User has **CPT work authorization** (no employer sponsorship required)
- Can work **40 hours/week** for 8 months
- **Zero cost/paperwork** for employer beyond offer letter
- Skip companies with explicit "no CPT/OPT" policies (HP, Lumafield)
- **INCLUDE "F1 CPT/OPT" in header title** for transparency and early filtering (concise format)

---

## ADDRESSING OVERQUALIFICATION

When needed:
- Use "Software Engineer" not "Senior Software Engineer" in title
- Lead with education (MS CS @ Northeastern, 3.89 GPA)
- Frame through co-op requirement
- Use "learn from" and "contribute to" language (sparingly)
- De-emphasize mentorship/leadership

---

## NEXT STEPS WHEN STARTING NEW SESSION

### Session Initialization Checklist

**✅ Step 1: Read CLAUDE.md (this file)**
- Understand system overview
- Check RECENT CHANGES LOG for latest updates
- Review CRITICAL QUALITY RULES section

**✅ Step 2: Read RESUME_GENERATION_GUIDELINES.md**
- **This is the living document** with user feedback
- Check User Feedback Log for latest corrections
- Review examples in relevant sections
- Understand user preferences and patterns

**✅ Step 3: Check Current Status**
- What company is in `config/current_application.yaml`?
- What was last generated?
- Any pending work?

**✅ Step 4: Ask User**
- "Ready for new JD or continue with current?"
- Don't assume - let user direct

**✅ Step 5: When User Provides JD**

**READ IN THIS EXACT ORDER:**
1. `docs/RESUME_GENERATION_GUIDELINES.md` (user preferences, feedback)
2. `docs/LLM_GUIDE_YAML_CREATION_v3.md` (technical YAML guide)
3. `docs/user_profile/CHANDAN_PROFILE_MASTER.md` (projects, skills)
4. `docs/user_profile/WORK_EXPERIENCE_DATABASE.md` (factual metrics)

**THEN GENERATE:**
1. Analyze JD (fit score, keywords)
2. Write summary PLAIN TEXT (no bold)
3. Write all bullets PLAIN TEXT (no bold)
4. Add bold markers (5-8 summary, 3-5 per bullet)
5. Verify constraints (char counts, bold counts)
6. Write to `config/current_application.yaml`
7. Tell user to run validation and generation

**✅ Step 6: After User Feedback**
- Add feedback to Guidelines User Feedback Log
- Update relevant sections if pattern change needed
- Document in RECENT CHANGES LOG if major

---

### Common First-Session Mistakes to Avoid

❌ **Skipping Guidelines document** - leads to repeating past mistakes
❌ **Writing with bold from start** - leads to exceeding limits
❌ **Using "showcasing" language** - user hates this
❌ **Including weak numbers** - reduces credibility
❌ **Short bullets** - all must be 150-250 chars
❌ **Fabricating experience** - verify EVERYTHING
❌ **Forgetting F1 CPT/OPT** - must be in header
❌ **Not explaining project purpose** - say WHAT it does first

---

## NEXT STEPS WHEN STARTING NEW SESSION

1. **Read this file:** `CLAUDE.md` (you're here!)
2. **Read Guidelines:** `docs/RESUME_GENERATION_GUIDELINES.md` (living document - check for updates)
3. **Check current status:** What's in `config/current_application.yaml`?
4. **Ask user:** "Ready for new JD or continue with current?"
5. **If new JD:**
   - Read ALL 4 docs in order (Guidelines → LLM Guide → Profile → Work Database)
   - Generate YAML
   - Validate
   - Run generator
   - Confirm ready
6. **If modifications:** Update YAML, validate, regenerate
7. **After user feedback:** Update Guidelines document with learned patterns

---

## TECHNICAL DETAILS

### Python Requirements
- python-docx
- PyYAML
- pathlib
- Standard library (os, time, etc.)

### Word Template Structure
- 41 paragraphs total
- Fixed sections: Header, Summary, Technical Skills, Work Experience, Projects
- Generator overwrites content but preserves formatting

### Validation Rules
Defined in `config/constraints.yaml`:
- Summary: min_chars, max_chars, min_bold, max_bold, required_keywords
- Skills: exact_categories, items_min_chars, items_max_chars
- Experience: exact_bullets per company, bullet_min_chars, bullet_max_chars, bullet_min_bold, bullet_max_bold
- Projects: exact_count, tech_max_chars, bullet_max_chars, bullet_min_bold, bullet_max_bold

---

## QUICK REFERENCE COMMANDS

```bash
# Navigate to project
cd D:\Git\virtual457-projects\job-application-automator

# Validate YAML
python validate_yaml.py

# Generate resume
python src/simple_generator.py

# Check git status
git status

# View recent changes
git diff config/current_application.yaml
```

---

## FILES TO NEVER MODIFY

- `templates/Chandan_Resume_Format.docx` (base template)
- `docs/user_profile/CHANDAN_PROFILE_MASTER.md` (only add projects, don't remove)
- `docs/user_profile/WORK_EXPERIENCE_DATABASE.md` (factual record)

## FILES TO MODIFY PER APPLICATION

- `config/current_application.yaml` (overwrite for each new job)

## FILES TO MODIFY FOR SYSTEM UPDATES

- `src/simple_generator.py` (generator logic, tab size, formatting)
- `validate_yaml.py` (validation logic)
- `config/constraints.yaml` (constraint rules)
- `CLAUDE.md` (this file - update status after major changes)

---

## RECENT CHANGES LOG

**2025-12-06 SESSION - COMPREHENSIVE RESUME GENERATION IMPROVEMENTS:**

**Major Workflow Changes:**
- **Bold Marker Workflow Revolution:** Changed from "bold while writing" to "write plain text first, then bold 5-8 key terms"
  - Eliminates exceeding bold limits
  - Saves significant time (no recounting iterations)
  - Results in better term selection (picks most important naturally)
  - Applied to summary AND all bullets (experience + projects)

**Quality & Factuality Enforcement:**
- **Zero Tolerance for Fabrication:** User caught Kubernetes fabrication at LSEG (LSEG had ZERO Kubernetes, only AWS)
  - Established: Always verify against WORK_EXPERIENCE_DATABASE.md
  - Rule: If uncertain, ASK user, never guess
- **Remove Weak Language:** Eliminated "showcasing", "demonstrating", "highlighting" from all bullets
  - Principle: Work demonstrates skill itself - don't add meta-commentary
  - Updated Guidelines with examples
- **Remove Weak Numbers:** Never use "1.5K+ lines", "15+ tables", "10 endpoints", "50+ procedures"
  - These reduce credibility and look AI-generated
  - Use descriptive language instead: "complex relational schema", "comprehensive stored procedures"
- **Professional English Standards:** User emphasized every sentence must be:
  - Well-thought-out (not filler)
  - Grammatically correct
  - Aligned with JD
  - Having real impact
  - Example caught: "implementing cloud best practices" = meaningless filler

**Content Structure Improvements:**
- **Projects Explain PURPOSE First:** Bullet 1 = WHAT it does, Bullet 2 = HOW it works
  - User said: "we need to explain what we do in the project like lmaro is a resume builder not just technicalities"
  - Updated all project bullets to lead with purpose/problem solved
- **Project Ordering by Spirit:** Prioritize projects matching JD emphasis even if other projects have exact framework matches
  - Example: For JD wanting "AI/ML exposure", put LMARO first even though Port Management has explicitly listed Django
  - Match what they WANT, not just what they SAY
- **All Bullets Must Be Proper Length:** Fixed recurring issue of bullets being too short
  - Infosys bullets were 105-134 chars (below 150 minimum)
  - Established: ALL bullets need 150-250 chars with full context

**Skills Section Updates:**
- **Removed Minimum Character Requirement:** Changed from 70-90 to max 90 only
  - User: "lets remove the minimum requirement for the categories lets add what is relevant and factual"
  - Principle: Quality over quantity - don't pad with filler
  - Updated constraints.yaml: removed items_min_chars, kept items_max_chars: 90

**Documentation Updates:**
- Added 3 detailed feedback entries to Guidelines User Feedback Log
- Created comprehensive "CRITICAL QUALITY RULES" section in CLAUDE.md
- Updated all 4 core docs with new workflows and constraints
- Added "Generate First, Bold Later" process documentation

**Resumes Generated This Session:**
1. Intuit Software Engineer (backend-focused) - 9.8/10 fit
2. Bose Cloud Identity Engineer - 9/10 fit
3. Cisco ML Infrastructure - 9.5/10 fit
4. Teradyne ML (LangChain focus) - 9.5/10 fit
5. Moody's Software Developer - 9/10 fit
6. PTC Onshape Full Stack - 8.5/10 fit
7. Dassault Systèmes AI Infrastructure - 9.8/10 fit (BEST MATCH - LangChain/RAG)
8. Simular AI Agents - 9.5/10 fit
9. OneStream AI Product - 8/10 fit
10. Domino Data Lab FDE - 8.5/10 fit
11. NYT AI Products Strategy - 8/10 fit
12. Camping World Agentic AI - 9.5/10 fit (LangChain perfect match)
13. Copart Software Engineer - 9/10 fit (Java/Spring)
14. Medical Device ML/CV - 8.5/10 fit
15. SAP Globalization - 8.5/10 fit
16. Tinder Backend Engineer - 9.5/10 fit (billions of events match)
17. Twitch Applied Science - 8.5/10 fit
18. GoFundMe Backend - 9/10 fit
19. Align Technology - 8/10 fit
20. Symbotic ML Scientist - 9/10 fit (PyTorch/CV)
21. NetApp Cloud Storage - 8.5/10 fit
22. IBM Storage Software - 8.5/10 fit
23. Tristar AI CV - 8.5/10 fit

**Key Patterns Identified:**
- LMARO is perfect for: LangChain roles, RAG systems, AI agents, semantic search
- Dino RL is perfect for: PyTorch roles, computer vision, RL, autonomous systems
- Orion Platform is perfect for: Kubernetes, Go, cloud infrastructure, DevOps
- LSEG experience strongest for: Backend at scale, distributed systems, AWS, compliance

---

**2025-12-03:**
- **WORKFLOW IMPROVEMENT - Bold Markers:** Generate plain text FIRST, then bold 5-8 key terms (saves time, ensures limit compliance)
- **CONSTRAINT UPDATE - Skills:** Removed minimum character requirement - now max 90 chars only (add only relevant, factual skills)
- Updated constraints.yaml: removed items_min_chars, kept items_max_chars: 90
- Updated all docs with new workflows and constraints
- Added "Generate First, Bold Later" process to Guidelines with step-by-step workflow
- **NEW FIELD:** Added `company_name` field to YAML structure for better tracking
- Updated YAML structure in CLAUDE.md and LLM_GUIDE_YAML_CREATION_v3.md to include company_name after header
- Format: `company_name: "[Company Name]"`
- **Reasoning:** Organizational improvement for tracking which company each resume is tailored for
- Generated Intuit Software Engineer Intern resume (9/10 fit)
- **CRITICAL UPDATE:** Made RESUME_GENERATION_GUIDELINES.md reading MANDATORY for every resume generation
- Added dedicated "LIVING DOCUMENT WORKFLOW" section explaining purpose and usage
- Updated YAML Generation Workflow to list Guidelines as #1 document to read (before all others)
- Added Guidelines to CRITICAL RULES → ALWAYS section
- Updated QUICK START to show Guidelines as first document
- Added guidelines to NEXT STEPS WHEN STARTING NEW SESSION
- **Reasoning:** Prevents repeating mistakes (like forgetting F1 CPT/OPT), captures user-specific preferences, provides institutional memory across sessions
- Generated Ai2 PRIOR Research Intern resume (9/10 fit)

**2025-12-01:**
- Created RESUME_GENERATION_GUIDELINES.md - living document for iterative feedback
- Generated NVIDIA Product Management Intern resume (9.5/10 fit)
- Projects used: LMARO (RAG/LangChain), Dino RL (PyTorch), Orion Platform (K8s)
- All validations passed: Summary 493c/7b, Skills 7 categories, Experience bullets optimized
- Updated CLAUDE.md to reference new guidelines document
- **FEEDBACK v1:** Changed policy to INCLUDE visa status in header title for transparency
- **FEEDBACK v2:** Shortened format "F-1 CPT/OPT Eligible" → "F1 CPT/OPT" for conciseness (saves ~10 chars)
- Updated guidelines, CLAUDE.md, and header template to reflect concise visa format

**2025-11-26:**
- Added LMARO project (#3) to CHANDAN_PROFILE_MASTER.md
- Updated positioning strategies for ML/AI roles to include LMARO
- Added RAG/LangChain/Multi-Agent keywords to ML section
- Changed tab size from 2.45" to 2.2" in simple_generator.py:189
- Deleted generate.bat (use Python command directly)
- Generated Waymo resume with LMARO (replaced Port Management)
- Created comprehensive CLAUDE.md handoff file
- **Increased bullet max from 200 → 250 chars** (constraints.yaml)
- **Lowered skills min from 70 → 35 chars** for Programming Languages (constraints.yaml)
- **Updated all docs to reference constraints.yaml** as single source of truth

---

## END OF HANDOFF

**System Status:** ✅ OPERATIONAL
**System Version:** v2.2 (comprehensive quality enforcement)
**Current YAML:** IBM Storage Software Engineer (8.5/10 fit)
**Last Generated:** December 6, 2025
**Validation Status:** Ready for validation
**Resume Output:** `output/Generated_Resume.docx`
**Guidelines:** Living document at `docs/RESUME_GENERATION_GUIDELINES.md` - **READ FIRST FOR EVERY GENERATION**

**Ready for next application!**

---

## KEY LEARNINGS QUICK REFERENCE (Dec 6, 2025 Session)

**For new Claude sessions - these are the MOST IMPORTANT rules learned:**

**1. WORKFLOW: Generate Plain → Then Bold**
   - Write all content WITHOUT bold first
   - Then pick 5-8 key terms for summary, 3-5 for each bullet
   - Never write with bold from start (always exceeds limits)

**2. FACTUALITY: Zero Tolerance**
   - Verify EVERY claim against databases
   - Never say "Kubernetes at LSEG" (LSEG = pure AWS)
   - When unsure, ASK user, never fabricate

**3. LANGUAGE: Remove Weak Words**
   - No "showcasing", "demonstrating", "highlighting"
   - No "1.5K+ lines", "15+ tables", "10 endpoints"
   - No meaningless filler like "implementing best practices"

**4. PROJECTS: Purpose Before Tech**
   - Bullet 1: WHAT it does ("resume optimizer", "logistics platform")
   - Bullet 2: HOW it works (technical details)
   - Don't lead with "Built backend server with 10 endpoints..."

**5. LENGTH: All Bullets 150-250 Chars**
   - Common mistake: Writing 120-140 char bullets (too short!)
   - Add context, details, impact to reach proper length

**6. ENGLISH: Every Sentence Matters**
   - User will call out bad English immediately
   - Don't write for the sake of writing
   - Each point must be factual + aligned + impactful

**Ready for next application!**