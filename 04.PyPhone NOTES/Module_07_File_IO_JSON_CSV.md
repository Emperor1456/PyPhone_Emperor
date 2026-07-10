# 📘 Module 07 – File I/O, JSON & CSV · Revision Note

---

## L36 – Reading Text Files
- `open("file", "r")` opens for reading; use `with` for auto‑close.
- `.read()` – entire file as string.
- `.readline()` – next line (including `\n`).
- `.readlines()` – list of all lines.
- Iterate over the file object for memory‑efficient reading.

```python
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())
```

---

## L37 – Writing & Appending Files
- `open("file", "w")` – write mode (overwrites).
- `open("file", "a")` – append mode.
- `.write(str)` – single string; `.writelines(list)` – multiple.
- Always use `with` to prevent data loss.

```python
with open("log.txt", "a") as f:
    f.write("New entry\n")
```

---

## L38 – CSV Files
- `csv.reader(f)` – rows as lists.
- `csv.DictReader(f)` – rows as dicts (header from first row).
- `csv.writer(f)` – write lists; `csv.DictWriter(f, fieldnames=…)` – write dicts.
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
- `json.load(f)` – read JSON from file → Python object.
- `json.dump(obj, f, indent=2)` – write Python object to file as JSON.
- `json.loads(str)` – parse JSON string.
- `json.dumps(obj)` – convert Python object to JSON string.

```python
import json
data = {"name": "Emperor", "age": 18}
with open("user.json", "w") as f:
    json.dump(data, f, indent=2)
```

---

## L40 – pathlib – Modern File Paths
- `Path("file.txt")` creates a path object.
- `.read_text()` / `.write_text()` – simple I/O.
- `.exists()`, `.is_file()`, `.is_dir()` – check properties.
- `.glob("*.py")` – find files; `.mkdir(exist_ok=True)` – create directories.

```python
from pathlib import Path
p = Path("config.json")
if p.exists():
    print(p.read_text())
```

---

*Quick Test:*  
- How to read a file line‑by‑line without loading it all into memory?  
- What happens if you open a file in `'w'` mode and it already exists?  
- How to write a list of dictionaries to a CSV?  
- Difference between `json.load()` and `json.loads()`?