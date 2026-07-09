# 📘 PyPhone Emperor · Module 6  
# 📖 L‑48 – Introduction to Exceptions (`try`, `except`) – Safe Error Handling

---

## 🎯 OBJECTIVE  
Master the `try`/`except` block to catch runtime errors and prevent crashes.  
Handle invalid user input, missing files, and division by zero gracefully.  
This is the hallmark of production‑ready software.

---

## 🧱 BRICK 1 – Catching Specific Exceptions

Place risky code inside a `try` block. If the specified exception occurs, the matching `except` block runs.

```python
try:
    # code that may fail
    int('abc')
except ValueError:
    print('error')
```

**① Catch a type conversion error (Easy practice)**
```python
try:
    int('abc')
except ValueError:
    print('error')
```
Output: `error` — the program continues without crashing.

**② Catch a division by zero (Medium practice)**
```python
try:
    10 / 0
except ZeroDivisionError:
    print('caught')
```
Output: `caught`.

**③ Catch a missing file (Hard practice)**
```python
try:
    open('nofile.txt')
except FileNotFoundError:
    print('missing')
```
Output: `missing`.

> 💡 **INSIGHT:** Always catch the most specific exception possible. This makes debugging easier and avoids masking unexpected errors.

---

## 🧱 BRICK 2 – Getting the Error Message and Universal Catch

**④ Inspect the exception object**
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
```

**⑤ Broad catch for logging (use sparingly)**
```python
try:
    risky_call()
except Exception as e:
    print(f"Something went wrong: {e}")
```
`Exception` covers almost all built‑in errors.

> ⚠️ **WARNING:** Never use a bare `except:` — it catches `KeyboardInterrupt` and `SystemExit`, making your program unstoppable.

> 💡 **ADVANCED TIP – Multiple `except` blocks:**  
> You can chain several `except` clauses to handle different errors differently.

---

## 💡 Real‑world Usage

**Banking – safe user input for amount**
```python
try:
    amount = float(input("Enter amount: "))
except ValueError:
    print("Invalid number.")
else:
    print("Processing...")
```

**E‑commerce – opening a product file**
```python
try:
    with open('products.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("Product list not found.")
```

**Logistics – parse a weight from a string**
```python
try:
    weight = float('12.5kg')   # will fail
except ValueError:
    weight = 0.0
```

**HR – reading employee data with fallback**
```python
try:
    with open('employees.txt', 'r') as f:
        staff = f.readlines()
except FileNotFoundError:
    staff = []
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Try to convert `'abc'` to int, catch `ValueError` and print `'error'`. | `error` |
| Medium | Divide 10 by 0, catch `ZeroDivisionError` and print `'caught'`. | `caught` |
| Hard   | Open a non‑existent file, catch `FileNotFoundError` and print `'missing'`. | `missing` |

Run the coach:
```bash
python ii_Practice_Sheets/L-48_Exceptions_intro.py
```

---

## 📌 Key Takeaway
- `try`/`except` prevents crashes from anticipated errors.
- Catch specific exceptions (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`).
- Use `as e` to get error details.
- Always handle errors gracefully in business‑critical applications.