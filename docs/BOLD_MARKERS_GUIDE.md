# Bold Markers Guide

## How to Use Bold Formatting in YAML

You can now bold specific words or phrases in your resume content using `**markers**` (like Markdown).

### ✅ Syntax

Wrap text with double asterisks:
```
**this will be bold**
```

### 📝 Where You Can Use It

**1. Summary:**
```yaml
summary: "Software Engineer with **4+ years** experience at **LSEG** building **event-driven systems**"
```

**2. Project Bullets:**
```yaml
bullet1: "Built **AWS Lambda** pipeline achieving **40% latency reduction**"
bullet2: "Processed **7.5M+ records** across **180+ countries**"
```

### 🎯 Best Practices

**DO bold:**
- ✅ Metrics and numbers: `**7.5M+ records**`, `**40% improvement**`
- ✅ Key technologies: `**AWS Lambda**`, `**Kubernetes**`, `**Python**`
- ✅ Important achievements: `**production-grade**`, `**real-time**`
- ✅ Company names: `**LSEG**`, `**Northeastern**`
- ✅ Quantified results: `**99.9% uptime**`, `**6+ design patterns**`

**DON'T over-bold:**
- ❌ Common words: `**the**`, `**and**`, `**with**`
- ❌ Entire sentences
- ❌ More than 30% of text
- ❌ Generic terms without impact

### 💡 Examples

**Good:**
```yaml
summary: "MS CS student at **Northeastern (3.89 GPA)** with **4+ years** production experience at **LSEG**"
```

**Bad (too much):**
```yaml
summary: "**MS CS student** at **Northeastern** **(3.89 GPA)** with **4+ years** **production experience**"
```

### 🔧 Technical Details

The script:
1. Splits text by `**` markers
2. Even parts (0, 2, 4...) = normal text
3. Odd parts (1, 3, 5...) = bold text
4. Automatically applies formatting in Word

### ⚠️ Important

- Always use **double asterisks** (not single `*`)
- Must have matching pairs: `**bold**` ✅ vs `**bold` ❌
- Works in: summary, project bullets
- Does NOT work in: skills items (those have fixed formatting)

---

**Now you can emphasize key achievements and metrics in your resume!** 🎯
