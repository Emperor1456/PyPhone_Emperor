# 📘 PyPhone Emperor · Module 8
# 📖 L‑63 – `try-except-else-finally` Review

---

## 🎯 OBJECTIVE
Solidify your understanding of Python’s complete
exception‑handling structure: `try`, `except`, `else`,
and `finally`. This review cements the exact order of
execution and the purpose of each block, ensuring you
write bullet‑proof, clean error‑handling code.

---

## 🧱 BRICK 1 – The Full Structure and Execution Order

Python executes these blocks in strict sequence:

```
try:
    # ① code that may raise an exception
except SpecificError:
    # ② runs only if SpecificError (or subclass) is raised
else:
    # ③ runs ONLY if try completed without any exception
finally:
    # ④ ALWAYS runs, regardless of exception or return
```

**Example:**
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
        print("Operation finished.")
```

- If `b == 0`: ① raises, ② runs, ③ is skipped, ④ runs.
- If `b != 0`: ① succeeds, ② skipped, ③ runs, ④ runs.

> 💡 **INSIGHT:** `finally` runs even if the `try` block
> contains a `return`, `break`, or `continue`. That’s why
> it’s perfect for closing files and releasing locks.

---

## 🧱 BRICK 2 – Common Pitfalls and Best Uses

### ① Overwriting exceptions in `finally`

A `return` inside `finally` overrides any exception or
previous return value — a subtle bug source.

```python
def demo():
    try:
        raise ValueError("Error!")
    finally:
        return "All good"   # exception is silenced

print(demo())   # "All good" (no error raised)
```

**Rule:** Never use `return` or `break` inside `finally`
unless you have a very specific reason.

### ② Using `else` for clarity

Code that should run **only on success** is safer in `else`
than in `try`, because `else` won’t accidentally catch
exceptions from that code.

```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File missing.")
else:
    content = file.read()   # only runs if file opened
    process(content)
finally:
    if 'file' in locals():
        file.close()
```

### ③ `finally` for cleanup

Always close resources, delete temporary files, or
release locks in `finally`.

```python
import os
tmp_file = "/tmp/temp.txt"
try:
    with open(tmp_file, "w") as f:
        f.write("data")
except IOError:
    print("Write failed.")
finally:
    if os.path.exists(tmp_file):
        os.remove(tmp_file)
```

> ⚠️ **WARNING:** A `finally` block is **not** optional
> when working with external resources. Forgetting it
> can leave files locked or memory leaked.

---

## 📌 Key Takeaway
- Order: `try` → `except` (if error) → `else` (if no error) → `finally` (always).
- Use `else` for success‑only logic, outside the risk zone.
- Use `finally` for mandatory cleanup (files, locks, network).
- Never silence exceptions by returning inside `finally`.