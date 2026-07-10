# 📘 PyPhone Emperor v3.0 · Module 1
# 📖 L‑01 – Variables, Memory & Dynamic Typing

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, **variables** will have no secrets.

- 🧠 **Mental Model:** Variables are name tags, not boxes.
- ⚡ **Dynamic Typing:** Types live on objects, not names.
- 🔬 **Memory:** How Python stores, references, and cleans up data.
- 🧪 **Identity vs Equality:** `is` checks the tag, `==` checks the value.
- 📛 **Naming:** Professional conventions for readable, maintainable code.
- 🔄 **Multi‑Assignment:** One‑line swaps without temp variables.

---

## 🧱 THE CORE CONCEPT – Variables Are Name Tags

In Python, a variable is not a box that holds data.
A variable is a **name tag** attached to an object
that lives somewhere in memory.

Think of memory as a giant warehouse.
When you write `x = 42`, Python:
1. Creates an integer object `42` somewhere in the warehouse.
2. Tags that object with the name `x`.

You can attach multiple tags to the same object:
```python
a = 300
b = a
```
Now both `a` and `b` point to the **same** object `300`.
If you later write `a = 500`, you are not modifying `300`.
You are detaching the tag `a` and sticking it onto `500`.
`b` still points to `300`.

> 💡 **INSIGHT:** Assignment never copies data.
> It only binds a name to an object. This is the single
> most important mental model in all of Python.

---

## 🧱 DYNAMIC TYPING – Types Live on Objects, Not Variables

Python is **dynamically typed**: a variable can refer
to any type at any time. The type belongs to the object,
not the variable name.

```python
x = 42          # x is an int
x = "Emperor"   # now x is a string
x = [1, 2, 3]   # now x is a list
```

Every object carries its type inside it. You can check:
```python
print(type(42))           # <class 'int'>
print(type("Emperor"))    # <class 'str'>
print(type([1, 2, 3]))    # <class 'list'>
```

This flexibility is powerful, but it also means you
must be disciplined. Python will not protect you from
assigning a string to a variable that should hold a number.

> ⚠️ **WARNING:** Dynamic typing is not a license for chaos.
> In enterprise code, you use clear naming (`user_count`,
> `total_price`) and optional type hints (L‑24) to keep
> your empire from descending into madness.

---

## 🧱 MEMORY MANAGEMENT – What Really Happens

Python manages memory automatically with two tools:
- **Reference counting** — each object tracks how many
  names point to it. When the count drops to zero,
  the object is deleted.
- **Garbage collection** — handles cycles (objects that
  reference each other but have no external names).

### Example: Reference Counting
```python
x = [1, 2, 3]   # list object created, ref count = 1
y = x            # ref count = 2
del x            # ref count = 1 (x removed, object stays)
del y            # ref count = 0, object deleted
```

### Small Integer Caching (Advanced)
Python pre‑creates integers from -5 to 256.
These are singletons — reused every time.
```python
a = 100
b = 100
print(a is b)   # True (same object from cache)

c = 300
d = 300
print(c is d)   # False (different objects, > 256)
```
`is` checks identity — whether two names point to
the *exact same object*. `==` checks equality —
whether the values are equivalent.
Never use `is` to compare values. Use `==`.

> 💡 **INSIGHT:** `is` is for identity. `==` is for equality.
> Mixing them is a bug that lives for years in codebases.

---

## 🧱 VARIABLE NAMING RULES & CONVENTIONS

- Must start with a letter or underscore (`_`).
- Can contain letters, digits, underscores.
- Case‑sensitive (`age` ≠ `Age`).
- Cannot be reserved keywords (`if`, `for`, `class`, etc.).

### Professional Conventions
| Style | Use |
|-------|-----|
| `snake_case` | Variables, functions |
| `UPPER_CASE` | Constants |
| `_private` | Internal use |
| Avoid `l`, `O`, `I` | Look like digits |

```python
MAX_RETRIES = 3
user_count = 142
_internal_state = None
```

---

## 🧱 MULTIPLE ASSIGNMENT & SWAPPING

Python lets you assign multiple variables in one line:
```python
x, y, z = 10, 20, 30
```

Swapping values without a temporary variable:
```python
a, b = b, a
```
This works because the right side is evaluated first,
creating a tuple `(b, a)`, then unpacked into `a, b`.

---

## 💡 Real‑world Usage

**Banking – Account balance with clear naming**
```python
account_balance = 5000.00
withdrawal_amount = 200.00
account_balance -= withdrawal_amount
print(account_balance)   # 4800.00
```

**E‑commerce – Product inventory**
```python
product_name = "Wireless Mouse"
unit_price = 24.99
stock = 150
reorder_threshold = 20
if stock <= reorder_threshold:
    print(f"Reorder {product_name}")
```

**Logistics – Tracking shipment weight**
```python
shipment_weight_kg = 12.5
is_oversized = shipment_weight_kg > 10
print(is_oversized)   # True
```

**HR – Employee record**
```python
employee_name = "Emperor"
employee_id = 101
is_active = True
```

---

## 🔍 Practice Preview
You will write a small inventory tracker that:
- Creates product variables with correct types.
- Swaps values between two products.
- Checks object identity with `is`.
- Demonstrates dynamic typing by reassigning a variable.

The practice engine will verify your output.

Run the coach:
```bash
python ii_Practice_Sheets/L01_Variables_Memory_Typing.py
```

---

## 📌 Key Takeaway
- Variables are name tags, not boxes.
- Types belong to objects, not variables.
- `is` checks identity; `==` checks value.
- Python handles memory automatically.
- Clear, snake_case naming is professional code.
- Master this mental model, and you own Python.

*For Emperor.*
