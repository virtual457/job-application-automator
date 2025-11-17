# LLM Guide: Creating Resume YAML Content for Chandan Gowda K S

## Overview
This guide is for an LLM assistant tasked with analyzing job descriptions and creating optimized YAML content for Chandan's resume generation system. The system automatically generates tailored Word resumes from a YAML configuration file.

---

## 📋 YAML File Structure & Restrictions

### **File Location:**
`config/current_application.yaml`

### **Complete YAML Schema:**

```yaml
header:
  name: "Chandan Gowda K S"
  title: "[CUSTOMIZED TITLE - MAX 100 CHARACTERS]"
  contact: "+1 (857) 421-7469; chandan.keelara@gmail.com; LinkedIn; Portfolio; GitHub;"

summary: "[CUSTOMIZED SUMMARY - MAX 590 CHARACTERS]"

skills:
  - category: "[CATEGORY NAME - MAX 35 CHARS]"
    items: "[SKILLS LIST - MAX 100 CHARS AFTER TAB]"
  
  # Repeat for exactly 7 skill categories
  # Order matters - put most relevant first

projects:
  - title: "[PROJECT NAME - MUST MATCH GITHUB URL DICTIONARY]"
    tech: "[TECHNOLOGIES - MAX 80 CHARS]"
    github: "GitHub"
    bullet1: "[ACHIEVEMENT - MAX 200 CHARS, 2 LINES]"
    bullet2: "[ACHIEVEMENT - MAX 200 CHARS, 2 LINES]"
  
  # Exactly 3 projects
  # Order matters - put most relevant first
```

---

## 🎯 Detailed Section Requirements

### **1. HEADER SECTION**

#### **`header.name`**
- **Value:** ALWAYS `"Chandan Gowda K S"`
- **Never change this**

#### **`header.title`**
- **Purpose:** One-line resume headline matching job requirements
- **Max Length:** 100 characters
- **Format:** `"Role | School | Key Skills"`
- **Examples:**
  ```
  "Software Engineer | MS CS @ Northeastern | Python, Java, Distributed Systems, Cloud"
  "ML/AI Engineer | MS CS @ Northeastern | Python, TensorFlow, Deep Learning"
  "Backend Engineer | MS CS @ Northeastern | C++, Java, Python | Algorithms & Systems"
  ```
- **Strategy:** Match job title + include 3-5 most important technologies from JD

#### **`header.contact`**
- **Value:** ALWAYS `"+1 (857) 421-7469; chandan.keelara@gmail.com; LinkedIn; Portfolio; GitHub;"`
- **Never change this** (hyperlinks are auto-added by script)

---

### **2. SUMMARY SECTION**

#### **Critical Constraints:**
- **Max Length:** 580 characters (reduced to accommodate bold formatting width)
- **Target Length:** 520-570 characters (leaves buffer)
- **Bold Markers:** Use `**text**` to bold important terms (see Bold Formatting Guide below)

#### **Required Elements (MUST include ALL):**
1. ✅ "Software Engineer and MS CS student" (MUST start with this exact phrase)
2. ✅ "seeking Spring/Summer 2026 co-op at **[COMPANY NAME]**"
3. ✅ "(January-August 2026, 8-month availability)"
4. ✅ Reference to LSEG experience with key metric
5. ✅ "Pursuing MS CS at Northeastern (**3.89 GPA**)"
6. ✅ Mention of specific technologies matching JD
7. ✅ "before completing final year of coursework"

#### **Template Structure:**
```
Software Engineer and MS CS student seeking Spring/Summer 2026 co-op at **[COMPANY]** (January-August 2026, 8-month availability). [UNIQUE VALUE PROPOSITION - 2-3 sentences highlighting experience/skills matching JD]. [LSEG ACHIEVEMENT with metrics]. Pursuing MS CS at Northeastern (**3.89 GPA**) to deepen expertise in [RELEVANT AREAS from JD] before completing final year of coursework.
```

#### **Bold Marker Strategy:**
- Bold: Company name, key technologies, metrics, GPA
- Typical: 5-8 bolded phrases per summary
- Example: `**LSEG**`, `**7.5M+ records**`, `**AWS Lambda**`, `**3.89 GPA**`

---

### **3. TECHNICAL SKILLS SECTION**

#### **Critical Constraints:**
- **Exactly 7 categories** (no more, no less)
- **Category name:** Max 35 characters
- **Items list:** Max ~100 characters after alignment
- **Order:** Most relevant to JD first
- **Formatting:** Categories auto-bold, items regular (script handles this)

#### **Standard Categories (Choose 7 based on JD):**

