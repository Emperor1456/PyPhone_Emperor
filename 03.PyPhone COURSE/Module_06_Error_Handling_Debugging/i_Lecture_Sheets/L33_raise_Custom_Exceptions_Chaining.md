# 📘 PyPhone Emperor v3.0 · Module 6
# 📖 L‑33 – `raise`, Custom Exceptions & Exception Chaining

---

## 🎯 OBJECTIVE — What You Will Master

> Signal errors on your own terms.

- 📢 **`raise`** – manually throw an exception
- 🏷️ **Custom exceptions** – define your own error types
- ⛓️ **Exception chaining** – `raise ... from e` to preserve context
- 🧪 **When to use** – validation, business rule violations

---

## 🧱 RAISING EXCEPTIONS

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(f"Age set to {age}")
```

---

## 🧱 CUSTOM EXCEPTIONS

```python
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough money")
    return balance - amount
```

---

## 🧱 EXCEPTION CHAINING

```python
try:
    withdraw(100, 200)
except InsufficientFundsError as e:
    raise RuntimeError("Withdrawal failed") from e
```

---

## 💡 Real‑world Usage

**Banking – validate transaction**
```python
if amount <= 0:
    raise ValueError("Amount must be positive")
```

**E‑commerce – out of stock**
```python
class OutOfStockError(Exception):
    pass
```

**Logistics – invalid tracking**
```python
if not tracking_id.startswith("TRK-"):
    raise ValueError("Bad tracking ID")
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Raise a `ValueError` if a number is negative. |
| Medium | Define a custom exception and raise it. |
| Hard | Catch a custom exception and re‑raise with chaining. |

Run the coach:
```bash
python ii_Practice_Sheets/L33_raise_Custom_Exceptions_Chaining.py
```

---

## 📌 Key Takeaway
- `raise` signals an error condition programmatically.
- Custom exceptions make your code self‑documenting.
- Use chaining to preserve the original error context.

*For Emperor.*