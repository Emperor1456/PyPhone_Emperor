# 📘 PyPhone Emperor · Module 6
# 📖 L‑49 – Handling Multiple Exceptions

---

## 🎯 OBJECTIVE
Learn to write robust code that gracefully handles
different kinds of errors in a single `try` block.
Master ordering of `except` clauses and how to handle
multiple exceptions with a single handler.

---

## 🧱 BRICK 1 – Multiple `except` Blocks

A `try` block can be followed by several `except` blocks,
each targeting a different exception type.
Python checks them **top to bottom** — the first match wins.

```python
try:
    num = int(input("Number: "))
    result = 100 / num
    print("Result:", result)
except ValueError:
    print("That's not a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

- If the user types `"abc"`, `ValueError` fires.
- If the user types `0`, `ZeroDivisionError` fires.
- Each error gets its own recovery path.

---

## 🧱 BRICK 2 – Catching Multiple Exceptions Together

You can group exceptions in a tuple if they share
the same handling logic.

```python
try:
    data = {"name": "Emperor"}
    print(data["age"])
except (KeyError, TypeError) as e:
    print(f"Data access error: {e}")
```

**Ordering rule:**
More specific exceptions must come **before** more
general ones. If you put `except Exception` first,
no other handler will ever run.

```python
# CORRECT ORDER
try:
    risky_call()
except FileNotFoundError:
    print("File missing.")
except Exception:
    print("Something else went wrong.")
```

> ⚠️ **WARNING:** Reversing the order (`Exception` first)
> silently swallows all errors and hides real bugs.

---

## 📌 Key Takeaway
- Multiple `except` blocks handle different errors.
- Python matches the first fitting clause.
- Use tuples `(Error1, Error2)` for shared handling.
- Order from most specific to least specific.