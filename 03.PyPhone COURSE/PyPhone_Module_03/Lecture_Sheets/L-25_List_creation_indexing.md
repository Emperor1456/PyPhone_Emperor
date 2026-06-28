# 📘 PyPhone Emperor · Module 3
# 📖 L‑25 – List Creation & Indexing

---

## 🎯 OBJECTIVE
Learn to create **lists** — Python’s most versatile
collection. A list holds an ordered sequence of items,
each accessible by its index. Lists can store mixed
types, can be modified, and are the backbone of
data processing.

---

## 🧱 BRICK 1 – Creating Lists

A list is written as comma‑separated values inside
square brackets `[]`.

```python
empty   = []
numbers = [10, 20, 30, 40]
fruits  = ["apple", "banana", "cherry"]
mixed   = [1, "two", 3.0, True]
```

**Nested lists:**
```python
matrix = [[1, 2], [3, 4], [5, 6]]
```

Use `len()` to get the number of items:
```python
print(len(fruits))   # 3
```

> 💡 **INSIGHT:** Lists are **mutable** — you can change
> their content after creation, unlike strings.

---

## 🧱 BRICK 2 – Indexing and Modifying

### Accessing elements (zero‑based)
```python
colors = ["red", "green", "blue"]
print(colors[0])      # red
print(colors[-1])     # blue  (last element)
```

### Changing an element
```python
colors[1] = "yellow"
print(colors)         # ['red', 'yellow', 'blue']
```

### Slicing works exactly like strings
```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])      # [1, 2, 3]
print(nums[:3])       # [0, 1, 2]
print(nums[::2])      # [0, 2, 4]
print(nums[::-1])     # [5, 4, 3, 2, 1, 0]
```

> ⚠️ **WARNING:** Accessing an out‑of‑range index raises
> an `IndexError`, but slicing is safe — it returns an
> empty list if the range is invalid.

---

## 📌 Key Takeaway
- Lists are created with `[]`, items separated by `,`.
- Indexing starts at 0; negative indices count from the end.
- Lists are mutable — change elements by assigning to an index.
- Slicing works identically to strings.