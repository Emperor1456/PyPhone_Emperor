# 📘 PyPhone Emperor · Module 2
# 📖 L‑14 – Basic `if` Statement

---

## 🎯 OBJECTIVE
Learn to make decisions in Python using the **`if`** statement.
When a condition is `True`, the indented code block runs.
When it’s `False`, the block is skipped entirely.
This is the foundation of all intelligent programs.

---

## 🧱 BRICK 1 – Syntax and Indentation

An `if` statement consists of three parts:

① The keyword `if`  
② A condition that evaluates to `True` or `False`  
③ A colon `:` followed by an **indented block** of code  

```python
if condition:
    # this line runs only if condition is True
    statement
    statement
```

**Crucial:** The indented lines must be indented **exactly the same amount** (4 spaces is the standard).  
If you mix spaces and tabs, Python will crash.

**Minimal example:**
```python
temperature = 35
if temperature > 30:
    print("It's a hot day.")
```
If `temperature` is 35, the condition `35 > 30` is `True`, so the message prints.  
If `temperature` were 25, nothing would print.

---

## 🧱 BRICK 2 – Conditions and the Flow

The condition can be:
- A comparison (`a == b`, `x > y`, `score <= 100`)
- A logical expression (`age >= 18 and has_license`)
- Any value that Python treats as `True` or `False` (truthiness – covered later)

The **flow** of an `if` statement:
```
       ┌─────────────┐
       │  condition? │
       └──────┬──────┘
          True│False
      ┌───────┐
      │ block │      (skip)
      └───────┘
```

> 💡 **INSIGHT:** The indented block can contain multiple lines, even other `if` statements (nested conditionals, which we’ll meet later).

---

## 💡 Real‑world Usage
```python
# Bank account withdrawal check
balance = 500
withdraw = 300

if withdraw <= balance:
    balance -= withdraw
    print("Withdrawal successful.")
    print("Remaining:", balance)
```
If `withdraw` is 300 and `balance` is 500, the condition holds, money is deducted, and the message appears.  
If `withdraw` is 700, nothing happens – the if‑block is skipped.

---

## 🔍 Practice Preview (for later coding)
```python
age = 18
if age >= 18:
    print("You can vote!")

score = 85
if score >= 90:
    print("Grade: A")
if score >= 80:
    print("Grade: B")
```

---

## 📌 Key Takeaway
- `if condition:` starts a decision block.
- The indented code runs **only** when the condition is `True`.
- Use consistent spacing (4 spaces per level).
- Conditions are built from comparisons and logical operators.