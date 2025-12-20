# LaTeX Resume Generation - Constraints & Rules

**Last Updated:** December 19, 2025

This file defines the strict rules and constraints for LaTeX resume generation.

---

## 📋 YAML STRUCTURE REQUIREMENTS

### Header Section
```yaml
header:
  name: STRING (required)
  title: STRING (optional, can be empty "")
  contact: STRING (required, raw LaTeX format)
```

**Constraints:**
- `name`: 1-50 characters
- `title`: 0-120 characters (leave empty "" for no subtitle)
- `contact`: Must be valid LaTeX with \\textbar\\ and \\href{} commands

---

### Company Name
```yaml
company_name: STRING (required)
```

**Constraints:**
- 1-100 characters
- Used for tracking only (not displayed in resume)

---

### Education Section
```yaml
education:
  ms_coursework: STRING (required)
  be_coursework: STRING (required)
```

**Constraints:**
- `ms_coursework`: 50-150 characters, 2-4 courses recommended
- `be_coursework`: 50-150 characters, 3-5 courses recommended

**Examples:**
- ML roles: "Machine Learning, Natural Language Processing, Deep Learning, Database Management"
- Backend: "Advanced Algorithms & Data Structures, Database Management Systems, Web Development"
- Full-Stack: "Web Development (MERN), Database Management, Machine Learning"

---

### Skills Section
```yaml
skills:
  - category: STRING
    items: STRING
  # ... repeat for exactly 7 categories
```

**Constraints:**
- **Exactly 7 categories** (no more, no less)
- `category`: 10-40 characters (short names like "Programming Languages", "AI & ML")
- `items`: 30-120 characters per category (add only relevant skills)
- Order categories by JD priority (most important first)

**Category Naming Guidelines:**
- ✅ Use: "Programming Languages", "AI & ML", "Backend Development"
- ❌ Avoid: "ML Engineering & Infrastructure" (too long)
- ❌ Avoid: "Container & Orchestration" (too niche)

---

### Work Experience Section
```yaml
experience:
  - company: STRING (required)
    role: STRING (required)
    duration: STRING (required)
    bullets: LIST (required)
  # ... repeat for 2 companies (LSEG, Infosys)
```

**Constraints:**
- **Exactly 2 companies:** LSEG (5 bullets), Infosys (4 bullets)
- `company`: 10-60 characters
- `role`: 10-40 characters (use "Software Engineer" not "Senior Software Engineer")
- `duration`: Fixed format "MMM YYYY -- MMM YYYY" (e.g., "Aug 2022 -- Dec 2024")
- `bullets`: Array of strings

**Bullet Constraints:**
- LSEG: Exactly 5 bullets
- Infosys: Exactly 4 bullets
- Each bullet: 150-300 characters
- Each bullet: 3-6 bold markers using `**text**`
- Must be factually accurate (from WORK_EXPERIENCE_DATABASE.md)

**Bold Marker Guidelines:**
- Bold: Technologies, metrics, key actions
- Don't bold: Articles (a, the), prepositions (in, on, for)
- Examples: `**Python**`, `**7.5M+ records**`, `**40% improvement**`

---

### Projects Section
```yaml
projects:
  - title: STRING (required)
    tech: STRING (required)
    github_link: STRING (required, must be valid URL)
    bullet1: STRING (required)
    bullet2: STRING (required)
  # ... repeat for exactly 3 projects
```

**Constraints:**
- **Exactly 3 projects**
- `title`: 10-60 characters (exact match to GitHub repository name)
- `tech`: 30-100 characters (comma-separated tech stack)
- `github_link`: Must be full URL starting with https://github.com/
- `bullet1`, `bullet2`: 150-300 characters each
- Each bullet: 3-6 bold markers using `**text**`

**Project Ordering:**
- Order by JD relevance (most relevant first)
- First project should be strongest match to JD requirements

---

## 📊 CHARACTER COUNT TARGETS

### Skills Categories
```
Min: 30 characters
Max: 120 characters
Optimal: 60-90 characters
```

### Work Experience Bullets
```
Min: 150 characters
Max: 300 characters
Optimal: 180-250 characters
```

### Project Bullets
```
Min: 150 characters
Max: 300 characters
Optimal: 200-280 characters
```

### Education Coursework
```
Min: 50 characters
Max: 150 characters
Optimal: 80-120 characters (3-4 courses)
```

---

