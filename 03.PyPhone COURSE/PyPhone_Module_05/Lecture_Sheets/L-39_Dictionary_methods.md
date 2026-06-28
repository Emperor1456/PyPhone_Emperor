# 📘 PyPhone Emperor · Module 5
# 📖 L‑39 – Dictionary Methods

---

## 🎯 OBJECTIVE
Master the most useful built‑in **dictionary methods**.
These methods allow you to extract keys, values, and
items, copy dictionaries, and set defaults — all
essential for efficient data manipulation.

---

## 🧱 BRICK 1 – Extracting Keys, Values, and Items

Three methods return **view objects** that reflect
live changes to the dictionary.

```python
user = {"name": "Emperor", "age": 18, "active": True}
```

- `.keys()` → all keys
- `.values()` → all values
- `.items()` → all key‑value pairs as tuples

```python
print(user.keys())        # dict_keys(['name', 'age', 'active'])
print(user.values())      # dict_values(['Emperor', 18, True])
print(user.items())       # dict_items([('name', 'Emperor'), ('age', 18), ('active', True)])
```

You can iterate over them directly:
```python
for key in user.keys():
    print(key)
```

> 💡 **INSIGHT:** Views are dynamic — if the dictionary
> changes, the view reflects the new state.

---

## 🧱 BRICK 2 – Copying, Defaults, and Clearing

### `.copy()` – shallow copy
```python
copy_dict = user.copy()
```

### `.setdefault(key, default)`
Returns the value for `key` if it exists.
If not, inserts `key` with the given default and returns it.

```python
balance = {"Emperor": 100}
balance.setdefault("Emperor", 0)    # returns 100 (already exists)
balance.setdefault("Guest", 0)      # inserts 'Guest': 0, returns 0
print(balance)  # {'Emperor': 100, 'Guest': 0}
```

### `.clear()` – empty the dictionary
```python
user.clear()   # {}
```

> ⚠️ **WARNING:** `dict1 = dict2` does **not** copy; it
> creates a second reference to the same dictionary.
> Use `.copy()` for an independent clone.

---

## 📌 Key Takeaway
- `.keys()`, `.values()`, `.items()` return live views.
- `.copy()` creates a shallow, independent copy.
- `.setdefault()` is ideal for initialising counters or defaults.
- `.clear()` wipes all entries.