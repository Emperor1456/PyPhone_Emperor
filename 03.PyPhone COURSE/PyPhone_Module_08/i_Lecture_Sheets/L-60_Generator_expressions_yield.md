# 📘 PyPhone Emperor · Module 8
# 📖 L‑60 – Generator Expressions & `yield`

---

## 🎯 OBJECTIVE
Learn to create **generators** — memory‑efficient iterables
that produce values one at a time, on demand. You’ll use
**generator expressions** for lazy evaluation and the
**`yield`** keyword to build custom generator functions.

---

## 🧱 BRICK 1 – Generator Expressions

A generator expression looks just like a list comprehension
but uses **parentheses** `()` instead of brackets `[]`.
It does not create a list in memory — it yields items lazily.

```python
squares = (x**2 for x in range(10))
print(squares)       # <generator object>
print(next(squares)) # 0
print(next(squares)) # 1
```

You can iterate with a `for` loop:
```python
for sq in (x**2 for x in range(5)):
    print(sq)
```
Output: 0, 1, 4, 9, 16

Use generator expressions when:
- The data source is huge (e.g., reading lines from a file).
- You only need to process items once.
- You want to save memory.

> 💡 **INSIGHT:** Summing a generator: `sum(x**2 for x in range(1000))`
> avoids building a 1000‑element list.

---

## 🧱 BRICK 2 – The `yield` Keyword

A function that contains `yield` becomes a **generator function**.
When called, it returns a generator object, and its body runs
only when you iterate over it.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num)   # 3, 2, 1
```

Each `yield` **pauses** the function and sends a value to the
caller. Execution resumes from that point on the next iteration.

### Example – reading large files lazily:
```python
def read_large_file(path):
    with open(path, "r") as f:
        for line in f:
            yield line.strip()
```

### Generator with multiple `yield`:
```python
def greetings():
    yield "Hello"
    yield "Hola"
    yield "Bonjour"
```

> ⚠️ **WARNING:** A generator is **exhausted** after one full
> iteration. To reuse, you must recreate it.

---

## 📌 Key Takeaway
- Generator expression: `(expr for var in iterable)`, returns a lazy iterator.
- `yield` makes a function a generator; it pauses and resumes.
- Generators save memory — values are produced on‑the‑fly.
- Use them for large data, infinite sequences, or pipeline processing.