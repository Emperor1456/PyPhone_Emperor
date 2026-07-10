# 📘 Module 04 – Dictionaries & Sets · Revision Note

---

## L19 – Dictionary – Key‑Value Pairs & Hash Tables
- `{"key": value}` – keys must be immutable.
- Access: `d[key]` (KeyError) or `d.get(key, default)`.
- Add/update: `d[key] = value`.
- `len(d)` returns pair count.

```python
user = {"name": "Emperor", "age": 18}
print(user["name"])               # Emperor
print(user.get("email", "N/A"))   # N/A
user["age"] = 19
```

---

## L20 – Dictionary Methods, Iteration & Counting
- `.keys()`, `.values()`, `.items()` – live views.
- Iterate: `for k in d:` or `for k, v in d.items():`.
- Counting: `d[key] = d.get(key, 0) + 1`.
- `.pop(key)`, `.popitem()`, `.update(d2)`.

```python
words = ["apple", "banana", "apple"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts)   # {'apple':2, 'banana':1}
```

---

## L21 – Nested Dictionaries & defaultdict
- Dicts can contain dicts → hierarchical data.
- `defaultdict(list)` groups; `defaultdict(int)` counts.

```python
from collections import defaultdict
by_letter = defaultdict(list)
for word in ["apple", "banana", "avocado"]:
    by_letter[word[0]].append(word)
print(dict(by_letter))
```

---

## L22 – Sets – Uniqueness, Membership, Operations
- `{1, 2, 3}` or `set([1,2,2])`.
- `in` checks membership in O(1).
- `.add()`, `.remove()`, `.discard()`, `.update()`.

```python
nums = [1,2,2,3,3,3]
unique = set(nums)          # {1,2,3}
print(2 in unique)          # True
```

---

## L23 – dataclass & namedtuple – Clean Data
- `namedtuple` – lightweight immutable records.
- `dataclass` (Python 3.7+) – auto‑generates `__init__`, `__repr__`.
- Use for configuration, records, ORM models.

```python
from dataclasses import dataclass
@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0
p = Product("Widget", 9.99)
print(p)
```

---

*Quick Test:*  
- How to safely retrieve a missing key from a dict?  
- What happens when you add a duplicate key?  
- How to remove duplicates from a list?  
- Why is namedtuple more memory‑efficient than a dict?