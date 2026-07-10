# 📘 PyPhone Emperor v3.0 · Module 7
# 📖 L‑36 – Reading Text Files – `open`, `read`, `readlines`

---

## 🎯 OBJECTIVE — What You Will Master

> Pull data from files into your Python programs.

- 📂 `open(file, mode)` – open for reading (`'r'`)
- 📖 `.read()` – entire file as a single string
- 📄 `.readline()` – read one line at a time
- 📑 `.readlines()` – list of all lines
- 🔒 **Context manager** (`with`) – automatic close

---

## 🧱 READING AN ENTIRE FILE

```python
with open("data.txt", "r") as f:
    content = f.read()
print(content)
```

`with` ensures the file is closed even if an error occurs.

---

## 🧱 READING LINE BY LINE

```python
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())
```

Memory‑efficient for large files.

---

## 🧱 READING SPECIFIC LINES

```python
with open("data.txt", "r") as f:
    first = f.readline()
    second = f.readline()
print(first, second)
```

---

## 💡 Real‑world Usage

**Banking – load transaction log**
```python
with open("transactions.txt") as f:
    for tx in f:
        print(f"Processing: {tx.strip()}")
```

**E‑commerce – read product list**
```python
with open("products.txt") as f:
    products = [line.strip() for line in f]
```

**Logistics – read shipping manifest**
```python
with open("manifest.txt") as f:
    if "DELIVERED" in f.read():
        print("All delivered")
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Read entire content of "test.txt" into a variable and print it. |
| Medium | Read all lines into a list and print the list. |
| Hard | Read only the first line and print it stripped. |

Run the coach:
```bash
python ii_Practice_Sheets/L36_Reading_Text_Files.py
```

---

## 📌 Key Takeaway
- Use `with open(file, 'r')` to read files safely.
- `.read()` for small files, iteration for large ones.
- Always strip newlines when processing lines.

*For Emperor.*