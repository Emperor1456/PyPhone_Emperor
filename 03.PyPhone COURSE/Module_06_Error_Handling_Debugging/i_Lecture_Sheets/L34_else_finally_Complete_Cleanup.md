# 📘 PyPhone Emperor v3.0 · Module 6
# 📖 L‑34 – `else`, `finally` & Complete Cleanup Pattern

---

## 🎯 OBJECTIVE — What You Will Master

> The full safety net: success‑only logic and guaranteed cleanup.

- ✅ **`else`** – runs only if `try` succeeded without exception
- 🧹 **`finally`** – runs always, even after `return` or exception
- 🔐 **Complete pattern** – `try` → `except` → `else` → `finally`
- 🧪 **Use cases** – resource cleanup, file closing, state resets

---

## 🧱 THE FULL STRUCTURE

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None
    else:
        print("Division successful.")
        return result
    finally:
        print("Operation complete.")
```

---

## 🧱 WHY `finally`?

Even if the `try` block contains a `return`, the `finally` block **still** executes.

```python
def demo():
    try:
        return "inside try"
    finally:
        print("finally block")
print(demo())   # prints "finally block", then "inside try"
```

> ⚠️ **WARNING:** Avoid `return` inside `finally` – it overrides the original return or exception.

---

## 💡 Real‑world Usage

**Banking – transaction with audit**
```python
try:
    process_payment()
except PaymentError:
    log("failed")
else:
    log("success")
finally:
    close_connection()
```

**E‑commerce – file processing**
```python
f = open("orders.txt")
try:
    process(f)
finally:
    f.close()
```

**Logistics – cleanup temporary files**
```python
try:
    generate_report()
except:
    print("Error")
finally:
    delete_temp_files()
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Use `try`/`finally` to print "cleanup". |
| Medium | Use `try`/`except`/`else` to print "else" on success. |
| Hard | Combine all four clauses with a deliberate error; ensure "finally" prints last. |

Run the coach:
```bash
python ii_Practice_Sheets/L34_else_finally_Complete_Cleanup.py
```

---

## 📌 Key Takeaway
- `else` isolates success‑only code.
- `finally` guarantees cleanup.
- The order: `try` → `except` → `else` → `finally`.

*For Emperor.*