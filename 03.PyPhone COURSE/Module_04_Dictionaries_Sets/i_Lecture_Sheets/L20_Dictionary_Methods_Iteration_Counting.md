# 📘 PyPhone Emperor v3.0 · Module 4
# 📖 L‑20 – Dictionary Methods, Iteration & Counting

---

## 🎯 OBJECTIVE — What You Will Master

> Full dictionary manipulation: keys, values, items, and counting patterns.

- 🔑 `.keys()`, `.values()`, `.items()` – extract data
- 🔁 Iteration – loops over keys, values, pairs
- 🧮 **Counting pattern** – using `.get()` to tally frequencies
- 🧹 `.pop()`, `.popitem()`, `.clear()` – removal
- 📋 `.update()` – merge dictionaries

---

## 🧱 EXTRACTING DATA

```python
user = {"name": "Emperor", "age": 18}
print(list(user.keys()))        # ['name', 'age']
print(list(user.values()))      # ['Emperor', 18]
print(list(user.items()))       # [('name', 'Emperor'), ('age', 18)]
```

---

## 🧱 ITERATION

```python
for key in user:
    print(key)

for value in user.values():
    print(value)

for key, value in user.items():
    print(f"{key} → {value}")
```

---

## 🧱 COUNTING WITH DICTIONARIES

```python
words = ["apple", "banana", "apple", "cherry"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts)   # {'apple': 2, 'banana': 1, 'cherry': 1}
```

---

## 🧱 REMOVING & MERGING

```python
age = user.pop("age")         # removes and returns value
last = user.popitem()         # removes last inserted pair
user.clear()                  # empty dict

d1 = {"a": 1}
d2 = {"b": 2}
d1.update(d2)                 # merge d2 into d1
```

> ⚠️ **WARNING:** `.pop()` raises `KeyError` if key missing; use `.pop(key, default)` to avoid.

---

## 💡 Real‑world Usage

**Banking – count transaction types**
```python
txns = ["deposit", "withdrawal", "deposit"]
cnt = {}
for t in txns: cnt[t] = cnt.get(t,0)+1
```

**E‑commerce – inventory summary**
```python
items = {"laptop": 5, "mouse": 12}
for product, qty in items.items():
    print(f"{product}: {qty}")
```

**HR – extract employee details**
```python
emp = {"id":101, "name":"Emperor", "dept":"Eng"}
print(emp.keys())
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Print all keys of a given dict. | `print(list(d.keys()))` |
| Medium | Iterate over items and print "key: value" pairs. | `for k,v in d.items(): print(f"{k}:{v}")` |
| Hard | Count occurrences of characters in a string using a dict. | `d[ch]=d.get(ch,0)+1` inside loop |

Run the coach:
```bash
python ii_Practice_Sheets/L20_Dictionary_Methods_Iteration_Counting.py
```

---

## 📌 Key Takeaway
- `.items()` is your main iteration tool.
- The counting pattern `dict.get(key, 0)+1` is essential.
- Use `.pop()` for safe removal, `.update()` for merging.

*For Emperor.*