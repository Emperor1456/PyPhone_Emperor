# 📘 PyPhone Emperor · Module 4  
# 📖 L‑36 – Recursion (Self‑Calling Functions)

---

## 🎯 OBJECTIVE  
Master **recursion** — a function calling itself to solve problems by breaking them into smaller, identical sub‑problems.  
Recursion is essential for tree structures, mathematical sequences, nested data, and divide‑and‑conquer algorithms.  
Every recursive solution needs a **base case** to stop and a **recursive case** that moves toward it.

---

## 🧱 BRICK 1 – The Recursive Pattern

A recursive function must have:
1. A **base case** — a condition that stops the recursion.
2. A **recursive case** — the function calls itself with a smaller/simpler input.

**① Factorial — product of all numbers from n down to 1**
```python
def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)   # recursive case

print(factorial(4))   # 24  (4×3×2×1)
```
- `factorial(4)` → `4 * factorial(3)` → `4 * 3 * factorial(2)` → `4 * 3 * 2 * factorial(1)`.  
- At `factorial(1)`, the base case returns 1, and the chain resolves backward.  
This is the Easy practice task.

**② Fibonacci — each number is the sum of the two before it**
```python
def fib(n):
    if n <= 1:          # base case: fib(0)=0, fib(1)=1
        return n
    return fib(n - 1) + fib(n - 2)   # recursive case

print(fib(5))   # 5  (sequence: 0,1,1,2,3,5)
```
- `fib(5)` = `fib(4) + fib(3)` = `(fib(3)+fib(2)) + (fib(2)+fib(1))` = ... = 5.  
This is the Medium practice task.

> 💡 **INSIGHT:** Recursion is a natural fit for problems with a self‑similar structure —  
> folders inside folders, reports within reports, or hierarchical data.

---

## 🧱 BRICK 2 – Building Lists with Recursion

**③ Countdown — building a descending list**
```python
def countdown(n):
    if n <= 0:                   # base case
        return []
    return [n] + countdown(n - 1)   # recursive case

print(countdown(5))   # [5, 4, 3, 2, 1]
```
- `countdown(5)` → `[5] + countdown(4)` → `[5] + [4] + countdown(3)` → ... → `[5,4,3,2,1]`.  
This is the Hard practice task — using recursion to generate a structured list.

**④ Summing a list recursively**
```python
def sum_list(lst):
    if not lst:            # base: empty list
        return 0
    return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4]))   # 10
```

**⑤ Reverse a string recursively**
```python
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string('PyPhone'))   # 'enohPyP'
```

> ⚠️ **WARNING:** Python has a recursion limit (~1000 calls).  
> If your base case never triggers, you'll get a `RecursionError`.  
> Always ensure the input moves toward the base case with each call.

> 💡 **ADVANCED TIP – Recursion vs. Iteration:**  
> Every recursive solution can be rewritten as a loop.  
> Choose recursion when it makes the logic cleaner — especially for tree traversal,  
> JSON processing, or any nested structure. Companion's memory search will use recursive descent.

---

## 💡 Real‑world Usage

**Banking – compound growth over years**
```python
def compound(principal, rate, years):
    if years == 0:
        return principal
    return compound(principal * (1 + rate), rate, years - 1)

print(compound(1000, 0.05, 3))   # 1157.625
```

**Logistics – traverse a package hierarchy**
```python
def count_packages(shipment):
    if not shipment:
        return 0
    return 1 + count_packages(shipment[1:])

print(count_packages(['Box1', 'Box2', 'Box3']))   # 3
```

**HR – organizational chart depth**
```python
def org_depth(node):
    if 'subordinates' not in node:
        return 0
    return 1 + max(org_depth(sub) for sub in node['subordinates'])
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Define recursive `factorial(n)`. Call with 4 and print. | `24` |
| Medium | Define recursive `fib(n)` returning nth Fibonacci (0-indexed). Call with 5 and print. | `5` |
| Hard   | Define recursive `countdown(n)` returning a list from n down to 1. Call with 5 and print. | `[5, 4, 3, 2, 1]` |

Run the coach:
```bash
python ii_Practice_Sheets/L-36_Recursion.py
```

---

## 📌 Key Takeaway
- Recursion is a function calling itself with a smaller input.
- Every recursion needs a **base case** to stop and a **recursive case** to continue.
- Use recursion for self‑similar problems: factorials, Fibonacci, nested structures.
- Avoid exceeding Python's recursion limit (~1000 calls).
- Recursive thinking is essential for trees, graphs, and JSON parsing — core to Companion's brain.