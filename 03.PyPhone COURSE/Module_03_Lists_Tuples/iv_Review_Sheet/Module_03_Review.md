# 📘 Module 03 – Lists & Tuples · Revision Guide

---

## L13 – List Creation, Indexing & Mutability

- Lists are ordered, mutable collections: `[1, 2, 3]`.
- Zero‑based indexing; negative indices count from the end.
- `list[index]` reads an element; `list[index] = value` modifies it.
- `len(list)` returns the number of elements.

```python
items = ["A", "B", "C"]
print(items[0])    # A
items[1] = "X"
print(items)       # ['A', 'X', 'C']
```

---

## L14 – List Methods – Add, Remove, Sort

- `.append(item)` adds to the end.
- `.insert(index, item)` inserts at a position.
- `.remove(value)` deletes the first occurrence.
- `.pop(index)` removes and returns the element (default last).
- `.sort()` sorts in place; `.reverse()` reverses in place.
- `.sort()` and `.reverse()` return `None`.

```python
nums = [3, 1, 5]
nums.append(7)
nums.sort()
print(nums)   # [1, 3, 5, 7]
```

---

## L15 – List Slicing & Slice Assignment

- `list[start:stop:step]` extracts a sublist.
- Slice assignment `list[start:stop] = iterable` replaces a segment.
- Empty slice `list[i:i]` can insert without removing.
- Slicing never raises `IndexError`.

```python
data = [0, 1, 2, 3, 4]
data[1:4] = [10, 20]   # replace indices 1-3
print(data)             # [0, 10, 20, 4]
```

---

## L16 – List Comprehension & Generator Expressions

- List comprehension: `[expr for var in iterable if cond]`.
- Generator expression: `(expr for var in iterable)` – lazy, memory‑friendly.
- Use comprehensions for simple transforms and filters.

```python
squares = [x**2 for x in range(5)]          # [0,1,4,9,16]
evens = [x for x in range(10) if x%2==0]    # [0,2,4,6,8]
```

---

## L17 – Tuples – Immutable Sequences

- Tuples are immutable: `(1, 2, 3)`.
- Single‑element tuple requires a trailing comma: `(42,)`.
- Unpacking: `a, b = (10, 20)`.
- Used as dictionary keys and function return values.

```python
point = (5, 8)
x, y = point
def min_max(lst): return min(lst), max(lst)
```

---

## L18 – Sequence Comparison & zip() Deep Dive

- Sequences compare element‑wise (lexicographically).
- `zip(seq1, seq2)` pairs elements; stops at the shortest.
- `zip_longest()` from `itertools` handles unequal lengths.

```python
names = ["Emperor", "Rahim"]
scores = [95, 88]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

---

**Quick Test:**  
- How do you copy a list without modifying the original?  
- What does `list.sort()` return?  
- Can a tuple be used as a dictionary key? Why?  
- What happens when you zip two lists of different lengths?

*Review complete. You are now ready for the Module 03 Practice Review.*