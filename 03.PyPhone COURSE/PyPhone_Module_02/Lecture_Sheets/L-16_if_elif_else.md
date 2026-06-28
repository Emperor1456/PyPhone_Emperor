# 📘 PyPhone Emperor · Module 2
# 📖 L‑16 – `if-elif-else` Chain

---

## 🎯 OBJECTIVE
Learn to handle multiple conditions in sequence
using the `if-elif-else` chain.
Python checks each condition in order;
the first `True` branch runs, and the rest are skipped.
If none are `True`, the `else` block (if present) executes.

---

## 🧱 BRICK 1 – The Ladder

```python
if condition1:
    # runs if condition1 is True
elif condition2:
    # runs if condition1 is False AND condition2 is True
elif condition3:
    # runs if all above are False AND condition3 is True
else:
    # runs if all conditions are False
```

**Example:**
```python
score = 82
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(grade)   # B
```

> 💡 **INSIGHT:** Only the first matching block runs. Even if later conditions also match, they are ignored.

---

## 🧱 BRICK 2 – Real‑world Patterns

**① Tiered pricing**
```python
quantity = 25
if quantity >= 100:
    price = 8
elif quantity >= 50:
    price = 9
elif quantity >= 10:
    price = 10
else:
    price = 12
```

**② Risk classification**
```python
age = 65
if age < 18:
    risk = "Low"
elif age < 50:
    risk = "Medium"
elif age < 70:
    risk = "High"
else:
    risk = "Critical"
```

> ⚠️ **WARNING:** Order matters. Place the most restrictive conditions first, or the chain may never reach later branches.

---

## 📌 Key Takeaway
- `if-elif-else` handles multiple exclusive paths.
- Exactly one block executes (or none if no `else`).
- Order is critical — first match wins.
- Use for grading, pricing, classification.