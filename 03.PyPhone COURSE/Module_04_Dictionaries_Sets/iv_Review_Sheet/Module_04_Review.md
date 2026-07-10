# 📘 Module 04 – Dictionaries & Sets · Revision Guide

---

## L19 – Dictionary – Key‑Value Pairs & Hash Tables

- A dictionary maps unique keys to values: `{"name":"Emperor", "age":18}`.
- Keys must be immutable (strings, numbers, tuples).
- Access: `d[key]` (KeyError if missing) or `d.get(key, default)`.
- Add/update: `d[key] = value`.
- `len(d)` returns number of pairs.

```python
user = {"name": "Emperor", "age": 18}
print(user["name"])               # Emperor
print(user.get("email", "N/A"))   # N/A
user["age"] = 19
```

---

## L20 – Dictionary Methods, Iteration & Counting

- `.keys()`, `.values()`, `.items()` return live views.
- Iterate with `for key in d:` or `for k, v in d.items():`.
- Counting pattern: `d[key] = d.get(key, 0) + 1`.
- `.pop(key)` removes and returns value; `.popitem()` removes last item.
- `.update(d2)` merges another dict in place.

```python
words = ["apple", "banana", "apple"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts)   # {'apple':2, 'banana':1}
```

---

## L21 – Nested Dictionaries & `defaultdict`

- A dict can contain another dict as a value → hierarchical data.
- `defaultdict` from `collections` auto‑creates missing keys.
- `defaultdict(list)` groups items; `defaultdict(int)` counts.

```python
from collections import defaultdict
by_letter = defaultdict(list)
for word in ["apple", "banana", "avocado"]:
    by_letter[word[0]].append(word)
print(dict(by_letter))   # {'a':['apple','avocado'], 'b':['banana']}
```

---

## L22 – Sets – Uniqueness, Membership & Operations

- A set stores unique elements: `{1, 2, 3}` or `set([1,2,2])`.
- `in` checks membership in O(1) average time.
- `.add(item)`, `.remove(item)`, `.discard(item)` (safe).
- `.update(iterable)` adds multiple elements.

```python
nums = [1,2,2,3,3,3]
unique = set(nums)          # {1,2,3}
print(2 in unique)          # True
```

---

## L23 – `dataclass` & `namedtuple` – Clean Data Containers

- `namedtuple` creates lightweight immutable objects.
- `dataclass` (Python 3.7+) auto‑generates `__init__`, `__repr__`, etc.
- Use for records, configuration, ORM models.

```python
from dataclasses import dataclass
@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0
p = Product("Widget", 9.99)
print(p)   # Product(name='Widget', price=9.99, quantity=0)
```

---

**Quick Test:**  
- How do you safely retrieve a value that may not exist in a dictionary?  
- What happens when you try to add a duplicate key to a dictionary?  
- How do you remove duplicates from a list?  
- Why is a `namedtuple` more memory‑efficient than a dictionary?

*Review complete. You are now ready for the Module 04 Practice Review.*