# 📘 PyPhone Emperor · Module 3
# 📖 L‑27 – List Slicing & Comprehensions

---

## 🎯 OBJECTIVE
Go beyond basic slicing and learn to **assign** slices
to modify lists, then master **list comprehensions** —
a concise, Pythonic way to create lists from any iterable
in a single, readable line.

---

## 🧱 BRICK 1 – Advanced Slicing and Slice Assignment

Slicing not only extracts parts of a list — it can also
**replace** a segment with new values.

### Slice assignment
```python
data = [0, 1, 2, 3, 4]
data[1:4] = [10, 20]        # replace indices 1,2,3 with [10,20]
print(data)                  # [0, 10, 20, 4]
```

### Insert with an empty slice
```python
data[2:2] = [100]           # insert at index 2 without replacing
print(data)                  # [0, 10, 100, 20, 4]
```

### Delete with slice assignment
```python
data[1:3] = []               # remove elements at indices 1 and 2
print(data)                   # [0, 20, 4]
```

> 💡 **INSIGHT:** Slice assignment replaces the selected
> range with any iterable, even of different length.

---

## 🧱 BRICK 2 – List Comprehensions

A list comprehension builds a new list by applying an
expression to each item of an iterable, optionally
filtering with an `if` condition.

### Basic syntax
```python
[expression for item in iterable if condition]
```

**Examples:**
```python
# Squares of 0‑9
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Even numbers only
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Uppercase words
words = ["hello", "world"]
upper = [w.upper() for w in words]
# ['HELLO', 'WORLD']
```

### Nested comprehensions
```python
matrix = [[1,2],[3,4],[5,6]]
flattened = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6]
```

> ⚠️ **NOTE:** List comprehensions are fast and readable,
> but don’t over‑nest them — if the logic is complex,
> a normal `for` loop is clearer.

---

## 📌 Key Takeaway
- Slice assignment `list[start:stop] = iterable` modifies in place.
- List comprehensions create new lists in one clean line.
- Format: `[expr for var in iterable if condition]`.
- Use comprehensions for simple transformations and filters.