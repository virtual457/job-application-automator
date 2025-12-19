# Resume Generation Guidelines - Living Document

**Last Updated:** December 1, 2025
**Purpose:** Capture iterative feedback and best practices for each resume section
**Status:** Living document - continuously updated based on user feedback

---

## OVERVIEW

This document captures learned patterns, user feedback, and best practices for generating high-quality, ATS-optimized resumes. Update this file after each feedback cycle.

---

## HEADER SECTION

### Format
```yaml
header:
  name: "Chandan Gowda K S"
  title: "[Role] | MS CS @ Northeastern | F1 CPT/OPT | [Top 3-5 JD Keywords]"
  contact: "+1 (857) 421-7469; chandan.keelara@gmail.com; LinkedIn; Portfolio; GitHub;"
```

### Guidelines

**Title Construction:**
- Start with role name (exact or close match to JD)
- Always include: "MS CS @ Northeastern"
- **Include: "F1 CPT/OPT"** (concise visa status, filters non-CPT companies)
- End with 3-5 most important keywords from JD
- Keep under 110 characters total

**Reasoning for including visa status:**
- ✅ Transparency upfront - no surprises for recruiters
- ✅ Filters out companies with "no CPT/OPT" policies early
- ✅ CPT = authorized to work, no employer sponsorship needed
- ✅ Saves time for both candidate and recruiter
- ✅ Concise format frees space for more technical keywords

**Examples:**
- Product Management: `"Product Management Intern | MS CS @ Northeastern | F1 CPT/OPT | PyTorch, Kubernetes, AI"`
- ML Engineering: `"ML Engineer | MS CS @ Northeastern | F1 CPT/OPT | PyTorch, Deep RL, RAG, LangChain"`
- Backend: `"Software Engineer Intern | MS CS @ Northeastern | F1 CPT/OPT | Python, FastAPI, AWS, LLMs"`

### User Feedback Log
- **2025-12-01 (v1):** User requested to INCLUDE F-1 CPT/OPT status in header title for transparency. Updated format to include visa status after institution name. Adjusted character limit from 100 to 120 chars. Reasoning: Filters non-CPT companies early, shows authorization to work upfront.
- **2025-12-01 (v2):** User requested to shorten "F-1 CPT/OPT Eligible" → "F1 CPT/OPT" for conciseness. Removed hyphen and "Eligible" to save ~10 chars for more keywords. Updated char limit to 110.

---

## SUMMARY SECTION

### Constraints
- **Length:** 450-520 characters (strict)
- **Bold markers:** 5-8 using `**text**`
- **Required keywords:**
  - "MS Computer Science student at Northeastern"
  - "**3.89 GPA**" (must be bolded)
  - "London Stock Exchange Group" or "LSEG"
  - 2-3 LSEG metrics

### Philosophy: Narrative Flow Over Checklist

**❌ BAD - Choppy, disconnected sentences:**
```
MS Computer Science student at Northeastern (3.89 GPA) with research in Deep RL, Multi-Agent AI, and Computer Vision. Developed autonomous RL agent with PyTorch and multi-agent system. Published IEEE paper. Built systems at London Stock Exchange Group processing 7.5M+ records. Expertise in PyTorch, Deep RL, and agents. Excited to advance embodied AI at Ai2 PRIOR.
```
**Why it's bad:**
- Short, disconnected sentences
- No narrative flow
- Feels like bullet points mashed together
- "Expertise in..." adds no value
- "Published IEEE paper" feels tacked on
- Doesn't connect the work at LSEG to the target role

**✅ GOOD - Flowing narrative with connections:**
```
MS Computer Science student at Northeastern (**3.89 GPA**) building **autonomous AI agents** and **distributed systems**. Developed **PyTorch-based Deep RL agent** (1.5M params) and **multi-agent system** with **LangChain ReAct**, while engineering **production pipelines** at **London Stock Exchange Group** processing **7.5M+ records** across **180+ countries**. Published **IEEE paper** on AI systems. Passionate about advancing embodied AI and agent research at Ai2 PRIOR.
```
**Why it's good:**
- Flows naturally from education → projects → work → publication → passion
- Connects technical work to target role
- Specific details (1.5M params, 180+ countries) add credibility
- Each phrase builds on the previous
- Ends with genuine enthusiasm for specific research area

### Structure Guidelines (FLEXIBLE TEMPLATE)

**Core components that MUST appear:**
1. MS CS student at Northeastern (**3.89 GPA**) - Always first
2. LSEG mention with 1-2 key metrics
3. 1-2 most relevant projects/achievements
4. Company-specific ending

