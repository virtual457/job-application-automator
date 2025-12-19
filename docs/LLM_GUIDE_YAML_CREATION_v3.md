# LLM Guide v3: Dynamic YAML Generation

**⚠️ CONSTRAINTS:** All limits defined in `config/constraints.yaml` - Validate with `python validate_yaml.py`

**Last Updated:** November 26, 2025
**Major Updates:**
- Work experience bullets generated dynamically based on JD
- Narrative flow summaries (no "seeking internship")
- All content customized per application
- **Bullet max: 250 chars** (increased for more space)
- **Skills: Max 90 chars** (no minimum - add only relevant skills)
- **Bold marker workflow:** Generate plain text first, then bold 5-8 key terms

---

## 🎯 GENERATION PHILOSOPHY

**Everything is dynamic and JD-specific:**
- ✅ Summary tailored to company and role focus
- ✅ Skills ordered by JD keyword priority
- ✅ **Work experience bullets generated fresh** (not selected from templates)
- ✅ Projects chosen and bullets written to match JD
- ✅ All using factual foundation from user profile database

**The databases are REFERENCE MATERIAL, not selection menus!**

---

## 📚 REQUIRED READING BEFORE GENERATION

**You MUST read these files for EVERY JD:**

1. **`docs/user_profile/CHANDAN_PROFILE_MASTER.md`**
   - Education details
   - Complete project portfolio (20 projects)
   - Keyword banks
   - Positioning strategies

2. **`docs/user_profile/WORK_EXPERIENCE_DATABASE.md`**
   - Actual work done at LSEG and Infosys
   - Real metrics and technologies
   - Example bullet variations
   - Bullet generation guidelines

---

## 📋 COMPLETE YAML STRUCTURE

```yaml
header:
  name: "Chandan Gowda K S"
  title: "[Role | MS CS @ Northeastern | Top 3-5 JD Keywords]"
  contact: "+1 (857) 421-7469; chandan.keelara@gmail.com; LinkedIn; Portfolio; GitHub;"

company_name: "[Company Name]"

summary: "[Narrative flow, 450-520 chars, 5-8 **bold** markers, company-specific]"

skills:
  - category: "[Category 1 - Most Important to JD]"
    items: "[Skills matching JD, max 90 chars - add only relevant]"

  - category: "[Category 2]"
    items: "[Skills, max 90 chars - add only relevant]"

  # ... exactly 7 categories total, ordered by JD priority

experience:
  - company: "London Stock Exchange Group (LSEG)"
    role: "Senior Software Engineer"
    location: "Bengaluru"
    duration: "08-2022 to 12-2024"
    bullets:
      - "[Custom bullet 1 with **bold**, 150-250 chars]"
      - "[Custom bullet 2 with **bold**, 150-250 chars]"
      - "[Custom bullet 3 with **bold**, 150-250 chars]"
      - "[Custom bullet 4 with **bold**, 150-250 chars]"
      - "[Custom bullet 5 with **bold**, 150-250 chars]"

  - company: "Infosys"
    role: "Senior Systems Engineer"
    location: "Bengaluru"
    duration: "10-2020 to 07-2022"
    bullets:
      - "[Custom bullet 1 with **bold**, 150-250 chars]"
      - "[Custom bullet 2 with **bold**, 150-250 chars]"
      - "[Custom bullet 3 with **bold**, 150-250 chars]"
      - "[Custom bullet 4 with **bold**, 150-250 chars]"

projects:
  - title: "[Project Name - EXACT MATCH to GitHub dict]"
    tech: "[Tech stack, max 80 chars]"
    github: "GitHub"
    bullet1: "[Custom bullet with **bold**, max 250 chars]"
    bullet2: "[Custom bullet with **bold**, max 250 chars]"
  
  # ... exactly 3 projects, ordered by JD relevance
```

---

## 🔄 COMPLETE GENERATION WORKFLOW

### Step 1: Analyze the Job Description (5 minutes)

**Extract and document:**

1. **Primary Technologies (rank by importance):**
   - Language: Python? Java? Go? JavaScript?
   - Backend: Microservices? APIs? Distributed systems?
   - Cloud: AWS? Kubernetes? Docker?
   - Other: ML? Databases? Frontend?

2. **Role Category:**
   - Backend engineer
   - ML/AI engineer
   - Full-stack developer
   - Data engineer
   - DevOps/Platform engineer
   - Automation/Workflow engineer

