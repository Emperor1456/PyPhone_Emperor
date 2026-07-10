# 📘 PyPhone Emperor v3.0 · Module 9
# 📖 L‑54 – Generator Expressions & `yield`

---

## 🎯 OBJECTIVE — What You Will Master

> Create memory‑efficient iterators for large or infinite sequences.

- ⚡ **Generator expression** – like a list comprehension, but lazy
- 🛠️ **`yield`** – turn a function into a generator
- 🧪 **Why generators** – handle infinite sequences, large files
- 🔁 **`next()`** – manually advance a generator

---

## 🧱 GENERATOR EXPRESSION

```python
squares = (x**2 for x in range(10))
print(next(squares))   # 0
print(next(squares))   # 1
```

Use in a loop:
```python
for sq in (x**2 for x in range(5)):
    print(sq)
```

---

## 🧱 GENERATOR FUNCTIONS WITH `yield`

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num)   # 3, 2, 1
```

Each `yield` pauses the function and returns a value; execution resumes from that point on the next call.

---

## 🧱 GENERATOR FOR LARGE FILES

```python
def read_large_file(filepath):
    with open(filepath, "r") as f:
        for line in f:
            yield line.strip()
```

This never loads the entire file into memory.

---

## 💡 Real‑world Usage

**Banking – stream transactions**
```python
def get_transactions(account_id):
    for tx in db.query("SELECT * FROM tx WHERE account=?", account_id):
        yield tx
```

**E‑commerce – paginate product list**
```python
def paginate(items, page_size):
    for i in range(0, len(items), page_size):
        yield items[i:i+page_size]
```

**Logistics – infinite shipment ID generator**
```python
def shipment_ids(prefix):
    i = 1
    while True:
        yield f"{prefix}-{i:05d}"
        i += 1
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Define a generator that yields 1, 2, 3 and print as a list. |
| Medium | Use a generator expression to sum squares of numbers. |
| Hard | Write a generator function for Fibonacci numbers and print the first 10. |

Run the coach:
```bash
python ii_Practice_Sheets/L54_Generator_Expressions_yield.py
```

---

## 📌 Key Takeaway
- Generators produce items on‑demand, saving memory.
- Use `yield` to create generator functions.
- Generator expressions are lazy versions of list comprehensions.

*For Emperor.*