**Available Categories:**
1. `Programming Language` - Languages used
2. `Backend Engineering` - Backend/systems skills
3. `Cloud & Infrastructure` - Cloud/DevOps skills
4. `AI/ML` - Machine learning technologies
5. `Algorithms & Data Structures` - CS fundamentals
6. `Software Engineering` - Engineering practices
7. `Development & DevOps` - Tools and workflows
8. `Databases` or `Databases & Data` - Database technologies
9. `Fintech & Systems` - Financial systems (use for finance roles)
10. `Data Processing` - For data engineering roles
11. `Web Development` - For full-stack roles

#### **Skill Selection Strategy:**

**For Backend/Distributed Systems Roles:**
```yaml
skills:
  - category: "Programming Language"
    items: "Python, Java, Go, C++, JavaScript, TypeScript"
  
  - category: "Backend Engineering"
    items: "Distributed Systems, Microservices, REST APIs, Event-Driven Architectures"
  
  - category: "Cloud & Infrastructure"
    items: "AWS (Lambda, SQS, API Gateway), Docker, Kubernetes, Terraform"
  
  - category: "Databases"
    items: "PostgreSQL, MySQL, MongoDB, SQL Query Optimization"
  
  - category: "Development & DevOps"
    items: "Git, CI/CD Pipelines, Linux/Unix, Agile/Scrum"
  
  - category: "AI/ML"
    items: "TensorFlow, PyTorch, Deep Reinforcement Learning"
  
  - category: "Software Engineering"
    items: "System Design, Microservices, Performance Optimization"
```

**For ML/AI Roles:**
```yaml
skills:
  - category: "Programming Language"
    items: "Python, Java, C++, JavaScript"
  
  - category: "AI/ML"
    items: "TensorFlow, PyTorch, Deep Reinforcement Learning, Computer Vision"
  
  - category: "Software Engineering"
    items: "Distributed Systems, Microservices, Production Engineering"
  
  - category: "Cloud & Infrastructure"
    items: "AWS (Lambda, SQS), Docker, Kubernetes"
  
  - category: "Development & DevOps"
    items: "Git, CI/CD, Linux/Unix"
  
  - category: "Databases & Data"
    items: "MySQL, PostgreSQL, Pandas, NumPy, Statistical Analysis"
  
  - category: "Algorithms & Data Structures"
    items: "Design Patterns, Graph Algorithms, Neural Network Optimization"
```

**For Algorithms/Systems Roles (like IBM EDA):**
```yaml
skills:
  - category: "Programming Language"
    items: "C++, Java, Python, Go, C"
  
  - category: "Algorithms & Data Structures"
    items: "Design Patterns, Graph Algorithms, Dynamic Programming"
  
  - category: "AI/ML"
    items: "TensorFlow, PyTorch, Deep Reinforcement Learning, Computer Vision"
  
  - category: "Software Engineering"
    items: "Test-Driven Development, System Design, Microservices"
  
  - category: "Development & DevOps"
    items: "Git, Linux/Unix, CI/CD Pipelines, Agile/Scrum"
  
  - category: "Cloud & Infrastructure"
    items: "AWS (Lambda, SQS, API Gateway), Docker, Kubernetes"
  
  - category: "Databases & Data"
    items: "MySQL, PostgreSQL, MongoDB, SQL Query Optimization"
```

#### **Key Rules:**
- ✅ Always put programming languages first
- ✅ Order remaining categories by JD priority
- ✅ Include technologies mentioned in JD
- ✅ Keep items concise - use commas to separate
- ✅ Avoid duplicates across categories

---

### **4. PROJECTS SECTION**

#### **Critical Constraints:**
- **Exactly 3 projects** (no more, no less)
- **Project title:** Must match GitHub URL dictionary (see list below)
- **Tech stack:** Max 80 characters, bold-italic formatted
- **Each bullet:** Max 200 characters, fits in ~2 lines
- **Bold markers:** Use `**text**` for key achievements

#### **Available Projects & GitHub URLs:**

The script has these project URLs pre-configured. **Use exact title names:**

| Project Title | GitHub URL | Best For |
|---------------|------------|----------|
| `Dino Game Deep RL Agent` | dino-game-AI | ML/AI roles |
| `Orion PaaS` or `Orion Platform` | Orion-platform | Backend, DevOps, Platform Eng |
| `Calendly - Calendar Management System` or `Calendly` | Calendly | Backend, Java, Enterprise |
| `Maritime Logistics Platform` | Port-Management-System | Backend, Algorithms, Databases |
| `Port Management System` | Port-Management-System | Backend, Algorithms, Databases |
| `Large Scale Data Analysis` | Data-analysis-on-pubg | Data Engineering, Analytics |
| `Data Analysis on PUBG` | Data-analysis-on-pubg | Data Engineering, Analytics |
| `Face Recognition & Validation System` | Recognition-and-Validation... | ML/CV roles |
| `Online Examination System` | Online-examination-using-mongodb | Backend, Python, NoSQL |

