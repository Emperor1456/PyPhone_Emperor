# 📘 PyPhone Emperor · Module 8  
# 📖 L‑60 – Generator Expressions & `yield` (Lazy Data Pipelines)

---

## 🎯 OBJECTIVE  
Master generators — memory‑efficient iterables that produce values on the fly.  
Use generator expressions for lazy evaluation, and the `yield` keyword to build custom generator functions.  
Generators are essential for processing large data sets, infinite sequences, and streaming business data without loading everything into memory.

---

## 🧱 BRICK 1 – Generator Expressions

A generator expression looks like a list comprehension but uses parentheses `()` instead of brackets `[]`. It yields items lazily, one at a time.

```python
gen = (x*2 for x in range(3))
print(list(gen))   # [0, 2, 4]   (once exhausted, empty)
```

**① Simple generator function (Easy practice)**
```python
def gen():
    yield 1
    yield 2
    yield 3

print(list(gen()))   # [1, 2, 3]
```
Calling `gen()` returns a generator object. `list()` consumes it and builds a list.

**② Iterating directly (Medium practice)**
```python
for val in gen():
    print(val)
```
Output:
```
1
2
3
```
The loop requests each value, one at a time, printing them.

**③ Fibonacci generator (Hard practice)**
```python
def fib_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fib_gen(5)))   # [0, 1, 1, 2, 3]
```
`yield` pauses the function, remembering its state. The next iteration resumes right after `yield`.

> 💡 **INSIGHT:** Generators save memory because they don't store the entire sequence — only the current state.

---

## 🧱 BRICK 2 – Generator Functions and Business Pipelines

**④ Infinite sequence (truncated)**
```python
def infinite_evens():
    n = 0
    while True:
        yield n
        n += 2

from itertools import islice
first_five = list(islice(infinite_evens(), 5))
print(first_five)   # [0, 2, 4, 6, 8]
```

**⑤ Reading a large file lazily**
```python
def read_lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

# Usage: for line in read_lines('huge.log'): process(line)
```

**⑥ Summing a generator (no list built)**
```python
total = sum(x for x in range(1_000_000) if x % 2 == 0)
print(total)   # 249999500000 — no 1M‑element list created
```

> ⚠️ **WARNING:** Generators are one‑time use. Once iterated, they’re exhausted. Re‑create if you need to iterate again.

> 💡 **ADVANCED TIP – `yield from`:**  
> `yield from` delegates to another generator, useful for combining sub‑generators.

---

## 💡 Real‑world Usage

**Banking – stream transactions from a database**
```python
def get_transactions(account_id):
    # Simulated: yields one transaction at a time
    for tx in [100, -50, 200]:
        yield tx

for tx in get_transactions('A100'):
    print(f"Processing: {tx}")
```

**E‑commerce – generate product IDs on demand**
```python
def product_ids(prefix, start, count):
    for i in range(start, start + count):
        yield f"{prefix}-{i:04d}"

for pid in product_ids('SKU', 100, 5):
    print(pid)
```

**Logistics – batch shipment processing**
```python
def shipments():
    yield 'TRK-100'
    yield 'TRK-200'

for s in shipments():
    print(f"Shipment: {s}")
```

**HR – generate employee badges**
```python
def badge_numbers(start, count):
    for i in range(start, start + count):
        yield f"EMP-{i:03d}"

for badge in badge_numbers(1, 3):
    print(badge)
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Define generator `gen()` that yields 1, then 2, then 3. Print `list(gen())`. | `[1, 2, 3]` |
| Medium | Use the generator to print values one by one using a `for` loop. | `1`<br>`2`<br>`3` |
| Hard   | Define generator `fib_gen(n)` yielding first n Fibonacci numbers (0,1,1,2,3,...). Call with n=5 and print as list. | `[0, 1, 1, 2, 3]` |

Run the coach:
```bash
python ii_Practice_Sheets/L-60_Generator_Expressions.py
```

---

## 📌 Key Takeaway
- Generator expression: `(expr for var in iterable)` — lazy, memory‑friendly.
- `yield` makes a function a generator; it pauses and resumes.
- Generators are ideal for large data, streaming, and infinite sequences.
- Always regenerate after exhaustion; they’re single‑use iterators.