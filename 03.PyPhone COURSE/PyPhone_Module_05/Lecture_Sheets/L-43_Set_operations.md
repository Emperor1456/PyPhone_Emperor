# 📘 PyPhone Emperor · Module 5
# 📖 L‑43 – Set Operations

---

## 🎯 OBJECTIVE
Learn the classic mathematical **set operations** —
union, intersection, difference, and symmetric difference.
Sets make these operations both intuitive and fast,
which is invaluable for comparing groups of data.

---

## 🧱 BRICK 1 – Union and Intersection

- **Union (`|` or `.union()`)** – elements that are in **either** set (or both).
- **Intersection (`&` or `.intersection()`)** – elements that are in **both** sets.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # {1, 2, 3, 4, 5}
print(a & b)   # {3}
```

Methods accept any iterable (list, tuple, etc.) as argument:
```python
print(a.union([4, 5, 6]))       # {1, 2, 3, 4, 5, 6}
print(a.intersection([2, 3]))   # {2, 3}
```

---

## 🧱 BRICK 2 – Difference and Symmetric Difference

- **Difference (`-` or `.difference()`)** – elements in the first set but **not** in the second.
- **Symmetric Difference (`^` or `.symmetric_difference()`)** – elements in **exactly one** of the two sets (not both).

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a - b)   # {1, 2}
print(a ^ b)   # {1, 2, 4, 5}
```

### Subset and Superset checks
- `.issubset()` / `<=` – all elements of A are also in B
- `.issuperset()` / `>=` – all elements of B are also in A

```python
print({1, 2}.issubset({1, 2, 3}))    # True
print({1, 2, 3}.issuperset({1, 2}))  # True
```

> 💡 **INSIGHT:** Use sets for quick comparisons of user groups,
> permissions, tags, or any collection where uniqueness matters.

---

## 📌 Key Takeaway
- `|` / `.union()` combines without duplicates.
- `&` / `.intersection()` finds common elements.
- `-` / `.difference()` finds elements in the first set only.
- `^` / `.symmetric_difference()` finds elements in either but not both.