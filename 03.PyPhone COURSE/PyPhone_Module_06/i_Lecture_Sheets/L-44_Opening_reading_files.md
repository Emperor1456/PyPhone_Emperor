# 📘 PyPhone Emperor · Module 6  
# 📖 L‑44 – Opening & Reading Files (Processing Business Data)

---

## 🎯 OBJECTIVE  
Master reading files using Python's `open()` and the `with` statement.  
Read entire files, line by line, or all lines at once.  
This is the entry point for processing logs, configuration files, and batch data feeds.

---

## 🧱 BRICK 1 – Opening and Reading a Whole File

Open a file in `'r'` mode and read its content with `.read()`.

```python
with open('test.txt', 'r') as f:
    content = f.read()
print(content)   # prints the whole file
```

**① Read a log header (Easy practice)**
```python
# test.txt contains "Hello"
with open('test.txt', 'r') as f:
    content = f.read()
print(content)   # Hello
```
This gives the full file as one string — ideal for small config files or message templates.

**② Read all lines into a list (Medium practice)**
```python
with open('test.txt', 'r') as f:
    lines = f.readlines()
print(lines)   # ['Hello\n', 'World\n']  (if file has two lines)
```
`.readlines()` returns a list where each element is a line (including the newline character).

**③ Read first line only and strip whitespace (Hard practice)**
```python
with open('test.txt', 'r') as f:
    first = f.readline().strip()
print(first)   # Hello
```
`.readline()` reads one line; `.strip()` removes the trailing `\n`.

> 💡 **INSIGHT:** Use `.read()` for small files, `.readlines()` when you need a list, and a `for` loop over the file object for memory‑efficient line processing.

> ⚠️ **WARNING:** Always use `with open(...)` — it automatically closes the file even if an error occurs.

---

## 🧱 BRICK 2 – Efficient Line‑by‑Line Processing

The file object itself is iterable; loop over it to read line by line without loading the entire file into memory.

```python
with open('test.txt', 'r') as f:
    for line in f:
        print(line.strip())   # process each line
```

**Real‑world – reading a configuration file**
```python
config = {}
with open('config.ini', 'r') as f:
    for line in f:
        if '=' in line:
            key, val = line.strip().split('=')
            config[key.strip()] = val.strip()
print(config)
```

> 💡 **ADVANCED TIP – Use `encoding='utf-8'`:**  
> Specify encoding to avoid crashes on non‑ASCII characters:
> `with open('data.txt', 'r', encoding='utf-8') as f:`

---

## 💡 Real‑world Usage

**Banking – reading transactions log**
```python
with open('transactions.txt', 'r') as f:
    for tx in f:
        print(f"Processing: {tx.strip()}")
```

**E‑commerce – loading product IDs**
```python
with open('products.txt', 'r') as f:
    ids = [line.strip() for line in f]
print(ids)
```

**Logistics – check delivery status from a manifest**
```python
with open('manifest.txt', 'r') as f:
    if 'DELIVERED' in f.read():
        print('Shipment complete')
```

**HR – reading employee list**
```python
with open('employees.txt', 'r') as f:
    headcount = len(f.readlines())
print(f"Total: {headcount}")
```

---

## 🔍 Practice Preview
You will read from a pre‑created file `test.txt` that contains two lines: `Hello` and `World`.

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Open `test.txt` in read mode, read its content into a variable, and print it. | `Hello` (depending on setup) |
| Medium | Read all lines from `test.txt` into a list and print the list. | `['Hello\n', 'World\n']` (or similar) |
| Hard   | Read the first line of `test.txt` and print it stripped. | `Hello` |

Run the coach:
```bash
python ii_Practice_Sheets/L-44_Opening_Reading_Files.py
```
The engine will create the file automatically.

---

## 📌 Key Takeaway
- `open('file', 'r')` opens for reading; use `with` for auto‑close.
- `.read()` = whole string, `.readlines()` = list, `.readline()` = one line.
- Iterate over the file object for memory‑efficient line processing.
- Always strip newlines with `.strip()` when printing or processing.