# Summary Generation Guide for LLMs

**Quick Reference for Generating Summary Sections**
**UPDATED:** November 27, 2025 - New constraint: 450-520 characters

---

## 🎯 **Format Template (450-520 chars):**

```
MS Computer Science student at Northeastern (**3.89 GPA**, Graduating **May 2027**), **F-1 CPT/OPT** eligible, available for **Summer 2026** internship. Experience building [JD-FOCUS] at **London Stock Exchange Group**. Developed [TECH-HIGHLIGHTS]. [ACHIEVEMENT]. Passionate about [INTEREST]. Excited to [VALUE-PROP] at **[COMPANY]**.
```

---

## ⚙️ **CRITICAL CONSTRAINTS:**

- **Characters:** 450-520 (STRICT - was 520-570, now SHORTER)
- **Bold markers:** 5-8
- **Sentences:** 4-5 sentences (reduced from 5-6)
- **Tone:** Professional bio

---

## 📋 **Step-by-Step Generation:**

### **Step 1: Fixed Opening (~165 chars)**
```
MS Computer Science student at Northeastern (**3.89 GPA**, Graduating **May 2027**), **F-1 CPT/OPT** eligible, available for **Summer 2026** internship.
```

### **Step 2: Experience Focus (~90 chars)**
```
Experience building [JD-FOCUS] at **London Stock Exchange Group**.
```

**Examples:**
- Experience building scalable backend systems at **London Stock Exchange Group**.
- Experience building AI-driven internal tools at **London Stock Exchange Group**.
- Experience building full-stack platforms at **London Stock Exchange Group**.

### **Step 3: Technical Highlights (~120 chars) - SHORTER NOW**

**Format:**
```
Developed [TECH-1] with [TECH-2], [SYSTEM] processing [METRIC], and [TECH-3].
```

**Examples:**
- Developed event-driven architectures with **Python** and **Java**, microservices processing **7.5M+ records**, and platform tools in Go.
- Developed **LLM applications** with multi-agent systems, **Deep RL agents**, and pipelines processing **7.5M+ records**.
- Developed applications with **FastAPI** and React, automation tools, and dashboards improving productivity by **35%**.

### **Step 4: Achievement (~30 chars) - BRIEF**

**Format:**
```
[Action verb] [metric].
```

**Examples:**
- Reduced latency by **40%**.
- Improved efficiency by **35%**.
- Achieved **99.9% uptime**.

### **Step 5: Passion + Company (~80 chars) - COMBINED**

**Format:**
```
Passionate about [INTEREST]. Excited to [VALUE-PROP] at **[COMPANY]**.
```

**Examples:**
- Passionate about reliable infrastructure. Excited to contribute to **Stripe**'s internet GDP mission.
- Passionate about **AI** advancement. Excited to build products at **Google**.
- Passionate about user experiences. Excited to connect travelers at **Airbnb**.

---

## 📊 **Character Budget (450-520):**

| Section | Target | % |
|---------|--------|---|
| Education + Status | 165 | 33% |
| Experience | 90 | 18% |
| Technical Highlights | 120 | 24% |
| Achievement | 30 | 6% |
| Passion + Company | 80 | 16% |
| **TOTAL** | **485** | **97%** |

**Wiggle room:** ~35 characters for adjustment

---

## ✅ **Valid Examples (All 450-520 chars):**

### **Example 1: Stripe Backend - 492 chars, 8 bold**
```
MS Computer Science student at Northeastern (**3.89 GPA**, Graduating **May 2027**), **F-1 CPT/OPT** eligible, available for **Summer 2026** internship. Experience building scalable backend systems at **London Stock Exchange Group**. Developed event-driven architectures with **Python** and **Java**, microservices processing **7.5M+ records**, and platform tools in Go. Reduced latency by **40%**. Passionate about reliable infrastructure. Excited to contribute to **Stripe**'s internet GDP mission.
```

### **Example 2: Google ML - 461 chars, 7 bold**
```
MS Computer Science student at Northeastern (**3.89 GPA**, Graduating **May 2027**), **F-1 CPT/OPT** eligible, available for **Summer 2026** internship. Experience building AI systems at **London Stock Exchange Group**. Developed **LLM applications**, **Deep RL agents**, and pipelines processing **7.5M+ records**. Improved efficiency by **35%**. Passionate about advancing **AI**. Excited to build products at **Google**.
```

### **Example 3: MongoDB Tools - 478 chars, 7 bold**
```
MS Computer Science student at Northeastern (**3.89 GPA**, Graduating **May 2027**), **F-1 CPT/OPT** eligible, available for **Summer 2026** internship. Experience building internal tools at **London Stock Exchange Group**. Developed automation platforms with **Python**, **FastAPI**, and React, processing **7.5M+ records**. Improved productivity by **35%**. Passionate about developer tools. Excited to build at **MongoDB**.
```

---

## 🚫 **Common Mistakes:**

1. ❌ **Going over 520 characters**
   - Was allowed before, NOT ANYMORE
   - 450-520 is the new strict range

2. ❌ **Too wordy** 
   - Cut unnecessary words
   - "performance optimization" → "optimization"
   - "that powers global platforms" → "infrastructure"

3. ❌ **Too many technical details**
   - Keep it high-level
   - Save details for experience bullets

---

## 🎯 **Generation Workflow:**

```
1. Use fixed opening (165 chars)
2. Add experience focus (90 chars)
3. Add technical highlights (120 chars)
4. Add ONE achievement (30 chars)
5. Add passion + company (80 chars)
6. Count total: Should be ~485 chars
7. Count bold: Should be 7-8
8. Verify range: 450-520 ✅
```

---

## 📏 **Length Guidelines:**

- **Minimum:** 450 characters (don't go under)
- **Target:** 480-500 characters (sweet spot)
- **Maximum:** 520 characters (hard limit)

**Old range was 520-570, NEW range is 450-520!**

---

**This format is now standard for ALL resumes.**