#### **Project Selection Strategy:**

**For Backend/Distributed Systems Roles:**
1. Orion PaaS (Go + Kubernetes)
2. Maritime Logistics Platform (Django + SQL algorithms)
3. Calendly (Java + Design Patterns)

**For ML/AI Roles:**
1. Dino Game Deep RL Agent (Deep RL, 1.5M params)
2. Large Scale Data Analysis (4.4M records)
3. Face Recognition & Validation System (CV + CNN)

**For Data Engineering Roles:**
1. Maritime Logistics Platform (SQL optimization)
2. Large Scale Data Analysis (4.4M records)
3. Online Examination System (MongoDB)

**For Algorithms-Heavy Roles (like IBM EDA):**
1. Calendly (6+ design patterns, algorithms)
2. Dino Game Deep RL Agent (AI/ML algorithms)
3. Orion PaaS (Systems programming)

#### **Project Bullet Guidelines:**

**Structure:** [Action Verb] + [What you built] + [Technologies] + [Quantified Impact]

**Bold Strategy:**
- Bold key technologies: `**AWS Lambda**`, `**Kubernetes Operator**`, `**Deep RL**`
- Bold quantified metrics: `**1.5M parameters**`, `**6+ design patterns**`, `**98% coverage**`
- Bold important concepts: `**production-grade**`, `**real-time**`, `**cloud-native**`
- 3-5 bold phrases per bullet

**Examples:**

```yaml
# Backend/Cloud Project
bullet1: "Architected a **cloud-native Platform-as-a-Service** with a custom **Kubernetes Operator** enabling **single-command application deployment** across multiple environments."

# ML Project  
bullet1: "Developed autonomous AI agent using **Double DQN** with **ResNet architecture (1.5M parameters)** achieving **real-time decision-making at 16.67 FPS**."

# Enterprise Java Project
bullet1: "Implemented **6+ design patterns** (Command, Factory, Adapter, Builder, Observer, Strategy) with **strict SOLID adherence** across **52 source files**."
```

---

## 📊 Source Data: Where to Find Information About Chandan

### **Primary Source: GitHub Analysis Document**

**Location:** Project files contain `Github Analysis.txt`

**What it contains:**
- Complete repository analysis for all projects
- Technical stack details
- Architecture information
- Key highlights for each project
- Best-fit role recommendations
- Project metrics and scale

**Projects covered:**
1. Orion-platform (Kubernetes operator)
2. stuffycare (Healthcare .NET MVC)
3. virtual457.github.io (Portfolio)
4. World (Data visualization)
5. webscrapping (Python ETL)
6. Cryptographic Algorithms (Python + Tkinter)
7. chandan (Python projects collection)
8. bingo (Web game)
9. Stocks-Simulator (Financial analysis)
10. Quiz-App-.netMVC (ASP.NET)
11. Pixel-Perfect (Image processing)
12. NS3 Network Simulation (C++)
13. face_detector (OpenCV)
14. EmployeeAdmin (HR system)
15. Drive-through (C++ + Qt)
16. simple-neural-network (MNIST)
17. Recognition-and-Validation-of-Faces (ML + CV)
18. Port-Management-System (Maritime + Dijkstra)
19. Online-examination-using-mongodb (Flask + MongoDB)
20. Data-analysis-on-pubg (4.4M+ records)
21. Calendly (Enterprise Java)

### **Work Experience Data:**

#### **London Stock Exchange Group (LSEG) - August 2022 to December 2024**
**Title:** Senior Software Engineer (use "Software Engineer" in resume to avoid overqualification)

**Key Achievements (USE THESE EXACT METRICS):**
- Engineered event-driven pipeline serving **180+ countries**
- Transformed **7.5M+ XML compliance records** into JSON
- Processing speed: **40 records/second**
- Data integrity: **99.9%**
- Multi-queue priority routing in **Python with AWS SQS and Lambda**
- Improved turnaround time by **35%** for high-priority cases
- Developed microservices in **Java Micronaut** on **AWS Lambda with API Gateway**
- Reduced latency by **40%** through optimization
- Integrated **AWS WAF, IAM secret rotation, TLS**
- Reduced security incidents by **50%**
- Mentored **5 junior engineers**
- Collaborated with **7 cross-functional teams**
- Zero-downtime migrations

**Technologies:** Python, Java (Micronaut), AWS (Lambda, SQS, API Gateway, WAF, IAM, CloudWatch), Event-Driven Architecture, Microservices, KYC/AML systems

#### **Infosys - October 2020 to July 2022**
**Title:** Senior Systems Engineer (use "Software Engineer" in resume)

