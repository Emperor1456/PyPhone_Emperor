# 📘 PyPhone Emperor v3.0 · Module 4
# 📖 L‑19 – Dictionary – Key‑Value Pairs & Hash Tables

---

## 🎯 OBJECTIVE — What You Will Master

> Dictionaries: the most important data structure in Python. Instant lookups.

- 📖 **Dictionary creation** – `{}`, `dict()`, mixed types
- 🔑 **Keys** – unique, immutable (strings, numbers, tuples)
- ⚡ **Hash tables** – O(1) average lookup time
- 🧪 **Access** – square brackets, `.get()`, `in`
- ✏️ **Mutation** – add/update pairs

---

## 🧱 CREATING DICTIONARIES

```python
user = {"name": "Emperor", "age": 18, "active": True}
empty = {}
config = dict(host="localhost", port=8080)
```

Keys are case‑sensitive; duplicates overwrite.

```python
d = {"a": 1, "a": 2}
print(d)   # {'a': 2}
```

---

## 🧱 ACCESSING VALUES

```python
print(user["name"])            # Emperor (KeyError if missing)
print(user.get("email"))       # None (safe)
print(user.get("email", "N/A"))# N/A (default)
```

Check existence:
```python
if "age" in user:
    print("Age present")
```

---

## 🧱 ADDING & UPDATING

```python
user["email"] = "emperor@pyphone.com"  # add
user["age"] = 19                        # update
```

---

## 💡 Real‑world Usage

**Banking – account by ID**
```python
accounts = {"A101": 5000, "A102": 3200}
print(accounts["A101"])
```

**E‑commerce – product catalog**
```python
catalog = {"SKU-1": "Mouse", "SKU-2": "Keyboard"}
```

**Logistics – tracking status**
```python
status = {"TRK-1": "in transit", "TRK-2": "delivered"}
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Create a dict with name, age and print it. | `d={"name":"Emperor","age":18}; print(d)` |
| Medium | Access a key safely using `.get()` and print the result. | `print(d.get("city","Not found"))` |
| Hard | Add a new key‑value pair and update an existing one, then print the dict. | `d["city"]="Dhaka"; d["age"]=19; print(d)` |

Run the coach:
```bash
python ii_Practice_Sheets/L19_Dictionary_Key_Value_Pairs_Hash_Tables.py
```

---

## 📌 Key Takeaway
- Dictionaries map unique keys to values; O(1) lookups.
- Use `.get()` for safe access; `in` to check existence.
- Keys must be immutable; strings and numbers are ideal.

*For Emperor.*