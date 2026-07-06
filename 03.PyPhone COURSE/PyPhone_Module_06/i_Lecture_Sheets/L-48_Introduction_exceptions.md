# 📘 PyPhone Emperor · Module 6
# 📖 L‑48 – Introduction to Exceptions (`try`, `except`)

---

## 🎯 OBJECTIVE
Learn to handle errors gracefully using **exceptions**.
Instead of crashing, your program can catch errors
with `try`/`except` and take corrective action —
an essential trait of production‑grade software.

---

## 🧱 BRICK 1 – The `try`/`except` Block

Dangerous code goes inside `try`.  
If an error occurs, the matching `except` block runs.

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("That's not a valid number.")
```

- `ZeroDivisionError` is caught only when division fails.
- `ValueError` is caught only when `int()` fails.
- If no error occurs, neither `except` block runs.

> 💡 **INSIGHT:** Always catch **specific** exceptions.
> A bare `except:` hides bugs and makes debugging hard.

---

## 🧱 BRICK 2 – Getting the Error Message

You can capture the exception object to inspect the
problem or log it.

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
```

**Universal fallback (use sparingly):**
```python
try:
    risky_operation()
except Exception as e:
    print(f"Unexpected error: {e}")
```

`Exception` is the base class for most built‑in errors.
It will catch almost everything except system‑exiting
events like `KeyboardInterrupt`.

> ⚠️ **WARNING:** Never use `except:` without a type —
> it catches even `SystemExit` and `KeyboardInterrupt`,
> making your program un‑stoppable.

---

## 📌 Key Takeaway
- `try` / `except` prevents crashes.
- Catch specific errors: `ValueError`, `ZeroDivisionError`, etc.
- `as e` captures the error object for logging.
- Use `except Exception` as a broad safety net, not a blanket.