**Key Achievements:**
- Python data processing pipelines with concurrent execution
- **3x throughput improvement**
- Reduced manual interventions by **50%**
- Database query optimization reducing latency by **35%**
- Improved data extraction accuracy by **20%**

**Technologies:** Python, Microservices, API orchestration, ETL pipelines, Database optimization

### **Education:**
- **MS in Computer Science**, Northeastern University, Boston, MA
  - CGPA: **3.89/4.0**
  - Duration: January 2025 to May 2027
  - Status: Current student (1st year)
  
- **BE in Computer Science**, Nitte Meenakshi Institute of Technology (NMIT), Bengaluru
  - CGPA: 8.76/10
  - Duration: August 2016 to August 2020

### **Certifications:**
- AWS Certified Cloud Practitioner
- Published IEEE Paper: "Doctor-Patient Assistance System using Artificial Intelligence"

### **Availability:**
- **Spring/Summer 2026 Co-op**
- **Available:** January 2026 through August 2026
- **Duration:** 8 months (MAJOR ADVANTAGE - most students only available 4 months)
- **Flexible start date:** Can start anytime between January and May 2026
- **Visa Status:** F1 with CPT (no employer sponsorship needed)

---

## 🎨 Bold Formatting Guide

### **Syntax:**
Use `**text**` to mark text for bold formatting (like Markdown)

### **Where to Apply Bold:**

#### **In Summary (5-8 bold markers):**
- ✅ Company name: `**IBM**`, `**Salesforce**`
- ✅ Key metrics: `**7.5M+ records**`, `**180+ countries**`, `**40% improvement**`
- ✅ Important technologies: `**AWS Lambda**`, `**Python**`, `**distributed systems**`
- ✅ GPA: `**3.89 GPA**`
- ✅ Years of experience: `**4+ years**`
- ✅ School: `**Northeastern**` or `**LSEG**`

#### **In Project Bullets (3-5 bold markers per bullet):**
- ✅ Key technologies: `**Kubernetes Operator**`, `**Deep RL**`, `**TensorFlow**`
- ✅ Quantified metrics: `**1.5M parameters**`, `**98% coverage**`, `**6+ design patterns**`
- ✅ Important concepts: `**production-grade**`, `**real-time**`, `**cloud-native**`
- ✅ Scale indicators: `**52 source files**`, `**40 records/second**`

#### **DON'T Over-Bold:**
- ❌ Common words: the, and, with, using, for
- ❌ More than 30% of text
- ❌ Entire sentences
- ❌ Generic verbs: built, developed, implemented (unless part of compound phrase)

### **Examples:**

**Good Summary:**
```yaml
summary: "Software Engineer and MS CS student seeking Spring/Summer 2026 co-op at **Salesforce** (January-August 2026, 8-month availability). Production experience building **distributed systems** processing **7.5M+ records** across **180+ countries** at **LSEG**. Expertise in **Python, Java, AWS serverless architecture**, and **event-driven systems**. Pursuing MS CS at Northeastern (**3.89 GPA**) to deepen expertise in distributed systems and cloud-native architectures before completing final year of coursework."
```

**Good Project Bullet:**
```yaml
bullet1: "Engineered **event-driven pipeline** serving **180+ countries** that transformed **7.5M+ XML compliance records** into standardized JSON at **40 records/second**, ensuring **99.9% data integrity**."
```

---

## 📚 Project Details Reference

Use this information when creating project bullets. Choose 3 most relevant projects for each JD.

### **Project 1: Dino Game Deep RL Agent**

**GitHub:** https://github.com/virtual457/dino-game-AI

**Tech Stack:** Python, PyTorch, Deep Reinforcement Learning, Computer Vision, ResNet, Neural Networks

**Key Metrics:**
- **1.5M parameters** in ResNet-based DDQN architecture
- **Real-time decision-making at 16.67 FPS**
- **7.6 training steps/second** performance
- **4-frame stacking** for temporal information
- Balanced experience replay with 50/50 sampling
- Automated training loops

**When to Use:**
- ML/AI engineering roles
- Computer vision positions
- Deep learning positions
- Algorithm-heavy roles

**Sample Bullets:**
```yaml
bullet1: "Developed autonomous AI agent using **Double DQN with ResNet architecture (1.5M parameters)** achieving **real-time decision-making at 16.67 FPS** through deep reinforcement learning."

bullet2: "Engineered **automated training pipeline** with balanced experience replay, **4-frame stacking** for temporal information, and performance optimization achieving **7.6 training steps/second**."
```

---

### **Project 2: Orion Platform / Orion PaaS**

**GitHub:** https://github.com/virtual457/Orion-platform

