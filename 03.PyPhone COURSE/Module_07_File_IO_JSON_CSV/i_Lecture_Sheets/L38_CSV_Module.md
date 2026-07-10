# 📘 PyPhone Emperor v3.0 · Module 7
# 📖 L‑38 – CSV Files – `csv.reader`, `DictReader`, `csv.writer`

---

## 🎯 OBJECTIVE — What You Will Master

> Handle spreadsheet data with Python’s built‑in `csv` module.

- 📊 `csv.reader` – read rows as lists
- 📇 `csv.DictReader` – read rows as dictionaries (headers from first row)
- ✍️ `csv.writer` – write lists as rows
- 📝 `csv.DictWriter` – write dictionaries using field names
- ⚠️ **Always** use `newline=''` when opening CSV files

---

## 🧱 READING A CSV

```python
import csv
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

---

## 🧱 READING WITH HEADERS

```python
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["Age"])
```

---

## 🧱 WRITING A CSV

```python
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Emperor", 18])
```

---

## 🧱 WRITING DICTIONARIES

```python
with open("users.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Age"])
    writer.writeheader()
    writer.writerow({"Name": "Emperor", "Age": 18})
```

---

## 💡 Real‑world Usage

**Banking – export transaction history**
```python
with open("txns.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows([("deposit", 100), ("withdraw", 50)])
```

**E‑commerce – import product catalog**
```python
with open("products.csv", "r") as f:
    for product in csv.DictReader(f):
        print(product["name"])
```

**Logistics – read delivery manifest**
```python
with open("manifest.csv", "r") as f:
    for row in csv.reader(f):
        print(f"Package {row[0]} to {row[1]}")
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Read a CSV file into a list of rows using `csv.reader`. |
| Medium | Read the same CSV using `DictReader` and print the list of dicts. |
| Hard | Write a CSV with header and one row, then read and print its content. |

Run the coach:
```bash
python ii_Practice_Sheets/L38_CSV_Module.py
```

---

## 📌 Key Takeaway
- `csv.reader`/`writer` for list‑based I/O.
- `csv.DictReader`/`DictWriter` for keyed columns.
- Always open with `newline=''` when writing.

*For Emperor.*