# 📘 PyPhone Emperor · Module 8  
# 📖 L‑63 – `try-except-else-finally` Review (Complete Error Handling Pattern)

---

## 🎯 OBJECTIVE  
Solidify the complete exception‑handling structure. Master the exact execution order of `try`, `except`, `else`, and `finally`.  
Use these blocks to separate risky code from error handling, success logic, and mandatory cleanup — essential for bullet‑proof business applications.

---

## 🧱 BRICK 1 – The Four‑Block Pattern

The full structure executes in strict order:
1. `try` — the risky code.
2. `except` — runs only if a matching exception occurs.
3. `else` — runs only if no exception occurred.
4. `finally` — runs always, regardless of exceptions or returns.

**① Deliberate error (Easy practice)**
```python
try:
    1 / 0
except:
    print('except')
finally:
    print('finally')
```
Output:
```
except
finally
```
`1 / 0` raises `ZeroDivisionError`, so `except` fires, `else` is skipped, `finally` still runs.

**② Success case – `else` runs (Medium practice)**
```python
try:
    x = 1
except:
    pass
else:
    print('else')
```
Output: `else`. No exception, so `except` is skipped and `else` prints.

**③ Complete safe division (Hard practice)**
```python
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'error'

print(safe_div(10, 2))   # 5.0
print(safe_div(10, 0))   # error
```
The function uses `try`/`except` internally; the caller gets either the result or the error string.

> 💡 **INSIGHT:** `else` separates success‑only logic from error‑prone code, reducing the chance of accidentally catching exceptions from non‑risky parts.

---

## 🧱 BRICK 2 – Common Pitfalls and Best Uses

**④ `finally` for resource cleanup**
```python
f = None
try:
    f = open('data.txt', 'r')
    content = f.read()
except FileNotFoundError:
    print('File missing')
finally:
    if f:
        f.close()
```
Even if `read()` fails, the file handle is closed.

**⑤ Avoid `return` inside `finally`**
A `return` in `finally` overrides the original return or exception, which is usually unintended.

**⑥ `else` in a data pipeline**
```python
try:
    raw = fetch_data()
except ConnectionError:
    print('Could not connect')
else:
    processed = transform(raw)   # only runs if fetch succeeded
    save(processed)
```

> ⚠️ **WARNING:** Don’t put cleanup in `else` — cleanup goes in `finally` so it always runs.

> 💡 **ADVANCED TIP:** Use `with` statements for file handling instead of manual `try`/`finally` when possible.

---

## 💡 Real‑world Usage

**Banking – transaction with audit trail**
```python
def transfer(sender, receiver, amount):
    try:
        sender.balance -= amount
        receiver.balance += amount
    except AttributeError:
        print('Invalid account')
    else:
        print('Transfer successful')
    finally:
        audit_log.append(f"Transfer attempted: {amount}")
```

**E‑commerce – order placement**
```python
try:
    inventory.reserve(items)
except OutOfStockError:
    print('Some items unavailable')
else:
    payment.charge(customer, total)
finally:
    print('Order process ended')
```

**Logistics – delivery status update**
```python
try:
    tracking.update_status('delivered')
except TrackingError:
    print('Update failed')
else:
    print('Status updated')
finally:
    connection.close()
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Use `try`/`except`/`else`/`finally` with a deliberate error (`1/0`). Print `'except'` and then `'finally'` on separate lines. | `except`<br>`finally` |
| Medium | Use `try`/`else` without exception: print `'else'`. | `else` |
| Hard   | Implement a safe division function that returns `'error'` on `ZeroDivisionError`, else the result. Call with `10/2` and print the result. | `5.0` |

Run the coach:
```bash
python ii_Practice_Sheets/L-63_try_except_else_finally.py
```

---

## 📌 Key Takeaway
- Order: `try` → `except` (if error) → `else` (if no error) → `finally` (always).
- `else` is for success‑only logic; keeps risky code separate.
- `finally` is for mandatory cleanup (files, locks, connections).
- Never silence exceptions without logging; never return from `finally`.