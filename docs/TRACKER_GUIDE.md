# Application Tracker Guide

## 🎯 Track Every Application in One Place

The application tracker helps you manage your 75+ applications with dates, companies, roles, and key details.

---

## 📊 Current Applications

You have **6 applications ready** based on the YAMLs we created:

| Company | Role | Key Skills | Resume Type | Status |
|---------|------|------------|-------------|--------|
| IBM | Software Developer - EDA | C++, Java, Algorithms, AI/ML | algorithms | Ready |
| Skild AI | ML Intern - RL | Python, PyTorch, Reinforcement Learning | ml | Ready |
| Intuit | AI Science Intern | Python, ML, Data Analysis, Spark | ml | Ready |
| SeatGeek | Backend/Platform Intern | Python, Go, AWS, Kubernetes | backend | Ready |
| Dassault | AI Software Engineer | TypeScript, React, LLM/NLP | general | Ready |
| Cohere | Software Engineering Intern | Python, Go, ML Infrastructure | backend | Ready |

---

## 🚀 How to Use

### **View All Applications**

```bash
# Windows
tracker view

# Or directly
cd src
python view_tracker.py
```

**Output:**
```
APPLICATION TRACKER
====================================
📊 TOTAL APPLICATIONS: 6

📈 BY STATUS:
  • Ready to Apply: 6

📝 BY RESUME TYPE:
  • backend: 2
  • ml: 2
  • algorithms: 1
  • general: 1
```

---

### **Log a New Application**

After applying to a company:

```bash
# Windows
tracker log

# Or directly
cd src
python quick_log.py
```

**Interactive prompts:**
```
Company name: Salesforce
Role title: Software Engineering Intern
Key skills required: Python, Java, Distributed Systems, AWS
Location: San Francisco
Resume type: backend
Referral name: John Smith
Notes: Applied through career page
```

---

### **Export to Excel**

```bash
# Windows  
tracker excel

# Or directly
cd src
python view_tracker.py excel
```

Opens `data/applications.xlsx` automatically.

---

## 📝 Tracking Fields

| Field | Description | Example |
|-------|-------------|---------|
| **date_applied** | Auto-filled with today's date | 2025-11-16 |
| **company** | Company name | Salesforce |
| **role** | Job title | Software Engineering Intern |
| **location** | Office location | San Francisco, CA |
| **key_skills_required** | Main technologies from JD | Python, AWS, Distributed Systems |
| **resume_type** | Which YAML template used | backend, ml, data, algorithms, general |
| **status** | Application status | Applied, OA Sent, Interview, Rejected, Offer |
| **referral_requested** | Did you request referral? | Yes/No |
| **referral_name** | Who referred you | John Smith |
| **notes** | Any additional details | Applied via referral |

---

## 🎯 Workflow

**After each application:**

1. ✅ Apply through company portal
2. ✅ Send referral requests (if applicable)
3. ✅ Run `tracker log` to record application
4. ✅ Move to next company

**Weekly review:**

1. ✅ Run `tracker view` to see progress
2. ✅ Update statuses (OA sent, interviews, etc.)
3. ✅ Follow up on pending referrals

---

## 📈 Progress Tracking

**Week 1 Goal:** 15 applications
**Week 2 Goal:** 30 more applications (45 total)
**Week 3 Goal:** 30 more applications (75 total)

Use `tracker view` to monitor progress toward goals.

---

## 🔄 Updating Application Status

Edit `data/applications.csv` directly or use Excel:

**Status options:**
- `Applied` - Submitted application
- `OA Sent` - Online assessment received
- `Phone Screen` - Phone interview scheduled
- `On-site` - Final interviews
- `Offer` - Received offer
- `Rejected` - Application rejected
- `Ghosted` - No response after 3+ weeks

---

## 📊 The Data File

**Location:** `data/applications.csv`

**Format:** Simple CSV file you can:
- Open in Excel/Google Sheets
- Import into Notion/Airtable
- Analyze with Python/Pandas
- Share with career advisor

**Backup:** Stored in Git repo for version control

---

## 💡 Tips

1. **Log immediately after applying** - Don't wait or you'll forget
2. **Track referrals** - Know who helped you
3. **Note key skills** - Helps for interview prep later
4. **Update statuses weekly** - Keep it current
5. **Export to Excel monthly** - Easier to review than CSV

---

## 🎯 Quick Commands

```bash
# Log new application
tracker log

# View all applications  
tracker view

# Export to Excel
tracker excel
```

---

**Start tracking your applications today!** 🚀
