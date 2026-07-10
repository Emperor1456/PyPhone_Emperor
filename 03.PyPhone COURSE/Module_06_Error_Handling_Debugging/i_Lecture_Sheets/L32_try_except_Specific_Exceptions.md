# 📘 PyPhone Emperor v3.0 · Module 6
# 📖 L‑32 – `try`/`except` – Catching Specific Exceptions

---

## 🎯 OBJECTIVE — What You Will Master

> Prevent crashes and handle errors gracefully.

- 🛡️ **`try` block** – wrap code that might fail
- 🎯 **`except SpecificError`** – catch only what you expect
- 🧪 **`as e`** – capture the error object for logging
- 🚫 **Avoid bare `except`** – it hides bugs

---

## 🧱 BASIC STRUCTURE

```python
try:
    num = int(input("Number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid number.")
```

---

## 🧱 COMMON EXCEPTIONS

| Exception | Cause |
|-----------|-------|
| `ValueError` | Invalid type conversion |
| `ZeroDivisionError` | Division by zero |
| `FileNotFoundError` | Missing file |
| `KeyError` | Missing dictionary key |
| `IndexError` | List index out of range |

---

## 💡 Real‑world Usage

**Banking – safe withdrawal**
```python
try:
    amount = float(input("Amount: "))
except ValueError:
    print("Invalid amount")
```

**E‑commerce – open product file**
```python
try:
    with open("products.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("Catalog missing")
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Catch `ValueError` when converting "abc" to int; print "error". |
| Medium | Catch `ZeroDivisionError` on `10/0`; print "caught". |
| Hard | Catch `FileNotFoundError` when opening missing file; print "missing". |

Run the coach:
```bash
python ii_Practice_Sheets/L32_try_except_Specific_Exceptions.py
```

---

## 📌 Key Takeaway
- Use `try`/`except` to handle expected errors.
- Catch specific exceptions; never bare `except:`.
- Production code must not crash on predictable failures.

*For Emperor.*