# 📘 Module 01 – Python Core · Revision Guide

---

## L01 – Variables, Memory & Dynamic Typing

- Variables are **name tags** attached to objects in memory.
- Assignment (`=`) never copies data; it binds a name.
- Python is dynamically typed: types live on objects, not names.
- `is` checks identity (same object); `==` checks value equality.
- Small integers (-5 to 256) are cached – `is` can be `True` for them.
- Naming: `snake_case` for variables, `UPPER_CASE` for constants.

```python
a = 100; b = 100
print(a is b)        # True (cached)
c = 300; d = 300
print(c is d)        # False (different objects)
```

---

## L02 – Numeric Types, Operators & Casting

- `int` (unlimited), `float` (64‑bit), `complex`.
- `+`, `-`, `*`, `/` (always float), `//` (floor), `%` (mod), `**` (power).
- Type casting: `int("42")`, `float("3.14")`, `str(100)`.
- Operator precedence: PEMDAS (Parentheses, Exponent, Mult/Div, Add/Sub).
- `int(3.9)` truncates, doesn’t round.

```python
print(10 / 3)         # 3.3333333333333335
print(10 // 3)        # 3
print(10 % 3)         # 1
print(int("  15  "))  # 15
```

---

## L03 – Strings: Indexing, Slicing & Immutability

- Strings are **immutable** sequences of Unicode characters.
- Positive index from left (0), negative from right (-1).
- Slicing: `[start:stop:step]`, `start` inclusive, `stop` exclusive.
- `[::-1]` reverses a string.
- Slicing never raises `IndexError`; out‑of‑range returns empty string.

```python
s = "Emperor"
print(s[0])      # E
print(s[-1])     # r
print(s[1:4])    # mpe
print(s[::-1])   # rorepmE
```

---

## L04 – String Methods & f‑strings

- `.strip()`, `.lstrip()`, `.rstrip()` remove whitespace.
- `.find(sub)`, `.count(sub)`, `.startswith()`, `.endswith()`.
- `.split(sep)`, `.join(iterable)`, `.replace(old, new)`.
- `.upper()`, `.lower()`, `.title()`.
- f‑strings: `f"{var}"`; format with `:.2f`, `:>10`, etc.

```python
raw = "   Emperor   "
print(raw.strip())                     # Emperor
print("apple,banana".split(","))       # ['apple', 'banana']
print(f"Total: ${24.99*3:.2f}")       # Total: $74.97
```

---

## L05 – User Input, CLI Arguments & `sys.argv`

- `input(prompt)` returns a string – cast to needed type.
- `sys.argv` is a list of command‑line arguments (script name at index 0).
- Always check `len(sys.argv)` before accessing indices.

```python
import sys
if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = input("Name: ")
print(f"Hello, {name}!")
```

---

## L06 – Boolean Logic, Truthiness & `is` vs `==`

- `True` / `False` from comparisons (`>`, `<`, `==`, `!=`).
- **Falsy values:** `None`, `False`, `0`, `0.0`, `""`, `[]`, `{}`, `()`, `set()`.
- `and`, `or`, `not`; short‑circuit evaluation.
- `==` compares values; `is` compares identity.
- Always use `is None` (never `== None`).

```python
print(bool([]))          # False
print(10 > 5 and 3 < 1)  # False
a = [1,2]; b = [1,2]
print(a == b, a is b)    # True False
```

---

## L07 – `None`, Optional Typing & Sentinel Values

- `None` is the singleton for “no value”.
- Use `is None` and `is not None` to check.
- Type hint: `Optional[int]` = `int` or `None`.
- Sentinel pattern: use `None` as default instead of mutable objects.

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

**Quick Test:**  
- What does `type(42)` return?  
- How do you reverse a string?  
- What is the difference between `10 / 3` and `10 // 3`?  
- What happens if you try to modify a string in place?  
- What does `sys.argv[0]` contain?

*Review complete. You are now ready for the Module 01 Practice Review.*