# 📘 PyPhone Emperor v3.0 · Module 3
# 📖 L‑18 – Sequence Comparison & `zip()` Deep Dive

---

## 🎯 OBJECTIVE — What You Will Master

> Compare, combine, and traverse multiple sequences simultaneously.

- ⚖️ **Comparison** – how lists/tuples are compared element‑wise
- 🤝 **`zip()`** – pair elements from multiple iterables
- 🔄 **`zip_longest()`** – handle unequal lengths
- 🧪 **Real‑world** – merging data, validating parallel arrays

---

## 🧱 COMPARING SEQUENCES

Python compares lists/tuples lexicographically – first differing element decides.

```python
print([1,2,3] < [1,2,4])   # True
print([1,2] < [1,2,0])     # True (shorter is smaller if all equal so far)
print((1,2) == (1,2))      # True
```

**Business – sort orders by date then amount**
```python
orders = [(1, 500), (2, 100), (1, 300)]
orders.sort()
print(orders)   # [(1, 300), (1, 500), (2, 100)]
```

---

## 🧱 `zip()` – PAIRING SEQUENCES

Combine two or more iterables element‑by‑element.

```python
names = ["Emperor", "Rahim"]
scores = [95, 88]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

**Business – match products with prices**
```python
products = ["Widget", "Gadget"]
prices = [9.99, 19.99]
inventory = list(zip(products, prices))
print(inventory)   # [('Widget', 9.99), ('Gadget', 19.99)]
```

---

## 🧱 `zip_longest()` – UNEQUAL LENGTHS

From `itertools` – fills missing values with a default.

```python
from itertools import zip_longest
a = [1, 2, 3]
b = ["x", "y"]
print(list(zip_longest(a, b, fillvalue="?")))
# [(1, 'x'), (2, 'y'), (3, '?')]
```

---

## 💡 Real‑world Usage

**Banking – compare account balances**
```python
bal1 = [100, 200]
bal2 = [150, 150]
for b1, b2 in zip(bal1, bal2):
    print(b1 > b2)
```

**E‑commerce – merge two product feeds**
```python
names = ["A", "B"]
prices = [10, 20]
catalog = dict(zip(names, prices))
```

**Logistics – assign drivers to routes**
```python
drivers = ["Ali", "Babu"]
routes = ["R1", "R2", "R3"]
for d, r in zip_longest(drivers, routes, fillvalue="UNASSIGNED"):
    print(f"{d} -> {r}")
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Check if `[1,2,3]` is equal to `[1,2,3]`. | `print([1,2,3]==[1,2,3])` |
| Medium | Zip two lists of names and ages, print each pair. | `for n,a in zip(names, ages): print(n,a)` |
| Hard | Given two lists of possibly different lengths, create a dictionary mapping keys to values using `zip_longest` with a default. | `dict(zip_longest(keys, vals, fillvalue=None))` |

Run the coach:
```bash
python ii_Practice_Sheets/L18_Sequence_Comparison_zip_Deep_Dive.py
```

---

## 📌 Key Takeaway
- Sequences compare element‑wise.
- `zip()` pairs iterables; `zip_longest()` handles unequal lengths.
- These are foundational for merging and aligning datasets.

*For Emperor.*