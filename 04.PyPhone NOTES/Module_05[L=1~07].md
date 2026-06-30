# 📘 PyPhone Emperor · Module 5  
# 🗃️ Comprehensive Note – Dictionaries, Tuples & Sets

---

## 🎯 Scope
This note covers the three core collection types from Module 5: dictionaries (key‑value pairs), tuples (immutable sequences), and sets (unordered unique elements).  
You will learn how to create, access, modify, and iterate over each type, along with the most useful methods and set operations.  
All code fits a phone screen; no sideways scrolling.

---

## 🧱 1. Dictionaries – Creation & Basics
A **dictionary** (`dict`) is a mutable, unordered collection of key‑value pairs.  
Keys must be **immutable** (e.g., strings, numbers, tuples).  
Values can be any type.

### Creating a Dictionary
```python
empty = {}
user = {"name": "Emperor", "age": 18, "active": True}
# Using dict() constructor
config = dict(host="localhost", port=8080)
```

### Accessing Values
- `d[key]` – raises `KeyError` if key is missing.
- `d.get(key, default)` – returns `None` (or a custom default) if key not found.

```python
print(user["name"])          # Emperor
print(user.get("phone", "N/A"))  # N/A
```

---

## 🧱 2. Dictionaries – Adding, Updating & Removing
### Add / Update
- `d[key] = value` – adds or overwrites.
- `d.update({key: value, ...})` – merges another dict.

```python
user["email"] = "e@domain.com"
user.update({"age": 19, "city": "Dhaka"})
```

### Remove
- `del d[key]` – removes key (raises error if missing).
- `d.pop(key, default)` – removes and returns value.
- `d.popitem()` – removes and returns last inserted pair (Python 3.7+).
- `d.clear()` – empties the dictionary.

```python
age = user.pop("age")   # returns 19
del user["email"]
```

### Checking Existence
```python
if "name" in user:
    print("Name exists")
```

---

## 🧱 3. Dictionary Methods & Iteration
### Key Methods
- `.keys()` – returns a view of all keys.
- `.values()` – returns a view of all values.
- `.items()` – returns a view of (key, value) tuples.

These views are dynamic – they reflect changes in the dict.

```python
for k in user.keys():
    print(k)
for v in user.values():
    print(v)
for k, v in user.items():
    print(f"{k} → {v}")
```

### Counting with `.get()`
```python
words = ["a", "b", "a"]
count = {}
for w in words:
    count[w] = count.get(w, 0) + 1
# {'a':2, 'b':1}
```

---

## 🧱 4. Tuples – Immutable Sequences
A **tuple** is an ordered, immutable collection.  
Defined with parentheses `()` (or just commas).  
Single‑element tuple requires a trailing comma: `(42,)`.

```python
point = (10, 20)
mixed = ("Emperor", 18, True)
single = (42,)
```

### Access & Slicing
Same as lists, but no modification allowed.
```python
print(point[0])      # 10
print(point[:1])     # (10,)
```

### Unpacking
```python
x, y = point        # x=10, y=20
```

### Why Use Tuples?
- Dictionary keys (because immutable).
- Returning multiple values from functions.
- Performance and safety (data that should not change).

---

## 🧱 5. Sets – Unordered Unique Elements
A **set** is a mutable, unordered collection with **no duplicates**.  
Written with curly braces `{}` (but `{}` alone is an empty dict).  
Use `set()` for an empty set.

```python
fruits = {"apple", "banana", "cherry"}
nums = set([1, 2, 2, 3, 3, 3])   # {1,2,3}
```

### Adding & Removing
- `.add(item)` – adds a single element.
- `.update(iterable)` – adds multiple elements.
- `.remove(item)` – removes element (raises KeyError if missing).
- `.discard(item)` – removes if present (no error).
- `.pop()` – removes and returns an arbitrary element.

```python
fruits.add("date")
fruits.update(["elderberry", "fig"])
fruits.discard("kiwi")
```

### Membership Testing
```python
"apple" in fruits   # True (very fast)
```

---

## 🧱 6. Set Operations
Sets support classic mathematical operations.

| Operation            | Syntax  | Meaning                                      |
|----------------------|---------|----------------------------------------------|
| Union                | `A \| B`  | Elements in **either** A or B (or both)      |
| Intersection         | `A & B`   | Elements in **both** A and B                 |
| Difference           | `A - B`   | Elements in A but **not** in B               |
| Symmetric Difference | `A ^ B`   | Elements in **exactly one** of A or B        |

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # {1,2,3,4,5}
print(a & b)   # {3}
print(a - b)   # {1,2}
print(a ^ b)   # {1,2,4,5}
```

### Subset / Superset
- `A <= B` – A is subset of B.
- `A >= B` – A is superset of B.

---

## 💡 Quick Reference
```python
# Dictionary
d = {"a":1, "b":2}
d["c"] = 3
d.get("x", 0)
d.keys(), d.values(), d.items()
d.pop("a")
del d["b"]

# Tuple
t = (1, 2, 3)
a, b, c = t
# Tuples are immutable, cannot be changed after creation.

# Set
s = {1, 2, 3}
s.add(4)
s.remove(2)
len(s)

# Set operations
{1,2} | {2,3}   # union {1,2,3}
{1,2} & {2,3}   # intersection {2}
{1,2} - {2,3}   # difference {1}
{1,2} ^ {2,3}   # symmetric difference {1,3}
```

---

## 📌 Key Takeaway
- Dictionaries are the go‑to for fast lookups and structured data; use `.get()` for safe access.
- Tuples are immutable lists – use them for constants, dict keys, and multiple return values.
- Sets enforce uniqueness and provide fast membership tests plus powerful mathematical operations.
- Choose the right collection for the task: `dict` for mapping, `tuple` for fixed data, `set` for uniqueness and comparisons.

*Study this sheet. Recall it from memory. Then practice.*