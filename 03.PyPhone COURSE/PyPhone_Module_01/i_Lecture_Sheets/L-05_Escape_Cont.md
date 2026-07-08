# 📘 PyPhone Emperor · Module 1  
# 📖 L‑05 – Escape Sequences (Log Formatting)

---

## 🎯 OBJECTIVE
Complete your mastery of escape sequences.
Learn to format log entries with tabs,
include special characters like the bell,
and use raw strings for file paths.
This ensures your program output is professional
and your strings can hold any text without breaking.

---

## 🧱 BRICK 1 – Tab, Bell, and Backslash

Escape sequences allow you to embed invisible characters
and special symbols inside strings.

### Tab `\t`
Used to align columns in log entries or reports.

```python
print("Name:\tEmperor")
print("Age:\t18")
```

Output:
```
Name:   Emperor
Age:    18
```

### Bell `\a` (Alert)
Historically made a beep; in modern terminals it may
do nothing but still represents an alert.

```python
print("Error!\a")   # may not produce sound, but the character is there
```

### Backslash `\\`
To display a single backslash, write two.

```python
print("Path: C:\\Users\\Emperor")
# Path: C:\Users\Emperor
```

### Escaping quotes – recap
- `\"` inside a double‑quoted string prints `"`
- `\'` inside a single‑quoted string prints `'`

---

## 🧱 BRICK 2 – Raw Strings

Sometimes you need backslashes to be treated literally,
not as escape characters. Prefix the string with `r`.

```python
print(r"\n is not a newline here")
# \n is not a newline here
```

**When to use raw strings**
- File paths on Windows: `r"C:\new_folder\temp"`
- Regular expressions (later)
- Displaying a literal `\n` or `\t` in output

> ⚠️ A raw string cannot end with a single backslash.
> `r"\"` is invalid.

---

## 💡 Real‑world Usage
In enterprise logging, you often format a line with
a timestamp, level, and message, separated by tabs.

```python
print("2026‑07‑08\tINFO\tServer started")
print("2026‑07‑08\tERROR\tDisk full")
print(r"Log path: C:\app\logs\server.log")
```

---

## 🔍 Practice Preview
You will produce log‑style output.

- **Easy:** Print `Name:\tAge` (with a real tab).
- **Medium:** Print a string containing the bell character `\a`.
- **Hard:** Print a raw string that shows `\n` literally.

Run the practice coach:
```bash
python ii_Practice_Sheets/L-05_Escape_Sequences_Cont.py
```

Choose your level, type the script, and the engine will verify.

---

## 📌 Key Takeaway
- `\t` aligns columns; `\a` represents an alert; `\\` prints one backslash.
- Raw strings (`r"..."`) ignore escape sequences.
- Use raw strings for file paths and any text with many backslashes.