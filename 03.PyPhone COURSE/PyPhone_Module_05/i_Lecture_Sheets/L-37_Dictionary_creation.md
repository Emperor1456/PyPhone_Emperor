# 📘 PyPhone Emperor · Module 5  
# 📖 L‑37 – Dictionary Creation & Key‑Value Pairs (Structured Business Data)

---

## 🎯 OBJECTIVE  
Master **dictionaries** — Python’s core mapping type — to store and retrieve structured business data.  
Dictionaries pair unique keys with values, allowing instant lookup of user profiles, product specs,  
config settings, and any data that needs fast, key‑based access.

---

## 🧱 BRICK 1 – Creating Dictionaries

A dictionary is defined with curly braces `{}` and colon‑separated `key: value` pairs.  
Keys must be immutable (strings, numbers, tuples); values can be anything.

**① Basic user profile**
```python
d = {'name': 'Emperor', 'age': 18}
print(d)   # {'name': 'Emperor', 'age': 18}
```
This is the Easy practice task — a simple employee or customer record.

**② Using the `dict()` constructor**
```python
info = dict(brand='Samsung', model='Galaxy')
print(info)   # {'brand': 'Samsung', 'model': 'Galaxy'}
```
The `dict()` constructor builds dictionaries from keyword arguments.  
This matches the Medium practice task — ideal for product specifications.

**③ Nested dictionaries for hierarchical data**
```python
person = {'name': 'Emperor', 'age': 18}
outer = {'person': person, 'city': 'Dhaka'}
print(outer)   # {'person': {'name': 'Emperor', 'age': 18}, 'city': 'Dhaka'}
```
A dictionary can contain another dictionary as a value, creating nested structures.  
This is the Hard practice task — use it to model orders with line items, addresses with coordinates, or configurations with sub‑sections.

**④ Mixed value types**
```python
config = {
    'host': 'localhost',
    'port': 8080,
    'debug': False,
    'tags': ['python', 'backend']
}
```

> 💡 **INSIGHT:** Keys are case‑sensitive and must be unique.  
> If you assign the same key twice, the last value overwrites the earlier one.

---

## 🧱 BRICK 2 – Accessing Values Safely

**⑤ Lookup by key (square brackets)**
```python
user = {'name': 'Emperor', 'age': 18}
print(user['name'])   # 'Emperor'
```
Raises a `KeyError` if the key doesn’t exist.

**⑥ Safe access with `.get()`**
```python
print(user.get('phone'))          # None (no error)
print(user.get('phone', 'N/A'))   # 'N/A' (custom default)
```
Use `.get()` when the key might be missing — this prevents runtime crashes.

**⑦ Adding and updating values**
```python
user['email'] = 'emperor@domain.com'   # add new pair
user['age'] = 19                        # update existing
```
Dictionaries are mutable; you can grow and modify them at any time.

> ⚠️ **WARNING:** Dictionaries are unordered in older Python versions, but from Python 3.7+ they maintain insertion order.  
> Always use keys for access, never rely on numeric indices.

> 💡 **ADVANCED TIP – Dictionary comprehensions (preview):**  
> `{k: v for k, v in pairs if condition}` builds a dict in one line.  
> This will be essential when you build Companion's memory index.

---

## 💡 Real‑world Usage

**Banking – store account details by account number**
```python
accounts = {
    'A100': {'name': 'Emperor', 'balance': 5000},
    'A101': {'name': 'Rahim', 'balance': 3200}
}
print(accounts['A100']['balance'])   # 5000
```

**E‑commerce – product catalog**
```python
products = {
    'SKU-001': {'name': 'Wireless Mouse', 'price': 24.99},
    'SKU-002': {'name': 'Keyboard', 'price': 49.99}
}
print(products['SKU-001']['name'])   # 'Wireless Mouse'
```

**Logistics – shipping addresses**
```python
address = {
    'street': '123 Main St',
    'city': 'Dhaka',
    'zip': '1212'
}
print(address['city'])   # 'Dhaka'
```

**HR – employee directory by ID**
```python
employees = {
    101: 'Emperor',
    102: 'Rahim',
    103: 'Karim'
}
print(employees[102])   # 'Rahim'
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Create a dict with keys `'name':'Emperor','age':18`. Print it. | `{'name': 'Emperor', 'age': 18}` |
| Medium | Create dict using `dict(brand='Samsung',model='Galaxy')`. Print it. | `{'brand': 'Samsung', 'model': 'Galaxy'}` |
| Hard   | Create nested dict: `person={'name':'Emperor','age':18}`, and outer dict with `'person':person, 'city':'Dhaka'`. Print outer. | `{'person': {'name': 'Emperor', 'age': 18}, 'city': 'Dhaka'}` |

Run the coach:
```bash
python ii_Practice_Sheets/L-37_Dictionary_Creation.py
```

---

## 📌 Key Takeaway
- Dictionaries store `key: value` pairs; keys must be unique and immutable.
- Create with `{}` or `dict()`; access with `dict[key]` or `.get()`.
- Nested dicts model complex, hierarchical business data.
- Dictionaries are the backbone of JSON, configs, and in‑memory databases — Companion's memory will be built on them.