3. **Key Focus Areas:**
   - Performance optimization?
   - Scale/throughput?
   - Automation/workflows?
   - Security/compliance?
   - ML/AI integration?
   - Team collaboration?

4. **Important Keywords (list 15-20):**
   - Technologies, frameworks, practices mentioned
   - Both acronyms and full terms
   - Domain-specific terms

### Step 2: Generate Summary (Narrative Flow)

**Read:** WORK_EXPERIENCE_DATABASE.md for LSEG metrics

**NEW WORKFLOW:**

**Step 2a: Write plain text summary (450-520 chars)**
```
MS Computer Science student at Northeastern (3.89 GPA) with backend engineering experience in Java, Python, and Django. Built Spring-based microservices and RESTful APIs at London Stock Exchange Group processing 7.5M+ records and achieving 40% latency reduction. [Continue story...]
```

**Step 2b: Identify 5-8 most important terms to bold**
- Required: **3.89 GPA** (always)
- Technologies matching JD: **Java**, **Python**, **Django** (2-3 terms)
- Metrics: **7.5M+ records**, **40% latency reduction** (1-2 terms)
- Role keywords: **backend engineering**, **RESTful APIs** (1-2 terms)
- Stop at 8 maximum

**Step 2c: Add bold markers to selected terms**
```yaml
summary: "MS Computer Science student at Northeastern (**3.89 GPA**) with **backend engineering** experience in Java, Python, and **Django**. Built **Spring-based microservices** and **RESTful APIs** at **London Stock Exchange Group** processing **7.5M+ records** and achieving **40% latency reduction**. [Continue...]"
```

**Guidelines:**
- 450-520 characters
- 5-8 bold markers (count as you add)
- Use 2-3 LSEG metrics that match JD focus
- Connect to company mission/product
- No "seeking internship" language

**Example for Adobe AI Developer:**
```
MS Computer Science student at Northeastern (**3.89 GPA**) with experience building **AI-powered automation systems** and **workflow orchestration** at **London Stock Exchange Group**. Developed **autonomous AI agent** using **Deep RL** and **full-stack applications** with **intelligent workflows**. Expertise in **Python, AI agents, orchestration**. Excited to build agentic workflows at Adobe.
```

### Step 3: Generate Work Experience Bullets

**Read:** WORK_EXPERIENCE_DATABASE.md

**For LSEG (generate 5 bullets):**

1. **Identify relevant work:**
   - What LSEG work matches JD focus?
   - Which metrics support the narrative?
   - Which technologies overlap?

2. **Generate bullet 1 (most impressive):**
   - Lead with biggest achievement matching JD
   - Use strongest metric
   - Include key JD technologies
   - 150-250 characters
   - 3-5 bold markers

3. **Generate bullets 2-4 (supporting):**
   - Different aspects of LSEG work
   - Vary the technologies mentioned
   - Use different metrics
   - Tell complete story

4. **Generate bullet 5 (depth or collaboration):**
   - Additional technical detail OR
   - Team collaboration/cross-functional work
   - Avoid mentorship unless senior role

**For Infosys (generate 4 bullets):**

1. **Complement LSEG story:**
   - Don't repeat same achievements
   - Fill gaps in JD coverage
   - Show breadth

2. **Generate 4 bullets:**
   - Each focusing on different aspect
   - Use different metrics than LSEG
   - Match JD keywords
   - 150-250 characters each
   - 3-5 bold markers each

**Critical Rules:**
- ✅ All bullets must be factually accurate (based on database)
- ✅ Use real metrics only (no fabrication)
- ✅ Technologies must match what was actually used
- ✅ Vary phrasing and focus between bullets
- ✅ No duplication between LSEG and Infosys

### Step 4: Select Skills (7 categories)

**Read:** CHANDAN_PROFILE_MASTER.md keyword banks

**Process:**
1. Extract top 50 keywords from JD
2. Match to Chandan's actual skills
3. Create 7 categories ordered by JD priority
4. Each category max 90 chars (add only relevant skills)
5. Include both acronyms and full terms

**Example categories based on role type:**

**Backend/Cloud Role:**
1. Programming Language
2. Backend Development
3. Cloud & Infrastructure
4. Databases
5. Development & DevOps
6. AI & Machine Learning (if mentioned)
7. Software Engineering

**ML/AI Role:**
1. Programming Language
2. AI & Machine Learning
3. Software Engineering
4. Cloud & Infrastructure
5. Backend Development
6. Databases
7. Development & DevOps

