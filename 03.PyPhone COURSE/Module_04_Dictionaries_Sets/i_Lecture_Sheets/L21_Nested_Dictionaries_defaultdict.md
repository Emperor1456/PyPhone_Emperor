# 📘 PyPhone Emperor v3.0 · Module 4
# 📖 L‑21 – Nested Dictionaries & `defaultdict`

---

## 🎯 OBJECTIVE — What You Will Master

> Complex data structures with nested dicts and automatic defaults.

- 🧩 **Nested dicts** – dict inside dict, representing hierarchical data
- 🔧 **`defaultdict`** – from `collections`, auto‑creates missing keys
- 🧪 **Real‑world** – JSON‑like structures, multi‑level configurations

---

## 🧱 NESTED DICTIONARIES

```python
employees = {
    "emp001": {"name": "Emperor", "age": 18, "dept": "Engineering"},
    "emp002": {"name": "Rahim", "age": 25, "dept": "Sales"}
}
print(employees["emp001"]["name"])   # Emperor
```

**Add nested data:**
```python
employees["emp003"] = {"name": "Karim", "age": 30, "dept": "HR"}
```

---

## 🧱 `defaultdict` – NO MORE KEY ERRORS

A `defaultdict` automatically creates a value for missing keys based on a factory function.

```python
from collections import defaultdict

# Group items by first letter
words = ["apple", "banana", "cherry", "avocado"]
by_letter = defaultdict(list)
for w in words:
    by_letter[w[0]].append(w)
print(dict(by_letter))   # {'a': ['apple', 'avocado'], 'b': ['banana'], 'c': ['cherry']}
```

**Counting with `defaultdict(int)`:**
```python
counts = defaultdict(int)
for letter in "mississippi":
    counts[letter] += 1
print(dict(counts))   # {'m':1, 'i':4, 's':4, 'p':2}
```

> ⚠️ **WARNING:** `defaultdict` only helps when accessing keys; if you check `if "key" in dd`, missing keys won't be created.

---

## 💡 Real‑world Usage

**Banking – account with nested transactions**
```python
accounts = {
    "A1": {"balance": 500, "txns": [100, -50]},
    "A2": {"balance": 300, "txns": [200]}
}
```

**E‑commerce – product categories**
```python
products = defaultdict(list)
products["Electronics"].append("Laptop")
products["Electronics"].append("Mouse")
```

**Logistics – route stops**
```python
routes = {
    "R1": {"stops": ["A","B","C"], "distance": 120},
    "R2": {"stops": ["D","E"], "distance": 80}
}
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Create a nested dict with two keys, each containing a dict, and print it. | `d={"a":{"x":1},"b":{"y":2}}; print(d)` |
| Medium | Access a value deep inside the nested dict and print it. | `print(d["a"]["x"])` |
| Hard | Use `defaultdict(list)` to group items by their length. | `from collections import defaultdict; dd=defaultdict(list); for w in words: dd[len(w)].append(w)` |

Run the coach:
```bash
python ii_Practice_Sheets/L21_Nested_Dictionaries_defaultdict.py
```

---

## 📌 Key Takeaway
- Nested dicts model complex, real‑world data.
- `defaultdict` eliminates repetitive `if key in dict` checks.
- Factory functions: `list`, `int`, `set`, etc.

*For Emperor.*