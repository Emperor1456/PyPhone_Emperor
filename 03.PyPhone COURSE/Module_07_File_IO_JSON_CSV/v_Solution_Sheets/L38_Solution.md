# L38 Solution – CSV Files

## 🟢 Easy 1 – Read CSV with csv.reader
```python
import csv
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)
print(rows)
```

## 🟢 Easy 2 – Read CSV with DictReader
```python
import csv
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    dict_rows = list(reader)
print(dict_rows)
```

## 🟡 Medium 1 – Write CSV with csv.writer
```python
import csv
with open('out.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age'])
    writer.writerow(['Emperor', '18'])
print(open('out.csv').read().strip())
```

## 🟡 Medium 2 – Write CSV with DictWriter
```python
import csv
with open('dict_out.csv', 'w', newline='') as f:
    fieldnames = ['name', 'age']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'Emperor', 'age': '18'})
print(open('dict_out.csv').read().strip())
```

## 🔴 Hard 1 – Sum a CSV Column
```python
import csv
total = 0
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        total += int(row['age'])
print(total)
```

## 🔴 Hard 2 – Filter CSV Rows
```python
import csv
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row['age']) > 28:
            print(row)
```