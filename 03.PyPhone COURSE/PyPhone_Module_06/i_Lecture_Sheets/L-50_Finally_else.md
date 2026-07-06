# 📘 PyPhone Emperor · Module 6
# 📖 L‑50 – `finally` & `else` in Exception Blocks

---

## 🎯 OBJECTIVE
Complete your exception‑handling toolkit with two
optional but powerful clauses: `else` (runs only when
no error occurs) and `finally` (runs no matter what).
Together they give you surgical control over cleanup
and success‑only logic.

---

## 🧱 BRICK 1 – `else` – Runs Only on Success

The `else` block executes **only if** the `try` block
completed without raising an exception.
It’s perfect for code that should run exclusively
when everything went right.

```python
try:
    num = int(input("Number: "))
except ValueError:
    print("Invalid number.")
else:
    print(f"You entered {num}.")
```

- If the user types `"abc"`, `except` runs, `else` is skipped.
- If the user types `42`, `except` is skipped, `else` runs.

> 💡 **INSIGHT:** Code in `else` is visually separated from
> the `try` block, making it clearer which part depends
> on success.

---

## 🧱 BRICK 2 – `finally` – Runs No Matter What

The `finally` block executes **always** — whether an
exception occurred or not, and even if you `return`
or `break` inside `try`.

```python
f = None
try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    if f:
        f.close()
    print("Cleanup done.")
```

**Typical uses:**
- Closing files or network connections.
- Releasing locks or resources.
- Resetting temporary states.

You can combine all four: `try` → `except` → `else` → `finally`.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero.")
else:
    print("Result is", result)
finally:
    print("Operation complete.")
```

> ⚠️ **WARNING:** A `return` inside `finally` overrides
> any previous `return` or exception, which can hide bugs.
> Use `finally` only for cleanup, not for changing the
> function’s result.

---

## 📌 Key Takeaway
- `else` runs only when no exception occurs.
- `finally` runs always — ideal for resource cleanup.
- Order: `try` → `except` → `else` → `finally`.
- Keep `finally` focused on cleanup, not logic.