**Components are FLEXIBLE - adjust to create flow:**
- Don't force all 21 projects into summary
- Don't list skills separately (weave into narrative)
- Don't include "Expertise in..." statements (show, don't tell)
- Don't make every sentence the same length
- Don't disconnect sentences from each other

**Think: What story am I telling?**
- For Research role: "I do research (projects) + have production engineering skills (LSEG)"
- For Backend role: "I build production systems (LSEG) + have diverse technical projects"
- For ML role: "I build ML systems (projects) + have scale experience (LSEG)"

### Examples by Role Type

**Research Role (Ai2 PRIOR - Good):**
```
MS Computer Science student at Northeastern (**3.89 GPA**) building **autonomous AI agents** and **multi-agent systems**. Developed **PyTorch-based Deep RL agent** (1.5M params) mastering complex decision-making and **LangChain ReAct multi-agent system** with **semantic search** across **25+ repositories**. Published **IEEE paper** on AI systems while engineering **production-scale pipelines** at **London Stock Exchange Group** processing **7.5M+ records**. Passionate about advancing embodied AI research at Ai2 PRIOR.
```
- 502 chars, 8 bold
- Natural flow: projects → publication → production experience → passion
- Connects research projects to production engineering skills
- Specific metrics add credibility without feeling choppy

**ML/AI Role (Alternative):**
```
MS Computer Science student at Northeastern (**3.89 GPA**) with hands-on experience in **Deep RL**, **multi-agent AI**, and **production ML systems**. Built **PyTorch Deep RL agent** achieving real-time decision-making and **RAG-powered multi-agent system** with **LangChain**, while architecting **data pipelines** at **London Stock Exchange Group** serving **180+ countries** with **7.5M+ daily records**. Strong foundation in PyTorch, distributed systems, and AI research. Excited to advance LLM infrastructure at [Company].
```
- 495 chars, 8 bold
- Flow: education + focus → projects with results → production scale → excitement
- More concise, still tells complete story

**Backend/Systems Role:**
```
MS Computer Science student at Northeastern (**3.89 GPA**) with production experience building **distributed systems** and **cloud infrastructure**. Engineered **event-driven pipelines** processing **7.5M+ records** across **180+ countries** at **London Stock Exchange Group**, achieving **40% latency reduction**. Developed **Kubernetes operator in Go** and **full-stack AI applications**. Passionate about building scalable, reliable infrastructure at [Company].
```
- 463 chars, 7 bold
- Flow: education → production systems → specific projects → passion
- Emphasizes production experience first, projects second

### Writing Process

**NEW WORKFLOW - Generate First, Bold Later:**

**Step 1: Write content WITHOUT bold markers**
- Focus on narrative flow and grammar
- Don't worry about bold count yet
- Get the story right first
- Aim for 450-520 characters

**Step 2: Identify 5-8 most important terms to bold**
- Required: **3.89 GPA** (always bold)
- JD-relevant technologies (2-3 terms)
- Key metrics (1-2 numbers like 7.5M+, 40%)
- Role-specific keywords (1-2 terms)
- Count as you add: stop at 8 maximum

**Step 3: Verify constraints**
- Character count: 450-520 ✓
- Bold markers: 5-8 ✓
- Required keywords present ✓
- Flow still natural ✓

**Why this approach:**
- ✅ Ensures we don't exceed 8 bold limit
- ✅ Saves time (no counting while writing)
- ✅ Picks MOST important terms naturally
- ✅ Avoids over-bolding everything

---