**Tech Stack:** Go, Kubernetes, Operator SDK, Docker, Custom Resource Definitions (CRDs), controller-runtime

**Key Features:**
- Custom Kubernetes operator in Go
- Single-command application deployment
- Environment-aware provisioning (local vs cloud)
- Automated PostgreSQL, Redis, MinIO setup
- Health monitoring and lifecycle management
- Production-grade infrastructure-as-code

**Key Metrics:**
- **1.5K+ lines of Go code**
- Custom CRDs and controllers
- Event-driven reconciliation loop
- Sub-second cluster state sync
- Supports 10+ concurrent deployments

**When to Use:**
- Backend/distributed systems roles
- DevOps/Platform engineering
- Cloud infrastructure positions
- Kubernetes-focused roles
- Systems programming

**Sample Bullets:**
```yaml
bullet1: "Architected **cloud-native Platform-as-a-Service** with custom **Kubernetes Operator in Go** enabling **single-command application deployment** across multiple environments."

bullet2: "Implemented **automated resource provisioning, scaling policies, and health monitoring** with **event-driven reconciliation loops**, demonstrating **production-grade distributed systems** design."
```

---

### **Project 3: Calendly - Calendar Management System**

**GitHub:** https://github.com/virtual457/Calendly

**Tech Stack:** Java 11, Maven, JUnit, Design Patterns, MVC Architecture, Test-Driven Development

**Key Metrics:**
- **6+ design patterns** (Command, Factory, Adapter, Builder, Observer, Strategy)
- **52 source files**
- **31 test classes**
- **98% line coverage**
- **95% mutation coverage** (PIT testing)
- **15+ command modules**
- Multi-interface: GUI, Console, Headless

**Key Features:**
- Enterprise-grade architecture
- SOLID principles adherence
- Comprehensive test-driven development
- Timezone support, CSV import/export
- Multi-calendar management

**When to Use:**
- Enterprise Java roles
- Software engineering positions emphasizing design patterns
- Roles requiring strong testing/TDD
- Traditional backend engineering
- Companies valuing software architecture (IBM, Salesforce)

**Sample Bullets:**
```yaml
bullet1: "Architected multi-interface calendar application implementing **6+ design patterns** (Command, Factory, Adapter, Builder, Observer, Strategy) with **strict SOLID adherence** across **52 source files**."

bullet2: "Developed **15+ command modules** with comprehensive **TDD methodology**, achieving **98% line coverage** and **95% mutation coverage**; shipped production-ready features including timezone support and multi-calendar management."
```

---

### **Project 4: Maritime Logistics Platform**

**GitHub:** https://github.com/virtual457/Port-Management-System

**Tech Stack:** Django, MySQL, Python, SQL Algorithms, JavaScript, Bootstrap, Stored Procedures

**Key Features:**
- **Dijkstra's pathfinding algorithm implemented in SQL**
- Complex stored procedures and triggers
- Multi-role authentication (Admin/Shipowner/Customer/Manager)
- **15+ interconnected database tables**
- RESTful API layer
- Spatial data with GPS coordinates
- CTEs (Common Table Expressions)

**Key Metrics:**
- Dijkstra algorithm in SQL (advanced)
- Complex relational database design
- Multi-tenant architecture
- 1000+ concurrent route calculations

**When to Use:**
- Backend engineering with database focus
- Roles emphasizing SQL optimization
- Algorithm-heavy positions
- Full-stack Python/Django roles
- Logistics/systems engineering

**Sample Bullets:**
```yaml
bullet1: "Developed full-stack port management system implementing **Dijkstra's pathfinding algorithm in SQL stored procedures** for optimal route calculation with **complex relational database schema (15+ tables)**."

bullet2: "Built **role-based authentication system** (Admin/Shipper/Customer/Manager), **RESTful API layer**, and **multi-tenant operations** supporting **1000+ concurrent route calculations**."
```

---

### **Project 5: Large Scale Data Analysis / Data Analysis on PUBG**

**GitHub:** https://github.com/virtual457/Data-analysis-on-pubg

**Tech Stack:** Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook, Statistical Analysis

**Key Metrics:**
- **4.4M+ match records** analyzed
- Statistical modeling across 29 gameplay features
- Multi-modal analysis (Solo/Duo/Squad)
- Correlation studies and win rate predictors
- Data visualization pipelines

**When to Use:**
- Data engineering roles
- Data analyst positions
- Business intelligence roles
- Roles emphasizing large-scale data processing

**Sample Bullets:**
```yaml
bullet1: "Analyzed **4.4M+ PUBG match records** across **29 gameplay features** using **Python (Pandas, NumPy)** to identify win rate predictors through statistical modeling and correlation analysis."

bullet2: "Developed **data preprocessing pipelines** and created comprehensive visualizations using **Matplotlib/Seaborn**, extracting actionable insights on player behavior patterns applicable to game analytics and engagement optimization."
```

