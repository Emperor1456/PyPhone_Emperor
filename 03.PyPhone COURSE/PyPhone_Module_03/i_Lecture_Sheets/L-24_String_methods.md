# 📘 PyPhone Emperor · Module 3  
# 📖 L‑24 – String Methods (Text Cleaning & Transformation)

---

## 🎯 OBJECTIVE  
Master Python’s built‑in string methods for case conversion, whitespace removal, searching, splitting, joining, and replacing.  
These are the everyday tools for cleaning user input, normalizing product codes, validating emails, and formatting reports.

---

## 🧱 BRICK 1 – Case Conversion and Whitespace Control

String methods return a **new string**; they never modify the original because strings are immutable.

**① Convert to uppercase for standard codes**
```python
s = 'emperor'
print(s.upper())   # 'EMPEROR'
```
Use `.upper()` to normalize product keys, country codes, or user IDs.

**② Convert to lowercase for case‑insensitive comparison**
```python
email = 'Emperor@Domain.Com'
normalized = email.lower()   # 'emperor@domain.com'
```

**③ Title case for proper names**
```python
name = 'emperor builder'
print(name.title())   # 'Emperor Builder'
```

**④ Remove surrounding whitespace with `.strip()`**
```python
t = '  data  '
clean = t.strip()
print(clean)   # 'data'
```
`.strip()` removes spaces, tabs, and newlines from both ends — essential for cleaning form inputs.

**⑤ Left/right variants**
```python
t.lstrip()   # left side only
t.rstrip()   # right side only
```

> 💡 **INSIGHT:** Always strip user‑provided text before processing.  
> A stray space at the end can break a query or mismatch a key.

> ⚠️ **WARNING:** `.strip()` does not change the original string.  
> You must assign the result: `s = s.strip()`.

---

## 🧱 BRICK 2 – Searching, Replacing, Splitting, and Joining

**⑥ Search with `.find()` and `.count()`**
```python
email = 'emperor@domain.com'
at_pos = email.find('@')          # 7
dot_count = email.count('.')       # 1
print(at_pos, dot_count)
```
`.find()` returns the index of the first match, or `-1` if not found — it never crashes.

**⑦ Check prefix/suffix with `.startswith()` and `.endswith()`**
```python
file = 'report_2026.pdf'
if file.endswith('.pdf'):
    print('PDF document')
```

**⑧ Replace substrings with `.replace()`**
```python
msg = 'Hello World'
updated = msg.replace('World', 'Emperor')
print(updated)   # 'Hello Emperor'
```
All occurrences are replaced unless you specify a count limit as a third argument.

**⑨ Split a string into a list**
```python
csv = 'apple,banana,grape'
fruits = csv.split(',')   # ['apple', 'banana', 'grape']
```
No separator: `.split()` splits on any whitespace and discards empty strings.

**⑩ Join a list back into a string**
```python
words = ['PyPhone', 'Emperor', 'Rocks']
sentence = ' '.join(words)   # 'PyPhone Emperor Rocks'
```
The separator goes **between** elements, not at the ends.

> 💡 **ADVANCED TIP – Chaining methods:**  
> Because each method returns a string, you can chain them:  
> `raw.strip().lower().replace(' ', '_')` — clean, normalize, then replace spaces with underscores.

---

## 💡 Real‑world Usage

**Banking – mask account number for display**
```python
acct = '1234567890123456'
masked = '****' + acct[-4:]
print(masked)   # ****3456
```

**E‑commerce – extract product attributes from a tag**
```python
tag = '  SKU‑123‑BLK   '
clean_tag = tag.strip()
parts = clean_tag.split('-')   # ['SKU', '123', 'BLK']
color = parts[-1]              # 'BLK'
print(color)
```

**Logistics – normalize address for label printing**
```python
address = '  123 Main St, Dhaka   '
clean_address = address.strip().title()
print(clean_address)   # '123 Main St, Dhaka'
```

**HR – validate an email domain**
```python
email = 'emperor@pyphone.com'
if email.endswith('@pyphone.com'):
    print('Internal employee')
else:
    print('External contact')
```

**Reporting – create a slug from a title**
```python
title = 'Monthly Sales Report 2026'
slug = title.lower().replace(' ', '-')
print(slug)   # 'monthly-sales-report-2026'
```

---

## 🔍 Practice Preview
You will write three string method mini‑programs.

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | `s='emperor'`. Print it in uppercase. | `EMPEROR`       |
| Medium | `t='  data  '`. Print it without surrounding spaces. | `data`          |
| Hard   | `msg='Hello World'`. Replace `'World'` with `'Emperor'` and print. | `Hello Emperor` |

Run the coach:
```bash
python ii_Practice_Sheets/L-24_String_Methods.py
```
Choose `1`, `2`, or `3`. Type your line; the engine checks output.

---

## 📌 Key Takeaway
- `.upper()`, `.lower()`, `.title()` change letter case.
- `.strip()` removes leading/trailing whitespace.
- `.find()`, `.count()`, `.startswith()`, `.endswith()` search strings.
- `.replace()` swaps substrings; `.split()` and `.join()` convert between strings and lists.
- Strings are immutable — always assign the returned value.