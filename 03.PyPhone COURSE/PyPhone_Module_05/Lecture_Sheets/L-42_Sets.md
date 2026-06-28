# 📘 PyPhone Emperor · Module 5
# 📖 L‑42 – Set – Unordered Unique Elements

---

## 🎯 OBJECTIVE
Learn to create and use **sets** — unordered collections
of unique elements. Sets automatically discard duplicates
and support fast membership tests and mathematical operations
like union and intersection.

---

## 🧱 BRICK 1 – Creating Sets

A set is written with curly braces `{}` containing
comma‑separated values (no colons — that would make it
a dictionary). To create an empty set, you must use `set()`.

```python
fruits = {"apple", "banana", "cherry"}
print(fruits)          # order may vary
print(len(fruits))     # 3
```

**Creating from a list (duplicates removed):**
```python
nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)
print(unique)          # {1, 2, 3}
```

> 💡 **INSIGHT:** Sets are **unordered** — you cannot
> access elements by index. The order is arbitrary.

---

## 🧱 BRICK 2 – Adding, Removing, and Membership

### Adding elements
- `.add(item)` — adds a single element
- `.update(iterable)` — adds multiple elements

```python
fruits.add("date")
fruits.update(["elderberry", "fig"])
```

### Removing elements
- `.remove(item)` — removes item (raises KeyError if missing)
- `.discard(item)` — removes item (no error if missing)
- `.pop()` — removes and returns an **arbitrary** element

### Checking membership (very fast)
```python
if "apple" in fruits:
    print("We have apple!")
```

> ⚠️ **WARNING:** Sets are **mutable** — you can add and
> remove elements. But elements themselves must be immutable
> (no lists or dicts inside a set). Sets cannot be nested.

---

## 📌 Key Takeaway
- Set = `{item, ...}` — unordered, unique elements.
- Use `.add()`, `.update()`, `.remove()`, `.discard()`.
- `in` checks membership extremely fast.
- Perfect for deduplication and membership testing.