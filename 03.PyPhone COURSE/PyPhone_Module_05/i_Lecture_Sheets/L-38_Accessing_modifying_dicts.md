# 📘 PyPhone Emperor · Module 5  
# 📖 L‑38 – Accessing & Modifying Dictionaries (Data Manipulation)

---

## 🎯 OBJECTIVE  
Master accessing, adding, updating, and removing key‑value pairs in dictionaries.  
These operations are the core of any dynamic business system — updating customer records, incrementing counters, merging configurations, and safely retrieving data.

---

## 🧱 BRICK 1 – Reading and Writing Keys

Dictionaries are mutable; you can change them on the fly.

**① Access a value by key (Easy practice)**
```python
d = {'name': 'Emperor', 'age': 18}
print(d['name'])   # 'Emperor'
```
Direct access is fast, but raises `KeyError` if the key is missing.

**② Add a new key‑value pair (Medium practice)**
```python
d = {'name': 'Emperor', 'age': 18}
d['city'] = 'Dhaka'
print(d)   # {'name': 'Emperor', 'age': 18, 'city': 'Dhaka'}
```
Just assign to a new key. Existing keys update; missing keys create.

**③ Update an existing value (Hard practice)**
```python
d = {'name': 'Emperor', 'age': 18}
d['age'] += 1          # increment age
print(d)               # {'name': 'Emperor', 'age': 19}
```
Perfect for counters, status fields, or balance adjustments.

> 💡 **INSIGHT:** Assignment `dict[key] = value` is the primary way to insert or modify data.

---

## 🧱 BRICK 2 – Removing, Merging, and Safe Access

**④ Remove a key with `.pop()`**
```python
d = {'name': 'Emperor', 'age': 18}
age = d.pop('age')     # removes and returns value
print(age)             # 18
print(d)               # {'name': 'Emperor'}
```
Use `.pop(key, default)` to avoid errors if key missing.

**⑤ Remove with `del`**
```python
del d['name']          # deletes the key; KeyError if absent
```

**⑥ Merge dictionaries with `.update()`**
```python
d = {'name': 'Emperor'}
d.update({'age': 18, 'city': 'Dhaka'})
print(d)   # {'name': 'Emperor', 'age': 18, 'city': 'Dhaka'}
```

**⑦ Safe retrieval with `.get()` and default**
```python
print(d.get('phone', 'Not provided'))   # 'Not provided'
```

**⑧ Conditional update using `.setdefault()`**
```python
inventory = {'laptop': 5}
inventory.setdefault('mouse', 0)   # adds only if missing
inventory['mouse'] += 1
print(inventory)                    # {'laptop': 5, 'mouse': 1}
```

> ⚠️ **WARNING:** Direct access (`dict[key]`) crashes on missing keys. Prefer `.get()` or check with `in`.

> 💡 **ADVANCED TIP – Dictionary merging with `|` (Python 3.9+):**  
> `merged = d1 | d2` creates a new combined dictionary. Clean and readable.

---

## 💡 Real‑world Usage

**Banking – update account balance**
```python
account = {'id': 'A1', 'balance': 500}
account['balance'] += 200
print(account['balance'])   # 700
```

**E‑commerce – modify shopping cart**
```python
cart = {'items': 3}
cart['items'] += 1   # add one more item
```

**Logistics – set shipping address**
```python
order = {'id': 101}
order['address'] = '123 Main St, Dhaka'
print(order)
```

**HR – update employee record**
```python
emp = {'name': 'Emperor', 'title': 'Intern'}
emp['title'] = 'Junior Developer'
emp['salary'] = 50000
print(emp)
```

**Reporting – safe data extraction**
```python
data = {'sales': 1200}
tax = data.get('tax_rate', 0.1) * data['sales']
print(f"Tax: {tax}")
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | `d={'name':'Emperor','age':18}`. Print the value of `'name'`. | `Emperor` |
| Medium | `d={'name':'Emperor','age':18}`. Add key `'city'='Dhaka'`, then print d. | `{'name': 'Emperor', 'age': 18, 'city': 'Dhaka'}` |
| Hard   | `d={'name':'Emperor','age':18}`. Increment age by 1, print the updated dict. | `{'name': 'Emperor', 'age': 19}` |

Run the coach:
```bash
python ii_Practice_Sheets/L-38_Accessing_Modifying_Dicts.py
```

---

## 📌 Key Takeaway
- `dict[key]` reads/writes; add new pairs by assigning to a new key.
- Use `.pop()` to remove and retrieve, `del` to just delete.
- `.update()` merges another dictionary in place.
- `.get()` and `.setdefault()` provide safe, elegant default handling.
- Mastering dictionary manipulation is essential for data‑driven applications, including Companion's dynamic memory.