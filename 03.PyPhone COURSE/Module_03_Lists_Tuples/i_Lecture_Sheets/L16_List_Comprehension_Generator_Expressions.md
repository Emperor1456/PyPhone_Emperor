# 📘 PyPhone Emperor v3.0 · Module 3
# 📖 L‑16 – List Comprehension & Generator Expressions

---

## 🎯 OBJECTIVE — What You Will Master

> Write concise, powerful list transformations in one line.

- 🧠 **List comprehension** – `[expr for item in iterable if cond]`
- 🔍 **Filtering** – keep only elements that satisfy a condition
- ⚡ **Generator expressions** – lazy evaluation with parentheses
- 🧪 **Real‑world** – data cleaning, report generation

---

## 🧱 LIST COMPREHENSION

```python
squares = [x**2 for x in range(10)]
print(squares)   # [0,1,4,9,16,25,36,49,64,81]
```

**Business – apply tax to prices**
```python
prices = [100, 200, 300]
with_tax = [p * 1.1 for p in prices]
print(with_tax)
```

**Filter with `if`:**
```python
evens = [x for x in range(20) if x % 2 == 0]
print(evens)   # [0,2,4,6,8,10,12,14,16,18]
```

**Business – filter out‑of‑stock items**
```python
stock = [12, 0, 5, 0, 8]
in_stock = [s for s in stock if s > 0]
print(in_stock)
```

---

## 🧱 GENERATOR EXPRESSIONS

Replace `[]` with `()` for lazy evaluation.

```python
squares_gen = (x**2 for x in range(10))
print(next(squares_gen))   # 0
print(next(squares_gen))   # 1
```

**Business – sum of prices without creating a new list**
```python
total = sum(p * 1.1 for p in prices)   # no intermediate list
print(total)
```

> ⚠️ **WARNING:** Generators are exhausted after one pass. Convert to list if you need to reuse.

---

## 💡 Real‑world Usage

**Banking – filter large transactions**
```python
txns = [120, 600, 80]
large = [t for t in txns if t > 100]
```

**E‑commerce – generate SKU list**
```python
skus = [f"SKU-{i:03d}" for i in range(1, 6)]
```

**Logistics – compute weights**
```python
boxes = [5, 10, 15]
total_weight = sum(w * 0.5 for w in boxes)
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Square each number in `[1,2,3]` with a comprehension. | `[x*x for x in [1,2,3]]` |
| Medium | Create a list of even numbers from 1 to 10 using comprehension. | `[x for x in range(1,11) if x%2==0]` |
| Hard | Use a generator expression to sum the lengths of words in `["apple","banana","cherry"]`. | `sum(len(w) for w in words)` |

Run the coach:
```bash
python ii_Practice_Sheets/L16_List_Comprehension_Generator_Expressions.py
```

---

## 📌 Key Takeaway
- List comprehension: `[expr for var in iterable if cond]`.
- Generator expression: `(expr for var in iterable)` – lazy.
- Use comprehension for clarity; generator for memory efficiency.

*For Emperor.*