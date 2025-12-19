# Generator vs Reviser - Complete Guide

**Created:** November 27, 2025

## 🎯 **Two Tools for YAML Creation**

1. **`generator.py`** - Creates YAML from scratch
2. **`reviser.py`** - Revises existing YAML based on feedback

---

## 📋 **When to Use Which?**

### **Use GENERATOR:**
- ✅ New job application
- ✅ Starting from scratch
- ✅ Have job description

### **Use REVISER:**
- ✅ Fix validation errors
- ✅ Improve quality/ATS scores
- ✅ Apply feedback

---

## 🚀 **Generator Usage:**

```bash
# Interactive
python generator.py

# From file
python generator.py --jd-file jd.txt

# With company
python generator.py --company "Stripe"
```

---

## 🔧 **Reviser Usage:**

```bash
# Interactive
python reviser.py

# Quick feedback
python reviser.py --feedback "Summary too long"

# From file
python reviser.py --feedback-file feedback.txt
```

---

## 🔄 **Complete Flow:**

```
1. python generator.py → Create YAML
2. python validate_yaml.py → Check constraints
3. python reviser.py → Fix errors (if any)
4. python main.py → Generate + validate
5. Apply!
```

---

**Both tools ready to use!** 🎉
