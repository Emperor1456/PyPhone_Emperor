# 📘 Module 06 – Error Handling & Debugging · Revision Guide

---

## L32 – try/except – Catching Specific Exceptions

- Wrap risky code in `try`, handle errors in `except`.
- Catch specific exceptions (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`).
- Use `as e` to capture the error object.

```python
try:
    num = int(input("Number: "))
except ValueError:
    print("Invalid number")
```

---

## L33 – raise, Custom Exceptions & Chaining

- `raise ValueError("message")` throws an exception manually.
- Define custom exceptions: `class MyError(Exception): pass`.
- Chain exceptions: `raise RuntimeError("wrapped") from e`.

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
```

---

## L34 – else, finally & Complete Cleanup

- `else` runs only if no exception occurred.
- `finally` runs always (cleanup).
- Order: `try` → `except` → `else` → `finally`.

```python
try:
    f = open("data.txt")
except FileNotFoundError:
    print("Missing")
finally:
    f.close()
```

---

## L35 – Debugging with pdb & Logging

- `import pdb; pdb.set_trace()` pauses execution for inspection.
- `logging` module provides leveled messages.
- Use `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.

```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Application started")
```

---

**Quick Test:**  
- Why should you never use a bare `except:` clause?  
- What is the difference between `else` and `finally` in error handling?  
- How do you throw a custom exception?  
- What is the purpose of the `logging` module?

*Review complete. You are now ready for the Module 06 Practice Review.*