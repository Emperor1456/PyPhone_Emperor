# 📘 PyPhone Emperor v3.0 · Module 2
# 📖 L‑11 – `for` Loops, `range()`, `enumerate()`, `zip()`

---

## 🎯 OBJECTIVE — What You Will Master

> Iterate over sequences like a pro – the workhorse of every data processing pipeline.

- 🔁 **`for` loop** – iterate over items in a sequence
- 🔢 **`range()`** – generate sequences of numbers
- 📇 **`enumerate()`** – get index and value together
- 🤝 **`zip()`** – iterate over multiple lists in parallel

---

## 🧱 THE `for` LOOP

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

The loop variable `fruit` takes each element in turn.

**Business example – total daily sales**
```python
sales = [150, 89, 320, 45]
total = 0
for amount in sales:
    total += amount
print(f"Total: ${total}")
```

---

## 🧱 `range()` – NUMBER GENERATOR

`range(start, stop, step)` generates integers from `start` (inclusive) to `stop` (exclusive).

```python
for i in range(1, 6):
    print(i)   # 1 2 3 4 5
```

`range(5)` → 0,1,2,3,4.  
`range(2, 10, 2)` → 2,4,6,8.

**Business – print receipt numbers**
```python
for receipt_no in range(1001, 1006):
    print(f"Receipt #{receipt_no}")
```

---

## 🧱 `enumerate()` – INDEX + VALUE

When you need the index while iterating.

```python
tasks = ["design", "code", "test"]
for idx, task in enumerate(tasks):
    print(f"{idx}: {task}")
```
Output:
```
0: design
1: code
2: test
```

**Business – number the invoice lines**
```python
items = ["Laptop", "Mouse", "Keyboard"]
for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")
```

---

## 🧱 `zip()` – PARALLEL ITERATION

Combine multiple lists element‑wise.

```python
names = ["Emperor", "Rahim"]
scores = [95, 88]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

**Business – match product names with prices**
```python
products = ["Widget", "Gadget"]
prices = [9.99, 19.99]
for product, price in zip(products, prices):
    print(f"{product}: ${price}")
```

> ⚠️ **WARNING:** `zip()` stops at the shortest list. To handle unequal lengths, use `itertools.zip_longest()`.

---

## 💡 Real‑world Usage

**Banking – apply interest to multiple accounts**
```python
balances = [1000, 2500, 500]
for i, bal in enumerate(balances):
    balances[i] = bal * 1.05
print(balances)
```

**E‑commerce – generate SKU list**
```python
prefixes = ["A", "B", "C"]
suffixes = [101, 102, 103]
for pre, suf in zip(prefixes, suffixes):
    print(f"SKU-{pre}{suf}")
```

**Logistics – calculate delivery days**
```python
distances = [100, 200, 300]
speeds = [50, 60, 70]
for dist, spd in zip(distances, speeds):
    days = dist / spd
    print(f"Delivery in {days:.1f} days")
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Sum a list of numbers `[1,2,3,4,5]` with a `for` loop. | `total=0; for x in [1,2,3,4,5]: total+=x` |
| Medium | Print each character of a string on a new line. | `for ch in "Emperor": print(ch)` |
| Hard | Given two lists of equal length (names, ages), print "Name is Age years old" for each. | Use `zip()` and f‑string |

Run the coach:
```bash
python ii_Practice_Sheets/L11_for_Loops_range_enumerate_zip.py
```

---

## 📌 Key Takeaway
- `for` iterates over any iterable (list, string, range, etc.).
- `range()` produces number sequences.
- `enumerate()` provides index along with value.
- `zip()` pairs multiple iterables together.

*For Emperor.*