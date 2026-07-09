# 📘 PyPhone Emperor · Module 5  
# 📖 L‑40 – Iterating Through Dictionaries (Processing Business Records)

---

## 🎯 OBJECTIVE  
Master dictionary iteration patterns: looping over keys, values, and key‑value pairs to process, filter, and transform business data.  
Use these techniques to generate reports, build summaries, and apply business rules to structured datasets.

---

## 🧱 BRICK 1 – Basic Iteration Over Keys, Values, and Items

**① List all keys (Easy practice using items)**
```python
d = {'name': 'Emperor', 'age': 18}
pairs = list(d.items())
print(pairs)   # [('name', 'Emperor'), ('age', 18)]
```
The Easy task expects the output of `.items()` as a list of tuples — this is your starting point for iteration.

**② Build a formatted string from items (Medium practice)**
```python
d = {'name': 'Emperor', 'age': 18}
result = ', '.join(f'{k}:{v}' for k, v in d.items())
print(result)   # 'name:Emperor, age:18'
```
This pattern is used to generate query strings, log entries, or readable summaries.

**③ Count values matching a condition (Hard practice)**
```python
d = {'a': 1, 'b': 2, 'c': 3}
count = sum(1 for v in d.values() if v % 2 == 0)
print(count)   # 1
```
Here we count even values — a common analytics task.

> 💡 **INSIGHT:** `for key in dict` is a shortcut for `for key in dict.keys()`. Use `.items()` when you need both key and value.

---

## 🧱 BRICK 2 – Advanced Iteration Patterns

**④ Filtering with conditions**
```python
scores = {'Ana': 85, 'Bob': 92, 'Emperor': 78}
high_scorers = {}
for name, score in scores.items():
    if score >= 80:
        high_scorers[name] = score
print(high_scorers)   # {'Ana': 85, 'Bob': 92}
```

**⑤ Building a frequency counter**
```python
words = ['apple', 'banana', 'apple', 'cherry']
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts)   # {'apple': 2, 'banana': 1, 'cherry': 1}
```

**⑥ Transforming keys and values**
```python
config = {'host': 'localhost', 'port': 8080}
env_vars = {k.upper(): str(v) for k, v in config.items()}
print(env_vars)   # {'HOST': 'localhost', 'PORT': '8080'}
```

> ⚠️ **WARNING:** Do not add or remove keys while iterating over the dictionary itself. Iterate over `list(d.keys())` if you need to modify the dict.

> 💡 **ADVANCED TIP – Dictionary comprehensions:**  
> `{k: v for k, v in d.items() if condition}` provides a concise way to filter and transform dicts.

---

## 💡 Real‑world Usage

**Banking – calculate total balance**
```python
accounts = {'A1': 500, 'A2': 320, 'A3': 100}
total = sum(accounts.values())
print(f"Total deposits: {total}")
```

**E‑commerce – list in‑stock products**
```python
inventory = {'laptop': 5, 'mouse': 0, 'keyboard': 3}
in_stock = {k: v for k, v in inventory.items() if v > 0}
print(in_stock)
```

**Logistics – print each shipment with weight**
```python
shipments = {'B1': 12, 'B2': 8, 'B3': 15}
for box, weight in shipments.items():
    print(f"{box}: {weight}kg")
```

**HR – find employees below salary threshold**
```python
salaries = {'Emperor': 50000, 'Rahim': 45000, 'Karim': 60000}
low_paid = [name for name, sal in salaries.items() if sal < 50000]
print(low_paid)
```

**Reporting – convert a record to JSON‑like string**
```python
record = {'date': '2026-07-09', 'sales': 1200}
line = ', '.join(f'"{k}": {v}' for k, v in record.items())
print(f'{{{line}}}')
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | `d={'name':'Emperor','age':18}`. Print all key‑value pairs as tuples using `items()`. | `[('name', 'Emperor'), ('age', 18)]` |
| Medium | Same d. Build a string `'name:Emperor, age:18'` and print it. | `name:Emperor, age:18` |
| Hard   | `d={'a':1,'b':2,'c':3}`. Count how many values are even, print count. | `1` |

Run the coach:
```bash
python ii_Practice_Sheets/L-40_Iterating_Through_Dicts.py
```

---

## 📌 Key Takeaway
- `for key in dict` iterates keys; `.items()` gives key‑value pairs.
- Use `.values()` to aggregate or filter by value.
- Dictionary comprehensions offer a concise way to build new dicts.
- When modifying during iteration, iterate over a static copy of keys.
- These patterns are fundamental for data processing in Companion’s memory retrieval and report generation.