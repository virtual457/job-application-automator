# Standard Project Titles Reference

**Last Updated:** November 27, 2025

## 🎯 **Always Use These Exact Titles**

These titles match the GitHub URL dictionary in `simple_generator.py` for proper hyperlink generation.

---

## 📋 **Project Titles (Copy Exactly):**

### **Top Projects (Most Used):**

1. **LLM Multi-Agent Resume Optimizer**
   - GitHub: https://github.com/virtual457/llm-multi-agent-resume-optimizer
   - ⚠️ Use this EXACT title (not "LMARO" or "LMARO - LLM...")

2. **Orion Platform**
   - GitHub: https://github.com/virtual457/Orion-platform

3. **Dino Game Deep RL Agent**
   - GitHub: https://github.com/virtual457/dino-game-AI

4. **Calendly - Calendar Management System**
   - GitHub: https://github.com/virtual457/Calendly
   - Alternative: **Calendly** (both work)

5. **Port Management System**
   - GitHub: https://github.com/virtual457/Port-Management-System
   - Alternative: **Maritime Logistics Platform** (both work)

6. **Data Analysis on PUBG**
   - GitHub: https://github.com/virtual457/Data-analysis-on-pubg
   - Alternative: **Large Scale Data Analysis** (both work)

7. **Kambaz Learning Management System**
   - GitHub: https://github.com/virtual457/kambaz-next-js

8. **Face Recognition & Validation System**
   - GitHub: https://github.com/virtual457/Recognition-and-Validation-of-Faces-using-Machine-Learning-and-Image-Processing

9. **Online Examination System**
   - GitHub: https://github.com/virtual457/Online-examination-using-mongodb

---

## ⚠️ **Common Mistakes:**

| ❌ Wrong Title | ✅ Correct Title |
|----------------|------------------|
| "LMARO" | "LLM Multi-Agent Resume Optimizer" |
| "LMARO - LLM Multi-Agent Resume Optimizer" | "LLM Multi-Agent Resume Optimizer" |
| "Orion PaaS" | "Orion Platform" (both work, but Platform preferred) |
| "Calendly" | "Calendly - Calendar Management System" (both work) |

---

## 🔧 **How GitHub Links Work:**

The generator has a hardcoded dictionary:
```python
github_urls = {
    "LLM Multi-Agent Resume Optimizer": "https://github.com/virtual457/llm-multi-agent-resume-optimizer",
    "Orion Platform": "https://github.com/virtual457/Orion-platform",
    # ... etc
}
```

**Logic:**
1. Check if YAML has `github: "http://..."` (full URL)
2. If not, look up `project['title']` in `github_urls` dictionary
3. If found → Create hyperlink
4. If not found → No hyperlink (just plain text)

**So title must match dictionary key EXACTLY!**

---

## 📝 **Standard Format in YAML:**

```yaml
projects:
  - title: "LLM Multi-Agent Resume Optimizer"  # ← EXACT title
    tech: "Python, LangChain, RAG, FastAPI, React 19, ChromaDB"
    github: "GitHub"  # ← Will be replaced with URL
    bullet1: "..."
    bullet2: "..."
```

---

**Always use these exact titles for proper hyperlink generation!** 🎯
