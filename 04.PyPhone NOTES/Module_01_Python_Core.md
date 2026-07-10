# 📘 Module 01 – Python Core · Revision Note

---

## L01 – Variables, Memory & Dynamic Typing
- Variables are **name tags** attached to objects.
- `=` never copies data; it binds names to objects.
- Types live on objects, not on variable names.
- `type(x)` returns the type; dynamic typing allows reassignment.
- `is` checks identity (same object); `==` checks equality (same value).
- Small ints (-5 to 256) are cached → `is` may be `True`.
- Naming: `snake_case` for variables, `UPPER_CASE` for constants.

```python
a = 100; b = 100
print(a is b)      # True (cached)
c = 300; d = 300
print(c is d)      # False (different objects)
```

---

## L02 – Numeric Types, Operators & Casting
- Types: `int` (unlimited), `float` (64‑bit), `complex`.
- Operators: `+`, `-`, `*`, `/` (always float), `//` (floor), `%` (mod), `**` (power).
- Precedence: PEMDAS (Parentheses → Exponent → Mult/Div → Add/Sub).
- Casting: `int("42")`, `float("3.14")`, `str(100)` – explicit only.
- `int(3.9)` truncates, doesn’t round.

```python
print(10 / 3)          # 3.3333333333333335
print(10 // 3)         # 3
print(10 % 3)          # 1
print(int("  15  "))   # 15
```

---

## L03 – Strings: Indexing, Slicing & Immutability
- Strings are immutable sequences of Unicode characters.
- Positive indices from left (0), negative from right (-1).
- Slicing: `[start:stop:step]` – start inclusive, stop exclusive.
- `[::-1]` reverses; slicing never raises `IndexError`.

```python
s = "Emperor"
print(s[0])      # E
print(s[-1])     # r
print(s[1:4])    # mpe
print(s[::-1])   # rorepmE
```

---

## L04 – String Methods & f‑strings
- Cleaning: `.strip()`, `.lstrip()`, `.rstrip()`.
- Search: `.find(sub)`, `.count(sub)`, `.startswith()`, `.endswith()`.
- Transform: `.upper()`, `.lower()`, `.title()`.
- Split/Join: `.split(sep)`, `.join(iterable)`, `.replace(old, new)`.
- Formatting: f‑strings `f"{var:.2f}"`, `f"{var:>10}"`.

```python
raw = "   Emperor   "
print(raw.strip())                    # Emperor
print("apple,banana".split(","))      # ['apple', 'banana']
print(f"Total: ${24.99*3:.2f}")      # Total: $74.97
```

---

## L05 – User Input, CLI Arguments & sys.argv
- `input(prompt)` always returns a string – cast to needed type.
- `sys.argv` is a list of command‑line arguments; script name at index 0.
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

## L06 – Boolean Logic, Truthiness & is vs ==
- `True` / `False` from comparisons (`>`, `<`, `==`, `!=`).
- Falsy values: `None`, `False`, `0`, `0.0`, `""`, `[]`, `{}`, `()`, `set()`.
- Logical operators: `and`, `or`, `not` – short‑circuit evaluation.
- `==` compares values; `is` compares identity. Always use `is None`.

```python
print(bool([]))          # False
print(10 > 5 and 3 < 1)  # False
a = [1,2]; b = [1,2]
print(a == b, a is b)    # True False
```

---

## L07 – None, Optional Typing & Sentinel Values
- `None` is the singleton for “no value”.
- Check with `is None` / `is not None`.
- Type hint: `Optional[int]` = `int | None`.
- Sentinel pattern: use `None` as default instead of mutable objects.

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

*Quick Test:*  
- `type(42)` → ?  
- Reverse `"hello"` → ?  
- `10 / 3` vs `10 // 3` → ?  
- Can you modify a string in place? → ?  
- `sys.argv[0]` contains → ?