# 📘 PyPhone Emperor · Module 5  
# 📖 L‑39 – Dictionary Methods (Extracting Keys, Values, and Items)

---

## 🎯 OBJECTIVE  
Master the built‑in dictionary methods `.keys()`, `.values()`, and `.items()` to extract and iterate over dictionary contents.  
Use `.copy()`, `.clear()`, and `.pop()` to manage dictionary lifecycles. These methods are the toolkit for processing configuration data, user profiles, and any structured business record.

---

## 🧱 BRICK 1 – Extracting Keys, Values, and Items

**① List of keys (Easy practice)**
```python
d = {'name': 'Emperor', 'age': 18}
keys = list(d.keys())
print(keys)   # ['name', 'age']
```
`.keys()` returns a view of all keys. Convert to list for indexing.

**② List of values (Medium practice)**
```python
values = list(d.values())
print(values)   # ['Emperor', 18]
```
`.values()` gives the corresponding values.

**③ List of key‑value pairs (preview of `.items()`)**
```python
pairs = list(d.items())
print(pairs)   # [('name', 'Emperor'), ('age', 18)]
```
Each pair is a tuple `(key, value)`.

> 💡 **INSIGHT:** These views are dynamic — if the dictionary changes, the view reflects the change.

---

## 🧱 BRICK 2 – Advanced Manipulation and Safe Operations

**④ Pop a key and capture the value (Hard practice)**
```python
d = {'name': 'Emperor', 'age': 18}
popped = d.pop('age')
print(popped)   # 18
print(d)        # {'name': 'Emperor'}
```
`.pop()` removes the key and returns the value. Use `.pop(key, default)` to avoid KeyError.

**⑤ Copy a dictionary**
```python
original = {'a': 1, 'b': 2}
copy = original.copy()
copy['a'] = 99
print(original)   # {'a': 1, 'b': 2} — unchanged
```

**⑥ Clear all entries**
```python
d.clear()
print(d)   # {}
```

**⑦ `setdefault()` – init if missing**
```python
counts = {}
counts.setdefault('emperor', 0)   # adds 'emperor':0 if not present
counts['emperor'] += 1
```

> ⚠️ **WARNING:** `dict1 = dict2` does not copy; it creates a second reference to the same dict. Use `.copy()` for independence.

> 💡 **ADVANCED TIP – Dictionary comprehensions:**  
> `{k: v for k, v in original.items() if condition}` builds filtered copies elegantly.

---

## 💡 Real‑world Usage

**Banking – generate report of all account holders**
```python
accounts = {'A1': 5000, 'A2': 3200}
for id in accounts.keys():
    print(f"Account {id}")
```

**E‑commerce – list all product names**
```python
products = {'SKU-1': 'mouse', 'SKU-2': 'keyboard'}
print(list(products.values()))   # ['mouse', 'keyboard']
```

**Logistics – list item and weight pairs**
```python
packages = {'box1': 12, 'box2': 8}
for item, weight in packages.items():
    print(f"{item}: {weight}kg")
```

**HR – remove terminated employee record**
```python
staff = {'E001': 'Emperor', 'E002': 'Rahim'}
terminated = staff.pop('E002', 'Not found')
print(terminated)
```

**Reporting – create a duplicate of daily stats before resetting**
```python
daily = {'sales': 1200, 'traffic': 340}
backup = daily.copy()
daily.clear()
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | `d={'name':'Emperor','age':18}`. Print list of keys. | `['name', 'age']` |
| Medium | Same d. Print list of values. | `['Emperor', 18]` |
| Hard   | `d={'name':'Emperor','age':18}`. Pop the `'age'` key, print the popped value and the remaining dict on two lines. | `18`<br>`{'name': 'Emperor'}` |

Run the coach:
```bash
python ii_Practice_Sheets/L-39_Dictionary_Methods.py
```

---

## 📌 Key Takeaway
- `.keys()`, `.values()`, `.items()` return dynamic views; convert to list for static snapshots.
- `.pop(key)` removes and returns a value; `.popitem()` removes the last inserted pair.
- `.copy()` creates a shallow independent copy; `.clear()` empties the dict.
- `.setdefault()` initializes missing keys elegantly.
- These methods form the core of dictionary‑based data processing for reporting and data transformation.