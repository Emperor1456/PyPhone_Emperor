# 📘 PyPhone Emperor · Module 1  
# 📖 L‑04 – Comments & Escape Sequences

---

## 🎯 OBJECTIVE
Learn to write human‑readable notes inside
your code using **comments**, and to use
**escape sequences** to include special
characters inside strings.
Both are essential for writing clean,
professional, and debug‑friendly code.

---

## 🧱 BRICK 1 – Comments in Python

Comments are lines Python ignores completely.
They explain **what** and **why**, not **how**.
Good comments make your code readable months later.

### Single‑line comment
```python
# This is a comment – Python skips it
name = "Emperor"   # inline comment
```

### Multi‑line comments (using triple quotes)
```python
"""
This is a multi‑line comment.
Python ignores this block as well.
Use it for longer explanations.
"""
```

### When to comment
- Explain a tricky section of code.
- State assumptions or constraints.
- Temporarily disable a line during testing.

### What NOT to do
```python
x = x + 1   # add 1 to x   ← useless comment
```
The code itself is obvious; don't state the obvious.

> 💡 **RULE OF THUMB:** Comment **why**, not **what**. The code already says what it does.

---

## 🧱 BRICK 2 – Basic Escape Sequences

Escape sequences let you insert characters that
are otherwise hard to type directly inside a string.
They start with a **backslash `\`**.

### Common escape sequences

- `\n` — new line (breaks the line)
- `\t` — tab (indentation)
- `\\` — backslash (prints `\`)

**Examples:**
```python
print("Hello\nWorld")
# Hello
# World

print("Name:\tEmperor")
# Name:   Emperor
```

**Mixing them:**
```python
print("Line 1\nLine 2\n\tIndented Line 3")
# Line 1
# Line 2
#     Indented Line 3
```

### Printing a literal backslash
```python
print("This is a backslash: \\")
# This is a backslash: \
```

> 💡 **INSIGHT:** Escape sequences are the reason you can’t write a file path like `C:\new_folder` directly — `\n` would become a newline. Use `C:\\new_folder` or a raw string `r"C:\new_folder"`.

---

## 💡 Real‑world Usage
In enterprise logging or report generation,
escape sequences help format readable output.

```python
print("=== REPORT ===")
print("Name:\tJohn Doe")
print("Dept:\tFinance\n")
print("Notes:\tPaid in full.")
```

---

## 🔍 Practice Preview (for later coding)
```python
# Single-line comment: print a greeting
print("Hello, Emperor!")   # This prints a message

"""
Multi-line comment:
This program demonstrates escape sequences.
"""
print("Item\t\tPrice\nApple\t\t$1.00\nBanana\t\t$0.50")
print("This is a backslash: \\")
```

---

## 📌 Key Takeaway
- Comments explain **why**, not what.
- Use `#` for single line, triple quotes for blocks.
- `\n` = newline, `\t` = tab, `\\` = backslash.
- Write comments that add value, not noise.