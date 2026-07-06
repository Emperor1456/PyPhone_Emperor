# 📘 PyPhone Emperor · Module 5
# 📖 L‑41 – Tuples – Immutable Sequences

---

## 🎯 OBJECTIVE
Learn to create and use **tuples** — ordered collections
that, unlike lists, cannot be changed after creation.
Tuples are ideal for fixed data, returning multiple
values from functions, and serving as dictionary keys.

---

## 🧱 BRICK 1 – Creating and Indexing Tuples

A tuple is written with parentheses `()` and comma‑separated
values. A single‑element tuple needs a trailing comma.

```python
empty = ()
point = (10, 20)
mixed = ("Emperor", 18, True)
single = (42,)          # note the comma
```

Access works exactly like lists:
```python
print(point[0])         # 10
print(point[-1])        # 20
```

Slicing also works:
```python
print(point[:1])        # (10,)
```

> 💡 **INSIGHT:** Tuples are **immutable** — you cannot
> add, remove, or change elements after creation. Any
> attempt raises an `AttributeError` or `TypeError`.

---

## 🧱 BRICK 2 – Why Use Tuples?

**① Returning multiple values from functions**
```python
def min_max(lst):
    return min(lst), max(lst)    # returns a tuple

low, high = min_max([4,1,9,3])
print(low)    # 1
print(high)   # 9
```

**② Dictionary keys**
Lists cannot be dict keys because they are mutable;
tuples can.

```python
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278):  "London"
}
```

**③ Unpacking**
```python
coordinates = (5, 8)
x, y = coordinates
print(x, y)   # 5 8
```

> ⚠️ **WARNING:** If you need to change elements, use a list.
> Tuples are for data that should not change — think constants.

---

## 📌 Key Takeaway
- Tuple = `(item, item, ...)` — immutable.
- Indexing and slicing work exactly like lists.
- Use tuples for fixed sequences, dict keys, and multiple returns.
- Unpack directly: `a, b = tuple`.