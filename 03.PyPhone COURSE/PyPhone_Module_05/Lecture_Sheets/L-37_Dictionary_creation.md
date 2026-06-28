# 📘 PyPhone Emperor · Module 5
# 📖 L‑37 – Dictionary Creation & Key‑Value Pairs

---

## 🎯 OBJECTIVE
Learn to create and work with **dictionaries** — Python’s
core mapping type. A dictionary stores pairs of keys and values,
allowing you to look up a value by its key almost instantly.
Dictionaries are the foundation of structured data in Python.

---

## 🧱 BRICK 1 – Creating a Dictionary

A dictionary is written with curly braces `{}` containing
comma‑separated `key: value` pairs. Keys must be unique and
immutable (strings, numbers, tuples are fine). Values can be
any type.

```python
# Empty dictionary
empty = {}

# Simple dictionary
user = {
    "name": "Emperor",
    "age": 18,
    "active": True
}
```

**Using `dict()` constructor:**
```python
user2 = dict(name="Emperor", age=18, active=True)
```

**Mixed value types:**
```python
config = {
    "host": "localhost",
    "port": 8080,
    "debug": False,
    "tags": ["python", "backend"]
}
```

> 💡 **INSIGHT:** Keys are case‑sensitive. `"Name"` and `"name"`
> are different keys. If you use the same key twice, the later
> value overwrites the earlier one.

---

## 🧱 BRICK 2 – Accessing Values

### Using square brackets `[]`
```python
print(user["name"])        # Emperor
```

If the key does not exist, Python raises a `KeyError`.

### Using `.get()` (safe access)
```python
print(user.get("name"))    # Emperor
print(user.get("phone"))   # None (no error)
print(user.get("phone", "N/A"))  # N/A (default value)
```

### Adding and updating
```python
user["email"] = "emperor@domain.com"   # add new pair
user["age"] = 19                        # update existing
```

> ⚠️ **WARNING:** Dictionaries are **mutable** — you can add,
> modify, and remove key‑value pairs after creation.

---

## 📌 Key Takeaway
- Dictionary = `{key: value, ...}`.
- Keys are unique and must be immutable.
- `dict[key]` raises `KeyError` if missing; `.get(key)` is safe.
- Add/update with `dict[key] = value`.