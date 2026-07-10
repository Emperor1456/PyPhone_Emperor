# 📘 PyPhone Emperor v3.0 · Module 1
# 📖 L‑07 – None, Optional Typing & Sentinel Values

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, you will represent "nothing" with absolute clarity.

- 🕳️ `None` – the singleton for "no value"
- 🧪 Checking for `None` – `is None`, not `== None`
- 🏷️ Optional typing – `Optional[int]` means "int or None"
- 🚩 Sentinel values – using `None` as a signal
- 🛡️ Avoiding the billion‑dollar mistake

---

## 🧱 WHAT IS `None`?

`None` is Python's built‑in constant for "no value here."
It is a singleton – only one `None` exists in memory.

```python
result = None
print(type(result))   # <class 'NoneType'>
```

Functions that don't return anything actually return `None`:

```python
def greet():
    print("Hello")

value = greet()   # prints "Hello"
print(value)      # None
```

---

## 🧱 CHECKING FOR `None` – ALWAYS USE `is`

```python
data = None

# Correct:
if data is None:
    print("No data")

# Also correct:
if data is not None:
    print("Data exists")

# WRONG – works but violates convention:
if data == None:
    print("Bad practice")
```

> ⚠️ **WARNING:** Always use `is None`, never `== None`. `is` checks identity directly; `==` can be overridden by objects to return unexpected results.

---

## 🧱 OPTIONAL TYPING – WHEN SOMETHING MIGHT BE `None`

Type hints can signal that a variable might be `None`:

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Emperor", 2: "Rahim"}
    return users.get(user_id)   # returns str or None

user = find_user(3)
if user is None:
    print("User not found")
else:
    print(f"Found: {user}")
```

`Optional[str]` means "this is either a `str` or `None`."
This makes your intent explicit and helps tools catch bugs.

---

## 🧱 SENTINEL VALUES – `None` AS A SIGNAL

Use `None` to represent a missing or default value:

```python
def connect(host: str, port: Optional[int] = None):
    if port is None:
        port = 5432   # default PostgreSQL port
    print(f"Connecting to {host}:{port}")

connect("localhost")          # uses default 5432
connect("localhost", 8080)    # uses 8080
```

This pattern avoids the mutable default pitfall:

```python
# BAD – shared list across calls
def add_item(item, items=[]):
    items.append(item)
    return items

# GOOD – None sentinel
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

## 💡 Real‑world Usage

**Banking – transaction that hasn't settled yet**
```python
settled_amount: Optional[float] = None
if settled_amount is None:
    print("Transaction pending")
```

**E‑commerce – optional discount**
```python
def apply_discount(price, discount_pct=None):
    if discount_pct is None:
        return price
    return price * (1 - discount_pct / 100)
```

**Logistics – missing weight data**
```python
weight: Optional[float] = None
if weight is None:
    print("Weigh package before shipping")
```

**HR – employee without a department yet**
```python
department: Optional[str] = None
if department is None:
    print("Unassigned")
```

---

## 🔍 Practice Preview
You will:
- Write functions that return `None` on failure.
- Use `Optional` type hints for parameters.
- Avoid the mutable default pitfall with `None` sentinels.
- Check for `None` correctly in business logic.

Run the coach:
```bash
python ii_Practice_Sheets/L07_None_Optional_Typing_Sentinels.py
```

---

## 📌 Key Takeaway
- `None` is the one and only "no value" in Python.
- Always check with `is None`, never `== None`.
- `Optional[X]` means "X or None" – use it in type hints.
- Use `None` as a sentinel to avoid mutable default bugs.
- Represent missing data explicitly – it prevents crashes.

*For Emperor.*