### Step 5: Select Projects (3 projects)

**Read:** CHANDAN_PROFILE_MASTER.md project portfolio

**Process:**
1. Match JD tech stack to projects
2. Select top 3 most relevant
3. Order by relevance (most relevant first)
4. Generate custom bullets for each project

**Common Project Combinations:**

**Backend/Distributed Systems:**
- Orion Platform (Go + Kubernetes)
- Port Management (Django + SQL)
- Calendly (Java + Design Patterns)

**ML/AI Engineering:**
- Dino Game Deep RL Agent (PyTorch + GPU)
- Face Recognition (TensorFlow + CV)
- PUBG Data Analysis (Data science)

**Full-Stack:**
- Kambaz LMS (Next.js + Node.js)
- Port Management (Django full-stack)
- Online Exam (Flask + MongoDB)

**Cloud/DevOps:**
- Orion Platform (Kubernetes operator)
- LSEG work in experience section
- Port Management (deployment)

**Data Engineering:**
- PUBG Analysis (4.4M records)
- Port Management (SQL optimization)
- LSEG work in experience section

### Step 6: Generate Project Bullets

**For each project:**
1. Read project details from CHANDAN_PROFILE_MASTER.md
2. Identify aspects matching JD
3. Write 2 bullets emphasizing those aspects
4. Use real metrics from database
5. Max 200 characters per bullet
6. 3-5 bold markers per bullet

**Example - Orion Platform for Cloud/DevOps role:**
```yaml
bullet1: "Architected **cloud-native Platform-as-a-Service** with **custom Kubernetes Operator in Go** enabling **single-command deployment** and **automated resource provisioning**."
bullet2: "Implemented **event-driven reconciliation loops** with **health monitoring** and **scaling policies**, demonstrating production-grade **k8s** and **infrastructure-as-code** expertise."
```

**Example - Orion Platform for Backend role:**
```yaml
bullet1: "Built **backend platform** in **Go** with **Kubernetes** enabling automated application deployment across multiple environments with **API-driven** configuration."
bullet2: "Designed **distributed system architecture** with **service orchestration** and **lifecycle management**, showcasing **backend engineering** and **cloud infrastructure** skills."
```

---

## 📋 QUALITY CHECKLIST

### Before Submitting YAML:

**Summary:**
- [ ] 520-570 characters
- [ ] Narrative flow (no "seeking internship")
- [ ] 5-8 bold markers
- [ ] Mentions LSEG
- [ ] Includes 3.89 GPA
- [ ] Company-specific ending
- [ ] Matches 5+ JD keywords

**Skills:**
- [ ] Exactly 7 categories
- [ ] Ordered by JD priority
- [ ] Each max 90 characters (no minimum - add only relevant skills)
- [ ] All critical JD keywords included
- [ ] No duplicates across categories

**Experience:**
- [ ] LSEG: Exactly 5 bullets
- [ ] Infosys: Exactly 4 bullets
- [ ] All bullets 150-250 characters
- [ ] 3-5 bold markers per bullet
- [ ] Uses real metrics from database
- [ ] Factually accurate
- [ ] Matches JD keywords
- [ ] No duplication between companies
- [ ] Story flows logically

**Projects:**
- [ ] Exactly 3 projects
- [ ] Titles match GitHub dictionary exactly
- [ ] Ordered by JD relevance
- [ ] Each bullet max 250 characters
- [ ] 3-5 bold markers per bullet
- [ ] Uses real metrics from database
- [ ] Emphasizes JD-relevant aspects

---

## 🚫 COMMON MISTAKES

### Work Experience Generation:

❌ **Copying database bullets word-for-word**
- Database is reference material, not templates
- Generate fresh bullets for each JD

❌ **Fabricating metrics or technologies**
- Only use metrics from database
- Only claim technologies actually used

❌ **Repeating same story in LSEG and Infosys**
- Each company should show different aspects
- Complement, don't duplicate

❌ **Ignoring JD keywords**
- Bullets should naturally include JD terms
- Mirror JD language where appropriate

❌ **Generic bullets that could apply to any role**
- Tailor specifically to this JD
- Emphasize what matters for THIS role

✅ **Best Practice:**
- Read JD thoroughly
- Understand what work is most relevant
- Generate bullets that tell the right story
- Use real metrics to support narrative
- Make it feel natural, not keyword-stuffed

---

## 📖 EXAMPLE: Complete YAML for Adobe Firefly SWE

**JD Focus:** Python, Go, backend services, k8s, GPU ML inference, web apps

