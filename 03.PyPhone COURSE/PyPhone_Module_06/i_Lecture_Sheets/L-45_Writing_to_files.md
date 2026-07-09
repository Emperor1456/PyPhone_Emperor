# 📘 PyPhone Emperor · Module 6  
# 📖 L‑45 – Writing to Files (Saving Business Results)

---

## 🎯 OBJECTIVE  
Master writing data to files with `'w'` mode.  
Create new files, overwrite existing ones, and save reports, logs, and user‑generated data persistently.

---

## 🧱 BRICK 1 – Opening and Writing a Single String

Open with `'w'` (write mode). It creates the file if missing, or **erases** existing content.

```python
with open('output.txt', 'w') as f:
    f.write('Emperor')
```

**① Write a simple value (Easy practice)**
```python
with open('output.txt', 'w') as f:
    f.write('Emperor')
# Read back to verify (engine does this)
# prints 'Emperor'
```
The file now contains exactly the string `'Emperor'`.

**② Overwrite with new content (Medium practice)**
```python
with open('output.txt', 'w') as f:
    f.write('PyPhone')
# Content now is 'PyPhone', replacing previous data
```
Writing again with `'w'` completely replaces the old content.

**③ Write multiple values as comma‑separated (Hard practice)**
```python
nums = [1, 2, 3]
with open('numbers.txt', 'w') as f:
    f.write(','.join(map(str, nums)))
# Content: '1,2,3'
```
Use `str.join()` to combine list elements, and `map(str, ...)` to convert integers to strings.

> 💡 **INSIGHT:** `'w'` mode is destructive; use it when you want a fresh file every time. For appending, use `'a'`.

---

## 🧱 BRICK 2 – Writing Multiple Lines and Reports

Use `.writelines()` for a list of strings, or multiple `.write()` calls.

```python
lines = ['First line\n', 'Second line\n']
with open('report.txt', 'w') as f:
    f.writelines(lines)
```

**Generate a sales report**
```python
sales = {'Jan': 4500, 'Feb': 5200}
with open('sales.csv', 'w') as f:
    f.write('Month,Sales\n')
    for month, amount in sales.items():
        f.write(f'{month},{amount}\n')
```

**Save user settings**
```python
settings = {'theme': 'dark', 'lang': 'en'}
with open('config.txt', 'w') as f:
    for k, v in settings.items():
        f.write(f'{k}={v}\n')
```

> ⚠️ **WARNING:** `'w'` erases the file immediately upon opening. If you need to keep old data, use append mode `'a'`.

> 💡 **ADVANCED TIP – `print()` to file:**  
> `print('Hello', file=f)` writes a line with automatic newline, often cleaner than `f.write()`.

---

## 💡 Real‑world Usage

**Banking – save transaction summary**
```python
with open('summary.txt', 'w') as f:
    f.write('Account: A123\nBalance: 5000\n')
```

**E‑commerce – generate order confirmation**
```python
order = {'id': 'ORD-1', 'item': 'Mouse', 'qty': 2}
with open('confirmation.txt', 'w') as f:
    f.write(f"Order {order['id']}: {order['qty']} x {order['item']}")
```

**Logistics – create shipping label**
```python
with open('label.txt', 'w') as f:
    f.write('To: Emperor\nAddress: Dhaka\nParcel: 2kg')
```

**HR – export employee list**
```python
staff = ['Emperor', 'Rahim', 'Karim']
with open('staff.txt', 'w') as f:
    f.write('\n'.join(staff))
```

---

## 🔍 Practice Preview
You will write to files using `'w'` mode. The engine may read back the file to verify output.

| Level  | Task | Expected Output (file content) |
|--------|------|-------------------------------|
| Easy   | Write `'Emperor'` to a file named `output.txt`. | `Emperor` |
| Medium | Overwrite `output.txt` with `'PyPhone'`. | `PyPhone` |
| Hard   | Write list `[1,2,3]` to `numbers.txt` as comma‑separated values, then print the file content. | `1,2,3` |

Run the coach:
```bash
python ii_Practice_Sheets/L-45_Writing_to_Files.py
```

---

## 📌 Key Takeaway
- `open('file', 'w')` creates/overwrites a file for writing.
- `.write(str)` writes a string; `.writelines(list)` writes multiple.
- Use `'w'` for fresh output, `'a'` to append.
- Always close with `with open(...)` to ensure data is flushed to disk.