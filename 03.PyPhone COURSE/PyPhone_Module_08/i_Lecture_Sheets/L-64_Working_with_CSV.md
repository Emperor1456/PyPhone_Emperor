# 📘 PyPhone Emperor · Module 8  
# 📖 L‑64 – Working with CSV Files (`csv` module) – Tabular Data Exchange

---

## 🎯 OBJECTIVE  
Master Python’s built‑in `csv` module to read and write CSV files — the universal format for spreadsheets, database exports, and business reports.  
Use `csv.reader` for simple row lists and `csv.DictReader` for header‑based access. Write data with `csv.writer` and `csv.DictWriter`.

---

## 🧱 BRICK 1 – Reading CSV Files

**① Read all rows into a list (Easy practice)**
```python
import csv

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

print(rows)
# [['name', 'age'], ['Alice', '30'], ['Bob', '25']]
```
The first row is often the header; subsequent rows are data. The Easy task returns this list of rows.

**② Read as dictionaries with DictReader (Medium practice)**
```python
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    dict_rows = list(reader)

print(dict_rows)
# [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]
```
`DictReader` treats the first row as column names, making each row a dictionary. This is perfect for business data with many fields.

**③ Iterating directly (memory‑efficient)**
```python
with open('data.csv', 'r') as f:
    for row in csv.reader(f):
        print(row)
```

> 💡 **INSIGHT:** Always use `newline=''` when writing CSV files to avoid extra blank lines on Windows. For reading, the default is fine.

---

## 🧱 BRICK 2 – Writing CSV Files

**④ Write a simple CSV (Hard practice)**
```python
import csv

with open('out.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age'])
    writer.writerow(['Emperor', '18'])

# Read back the written content
with open('out.csv', 'r') as f:
    content = f.read().strip()
print(content)
# name,age
# Emperor,18
```
The Hard task writes a header and a data row, then prints the file content exactly as it appears.

**⑤ Write dictionaries with DictWriter**
```python
with open('users.csv', 'w', newline='') as f:
    fieldnames = ['name', 'age']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'Emperor', 'age': 18})
```

**⑥ Custom delimiters and quoting**
```python
with open('pipe.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['name', 'age'])
    writer.writerow(['Emperor', 18])
```

> ⚠️ **WARNING:** Always open CSV files with `newline=''` when writing; otherwise you may get double‑spaced lines.

> 💡 **ADVANCED TIP:** For large datasets, iterate over `reader` directly instead of loading everything into a list.

---

## 💡 Real‑world Usage

**Banking – export transaction history**
```python
transactions = [('A1', 500), ('A2', -200)]
with open('tx.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['account', 'amount'])
    writer.writerows(transactions)
```

**E‑commerce – import product catalog**
```python
with open('products.csv', 'r') as f:
    reader = csv.DictReader(f)
    for product in reader:
        print(f"{product['name']}: ${product['price']}")
```

**Logistics – delivery manifest**
```python
with open('manifest.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        print(f"Package {row[0]} to {row[1]}")
```

**HR – employee directory export**
```python
employees = [{'id': 101, 'name': 'Emperor'}, {'id': 102, 'name': 'Rahim'}]
with open('staff.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['id', 'name'])
    writer.writeheader()
    writer.writerows(employees)
```

---

## 🔍 Practice Preview
The engine creates `data.csv` with two data rows (`Alice,30` and `Bob,25`) plus a header.

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Read `data.csv` into a list of rows using `csv.reader`. Print the rows. | `[['name', 'age'], ['Alice', '30'], ['Bob', '25']]` |
| Medium | Read the same CSV using `csv.DictReader` and print the list of dicts. | `[{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]` |
| Hard   | Write a CSV file `out.csv` with header `name,age` and one row `Emperor,18`. Then read and print its content. | `name,age`<br>`Emperor,18` |

Run the coach:
```bash
python ii_Practice_Sheets/L-64_CSV_Files.py
```

---

## 📌 Key Takeaway
- `csv.reader(file)` → list of lists; `csv.DictReader(file)` → list of dicts.
- `csv.writer(file)` writes lists; `csv.DictWriter(file, fieldnames)` writes dicts.
- Always open files with `newline=''` when writing.
- CSV is the universal lightweight format for tabular business data.