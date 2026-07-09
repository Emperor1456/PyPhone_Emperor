# 📘 PyPhone Emperor · Module 8  
# 📖 L‑62 – Error Handling Best Practices (Robust Business Applications)

---

## 🎯 OBJECTIVE  
Master error‑handling best practices: catch only expected exceptions, keep `try` blocks small, use `else` for success‑only logic, and always log errors.  
Robust error handling is the mark of production‑ready code — critical for banking transactions, order processing, and data pipelines.

---

## 🧱 BRICK 1 – Specific Catching and Small `try` Blocks

**① Catch FileNotFoundError specifically (Easy practice)**
```python
try:
    open('nofile.txt')
except FileNotFoundError:
    print('file missing')
```
Output: `file missing`. Only that specific error triggers the handler.

**② Catch ValueError (Medium practice)**
```python
try:
    int('abc')
except ValueError:
    print('value error')
```
Output: `value error`. A different error would still crash — which is good, because unexpected errors should be visible.

**③ Combining blocks (Hard practice preview)**
```python
try:
    print('try')         # safe operation
except:
    pass
else:
    print('else')        # runs on success
finally:
    print('finally')     # runs always
```
Output:
```
try
else
finally
```
Because no exception occurred, `except` is skipped, `else` runs, and `finally` always runs. This is the Hard practice output.

> 💡 **INSIGHT:** Keep `try` blocks focused on the single statement that might fail. This prevents accidentally catching exceptions from unrelated code.

---

## 🧱 BRICK 2 – The Golden Rules

**④ Never use bare `except:`**
A bare `except:` catches `KeyboardInterrupt` and `SystemExit`, making the program unstoppable. Always specify at least `except Exception`.

**⑤ Log errors instead of silencing them**
```python
import logging
try:
    risky_operation()
except Exception as e:
    logging.exception("Operation failed")   # logs full traceback
    # optionally re‑raise or handle
```

**⑥ Use `else` for logic that depends on success**
```python
try:
    file = open('data.txt', 'r')
except FileNotFoundError:
    print('File not found')
else:
    content = file.read()   # safe to read
    process(content)
finally:
    if 'file' in locals():
        file.close()
```

**⑦ Never use exceptions for normal flow control**
```python
# BAD
try:
    value = dict[key]
except KeyError:
    value = default

# GOOD
value = dict.get(key, default)
```

> ⚠️ **WARNING:** Exception handling is slower than condition checks. Use `if`/`else` for expected situations, `try`/`except` for truly exceptional ones.

> 💡 **ADVANCED TIP – Custom exceptions:**  
> Define your own exception classes for business‑specific errors, e.g., `InsufficientFundsError`, to make error handling expressive and maintainable.

---

## 💡 Real‑world Usage

**Banking – safe withdrawal**
```python
def withdraw(account, amount):
    try:
        if amount > account.balance:
            raise ValueError('Insufficient funds')
        account.balance -= amount
    except ValueError as e:
        print(e)
        return False
    else:
        return True
    finally:
        print('Transaction attempt ended')
```

**E‑commerce – load product catalog**
```python
try:
    with open('products.json', 'r') as f:
        catalog = json.load(f)
except FileNotFoundError:
    print('Catalog not found, using defaults')
    catalog = []
except json.JSONDecodeError:
    print('Invalid catalog format')
```

**Logistics – process shipment list**
```python
for tracking_id in ids:
    try:
        status = lookup_status(tracking_id)
    except LookupError:
        print(f"Failed for {tracking_id}, skipping")
        continue
    print(f"{tracking_id}: {status}")
```

**HR – import employee data**
```python
try:
    with open('employees.csv', 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
except FileNotFoundError:
    print('No employee file yet')
    data = []
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Open a non‑existent file, catch `FileNotFoundError` and print `'file missing'`. | `file missing` |
| Medium | Try to convert `'abc'` to int, catch `ValueError` and print `'value error'`. | `value error` |
| Hard   | Combine `try`/`except`/`else`/`finally` with a safe operation. Print `'try'`, then `'else'`, then `'finally'` on separate lines by executing appropriate blocks. | `try`<br>`else`<br>`finally` |

Run the coach:
```bash
python ii_Practice_Sheets/L-62_Error_Handling_Best_Practices.py
```

---

## 📌 Key Takeaway
- Catch specific exceptions; avoid bare `except`.
- Keep `try` blocks as small as possible.
- Use `else` for success‑only logic and `finally` for cleanup.
- Log errors; never silently swallow them.
- Prefer conditionals over exceptions for normal flow.