```yaml
header:
  name: "Chandan Gowda K S"
  title: "Software Engineer | MS CS @ Northeastern | Python, Go, Kubernetes, Backend"
  contact: "+1 (857) 421-7469; chandan.keelara@gmail.com; LinkedIn; Portfolio; GitHub;"

summary: "MS Computer Science student at Northeastern (**3.89 GPA**) with production backend experience at **London Stock Exchange Group** building **Python and Java microservices** processing **7.5M+ records** with **40% latency reduction**. Developed **Kubernetes Operator in Go** and **Django backend** systems with SQL optimization. Expertise in **Python, Go, containerization, Kubernetes**, cloud infrastructure, and GPU-based ML. Excited to build scalable infrastructure for Adobe Firefly's generative AI platform."

skills:
  - category: "Programming Language"
    items: "Python, Go, Java, JavaScript, TypeScript, C++, SQL"
  
  - category: "Backend Development"
    items: "Microservices, REST APIs, Distributed Systems, Big Data, Service Architecture"
  
  - category: "Cloud & Infrastructure"
    items: "Kubernetes, Docker, AWS, Containerization, Cloud Platforms, Deployment"
  
  - category: "AI & Machine Learning"
    items: "PyTorch, TensorFlow, GPU Training, ML Inference, Deep Learning, Neural Networks"
  
  - category: "Databases"
    items: "MySQL, PostgreSQL, MongoDB, NoSQL, SQL Optimization, Database Design"
  
  - category: "Development & DevOps"
    items: "Git, CI/CD, Testing, Code Review, Agile, SDLC, Linux/Unix"
  
  - category: "Software Engineering"
    items: "System Design, Performance Optimization, Scalability, OOP, Algorithms"

experience:
  - company: "London Stock Exchange Group (LSEG)"
    role: "Senior Software Engineer"
    location: "Bengaluru"
    duration: "08-2022 to 12-2024"
    bullets:
      - "Engineered **event-driven pipeline** serving **180+ countries**, transforming **7.5M+ XML records** into JSON at **40 records/second** with **Python** and **AWS**, ensuring **99.9% data integrity**."
      - "Architected **microservices** in **Java Micronaut** on **AWS Lambda** with **API Gateway**, providing low-latency **REST APIs** for compliance data workflows."
      - "Optimized **Lambda-based APIs** through **batch processing** tuning and **CloudWatch** monitoring, reducing **latency by 40%** and supporting high-throughput workloads."
      - "Implemented **AWS security** with **WAF**, **IAM secret rotation**, and **TLS**, reducing security incidents by **50%** for **cloud-based** systems."
      - "Collaborated with **7 cross-functional teams** to deliver **zero-downtime** migrations and **production deployments** across global infrastructure."
  
  - company: "Infosys"
    role: "Senior Systems Engineer"
    location: "Bengaluru"
    duration: "10-2020 to 07-2022"
    bullets:
      - "Engineered **Python data processing pipelines** with **concurrent execution**, achieving **3x throughput improvement** through parallel task execution."
      - "Designed **microservices integration** patterns and **API orchestration**, reducing manual **interventions by 50%** through automation."
      - "Optimized **database queries** and **ETL pipelines** through indexing, reducing processing **latency by 35%** for enterprise workloads."
      - "Developed **monitoring and error-handling frameworks** with **automated retry mechanisms**, improving data accuracy by **20%**."

projects:
  - title: "Orion Platform"
    tech: "Go, Kubernetes, Operator SDK, Docker, Cloud-Native"
    github: "GitHub"
    bullet1: "Architected **cloud-native PaaS** with **custom Kubernetes Operator in Go**, enabling **single-command deployment** across environments with **automated provisioning**."
    bullet2: "Implemented **event-driven reconciliation**, **scaling policies**, and **health monitoring**, demonstrating **production-grade distributed systems** and **k8s** expertise."
  
  - title: "Dino Game Deep RL Agent"
    tech: "Python, PyTorch, Deep Learning, GPU Training"
    github: "GitHub"
    bullet1: "Developed autonomous agent with **PyTorch** and **ResNet (1.5M parameters)** using **GPU-based training**, achieving **real-time inference at 16.67 FPS**."
    bullet2: "Engineered **automated training pipeline** with **experience replay** and monitoring, showcasing **scalable ML systems** and **GPU-accelerated workflows**."
  
  - title: "Port Management System"
    tech: "Django, Python, MySQL, Advanced SQL, REST APIs"
    github: "GitHub"
    bullet1: "Developed **Django backend** implementing **Dijkstra's algorithm in SQL**, showcasing advanced **database optimization** and **Python** development."
    bullet2: "Built **RESTful API layer** with **complex database schema (15+ tables)** and **50+ stored procedures** for **scalable backend architecture**."
```

