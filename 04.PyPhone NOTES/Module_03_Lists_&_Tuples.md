# 📘 Module 03 – Lists & Tuples · Revision Note

---

## L13 – List Creation, Indexing & Mutability
- Ordered, mutable: `[1, 2, 3]`.
- Zero‑based indexing; negative indices from end.
- `list[index]` reads; `list[index] = value` modifies.
- `len(list)` returns number of elements.

```python
items = ["A", "B", "C"]
print(items[0])    # A
items[1] = "X"
print(items)       # ['A', 'X', 'C']
```

---

## L14 – List Methods – Add, Remove, Sort
- `.append(item)`, `.insert(i, item)`, `.extend(iterable)`.
- `.remove(value)`, `.pop(i)` (returns), `.clear()`.
- `.sort()` and `.reverse()` modify in place, return `None`.

```python
nums = [3, 1, 5]
nums.append(7)
nums.sort()
print(nums)   # [1, 3, 5, 7]
```

---

## L15 – List Slicing & Slice Assignment
- `list[start:stop:step]` extracts sublist.
- Slice assignment `list[range] = iterable` replaces.
- Empty slice `list[i:i]` inserts; `list[i:j] = []` deletes.
- Slicing never raises `IndexError`.

```python
data = [0, 1, 2, 3, 4]
data[1:4] = [10, 20]   # replace indices 1‑3
print(data)             # [0, 10, 20, 4]
```

---

## L16 – List Comprehension & Generator Expressions
- `[expr for var in iterable if cond]` – builds list.
- `(expr for var in iterable)` – lazy generator.
- Use comprehensions for clean transforms/filters.

```python
squares = [x**2 for x in range(5)]          # [0,1,4,9,16]
evens = [x for x in range(10) if x%2==0]    # [0,2,4,6,8]
sum_sq = sum(x*x for x in range(1,6))       # 55
```

---

## L17 – Tuples – Immutable Sequences
- `(1, 2, 3)` – ordered, immutable.
- Single‑element: `(42,)`.
- Unpacking: `a, b = (10, 20)`.
- Used as dict keys, multiple return values.

```python
point = (5, 8)
x, y = point
def min_max(lst): return min(lst), max(lst)
```

---

## L18 – Sequence Comparison & zip() Deep Dive
- Sequences compare element‑wise (lexicographic).
- `zip(seq1, seq2)` pairs; stops at shortest.
- `zip_longest(fillvalue=)` for unequal lengths.

```python
names = ["Emperor", "Rahim"]
scores = [95, 88]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

---

*Quick Test:*  
- How to copy a list without modifying the original?  
- What does `list.sort()` return?  
- Can a tuple be a dict key? Why?  
- What happens when you zip lists of different lengths?