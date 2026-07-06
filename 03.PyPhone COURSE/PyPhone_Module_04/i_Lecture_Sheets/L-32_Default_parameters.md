# 📘 PyPhone Emperor · Module 4
# 📖 L‑32 – Default Parameters

---

## 🎯 OBJECTIVE
Learn to give function parameters **default values**.
When an argument is omitted at call time, the default
is used automatically. Default parameters make functions
more flexible and reduce the need for overloads.

---

## 🧱 BRICK 1 – Defining a Default Value

Assign a value to a parameter in the `def` statement
using `=`. The default is used only if the caller
does not provide that argument.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Emperor")   # Hello, Emperor!
greet()            # Hello, Guest!
```

Multiple parameters can have defaults. Parameters
with defaults must come **after** parameters without
defaults.

```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # 9  (3²)
print(power(3, 3))   # 27 (3³)
```

> ⚠️ **WARNING:** Default parameters are evaluated only
> **once** when the function is defined, not each time
> it is called. Avoid mutable defaults like `[]`.

---

## 🧱 BRICK 2 – Mutable Default Pitfall and Safe Patterns

A mutable default (like a list or dict) is created once
and shared across all calls — a common bug.

```python
# BAD: shared list
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))   # [1]
print(add_item(2))   # [1, 2]   ← unexpected!
```

**Fix:** use `None` as a sentinel and create the mutable
object inside the function.

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))   # [1]
print(add_item(2))   # [2]      ← correct
```

---

## 📌 Key Takeaway
- Default values allow optional arguments.
- Non‑default parameters must appear before default ones.
- Never use mutable objects as default values directly.
- Use `None` as the default and create the mutable object inside.