---

## 💡 KEY PRINCIPLES

### 1. Be Factually Accurate
- Use only real metrics from database
- Claim only technologies actually used
- Don't exaggerate achievements

### 2. Be JD-Specific
- Every bullet should feel tailored to THIS role
- Mirror JD language naturally
- Emphasize what matters for THIS company

### 3. Be Strategic
- Lead with strengths matching JD
- Use bold markers on JD keywords
- Tell coherent story across all sections

### 4. Be Concise (See constraints.yaml for exact limits)
- Work experience bullets: 150-250 chars
- Project bullets: max 250 chars
- Summary: 450-520 chars
- Skills: max 90 chars per category (no minimum - add only relevant)

---

## 🎯 ROLE-SPECIFIC GENERATION STRATEGIES

### For Backend/Distributed Systems Roles:

**Summary Focus:** Microservices, scale, distributed systems
**LSEG Bullets:** Event-driven pipeline, Java microservices, AWS, performance, collaboration
**Infosys Bullets:** Python pipelines, microservices integration, ETL, monitoring
**Projects:** Orion Platform, Port Management, Calendly
**Skills Priority:** Programming > Backend > Cloud > Databases > DevOps > ML > Software Engineering

---

### For ML/AI Roles:

**Summary Focus:** AI/ML experience, neural networks, model training
**LSEG Bullets:** Data processing scale, automation/orchestration, Python, performance
**Infosys Bullets:** Python pipelines, data transformation, monitoring
**Projects:** Dino RL, Face Recognition, PUBG Analysis
**Skills Priority:** Programming > AI/ML > Software Engineering > Cloud > Backend > Databases > DevOps

---

### For Cloud/DevOps Roles:

**Summary Focus:** AWS, Kubernetes, containerization, infrastructure
**LSEG Bullets:** AWS Lambda/SQS, microservices, performance, security, zero-downtime
**Infosys Bullets:** Pipeline optimization, monitoring, automation
**Projects:** Orion Platform, LSEG work emphasized, Port Management
**Skills Priority:** Programming > Cloud/Infra > Backend > DevOps > Databases > Software Engineering > ML

---

### For Full-Stack Roles:

**Summary Focus:** Full-stack capabilities, frontend + backend
**LSEG Bullets:** Microservices, APIs, workflows, collaboration
**Infosys Bullets:** API orchestration, integration, workflows
**Projects:** Kambaz LMS, Port Management, Orion Platform
**Skills Priority:** Programming > Backend > Frontend > Databases > Cloud > DevOps > Software Engineering

---

### For Automation/Workflow/AI Agent Roles:

**Summary Focus:** Automation, workflows, intelligent systems, AI
**LSEG Bullets:** Workflow orchestration, intelligent routing, automation, event-driven
**Infosys Bullets:** Python automation, API orchestration, automated workflows
**Projects:** Dino RL (agent), Port Management (workflow), Kambaz (workflow)
**Skills Priority:** Programming > AI/Agents > Backend > ML > Cloud > Databases > Software Engineering

---

### For Data Engineering Roles:

**Summary Focus:** Data pipelines, ETL, large-scale processing
**LSEG Bullets:** 7.5M records processing, data transformation, pipeline architecture
**Infosys Bullets:** Python pipelines, ETL optimization, data transformation, accuracy
**Projects:** PUBG Analysis (4.4M records), Port Management (SQL), Online Exam (MongoDB)
**Skills Priority:** Programming > Backend > Databases > Cloud > Data Tools > DevOps > Software Engineering

---

## 📝 FINAL NOTES

**Before generating each YAML:**
1. Read the JD carefully (5 minutes)
2. Read both user profile databases (2 minutes)
3. Plan the narrative (what story to tell)
4. Generate all sections fresh
5. Verify factual accuracy
6. Check character limits
7. Ensure keyword optimization

**Remember:**
- Databases are REFERENCE, not SELECTION MENUS
- Generate content DYNAMICALLY for each JD
- Stay FACTUALLY ACCURATE always
- Make it feel NATURAL, not keyword-stuffed

---

**END OF LLM GUIDE v3**
