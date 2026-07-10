# 📘 PyPhone Emperor v3.0 · Module 3
# 📖 L‑17 – Tuples – Immutable Sequences

---

## 🎯 OBJECTIVE — What You Will Master

> Fixed data that cannot change – the foundation of safe, predictable code.

- 🔒 **Immutability** – once created, cannot modify
- 📦 **Packing & Unpacking** – assign multiple values at once
- 🧱 **Why tuples?** – dictionary keys, function returns, constants
- 🧪 **Real‑world** – coordinates, configuration, DB rows

---

## 🧱 CREATING TUPLES

```python
point = (10, 20)
mixed = ("Emperor", 18, True)
single = (42,)          # comma is mandatory for single element
empty = ()
```

Access works like lists:
```python
print(point[0])         # 10
print(mixed[-1])        # True
```

---

## 🧱 PACKING & UNPACKING

```python
coordinates = (5, 8)
x, y = coordinates
print(x, y)   # 5 8
```

**Swap variables:**
```python
a, b = b, a
```

**Return multiple values from a function:**
```python
def min_max(lst):
    return min(lst), max(lst)   # returns a tuple

low, high = min_max([4,1,9,3])
print(low, high)   # 1 9
```

---

## 🧱 WHY TUPLES?

- **Dictionary keys** – lists are unhashable, tuples work.
- **Data integrity** – constants that shouldn’t be altered.
- **Performance** – tuples are slightly faster than lists for fixed data.

```python
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}
```

> ⚠️ **WARNING:** Tuples are immutable, but if they contain mutable objects (like a list), that inner object can still be changed. Be careful with nested mutability.

---

## 💡 Real‑world Usage

**Banking – fixed interest rates**
```python
rates = (0.05, 0.10, 0.15)
```

**E‑commerce – product dimensions**
```python
size = (1920, 1080)
print(f"Resolution: {size[0]}x{size[1]}")
```

**HR – employee status codes**
```python
statuses = ("active", "inactive", "terminated")
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Create a tuple of three numbers and print it. | `t = (1,2,3); print(t)` |
| Medium | Unpack a tuple into separate variables and print them. | `a,b,c = t; print(a,b,c)` |
| Hard | Use a tuple as a dictionary key and retrieve its value. | `d = {(1,2): "point"}; print(d[(1,2)])` |

Run the coach:
```bash
python ii_Practice_Sheets/L17_Tuples_Immutability_Packing_Unpacking.py
```

---

## 📌 Key Takeaway
- Tuples are ordered, immutable sequences.
- Use packing/unpacking for clean multi‑variable assignments.
- Ideal for dictionary keys, constants, and multiple returns.

*For Emperor.*