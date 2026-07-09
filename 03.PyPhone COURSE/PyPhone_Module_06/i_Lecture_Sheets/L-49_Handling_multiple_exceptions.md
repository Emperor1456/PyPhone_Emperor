# 📘 PyPhone Emperor · Module 6  
# 📖 L‑49 – Handling Multiple Exceptions (Robust Error Recovery)

---

## 🎯 OBJECTIVE  
Master handling different error types in a single `try` block.  
Use multiple `except` clauses and tuple grouping to create precise recovery paths for each possible failure.

---

## 🧱 BRICK 1 – Multiple `except` Blocks

List distinct `except` blocks for different exceptions; Python checks them top‑to‑bottom, running the first match.

**① Catch ValueError (Easy practice)**
```python
try:
    int('abc')
except ValueError:
    print('ValueError')
```
Output: `ValueError`.

**② Catch TypeError (Medium practice)**
```python
try:
    len(5)
except TypeError:
    print('TypeError')
```
Output: `TypeError`.

**③ Choose between ZeroDivisionError and ValueError (Hard practice)**
```python
try:
    5 / 0
except ZeroDivisionError:
    print('ZeroDivisionError')
except ValueError:
    print('ValueError')
```
Only `ZeroDivisionError` fires; print `ZeroDivisionError`.

> 💡 **INSIGHT:** Order matters — place more specific exceptions before more general ones (e.g., `FileNotFoundError` before `OSError`).

---

## 🧱 BRICK 2 – Grouping Exceptions and Advanced Handling

**④ Group exceptions with a tuple**
```python
try:
    d = {'name': 'Emperor'}
    print(d['age'])
except (KeyError, TypeError) as e:
    print(f"Data error: {e}")
```

**⑤ Broad fallback after specific catches**
```python
try:
    risky_operation()
except FileNotFoundError:
    print("File missing")
except PermissionError:
    print("Permission denied")
except Exception:
    print("Something else went wrong")
```

> ⚠️ **WARNING:** Never put a bare `except` or `except Exception` before more specific handlers — it will swallow all errors.

> 💡 **ADVANCED TIP – `raise` from:**  
> Use `raise ... from e` to chain exceptions for better debugging.

---

## 💡 Real‑world Usage

**Banking – handle withdrawal errors**
```python
try:
    amount = int(input("Amount: "))
    if amount > balance:
        raise ValueError("Insufficient funds")
except ValueError as e:
    print(e)
except Exception:
    print("Unexpected error")
```

**E‑commerce – process order file**
```python
try:
    with open('orders.txt', 'r') as f:
        orders = f.readlines()
except FileNotFoundError:
    print("No orders today")
except PermissionError:
    print("Cannot access order file")
```

**Logistics – parse delivery data**
```python
try:
    weight = float(data['weight'])
except KeyError:
    weight = 0
except ValueError:
    weight = 0
```

**HR – multiple input validations**
```python
try:
    age = int(input("Age: "))
    name = employees[age]   # might be KeyError
except ValueError:
    print("Age not number")
except KeyError:
    print("No employee at that index")
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Try `int('abc')`, catch `ValueError` and print `'ValueError'`. | `ValueError` |
| Medium | Try `len(5)`, catch `TypeError` and print `'TypeError'`. | `TypeError` |
| Hard   | Try `5/0`, catch both `ZeroDivisionError` and `ValueError`; print the exception type name that was caught. | `ZeroDivisionError` |

Run the coach:
```bash
python ii_Practice_Sheets/L-49_Multiple_Exceptions.py
```

---

## 📌 Key Takeaway
- Multiple `except` blocks allow distinct handling for different errors.
- Use tuples to group exceptions with common handling.
- Order handlers from specific to general to avoid masking.
- Robust error handling is critical for reliable business software.