**OLD PROCESS (Don't Use):**
~~Step 1: Identify the core story for this role~~
~~Step 2: Draft without worrying about constraints~~
~~Step 3: Edit for constraints~~
~~Step 4: Read aloud~~

### Common Mistakes to Avoid

❌ **Listing without connecting:**
```
Developed X. Built Y. Created Z. Expertise in A, B, C.
```

✅ **Weaving into narrative:**
```
Developed X and Y while building Z, demonstrating expertise in solving complex problems.
```

❌ **Generic "expertise" statements:**
```
Expertise in PyTorch, Deep RL, and agents.
```

✅ **Show through accomplishments:**
```
Built PyTorch Deep RL agent and multi-agent systems demonstrating hands-on ML engineering.
```

❌ **Choppy, disconnected facts:**
```
Published IEEE paper. Built systems at LSEG. Excited about role.
```

✅ **Connected narrative:**
```
Published IEEE paper on AI systems while engineering production pipelines at LSEG, bringing both research rigor and production experience to [role].
```

### Guidelines

**Numbers in Summary:**
- ✅ Use 2-3 key numbers maximum (GPA always counts as 1)
- ✅ Each number should add unique value to the story
- ✅ Common pattern: GPA + 1-2 production metrics (7.5M records, 180 countries, 40% improvement)
- ❌ Don't include 4+ numbers (overwhelming, competes for attention)
- ❌ Don't include numbers just because they exist (1.5M params, 25+ repos, etc.)
- **Principle:** Quality over quantity - fewer impactful numbers > many competing numbers

**DO:**
- ✅ Lead with education (MS CS, 3.89 GPA)
- ✅ Mention LSEG early for credibility
- ✅ Use 2-3 real LSEG metrics strategically
- ✅ Include top 2-3 projects if highly relevant
- ✅ End with company-specific statement
- ✅ Bold JD-relevant keywords
- ✅ Keep narrative flow (not keyword-stuffed)

**DON'T:**
- ❌ Use "seeking internship" or "looking for" language
- ❌ Exceed character limits (450-520 strict)
- ❌ Use more than 8 bold markers
- ❌ List technologies without context
- ❌ Use generic endings

### Examples by Role Type

**ML/AI Role (NVIDIA PM):**
```
MS Computer Science student at Northeastern (**3.89 GPA**) building **AI workflows** and **ML models** at **London Stock Exchange Group**. Developed **PyTorch Deep RL agent** (1.5M params), RAG system with LangChain, and Kubernetes operator in Go. Built systems processing **7.5M+ records** with 40% latency reduction, collaborating across 7 cross-functional teams. Strong in PyTorch, Kubernetes, AI automation, and product delivery. Excited to shape AI infrastructure platforms at **NVIDIA**.
```
- 493 chars, 7 bold
- Emphasizes: AI workflows, ML models, PyTorch, Kubernetes, enterprise scale
- Metrics: 7.5M+ records, 40% reduction
- Company-specific: "AI infrastructure platforms at NVIDIA"

**Backend/Distributed Systems:**
```
MS Computer Science student at Northeastern (**3.89 GPA**) with production experience building **distributed systems** and **microservices** at **London Stock Exchange Group**. Engineered event-driven pipeline processing **7.5M+ records** across **180+ countries** with **Python** and **AWS**, achieving **40% latency reduction**. Developed Kubernetes operator in Go and full-stack applications. Strong in Python, AWS, Kubernetes, distributed systems. Excited to build scalable infrastructure at **[Company]**.
```

**Full-Stack:**
```
MS Computer Science student at Northeastern (**3.89 GPA**) with full-stack experience at **London Stock Exchange Group**. Built **microservices** with **Python** and **Java** processing **7.5M+ records**, developed **Next.js** applications, and created **Kubernetes operator** in **Go**. Strong in React, Next.js, FastAPI, Django, AWS, and distributed systems. Excited to build end-to-end products at **[Company]**.
```

### User Feedback Log
- **2025-12-03 (v1):** User emphasized summary must have **narrative flow**, not choppy disconnected sentences. Template is FLEXIBLE guide, not rigid structure. "Expertise in..." statements add no value (show, don't tell). Each phrase should connect to the next. Recruiter only reads summary - must tell compelling story. Updated entire section with bad/good examples, writing process, and flexibility emphasis. Example of bad: "Developed X. Published Y. Built Z. Expertise in A, B, C." - feels like bullet points mashed together.
- **2025-12-03 (v2):** User clarified **don't overwhelm with too many numbers** in summary. Use **2-3 impactful numbers** (e.g., GPA + 1-2 key metrics) instead of 4+. Numbers should support the story, not compete for attention. Example: Removed "1.5M params" and "25+ repositories" from Ai2 summary, kept only "3.89 GPA", "7.5M+ records", "180+ countries" (3 numbers total). Quality over quantity - each number should add unique value.
- **2025-12-03 (v3):** User specified **DO NOT include IEEE paper in summary**. Keep publications in Achievements section only. Summary should focus on projects and work experience, not academic publications.

---

## SKILLS SECTION

### Constraints
- **Exact count:** 7 categories (no more, no less)
- **Character limit:** Maximum 90 characters per category (no minimum - add only relevant, factual skills)
- **Ordering:** By JD priority (most important first)

### Category Types & Typical Ordering

**For ML/AI Roles:**
1. Programming Languages
2. AI & Machine Learning
3. ML Engineering & Workflows (if RAG/LangChain/agents relevant)
4. Cloud & Infrastructure
5. Backend Development
6. Databases & Tools
7. Software Engineering & Product

**For Backend/Infrastructure Roles:**
1. Programming Languages
2. Backend Development
3. Cloud & Infrastructure
4. Databases & Tools
5. Development & DevOps
6. AI & Machine Learning (if mentioned in JD)
7. Software Engineering

**For Full-Stack Roles:**
1. Programming Languages
2. Backend Development
3. Frontend Development
4. Databases & Tools
5. Cloud & Infrastructure
6. Development & DevOps
7. Software Engineering

### Guidelines

**DO:**
- ✅ Extract top 50 keywords from JD
- ✅ Order categories by JD importance
- ✅ Include both acronyms and full terms where relevant
- ✅ Match JD language exactly when possible
- ✅ Balance breadth with depth

**DON'T:**
- ❌ Exceed 90 chars per category
- ❌ Include skills not actually possessed
- ❌ Duplicate skills across categories
- ❌ Use more or fewer than 7 categories
- ❌ Pad categories with irrelevant skills to meet character count

### Standard Category Templates

**Note:** No minimum character requirement - add only relevant skills. Maximum 90 chars per category.

```yaml
# Programming Languages (add all relevant)
"Python, Java, JavaScript, TypeScript, Go, C++, SQL"

# AI & Machine Learning (if relevant to JD)
"PyTorch, TensorFlow, Deep Learning, Neural Networks, Deep RL, Computer Vision, GPU Training"

# ML Engineering & Workflows (if RAG/agents relevant)
"RAG, LangChain, Multi-Agent Systems, Semantic Search, Vector Databases, AI Workflows"

# Backend Development
"Microservices, REST APIs, Distributed Systems, FastAPI, Django, Event-Driven Architecture"

# Cloud & Infrastructure
"AWS (Lambda, SQS, API Gateway), Docker, Kubernetes, Cloud Platforms, CI/CD"

# Frontend Development (if relevant)
"React, Next.js, TypeScript, Redux, Server-Side Rendering, Responsive Design"

# Databases
"MySQL, PostgreSQL, MongoDB, NoSQL, SQL Optimization, Database Design, Query Performance"

# Development & DevOps
"Git, CI/CD, Testing, Code Review, Agile, Docker, Deployment Automation"

# Software Engineering
"OOP, Design Patterns, System Design, Algorithms, Data Structures, Debugging, Scalability"
```

### User Feedback Log
- **2025-12-03 (v1):** User specified to ALWAYS use **"LLM Multi-Agent Resume Optimizer"** as the exact project title (not "LMARO" or "LLM Multi-Agent Resume Optimizer (LMARO)"). This is the standard title format. Updated YAML and will use consistently going forward.
- **[Date]:** [Feedback here]

---

## EXPERIENCE SECTION - LSEG

### Constraints
- **Exact bullets:** 5 (no more, no less)
- **Length:** 150-250 characters per bullet
- **Bold markers:** 3-5 per bullet
- **Factually accurate:** Use only real metrics from WORK_EXPERIENCE_DATABASE.md

### Real Metrics Available
- **7.5M+ records** processed daily
- **180+ countries** served
- **40 records/second** throughput
- **99.9% data integrity**
- **35% improvement** in turnaround time
- **40% latency reduction**
- **50% security incident reduction**
- **5 engineers** mentored
- **7 cross-functional teams**
- **Zero-downtime** migrations

### Technologies Used
- Python, Java (Micronaut)
- AWS Lambda, SQS, API Gateway, CloudWatch, WAF, IAM
- Event-driven architecture, Microservices
- KYC/AML compliance data

### Bullet Generation Strategy

**Bullet 1 (Flagship):**
- Most impressive achievement matching JD
- Largest scale metric
- Key technologies from JD
- 200-250 characters

**Bullets 2-4 (Supporting):**
- Different aspects of work
- Vary technologies mentioned
- Different metrics
- Build complete story

**Bullet 5 (Depth/Collaboration):**
- Technical depth OR
- Cross-functional collaboration OR
- Product/PM skills (if PM role)
- Avoid mentorship unless senior role

### Guidelines

**DO:**
- ✅ Generate FRESH bullets for each JD (never copy verbatim)
- ✅ Tailor language to match JD keywords
- ✅ Use real metrics from database
- ✅ Vary focus across bullets
- ✅ Tell coherent story
- ✅ Bold JD-relevant terms

**DON'T:**
- ❌ Copy database bullets word-for-word
- ❌ Fabricate metrics or technologies
- ❌ Repeat same focus across bullets
- ❌ Use more than 5 bold per bullet
- ❌ Exceed 250 characters

### Example Bullet Variations by Role

**For Product Management Role:**
```
"Built **enterprise-scale systems** with **Python** processing **7.5M+ records daily** across **180+ countries**, demonstrating **product delivery** and distributed systems expertise for global financial infrastructure."
```
- Emphasizes: product delivery, scale, distributed systems
- 5 bold, 218 chars

**For ML/AI Role:**
```
"Architected **data processing pipeline** with **Python** handling **7.5M+ records** for **AI-ready workflows**, achieving **99.9% data integrity** and enabling downstream ML model training at scale."
```
- Emphasizes: AI-ready, data quality, ML workflows
- 5 bold

**For Backend Role:**
```
"Engineered **event-driven pipeline** serving **180+ countries**, transforming **7.5M+ XML records** at **40 records/second** with **Python** and AWS, ensuring high-throughput microservices architecture."
```
- Emphasizes: event-driven, throughput, microservices
- 5 bold

### User Feedback Log
- **[Date]:** [Feedback here]

---

## EXPERIENCE SECTION - INFOSYS

### Constraints
- **Exact bullets:** 4 (no more, no less)
- **Length:** 150-250 characters per bullet
- **Bold markers:** 3-5 per bullet
- **Purpose:** Complement LSEG story (don't duplicate)

### Real Metrics Available
- **3x throughput** improvement
- **50% reduction** in manual interventions
- **35% latency reduction**
- **20% accuracy improvement**
- **100+ manual hours** eliminated weekly
- **25-30 concurrent executions**
- **10+ workflows** automated

### Technologies Used
- Python (primary)
- ETL pipelines, Data processing
- API orchestration, Microservices integration
- Automation workflows, Bot orchestration

### Guidelines

**DO:**
- ✅ Complement LSEG bullets (different focus)
- ✅ Fill gaps in JD requirements
- ✅ Show breadth of experience
- ✅ Use different metrics than LSEG

**DON'T:**
- ❌ Repeat LSEG achievements
- ❌ Use same technologies as primary focus
- ❌ Duplicate story

### Example Bullets by Role

**For ML/AI Role:**
```
"Engineered **Python data pipelines** with **concurrent execution**, achieving **3x throughput improvement** through performance tuning, showcasing ability to optimize **ML-adjacent workflows** and backend systems."
```

**For Product Management:**
```
"Designed **API orchestration** and **microservices integration**, reducing manual interventions by **50%** through automation, demonstrating **product thinking** for workflow optimization and enterprise integration."
```

### User Feedback Log
- **[Date]:** [Feedback here]

---

## PROJECTS SECTION

### Constraints
- **Exact count:** 3 projects
- **Ordering:** Most JD-relevant first
- **Tech line:** Max 80 characters
- **Bullets:** Max 250 characters each, 3-5 bold each
- **Fields:** Use `bullet1` and `bullet2` (NOT `bullets` array)

### Project Selection by Role Type

**ML/AI Roles:**
1. LMARO (RAG, LangChain, multi-agent) OR Dino RL (PyTorch, GPU)
2. Dino RL (PyTorch, Deep RL) OR Face Recognition (TensorFlow, CNN)
3. LMARO OR Face Recognition OR PUBG Analysis

**Backend/Distributed Systems:**
1. Orion Platform (Kubernetes, Go)
2. Port Management (Django, SQL) OR LMARO (backend focus)
3. Calendly (Java, design patterns) OR Kambaz LMS

**Full-Stack:**
1. LMARO (FastAPI + Next.js) OR Kambaz LMS
2. Kambaz LMS OR Port Management
3. Port Management OR Online Exam System

**Cloud/DevOps:**
1. Orion Platform (Kubernetes operator)
2. LMARO (infrastructure) OR Port Management
3. Kambaz LMS (deployment)

**Product Management + Technical:**
1. LMARO (end-to-end product)
2. Dino RL (ML product) OR Orion Platform (infrastructure product)
3. Kambaz LMS (full product lifecycle)

### Guidelines

**DO:**
- ✅ Select projects matching JD tech stack
- ✅ Order by relevance (most relevant first)
- ✅ Generate custom bullets emphasizing JD aspects
- ✅ Use exact GitHub URLs from CHANDAN_PROFILE_MASTER.md
- ✅ Bold JD-relevant technologies and metrics

**DON'T:**
- ❌ Include projects not in profile database
- ❌ Use incorrect GitHub links
- ❌ Exceed 250 chars per bullet
- ❌ Use more than 5 bold per bullet
- ❌ Use `bullets` array (use `bullet1`, `bullet2`)

### Example Project Bullets

**LMARO for ML/AI Role:**
```yaml
bullet1: "Architected **end-to-end AI product** with **LangChain ReAct agent**, **RAG system** (ChromaDB vector database), and **FastAPI backend**, demonstrating **full-stack AI workflow development** from concept to deployment."
bullet2: "Implemented **AI-powered automation** with **multi-agent orchestration**, **tool calling**, and semantic search across **25+ repositories**, achieving **90+ quality scores** through iterative refinement, showcasing AI integration."
```

**Orion Platform for Cloud/DevOps:**
```yaml
bullet1: "Built **Kubernetes-native platform** with **custom operator in Go** (1.5K+ lines), enabling **single-command deployment** and **automated provisioning** of PostgreSQL, Redis, MinIO, demonstrating **K8s orchestration** for AI infrastructure."
bullet2: "Architected **event-driven reconciliation** with **CRDs** and **health monitoring**, supporting **10+ concurrent deployments** with sub-second sync, showcasing **distributed systems design** and infrastructure-as-code for enterprise platforms."
```

### User Feedback Log
- **[Date]:** [Feedback here]

---

## GENERAL PRINCIPLES

### ATS Optimization
- Use exact JD keywords naturally
- Include both acronyms and full terms (e.g., "ML" and "Machine Learning")
- Bold important keywords strategically
- Maintain natural narrative flow

### Tone & Voice
- Professional, confident, factual
- Active voice (built, developed, architected)
- Past tense for completed work
- Quantify achievements with metrics
- Avoid fluff and superlatives

### Common Patterns

**For Product Management Roles:**
- Emphasize: product delivery, cross-functional collaboration, stakeholder management
- Include: product thinking, end-to-end ownership, user-focused
- Show: technical depth + product mindset

**For ML/AI Roles:**
- Lead with: ML frameworks, model training, AI systems
- Show: hands-on technical skills (PyTorch, TensorFlow)
- Include: metrics (parameters, accuracy, FPS)

**For Backend/Infrastructure:**
- Focus on: scale, performance, reliability
- Show: distributed systems, microservices, cloud
- Include: throughput, latency, uptime metrics

### What Makes a Great Resume

✅ **JD-Specific:** Every section tailored to this specific role
✅ **Factually Accurate:** All metrics and technologies verifiable
✅ **Coherent Story:** Flows logically from summary → experience → projects
✅ **Natural Language:** Reads well, not keyword-stuffed
✅ **Constraint-Compliant:** Passes all validation checks
✅ **Keyword-Optimized:** 75%+ JD keyword match

---

## USER FEEDBACK LOG

### Format for Adding Feedback

```
**Date:** YYYY-MM-DD
**Section:** [Summary/Skills/Experience/Projects/General]
**Feedback:** [User's feedback verbatim]
**Action Taken:** [What was changed in guidelines]
**Example:** [Before/After if applicable]
---
```

### Feedback History

**Date:** 2025-12-01
**Section:** Initial Creation
**Feedback:** User requested guidelines.md file to integrate iterative feedback
**Action Taken:** Created comprehensive living document with all sections
**Example:** N/A
---

**Date:** 2025-12-03
**Section:** General - Tool Usage
**Feedback:** User emphasized to NEVER use code/bash capabilities, ONLY use Filesystem tools
**Action Taken:** Added reminder to always use Filesystem tools (read_text_file, edit_file, write_file, etc.) instead of bash_tool for validation and generation
**Example:** ❌ bash_tool for validation → ✅ Manual validation using Filesystem tools
---

**Date:** 2025-12-03
**Section:** Summary - Bold Markers
**Feedback:** Initial FanDuel summary had 12 bold markers (exceeded 8 max). User caught violation of Guidelines constraint.
**Action Taken:** Reduced bold markers from 12 to 7 by removing bold from: "microservices", "React and Next.js applications", "advanced SQL", "RESTful APIs", "team environments", keeping only: GPA, full-stack development, LSEG, Java and Python, 7.5M+ records, 40% latency reduction, heavily regulated
**Example:** 
Before: 12 bold markers (violated constraint)
After: 7 bold markers (within 5-8 range)
---

**Date:** 2025-12-03
**Section:** Summary - Narrative Flow
**Feedback:** Initial FanDuel summary had disconnected sentence "Developed React, Next.js, and Django applications" that didn't flow naturally
**Action Taken:** Connected sentences using "while developing" to create narrative flow from backend → frontend work
**Example:**
Before: "Engineered Python and Java systems... Developed React, Next.js, and Django applications." (disconnected)
After: "Built Java and Python microservices... while developing React and Next.js applications..." (connected flow)
---

**Date:** 2025-12-03
**Section:** Summary - CRITICAL FACTUAL ACCURACY
**Feedback:** User caught FABRICATION: Summary claimed full-stack/React/Next.js work at LSEG, but LSEG was PURELY BACKEND (Java/Python microservices, AWS, data pipelines). NO frontend work at LSEG.
**Action Taken:** Fixed to separate LSEG backend work from project-based full-stack experience. NEVER claim work experience that didn't happen. Full-stack comes from PROJECTS (LMARO, Kambaz, Port Management), NOT LSEG.
**Example:**
Before (FABRICATED): "full-stack development experience at London Stock Exchange Group... while developing React and Next.js applications"
After (ACCURATE): "backend engineering at London Stock Exchange Group... Developed full-stack projects with React, Next.js"
**CRITICAL RULE:** Always verify work experience claims against WORK_EXPERIENCE_DATABASE.md. LSEG = backend only. Projects = full-stack.
---

**Date:** 2025-12-03
**Section:** Summary - Tell a Story About the PERSON, Not Project Features
**Feedback:** Glean summary was too project-focused with excessive details: "Architected semantic search across diverse data sources (GitHub repos, work history, skills, projects, certifications), achieving 90+ quality scores..." User said: "we dont have to give so much details about the project in the summary it must be a story about myself"
**Action Taken:** Rewrote to focus on WHO the person is (expertise areas) rather than WHAT the project does (feature list). Summary should tell YOUR story as a builder/engineer, not enumerate project capabilities.
**Example:**
Before (PROJECT-FOCUSED): "Architected semantic search across diverse data sources (GitHub repos, work history, skills, projects, certifications), achieving 90+ quality scores through multi-agent AI"
After (PERSON-FOCUSED): "with expertise in enterprise search, RAG systems, and backend engineering. Built semantic search and multi-agent AI systems"
**KEY PRINCIPLE:** Summary = who you are + what you've built + your passion. NOT a feature specification of your projects.
---

**Date:** 2025-12-03
**Section:** Projects - LMARO Scope Update
**Feedback:** User corrected LMARO project scope - it's NOT just "25+ GitHub repositories". It's a comprehensive knowledge system searching across: GitHub repositories, work experience history, education, skills, projects, certifications (both structured and unstructured data).
**Action Taken:** Updated CHANDAN_PROFILE_MASTER.md LMARO section to accurately reflect comprehensive data ingestion across enterprise knowledge sources. Updated resume bullet templates to say "comprehensive data sources" or "diverse knowledge sources" instead of "25+ GitHub repositories".
**Example:**
Before (INCOMPLETE): "semantic search across 25+ GitHub repositories"
After (ACCURATE): "semantic search across comprehensive data sources (GitHub code, work history, education, skills, projects, certifications)"
**CRITICAL RULE:** LMARO searches across ALL enterprise knowledge (structured + unstructured), not just code repos. This is what makes it similar to Glean's Enterprise Graph.
---

**Date:** 2025-12-03
**Section:** Summary - Grammar & English Clarity
**Feedback:** User caught awkward phrasing: "processing 7.5M+ records with 40% latency reduction" - grammatically incorrect. You can't "process records WITH latency reduction". These are two separate achievements forced together.
**Action Taken:** Fixed to proper English using "and achieving" to connect separate accomplishments: "processing 7.5M+ records and achieving 40% latency reduction"
**Example:**
❌ Before (AWKWARD): "processing 7.5M+ records with 40% latency reduction"
✅ After (CORRECT): "processing 7.5M+ records and achieving 40% latency reduction"
**KEY RULE:** Use "and achieving" or "and" to connect separate metrics. Don't use "with" when metrics aren't causally related. Read summaries aloud to catch awkward phrasing.
---

**Date:** 2025-12-03
**Section:** Projects - Explain WHAT Projects Do, Not Just Technical Specs
**Feedback:** User said project bullets were too technical without explaining PURPOSE. For Intuit backend-focused resume, LMARO bullets were: "Built backend server with FastAPI framework (10 REST endpoints, WebSocket/SSE)..." User asked: "we need to explain what we do in the project like what it is like lmaro is a resume builder and optimizer not just technicalities and numbers"
**Action Taken:** Rewrote project bullets to explain WHAT the project does FIRST (resume optimizer, logistics platform, calendar app), THEN show technical implementation. Bullet 1 = purpose + impact, Bullet 2 = technical depth.
**Example:**
❌ Before (TECH-ONLY): "Built backend server with FastAPI framework (10 REST endpoints, WebSocket/SSE) and database integration..."
✅ After (PURPOSE-FIRST): "Built AI-powered resume optimization platform that intelligently tailors resumes to job descriptions using RAG, semantic search, and multi-agent AI..."
**KEY PRINCIPLE:** Projects should answer "What does this do?" before "How is it built?". Recruiters care about problem-solving, not just tech stack.
---

**Date:** 2025-12-03
**Section:** Projects - Ordering by Role Requirements
**Feedback:** For Intuit backend-focused posting emphasizing AI/ML exposure, user questioned why Port Management (Django) was before LMARO (FastAPI + AI). Initially ordered Port Management first because Django was explicitly mentioned in JD.
**Action Taken:** Reordered to put LMARO first because: (1) JD explicitly wants "AI/ML exposure" and LMARO is the strongest AI project, (2) FastAPI is still a modern server framework even if not explicitly listed, (3) More impressive overall project. Changed order from Port Management → LMARO → Calendly to LMARO → Port Management → Calendly.
**Example:**
❌ Before: Port Management first (because Django explicitly listed)
✅ After: LMARO first (because AI/ML exposure explicitly wanted + more impressive)
**KEY PRINCIPLE:** When JD explicitly calls out something like "AI/ML exposure", prioritize projects demonstrating that, even if other projects match explicit framework names. Match the spirit, not just keywords.
---

**Date:** 2025-12-03
**Section:** Skills - Character Limit Update
**Feedback:** User requested to change skills character limits from 35-95 to 70-90 for ALL categories (no exceptions).
**Action Taken:** Updated constraints.yaml from items_min_chars: 35, items_max_chars: 95 → items_min_chars: 70, items_max_chars: 90. Updated all documentation (CLAUDE.md, LLM_GUIDE, RESUME_GENERATION_GUIDELINES.md) to reflect 70-90 range. Removed Programming Languages exception.
**Example:**
Before: 35-95 chars (Programming Languages ~40, others 70-95)
After: 70-90 chars (all categories standardized)
**Reasoning:** Standardized range ensures more consistent category lengths, eliminates special cases, easier to remember and validate.
---

**Date:** 2025-12-03
**Section:** Skills - Remove Minimum Requirement
**Feedback:** User said "lets remove the minimum requirement for the categories lets add what is relevant and factual" - don't pad categories to meet arbitrary character counts.
**Action Taken:** Removed items_min_chars from constraints.yaml. Updated to: "Maximum 90 characters per category (no minimum - add only relevant, factual skills)". Updated all docs to reflect this.
**Example:**
Before: 70-90 chars (forced to add filler to meet 70)
After: Max 90 chars (add only what's relevant)
**KEY PRINCIPLE:** Quality over quantity. Include only skills that are real and relevant to JD. Don't pad with filler.
---

**Date:** 2025-12-03
**Section:** Summary - NEW Bold Marker Workflow
**Feedback:** User said "we are always increasing the number of bold when generating content. lets generate without bold and then after generating lets try to find things to bold so that we will have count and will save time"
**Action Taken:** Changed writing process to: (1) Write content WITHOUT bold first, focusing on flow and grammar, (2) THEN identify 5-8 most important terms to bold, (3) Verify constraints. Updated Writing Process section with new workflow.
**Example:**
Old approach: Write with bold → often exceed 8 → remove bold → recount → repeat
New approach: Write plain text → pick 5-8 best terms → bold them → done
**KEY BENEFIT:** Saves time, ensures we never exceed limit, picks most important terms naturally.
---

**Date:** 2025-12-03
**Section:** Projects - Remove Weak "Showcasing" Language
**Feedback:** User caught weak resume writing in project bullets: "Built RESTful API with MongoDB integration, showcasing backend engineering" - the word "showcasing" is unnecessary filler. User said: "why are you telling showcasing so and so in resume just showcase in project bullets"
**Action Taken:** Removed all "showcasing", "demonstrating", "highlighting" phrases from project bullets. The work itself demonstrates the skill - don't explicitly say "showcasing".
**Example:**
❌ Before (WEAK): "Built RESTful API with MongoDB integration, showcasing backend engineering, NoSQL databases, and TypeScript proficiency"
✅ After (STRONG): "Built RESTful API with MongoDB integration for backend engineering, NoSQL databases, and TypeScript proficiency"
**KEY PRINCIPLE:** State what was done confidently. The accomplishment speaks for itself. Don't add meta-commentary like "showcasing" or "demonstrating" - it weakens the statement.
---

---

## HOW TO USE THIS DOCUMENT

1. **Before generating YAML:** Review relevant sections for the role type
2. **During generation:** Follow guidelines and constraints strictly
3. **After user feedback:** Add to feedback log in relevant section
4. **Update guidelines:** Modify templates/examples based on feedback
5. **Version control:** Commit changes with descriptive messages

---

## QUICK REFERENCE CHECKLIST

Before finalizing YAML:

- [ ] Summary: 450-520 chars, 5-8 bold, includes required keywords
- [ ] Skills: Exactly 7 categories, max 90 chars each (no minimum), JD-prioritized
- [ ] LSEG: 5 bullets, 150-250 chars, 3-5 bold, uses real metrics
- [ ] Infosys: 4 bullets, 150-250 chars, 3-5 bold, complements LSEG
- [ ] Projects: 3 projects, ordered by relevance, tech max 80 chars
- [ ] Project bullets: Max 250 chars, 3-5 bold each
- [ ] All metrics factually accurate
- [ ] JD keywords naturally integrated
- [ ] Passes `python validate_yaml.py`

---

**END OF GUIDELINES**

*This is a living document. Update after each feedback cycle to continuously improve resume quality.*
