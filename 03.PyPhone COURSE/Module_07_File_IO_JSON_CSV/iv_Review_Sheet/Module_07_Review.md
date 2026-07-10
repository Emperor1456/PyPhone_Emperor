# 📘 Module 07 – File I/O, JSON & CSV · Revision Guide

---

## L36 – Reading Text Files

- `open("file", "r")` opens for reading; use `with` for automatic close.
- `.read()` – entire file as a string.
- `.readline()` – next line (including `\n`).
- `.readlines()` – list of all lines.
- Iterate over the file object for memory‑efficient line reading.

```python
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())
```

---

## L37 – Writing & Appending Files

- `open("file", "w")` – write mode (overwrites).
- `open("file", "a")` – append mode.
- `.write(str)` – writes a single string.
- `.writelines(list)` – writes a list of strings.
- Always use `with` to prevent data loss.

```python
with open("log.txt", "a") as f:
    f.write("New entry\n")
```

---

## L38 – CSV Files

- `csv.reader(f)` – read rows as lists.
- `csv.DictReader(f)` – read rows as ordered dicts using the header.
- `csv.writer(f)` – write rows from lists.
- `csv.DictWriter(f, fieldnames=…)` – write rows from dicts.
- Always open with `newline=""` when writing.

```python
import csv
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])
```

---

## L39 – JSON

- `json.load(f)` – read JSON from a file → Python object.
- `json.dump(obj, f, indent=2)` – write Python object to file as JSON.
- `json.loads(str)` – parse a JSON string.
- `json.dumps(obj)` – convert Python object to JSON string.
- `indent` makes the output human‑readable.

```python
import json
data = {"name": "Emperor", "age": 18}
with open("user.json", "w") as f:
    json.dump(data, f, indent=2)
```

---

## L40 – pathlib – Modern File Paths

- `Path("file.txt")` creates a path object.
- `.read_text()` / `.write_text()` – simple file I/O.
- `.exists()`, `.is_file()`, `.is_dir()` – check properties.
- `.glob("*.py")` – find files matching a pattern.
- `.mkdir(exist_ok=True)` – create directories.

```python
from pathlib import Path
p = Path("config.json")
if p.exists():
    print(p.read_text())
```

---

**Quick Test:**  
- How do you read a file line by line without loading the whole file?  
- What happens if you open a file in `'w'` mode and it already exists?  
- How do you write a list of dictionaries to a CSV file?  
- What is the difference between `json.load()` and `json.loads()`?

*Review complete. You are now ready for the Module 07 Practice Review.*