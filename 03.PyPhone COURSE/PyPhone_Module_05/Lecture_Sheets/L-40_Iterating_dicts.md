# 📘 PyPhone Emperor · Module 5
# 📖 L‑40 – Iterating Through Dictionaries

---

## 🎯 OBJECTIVE
Learn to loop over dictionaries efficiently.
You can iterate over keys, values, or both
at once. This is essential for processing
configuration data, user profiles, and
any structured information stored as dicts.

---

## 🧱 BRICK 1 – Looping Over Keys and Values

**Iterate over keys directly (default behavior):**
```python
user = {"name": "Emperor", "age": 18, "active": True}
for key in user:
    print(key)           # name, age, active
```

**Iterate over values:**
```python
for value in user.values():
    print(value)         # Emperor, 18, True
```

**Iterate over key‑value pairs:**
```python
for key, value in user.items():
    print(f"{key} → {value}")
```
Output:
```
name → Emperor
age → 18
active → True
```

> 💡 **INSIGHT:** `for key in dict` is a shortcut for
> `for key in dict.keys()`. Both work identically.

---

## 🧱 BRICK 2 – Practical Patterns

**① Filtering while iterating:**
```python
scores = {"Ana": 85, "Bob": 92, "Emperor": 78}
high_scorers = {}
for name, score in scores.items():
    if score >= 80:
        high_scorers[name] = score
print(high_scorers)   # {'Ana': 85, 'Bob': 92}
```

**② Building a lookup table:**
```python
words = ["apple", "banana", "apple", "cherry"]
count = {}
for w in words:
    count[w] = count.get(w, 0) + 1
print(count)   # {'apple': 2, 'banana': 1, 'cherry': 1}
```

**③ Transforming data:**
```python
config = {"host": "localhost", "port": 8080}
env_vars = {k.upper(): str(v) for k, v in config.items()}
print(env_vars)   # {'HOST': 'localhost', 'PORT': '8080'}
```

> ⚠️ **WARNING:** Do not modify the size of a dictionary
> (add or remove keys) while iterating over it directly.
> Iterate over a copy of keys instead: `for k in list(dict.keys())`.

---

## 📌 Key Takeaway
- `for k in dict` iterates keys.
- `dict.values()` gives values; `dict.items()` gives pairs.
- Use `.get()` for safe counting or defaults inside loops.
- Avoid changing dict size during iteration.