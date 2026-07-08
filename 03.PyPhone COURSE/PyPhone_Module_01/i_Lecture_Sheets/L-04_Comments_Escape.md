# 📘 PyPhone Emperor · Module 1  
# 📖 L‑04 – Comments & Escape Sequences in Reports

---

## 🎯 OBJECTIVE
Learn to write human‑readable comments
and use escape sequences to format
professional‑looking printed output.
Both are essential for clear, maintainable code
and generating well‑structured business reports.

---

## 🧱 BRICK 1 – Comments in Python

Comments are lines Python ignores completely.
They explain **why** something is done,
not what the code does.
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
Python ignores this block.
Use it for longer explanations.
"""
```

### Good commenting practice
- Explain complex logic or business rules.
- Temporarily disable a line during testing.
- Never state the obvious (`x = x + 1  # add 1` is useless).

> 💡 **RULE OF THUMB:** Comment **why**, not **what**.  
> The code already says what it does.

---

## 🧱 BRICK 2 – Basic Escape Sequences

Escape sequences let you include special characters
inside a string that are otherwise hard to type.
They start with a **backslash `\`**.

### Essential escape sequences

| Sequence | Meaning               | Example output       |
|----------|-----------------------|----------------------|
| `\n`     | new line              | breaks the line      |
| `\t`     | tab (indent)          | horizontal space     |
| `\\`     | literal backslash     | `\`                  |
| `\"`     | double quote          | `"`                  |

### Using them in a business report

```python
print("=== REPORT ===")
print("Item:\tMouse")
print("Price:\t$24.99")
print("Path: C:\\Users\\Emperor")
print("She said \"Hello\"")
```

Output:
```
=== REPORT ===
Item:   Mouse
Price:  $24.99
Path:   C:\Users\Emperor
She said "Hello"
```

### Why backslashes matter
File paths on Windows use `\`.  
If you write `"C:\new_folder"`, Python sees `\n` as a newline.  
Always use `"C:\\new_folder"` or a raw string `r"C:\new_folder"`.

---

## 💡 Real‑world Usage
In enterprise logging or invoice generation,
escape sequences help format readable output.

```python
# Comment: Generate invoice header
print("INVOICE\n------")
print("Customer:\tEmperor")
print("Address:\tDhaka, Bangladesh")
print("Note:\t\t\"Priority shipment\"")
```

---

## 🔍 Practice Preview
You will generate a formatted report.

- **Easy:** Add a comment, then print a string containing a newline (`Hello\nWorld`).
- **Medium:** Print a string that includes double quotes (`She said "Hi"`).
- **Hard:** Print a Windows file path with backslashes (`C:\Users\Emperor`).

Run the practice coach:
```bash
python ii_Practice_Sheets/L-04_Comments_Escape_Sequences.py
```

Choose your level, type the script, and the engine will verify.

---

## 📌 Key Takeaway
- Comments explain **why**; use `#` for single lines.
- Escape sequences (`\n`, `\t`, `\\`, `\"`) embed special characters.
- File paths must double the backslash unless using a raw string.
- Professional output is readable output.