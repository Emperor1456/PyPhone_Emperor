# 📘 PyPhone Emperor v3.0 · Module 1
# 📖 L‑04 – String Methods & f‑strings

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, text transformation becomes second nature.

- 🧼 Cleaning – `strip()`, `lstrip()`, `rstrip()`
- 🔍 Searching – `find()`, `count()`, `startswith()`, `endswith()`
- ✂️ Splitting & Joining – `split()`, `join()`
- 🔄 Replacing – `replace()`
- 🎨 Formatting – f‑strings for professional output
- 🧪 Case Conversion – `upper()`, `lower()`, `title()`

---

## 🧱 CLEANING & SEARCHING

Whitespace destroys data integrity. Strip it.

```python
raw = "   Emperor   "
clean = raw.strip()
print(clean)          # "Emperor"
print(raw.lstrip())   # "Emperor   "
print(raw.rstrip())   # "   Emperor"
```

Search inside strings:

```python
email = "emperor@pyphone.com"
print(email.find("@"))           # 7
print(email.count("o"))          # 2
print(email.startswith("emp"))   # True
print(email.endswith(".com"))    # True
```

`.find()` returns `-1` if not found – never crashes.

---

## 🧱 SPLITTING, JOINING & REPLACING

Split a string into a list:

```python
csv = "apple,banana,grape"
fruits = csv.split(",")
print(fruits)   # ['apple', 'banana', 'grape']
```

Join a list into a string:

```python
words = ["PyPhone", "Emperor", "v3"]
sentence = " ".join(words)
print(sentence)   # "PyPhone Emperor v3"
```

Replace substrings:

```python
msg = "Hello World"
updated = msg.replace("World", "Emperor")
print(updated)   # "Hello Emperor"
```

> 💡 **INSIGHT:** Strings are immutable. All these methods return **new** strings.

---

## 🧱 F‑STRINGS – THE PROFESSIONAL FORMAT

f‑strings embed variables directly inside a string.

```python
name = "Emperor"
age = 18
print(f"{name} is {age} years old.")
# Emperor is 18 years old.
```

Format numbers:

```python
price = 24.99
qty = 3
print(f"Total: ${price * qty:.2f}")   # Total: $74.97
```

Align columns:

```python
for item, val in [("A", 10), ("B", 200)]:
    print(f"{item:>5} {val:>5}")
#     A    10
#     B   200
```

---

## 🧱 CASE CONVERSION

```python
s = "pyPhone emperor"
print(s.upper())       # PYPHONE EMPEROR
print(s.lower())       # pyphone emperor
print(s.title())       # Pyphone Emperor
```

---

## 💡 Real‑world Usage

**Banking – sanitize user input**
```python
acct = input("Account: ").strip().upper()
print(f"Looking up {acct}")
```

**E‑commerce – generate product slug**
```python
name = "Wireless Mouse Pro"
slug = name.lower().replace(" ", "-")
print(slug)   # "wireless-mouse-pro"
```

**Logistics – parse CSV shipment data**
```python
line = "TRK-123,Dhaka,12.5"
parts = line.split(",")
tracking, dest, weight = parts
```

**HR – format employee badge**
```python
emp = {"first": "Emperor", "last": "PyPhone", "id": 101}
badge = f"{emp['last'].upper()}, {emp['first']} (#{emp['id']:04d})"
print(badge)   # PYPHONE, Emperor (#0101)
```

---

## 🔍 Practice Preview
You will:
- Strip and clean user input strings.
- Parse CSV lines with `split()`.
- Build formatted receipts using f‑strings.
- Generate slugs and codes with `replace()` and `lower()`.

Run the coach:
```bash
python ii_Practice_Sheets/L04_String_Methods_fstrings.py
```

---

## 📌 Key Takeaway
- `.strip()`, `.split()`, `.join()`, `.replace()` are your daily tools.
- f‑strings embed variables and format numbers with precision.
- All string methods return a new string – never modify in place.
- Clean data before it enters your system.

*For Emperor.*