---

### **Project 6: Face Recognition & Validation System**

**GitHub:** https://github.com/virtual457/Recognition-and-Validation-of-Faces-using-Machine-Learning-and-Image-Processing

**Tech Stack:** Python, TensorFlow/Keras, OpenCV, CNN, Computer Vision

**Key Metrics:**
- Custom 5-layer CNN architecture
- **88.2% validation accuracy**
- **500,000+ training steps**
- Real-time inference capabilities

**When to Use:**
- Computer vision roles
- ML engineering positions
- CV/image processing roles

**Sample Bullets:**
```yaml
bullet1: "Developed end-to-end face recognition system using **custom 5-layer CNN** achieving **88.2% validation accuracy** with complete **ML pipeline** (preprocessing, training, inference)."

bullet2: "Implemented CNN architecture with **progressive filter reduction** and **dropout regularization** trained over **500,000 steps**, demonstrating expertise in neural network design and computer vision."
```

---

## 🎯 JD Analysis Process

### **Step 1: Extract Key Requirements**

From the job description, identify:
1. **Primary technologies** (Python, Java, C++, AWS, Kubernetes, etc.)
2. **Required skills** (distributed systems, ML, algorithms, etc.)
3. **Preferred qualifications** (MS degree, GPA, specific experience)
4. **Domain focus** (fintech, ML infrastructure, systems programming, etc.)
5. **Keywords for ATS** (specific tools, frameworks, methodologies)

### **Step 2: Determine Role Type**

Categorize as one of:
- `backend` - General backend/distributed systems
- `ml` - ML/AI engineering
- `data` - Data engineering/analytics
- `algorithms` - Algorithm-heavy, systems programming
- `general` - Mix of everything

### **Step 3: Map to Chandan's Experience**

**Match strengths:**
- LSEG experience (7.5M records, 180 countries, AWS serverless)
- MS CS student at Northeastern (3.89 GPA)
- 4+ years production experience
- Multi-language: Python, Java, Go, C++
- Projects spanning backend, ML, infrastructure

**Address concerns:**
- Overqualification (hence "co-op" terminology)
- Why internship after senior role (MS degree requirement)
- F1 visa (CPT = no sponsorship needed)

### **Step 4: Create Optimized YAML**

#### **Title Optimization:**
- Include exact job title if possible
- Include school: "MS CS @ Northeastern"
- Include 3-5 key technologies from JD
- Max 100 characters

#### **Summary Optimization:**
- Start with required phrase: "Software Engineer and MS CS student"
- Mention company name (bolded)
- Include 8-month availability
- Reference 1-2 LSEG achievements with metrics
- Match 5-7 key technologies from JD
- Keep to 540-590 characters
- Apply 5-8 bold markers

#### **Skills Optimization:**
- Extract top 7 skill categories needed for role
- Order by JD priority
- Front-load with JD keywords
- Include both acronyms and full terms
- Each category max 35 chars, items max ~100 chars

#### **Projects Optimization:**
- Select 3 projects most relevant to JD
- Order by relevance (most relevant first)
- Write bullets emphasizing aspects matching JD
- Include quantified metrics
- Apply 3-5 bold markers per bullet
- Max 200 characters per bullet

---

## ✅ Quality Checklist

Before finalizing YAML content, verify:

### **Summary:**
- [ ] Starts with "Software Engineer and MS CS student"
- [ ] Mentions company name (bolded)
- [ ] Includes "January-August 2026, 8-month availability"
- [ ] References LSEG with specific metric
- [ ] Mentions "Northeastern (**3.89 GPA**)"
- [ ] Includes "before completing final year of coursework"
- [ ] 540-590 characters total
- [ ] 5-8 bold markers applied
- [ ] Matches 5+ keywords from JD

### **Skills:**
- [ ] Exactly 7 categories
- [ ] Categories ordered by JD priority
- [ ] Includes all critical technologies from JD
- [ ] Category names max 35 chars
- [ ] Items lists max ~100 chars
- [ ] No duplicate skills across categories

### **Projects:**
- [ ] Exactly 3 projects
- [ ] Project titles match GitHub URL dictionary exactly
- [ ] Ordered by relevance to JD
- [ ] Tech stacks max 80 chars
- [ ] Each bullet max 200 chars (~2 lines)
- [ ] Each bullet has 3-5 bold markers
- [ ] Bullets emphasize aspects matching JD requirements
- [ ] Include quantified metrics where possible

---

## 🚫 Common Mistakes to Avoid

