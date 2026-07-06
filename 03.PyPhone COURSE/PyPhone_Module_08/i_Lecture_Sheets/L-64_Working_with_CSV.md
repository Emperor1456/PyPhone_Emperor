# 📘 PyPhone Emperor · Module 8
# 📖 L‑64 – Working with CSV Files (`csv` module)

---

## 🎯 OBJECTIVE
Learn to read and write CSV (Comma‑Separated Values)
files using Python’s built‑in `csv` module. CSV is the
universal format for spreadsheet data, database exports,
and tabular data exchange. You’ll master both basic
and advanced usage patterns.

---

## 🧱 BRICK 1 – Reading CSV Files

The `csv.reader()` function parses a file line by line,
returning each row as a list of strings.

```python
import csv

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)   # row is a list
```

**Example `data.csv`:**
```
Name,Age,City
Emperor,18,Dhaka
Guest,25,London
```

**Reading with headers – `DictReader`:**
```python
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["Age"])
```
`DictReader` uses the first row as column names,
returning each row as an `OrderedDict` (or dict).

> 💡 **INSIGHT:** `csv.reader` is great for simple data;
> `DictReader` is preferred for datasets with many columns.

---

## 🧱 BRICK 2 – Writing CSV Files

`csv.writer()` writes lists as rows.

```python
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Emperor", 18, "Dhaka"])
```

**Writing dictionaries – `DictWriter`:**
```python
with open("users.csv", "w", newline="") as f:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name": "Emperor", "Age": 18, "City": "Dhaka"})
```

### Customising delimiters and quoting:
```python
import csv

with open("pipe_data.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter="|", quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Emperor", 18])
```

- `delimiter` changes the field separator (e.g., `|`, `;`, tab `\t`).
- `quoting` controls when quotes are added: `csv.QUOTE_ALL`, `QUOTE_MINIMAL`, `QUOTE_NONNUMERIC`.

> ⚠️ **WARNING:** Always open files with `newline=""` when
> using `csv.writer` – this prevents extra blank lines on
> some systems.

---

## 📌 Key Takeaway
- `csv.reader` returns rows as lists; `csv.DictReader` uses header names.
- `csv.writer` writes lists; `csv.DictWriter` writes dicts.
- Always use `newline=""` when opening CSV files for writing.
- The `csv` module handles quoting and delimiters cleanly.