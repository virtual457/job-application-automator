# Job Application Automator

**End-to-end automation pipeline for Spring/Summer 2026 co-op applications**

## 🎯 Goal
Automate the complete job application workflow: resume tailoring, cover letter generation, application tracking, and follow-up management.

## 📦 Modules

### 1. Resume Generator (Current Focus)
- Programmatically generate tailored resumes for each company
- Support multiple role types (Backend, ML/AI, Data Engineering)
- Template-based customization (header, summary, skills, projects)

### 2. Application Tracker (Coming Soon)
- Track all applications in one place
- Log referral requests and responses
- Generate follow-up reminders

### 3. Referral Automator (Coming Soon)
- LinkedIn connection request templates
- Automated referral request tracking
- Response rate analytics

### 4. Cover Letter Generator (Coming Soon)
- Company-specific cover letter generation
- Job description analysis and keyword matching

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Generate a tailored resume
python src/main.py generate-resume --company "Salesforce" --role "backend"

# Track an application
python src/main.py track-application --company "Salesforce" --status "applied"
```

## 📁 Project Structure

```
job-application-automator/
├── src/                    # Source code
│   ├── resume_generator.py # Resume generation logic
│   ├── application_tracker.py
│   └── main.py            # CLI entry point
├── config/                # Configuration files
│   ├── resume_config.yaml # Resume templates and variations
│   └── companies.yaml     # Target companies and roles
├── templates/             # Resume/cover letter templates
│   └── base_resume.docx   # Base resume template
├── output/                # Generated files
│   └── resumes/           # Generated resumes
├── tests/                 # Unit tests
├── docs/                  # Documentation
└── README.md
```

## 🎓 Target: 75+ Applications by November 30, 2025

**Progress:**
- [ ] Week 1: 15 applications (Nov 16-17)
- [ ] Week 2: 30 applications (Nov 18-24)
- [ ] Week 3: 30 applications (Nov 25-30)

**Key Metrics:**
- Applications submitted: 0/75
- Referrals secured: 0/10
- Callbacks received: 0
- Interviews scheduled: 0

## 👨‍💻 Author
Chandan Gowda K S  
MS CS @ Northeastern University  
Available: January - August 2026

