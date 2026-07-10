# 📘 PyPhone Emperor v3.0 · Module 5
# 📖 L‑31 – Recursion & Memoization

---

## 🎯 OBJECTIVE — What You Will Master

> Functions that call themselves – elegant solutions to self‑similar problems.

- 🔁 **Recursion** – a function calling itself with a smaller input
- 🛑 **Base case** – stops the recursion
- ⚡ **Recursive case** – breaks the problem down
- 🧠 **Memoization** – caching results to avoid recomputation
- ⚠️ **Recursion limit** – Python’s default ~1000 calls

---

## 🧱 CLASSIC RECURSION – FACTORIAL

```python
def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)
print(factorial(5))   # 120
```

---

## 🧱 FIBONACCI & THE COST

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(6))   # 8
```

This is inefficient because it recomputes the same values many times.

---

## 🧱 MEMOIZATION WITH `functools.lru_cache`

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(100))   # instant!
```

> ⚠️ **WARNING:** Python limits recursion to ~1000 frames. Deep recursion without a base case will raise `RecursionError`.

---

## 💡 Real‑world Usage

**Banking – compound interest recursively**
```python
def compound(p, r, t):
    if t == 0:
        return p
    return compound(p * (1+r), r, t-1)
```

**E‑commerce – category tree traversal**
```python
def count_products(category):
    if not category["subcategories"]:
        return len(category["products"])
    return len(category["products"]) + sum(count_products(sub) for sub in category["subcategories"])
```

**Logistics – route depth**
```python
def max_depth(route):
    if not route["connections"]:
        return 1
    return 1 + max(max_depth(conn) for conn in route["connections"])
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Recursive factorial of 4. | `def factorial(n): ...; print(factorial(4))` |
| Medium | Fibonacci of 5. | `def fib(n): ...; print(fib(5))` |
| Hard | Countdown from 5 using recursion, returning a list. | `def countdown(n): return [n] + countdown(n-1) if n>0 else []` |

Run the coach:
```bash
python ii_Practice_Sheets/L31_Recursion_Memoization.py
```

---

## 📌 Key Takeaway
- Recursion breaks a problem into smaller copies of itself.
- Always define a base case.
- Memoization dramatically speeds up repeated recursive calls.

*For Emperor.*