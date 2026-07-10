# 📘 PyPhone Emperor v3.0 · Module 1
# 📖 L‑06 – Boolean Logic, Truthiness & is vs ==

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, every decision in your code will be precise.

- ✅ Boolean values – `True` and `False`
- 🧠 Truthiness – what Python considers true or false
- 🔗 Logical operators – `and`, `or`, `not`
- ⚖️ `is` vs `==` – identity vs equality
- 🔀 Short‑circuit evaluation

---

## 🧱 BOOLEAN BASICS

A `bool` is either `True` or `False`.

```python
is_active = True
is_empty = False
print(type(is_active))   # <class 'bool'>
```

Booleans are created by comparisons:

```python
print(10 > 5)    # True
print(10 == 5)   # False
print(10 != 5)   # True
```

---

## 🧱 TRUTHINESS – EVERYTHING IS TRUE OR FALSE

In Python, **every object** has a truth value.
These are **falsy**:

| Falsy Value | Reason |
|-------------|--------|
| `None` | Represents nothing |
| `False` | The boolean false |
| `0`, `0.0` | Zero |
| `""` | Empty string |
| `[]` | Empty list |
| `{}` | Empty dict |
| `()` | Empty tuple |
| `set()` | Empty set |

**Everything else is truthy.**

```python
if "hello":      # truthy – block runs
    print("Yes")

if "":           # falsy – block skipped
    print("No")

if 0:            # falsy – skipped
    print("Zero")
```

> 💡 **INSIGHT:** Use truthiness to check if a list or string is non‑empty without writing `len(x) > 0`.

---

## 🧱 LOGICAL OPERATORS

- `and` – True if **both** are true
- `or` – True if **at least one** is true
- `not` – flips the boolean

```python
age = 25
has_license = True
print(age >= 18 and has_license)   # True
print(age < 18 or has_license)     # True
print(not has_license)             # False
```

**Short‑circuit evaluation:**
Python stops evaluating as soon as the result is determined.

```python
def check():
    print("checked")
    return True

print(False and check())   # "checked" never prints
print(True or check())     # "checked" never prints
```

---

## 🧱 `is` vs `==` – THE CRITICAL DIFFERENCE

- `==` checks **value equality** – are the contents the same?
- `is` checks **identity** – are they the exact same object in memory?

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True  (same contents)
print(a is b)   # False (different objects)
print(a is c)   # True  (same object)
```

**Integer caching exception:**

```python
print(100 is 100)   # True  (cached: -5 to 256)
print(300 is 300)   # False (different objects)
```

> ⚠️ **WARNING:** Never use `is` to compare values. Use `is` only for `None` checks: `if x is None`.

---

## 💡 Real‑world Usage

**Banking – validate transaction**
```python
balance = 500
amount = 200
is_valid = amount > 0 and amount <= balance
print(is_valid)   # True
```

**E‑commerce – check product availability**
```python
stock = 0
if not stock:
    print("Out of stock")
```

**Logistics – check if shipment is active**
```python
status = "delivered"
if status == "delivered":
    print("Archive shipment")
```

**HR – check new employee vs existing**
```python
new_emp = {"id": 101}
current_emp = new_emp
print(new_emp is current_emp)   # True – same record
```

---

## 🔍 Practice Preview
You will:
- Evaluate business rules with `and`, `or`, `not`.
- Test truthiness of various data types.
- Distinguish `is` from `==` with real examples.
- Use short‑circuit evaluation in a validation chain.

Run the coach:
```bash
python ii_Practice_Sheets/L06_Boolean_Logic_Truthiness.py
```

---

## 📌 Key Takeaway
- `True` and `False` are the only booleans.
- Every object has a truthiness – use it for clean conditions.
- `and`, `or`, `not` combine conditions; they short‑circuit.
- `==` compares values; `is` compares identity. Never mix them.

*For Emperor.*