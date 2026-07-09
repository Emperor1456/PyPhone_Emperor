# 📘 PyPhone Emperor · Module 8  
# 📖 L‑59 – Advanced List & Dictionary Comprehensions (Data Transformation at Scale)

---

## 🎯 OBJECTIVE  
Master advanced comprehensions to build lists, dictionaries, and sets in a single, readable line.  
Use nested loops, conditional expressions, and filtering to transform business datasets —  
from filtering transaction logs to generating product lookup tables — with maximum efficiency.

---

## 🧱 BRICK 1 – Advanced List Comprehensions

**① Squares of a list (Easy practice)**
```python
squares = [x * x for x in [1, 2, 3]]
print(squares)   # [1, 4, 9]
```
This maps each element to its square — exactly the Easy task.

**② Conditionals in the expression (ternary mapping)**
```python
labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 6)]
print(labels)   # ['odd', 'even', 'odd', 'even', 'odd']
```

**③ Filtering with `if` at the end**
```python
evens = [x for x in range(20) if x % 2 == 0]
print(evens)   # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

**④ Nested loops – flattening a matrix**
```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)   # [1, 2, 3, 4, 5, 6]
```

> 💡 **INSIGHT:** List comprehensions are faster than equivalent `for` loops and keep transformations concise. For complex logic, however, a regular loop is clearer.

---

## 🧱 BRICK 2 – Dictionary and Set Comprehensions

**⑤ Dict comprehension – number to square (Medium practice)**
```python
d = {x: x * x for x in [1, 2, 3]}
print(d)   # {1: 1, 2: 4, 3: 9}
```
This maps keys to values in one shot — a lookup table.

**⑥ Dict comprehension with filtering**
```python
scores = {"Ana": 85, "Bob": 92, "Emperor": 78}
high = {name: score for name, score in scores.items() if score >= 80}
print(high)   # {'Ana': 85, 'Bob': 92}
```

**⑦ Set comprehension – unique lengths**
```python
words = ["apple", "banana", "cherry", "apple"]
lengths = {len(w) for w in words}
print(lengths)   # {5, 6}
```

**⑧ Even squares with filter (Hard practice)**
```python
even_squares = [x * x for x in range(1, 6) if (x * x) % 2 == 0]
print(even_squares)   # [4, 16]
```
Only squares that are even survive — a combination of mapping and filtering.

> ⚠️ **WARNING:** Avoid deeply nested comprehensions (more than two levels). They become hard to read and maintain.

> 💡 **ADVANCED TIP:** Use generator expressions `(...)` instead of list comprehensions when you don't need the whole list in memory, e.g., `sum(x*x for x in range(1000000))`.

---

## 💡 Real‑world Usage

**Banking – filter high‑value transactions**
```python
txns = [120, 45, 600, 80]
large = [t for t in txns if t > 100]
print(large)   # [120, 600]
```

**E‑commerce – price with tax mapping**
```python
prices = [100, 200, 300]
with_tax = [p * 1.1 for p in prices]
print(with_tax)   # [110.0, 220.0, 330.0]
```

**Logistics – build a tracking dictionary**
```python
tracking_ids = ['TRK-1', 'TRK-2', 'TRK-3']
tracking_status = {tid: 'pending' for tid in tracking_ids}
print(tracking_status)
```

**HR – list of employee emails**
```python
names = ['emperor', 'rahim']
emails = [f"{n}@pyphone.com" for n in names]
print(emails)
```

**Reporting – unique departments from a list**
```python
dept_list = ['Sales', 'Engineering', 'Sales', 'HR']
unique_depts = set(dept_list)
print(unique_depts)   # {'Engineering', 'HR', 'Sales'}
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Use list comprehension to create squares of `[1,2,3]` → `[1,4,9]`. Print the list. | `[1, 4, 9]` |
| Medium | Create dict comprehension `{x: x*x for x in [1,2,3]}`. Print the dict. | `{1: 1, 2: 4, 3: 9}` |
| Hard   | From `range(1,6)`, create list of squares only if the square is even. Print the list. | `[4, 16]` |

Run the coach:
```bash
python ii_Practice_Sheets/L-59_Advanced_Comprehensions.py
```

---

## 📌 Key Takeaway
- List comp: `[expr for var in iterable if cond]`.
- Dict comp: `{key: val for var in iterable if cond}`.
- Set comp: `{expr for var in iterable if cond}`.
- Use nested loops left‑to‑right; keep them shallow for readability.