# Character Counting Logic - UPDATED

**Date:** November 27, 2025

## ✅ **New Behavior: `**` Markers NOT Counted**

The validator now **excludes `**` markers** from character counts.

---

## 📊 **How Character Counting Works:**

### **Example:**

**YAML Text:**
```
Built **AWS Lambda** pipeline with **Python**
```

**Old Counting (WITH `**`):**
- Total characters: 48 (includes the 8 asterisks)

**New Counting (WITHOUT `**`):**
- Text only: "Built AWS Lambda pipeline with Python"
- Total characters: 40 (excludes the 8 asterisks)

---

## 🔧 **Code Implementation:**

```python
def _strip_bold_markers(text: str) -> str:
    """Remove ** markers from text for character counting"""
    return text.replace('**', '')

# Usage:
summary = "Built **AWS** with **Python**"
summary_text_only = _strip_bold_markers(summary)  # "Built AWS with Python"
summary_len = len(summary_text_only)  # 23 chars (not 31)
```

---

## 📋 **What This Means:**

### **Summary Constraint: 450-520 chars**

**Counts:**
- ✅ All actual text
- ❌ NOT the `**` markers

**Example:**
```yaml
summary: "MS at Northeastern (**3.89 GPA**), available for **Summer 2026**."
```

**Character count:**
- With **: 69 characters
- Without **: 61 characters ← **This is what validator counts**

---

## 🎯 **Benefits:**

1. ✅ **More intuitive** - Count actual readable text
2. ✅ **Consistent with Word output** - Word doesn't show `**`
3. ✅ **Fair limits** - More space for actual content
4. ✅ **Matches user expectations** - Bold is formatting, not content

---

## ⚙️ **Applied To:**

- ✅ Summary character count
- ✅ Experience bullet character counts
- ✅ Project bullet character counts
- ❌ Skills items (no bold markers in skills anyway)

---

**All validation now excludes `**` from character counts!** 🎉