### **Summary Mistakes:**
- ❌ Starting with anything other than "Software Engineer and MS CS student"
- ❌ Forgetting company name or 8-month availability
- ❌ Exceeding 590 characters
- ❌ Not mentioning LSEG experience
- ❌ Missing GPA mention
- ❌ Too few or too many bold markers

### **Skills Mistakes:**
- ❌ Having fewer or more than 7 categories
- ❌ Category names over 35 characters
- ❌ Skills items over ~100 characters
- ❌ Duplicating skills across categories
- ❌ Ignoring JD keywords

### **Projects Mistakes:**
- ❌ Using project titles not in GitHub URL dictionary
- ❌ Having fewer or more than 3 projects
- ❌ Bullets over 200 characters (won't fit in 2 lines)
- ❌ No bold markers or too many bold markers
- ❌ Missing quantified metrics
- ❌ Generic descriptions not tailored to JD

---

## 📋 Example: Complete YAML for Backend Role

```yaml
header:
  name: "Chandan Gowda K S"
  title: "Software Engineer | MS CS @ Northeastern | Python, Java, AWS, Distributed Systems"
  contact: "+1 (857) 421-7469; chandan.keelara@gmail.com; LinkedIn; Portfolio; GitHub;"

summary: "Software Engineer and MS CS student seeking Spring/Summer 2026 co-op at **Salesforce** (January-August 2026, 8-month availability). Production experience building **distributed systems** processing **7.5M+ records** across **180+ countries** at **LSEG** using **Python, Java, and AWS serverless architecture**. Proven expertise in **event-driven systems, microservices, and performance optimization** with **40% latency reduction** achievements. Pursuing MS CS at Northeastern (**3.89 GPA**) to deepen expertise in cloud-native architectures before completing final year of coursework."

skills:
  - category: "Programming Language"
    items: "Python, Java, Go, C++, JavaScript, TypeScript"
  
  - category: "Backend Engineering"
    items: "Distributed Systems, Microservices, REST APIs, Event-Driven Architectures"
  
  - category: "Cloud & Infrastructure"
    items: "AWS (Lambda, SQS, API Gateway), Docker, Kubernetes, Terraform"
  
  - category: "Databases"
    items: "PostgreSQL, MySQL, MongoDB, SQL Query Optimization"
  
  - category: "Development & DevOps"
    items: "Git, CI/CD Pipelines, Linux/Unix, Agile/Scrum"
  
  - category: "AI/ML"
    items: "TensorFlow, PyTorch, Deep Reinforcement Learning"
  
  - category: "Software Engineering"
    items: "System Design, Performance Optimization, Microservices Architecture"

projects:
  - title: "Orion Platform"
    tech: "Go, Kubernetes, Operator SDK, Docker"
    github: "GitHub"
    bullet1: "Architected **cloud-native Platform-as-a-Service** with custom **Kubernetes Operator in Go** enabling **single-command application deployment** across multiple environments."
    bullet2: "Implemented **automated resource provisioning, scaling policies, and health monitoring** with **event-driven reconciliation loops**, demonstrating **production-grade distributed systems** design."
  
  - title: "Maritime Logistics Platform"
    tech: "Django, MySQL, SQL Algorithms, Python"
    github: "GitHub"
    bullet1: "Developed full-stack port management system implementing **Dijkstra's pathfinding algorithm in SQL** for optimal route calculation with **complex database schema (15+ tables)**."
    bullet2: "Built **role-based authentication**, **RESTful API layer**, and **multi-tenant operations** supporting **1000+ concurrent route calculations** with advanced stored procedures."
  
  - title: "Calendly - Calendar Management System"
    tech: "Java 11, Maven, JUnit, Design Patterns"
    github: "GitHub"
    bullet1: "Architected multi-interface application implementing **6+ design patterns** (Command, Factory, Adapter, Builder, Observer, Strategy) with **strict SOLID adherence** across **52 source files**."
    bullet2: "Achieved **98% line coverage** and **95% mutation coverage** through **comprehensive TDD (31 test classes)**, shipping production-ready features with robust error handling."
```

---

## 🎯 Decision Tree for Project Selection

### **If JD mentions Kubernetes, Go, Infrastructure, DevOps:**
→ Lead with **Orion Platform**

### **If JD mentions ML, AI, Deep Learning, Computer Vision:**
→ Lead with **Dino Game Deep RL Agent**

### **If JD mentions Algorithms, Data Structures, Design Patterns, Java:**
→ Lead with **Calendly**

### **If JD mentions Databases, SQL, Backend, Django:**
→ Lead with **Maritime Logistics Platform**

### **If JD mentions Data Engineering, Analytics, Big Data:**
→ Lead with **Large Scale Data Analysis**

### **Always include:**
- At least 1 project matching primary tech stack
- At least 1 project showing LSEG-level sophistication
- Mix of languages if JD is multi-language

---

## 💼 Special Positioning Considerations

### **The Overqualification Problem:**
Chandan has 4+ years senior engineering experience but is applying for internships/co-ops. This triggers red flags.

**How to Address in YAML:**

1. **Use "Software Engineer"** not "Senior Software Engineer" in summary
2. **Emphasize learning**: "to deepen expertise", "while learning", "before completing final year"
3. **Frame as co-op requirement**: "participating in Northeastern's co-op program"
4. **Highlight 8-month availability** (shows serious commitment, not just summer)
5. **De-emphasize leadership**: Don't mention "mentored 5 engineers" in summary
6. **Focus on technical skills**: Not management/leadership

### **The F1 Visa Concern:**
Companies may worry about sponsorship.

**How to Address:**
- Don't mention F1 status in resume
- CPT requires zero sponsorship (handled in interviews)
- Northeastern's co-op program is CPT-integrated

### **The Late Timing Issue:**
Applying in November 2025 for Summer 2026 = late in cycle.

**How to Address:**
- Emphasize flexible January start (can fill Spring co-ops)
- 8-month commitment = more valuable than summer-only candidates
- Apply to 75+ positions to overcome late-cycle disadvantage

---

## 🔍 ATS Optimization Rules

### **Keyword Matching:**
- Include exact phrases from JD (not just synonyms)
- Use both acronyms and full terms: "ML" AND "Machine Learning"
- Repeat important keywords 2-3 times across resume
- Target 75%+ keyword match with JD

### **Formatting for ATS:**
- No tables, columns, or graphics (our system avoids these)
- Standard section headers: EDUCATION, TECHNICAL SKILLS, WORK EXPERIENCE, PROJECTS
- Use standard fonts (Calibri - our template handles this)
- Include both acronyms and full spellings

### **Content Optimization:**
- Lead with education (signals student status)
- Quantify everything possible
- Use action verbs: Engineered, Architected, Developed, Implemented
- Include metrics: %, numbers, scale indicators

---

## 📞 When to Reach Out for Clarification

### **Ask for More Info If:**
1. JD has ambiguous requirements (e.g., "full-stack" without specifying frontend/backend focus)
2. Unclear which technologies are must-have vs nice-to-have
3. Role could fit multiple categories (both ML and backend)
4. JD is very short/vague without specific requirements

### **Don't Ask - Just Decide:**
1. Which 3 projects to include (use decision tree above)
2. Skill category ordering (match JD priorities)
3. What to bold (use guidelines above)
4. Summary length (stay within 540-590 chars)

---

## 🎓 Success Metrics

**Your generated YAML should enable:**
- ✅ 75%+ ATS keyword match
- ✅ Clear student positioning (avoid overqualification flags)
- ✅ Proper emphasis on relevant experience
- ✅ Professional formatting when rendered
- ✅ Quantified achievements throughout
- ✅ Company-specific customization

**Red flags to avoid:**
- ❌ Generic content not tailored to JD
- ❌ Missing critical JD keywords
- ❌ Over-emphasizing senior experience
- ❌ Forgetting 8-month availability advantage
- ❌ Character limit violations

---

## 🚀 Final Output Format

Always provide YAML in this exact structure:

```yaml
header:
  name: "Chandan Gowda K S"
  title: "[CUSTOMIZED]"
  contact: "+1 (857) 421-7469; chandan.keelara@gmail.com; LinkedIn; Portfolio; GitHub;"

summary: "[CUSTOMIZED WITH **BOLD MARKERS**]"

skills:
  - category: "[CATEGORY 1]"
    items: "[ITEMS]"
  # ... exactly 7 categories total

projects:
  - title: "[PROJECT 1 - EXACT NAME FROM GITHUB URL DICT]"
    tech: "[TECH STACK]"
    github: "GitHub"
    bullet1: "[BULLET WITH **BOLD MARKERS**]"
    bullet2: "[BULLET WITH **BOLD MARKERS**]"
  # ... exactly 3 projects total
```

---

## 🎯 Remember

**Chandan's Goal:** Land Spring/Summer 2026 co-op (Jan-Aug availability)

**Target Companies:** FAANG (Google, Meta, Amazon, Microsoft, Apple), Stripe, Salesforce, Intuit, ByteDance, Adobe, Databricks, Snowflake, and 60+ others

**Success Criteria:** 
- Generate 75+ tailored resumes
- Secure 5-10 referrals
- Get 8-12 callbacks
- Convert to 1-2 offers

**Your Role:** Create ATS-optimized YAML content that positions Chandan as a strong co-op candidate (not overqualified senior engineer) while leveraging his production experience as an asset.

---

**End of Guide. Use this to generate high-quality, tailored YAML content for each job application.**