## 🎯 BOLD MARKER GUIDELINES

### How Many Bold Markers?

**Work Experience Bullets:**
- Minimum: 3 bold markers
- Maximum: 6 bold markers
- Optimal: 4-5 bold markers

**Project Bullets:**
- Minimum: 3 bold markers
- Maximum: 6 bold markers
- Optimal: 4-5 bold markers

### What to Bold?

**Always bold:**
- ✅ Technologies: `**Python**`, `**AWS Lambda**`, `**PyTorch**`
- ✅ Metrics: `**7.5M+ records**`, `**40% improvement**`, `**99.9% uptime**`
- ✅ Key actions: `**architected**`, `**optimized**`, `**implemented**`

**Never bold:**
- ❌ Articles: a, an, the
- ❌ Prepositions: in, on, for, with, through
- ❌ Common words: and, or, by, to

**Example:**
```yaml
"Built **event-driven services** on **AWS Lambda** improving **latency by 40%**"
```
Bold count: 3 ✓

---

## 📏 VALIDATION RULES

### Before Generating LaTeX:

**Header:**
- [ ] Name is present and non-empty
- [ ] Contact has valid LaTeX formatting
- [ ] Title is optional (can be empty)

**Education:**
- [ ] Both ms_coursework and be_coursework present
- [ ] Each has 2-5 courses

**Skills:**
- [ ] Exactly 7 categories
- [ ] Each category has items
- [ ] No category exceeds 120 chars

**Experience:**
- [ ] Exactly 2 companies (LSEG, Infosys)
- [ ] LSEG has exactly 5 bullets
- [ ] Infosys has exactly 4 bullets
- [ ] All bullets have 3-6 bold markers

**Projects:**
- [ ] Exactly 3 projects
- [ ] Each has title, tech, github_link, bullet1, bullet2
- [ ] All GitHub links are valid URLs

---

## 🚫 COMMON MISTAKES TO AVOID

### ❌ Wrong YAML Structure
```yaml
# WRONG - missing education section
header: {...}
skills: [...]
```

### ✅ Correct YAML Structure
```yaml
header: {...}
education:
  ms_coursework: "..."
  be_coursework: "..."
skills: [...]
```

---

### ❌ Too Many/Few Skills Categories
```yaml
# WRONG - only 5 categories
skills:
  - category: "Languages"
    items: "Python, Java"
  # ... only 5 total
```

### ✅ Correct - Exactly 7
```yaml
skills:
  - category: "Programming Languages"
    items: "Python, Java, Go"
  # ... must have exactly 7
```

---

### ❌ Wrong Bullet Count
```yaml
# WRONG - LSEG has 4 bullets (should be 5)
experience:
  - company: "LSEG"
    bullets:
      - "Bullet 1"
      - "Bullet 2"
      - "Bullet 3"
      - "Bullet 4"
```

### ✅ Correct - 5 bullets for LSEG
```yaml
experience:
  - company: "LSEG"
    bullets:
      - "Bullet 1"
      - "Bullet 2"
      - "Bullet 3"
      - "Bullet 4"
      - "Bullet 5"
```

---

## 📖 TEMPLATE VARIABLES REFERENCE

### Available in Templates

```
header.name          - Full name
header.title         - Subtitle (optional)
header.contact       - Contact line (raw LaTeX)

company_name         - Target company

education.ms_coursework  - MS relevant courses
education.be_coursework  - BE relevant courses

skills               - List of {category, items}
experience           - List of {company, role, duration, bullets}
projects             - List of {title, tech, github_link, bullet1, bullet2}
```

---

## 🎯 QUALITY STANDARDS

### Professional English
- ✅ Complete sentences
- ✅ Proper grammar
- ✅ Active voice
- ✅ Varied sentence structure
- ❌ No "showcasing", "demonstrating" filler words

### Factual Accuracy
- ✅ All metrics from WORK_EXPERIENCE_DATABASE.md
- ✅ All technologies actually used
- ✅ All project details from CHANDAN_PROFILE_MASTER.md
- ❌ No fabrication
- ❌ No exaggeration

### Technical Depth
- ✅ Specific technologies mentioned
- ✅ Clear business impact
- ✅ Quantified results
- ❌ No vague statements
- ❌ No weak numbers ("10+ endpoints", "15+ tables")

---

**END OF CONSTRAINTS**

Use this as reference when creating YAML configurations.
