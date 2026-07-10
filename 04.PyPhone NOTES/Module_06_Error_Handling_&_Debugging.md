# 📘 Module 06 – Error Handling & Debugging · Revision Note

---

## L32 – try/except – Catching Specific Exceptions
- `try:` wraps risky code; `except SpecificError:` handles it.
- Catch only what you expect; never use bare `except:`.
- Use `as e` to capture the error object.
- Common: `ValueError`, `ZeroDivisionError`, `FileNotFoundError`.

```python
try:
    num = int(input("Number: "))
except ValueError:
    print("Invalid number")
```

---

## L33 – raise, Custom Exceptions & Chaining
- `raise ValueError("msg")` throws manually.
- Custom exception: `class MyError(Exception): pass`.
- Chaining: `raise RuntimeError("wrapped") from e`.

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
```

---

## L34 – else, finally & Complete Cleanup
- `else` runs only if no exception occurred.
- `finally` runs always – perfect for cleanup.
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
- `import pdb; pdb.set_trace()` pauses execution.
- `logging` module gives leveled output: DEBUG, INFO, WARNING, ERROR, CRITICAL.
- Prefer `logging` over `print()` for production.

```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Application started")
```

---

*Quick Test:*  
- Why never use bare `except:`?  
- Difference between `else` and `finally`?  
- How to throw a custom exception?  
- Purpose of `logging` module?