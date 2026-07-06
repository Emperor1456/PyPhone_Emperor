# 📘 PyPhone Emperor · Module 4
# 📖 L‑36 – Recursion

---

## 🎯 OBJECTIVE
Learn to write functions that call **themselves** to solve
problems by breaking them into smaller, identical sub‑problems.
Recursion is a powerful tool for tree structures, mathematical
definitions, and divide‑and‑conquer algorithms.

---

## 🧱 BRICK 1 – The Recursive Pattern

A recursive function must have:
① A **base case** that stops the recursion.  
② A **recursive case** that calls the function with a
   simpler or smaller input, moving toward the base case.

**Classic example — factorial:**
```python
def factorial(n):
    if n <= 1:            # base case
        return 1
    return n * factorial(n - 1)  # recursive case

print(factorial(5))   # 120
```

The call stack for `factorial(5)`:
```
factorial(5) → 5 * factorial(4)
             → 5 * 4 * factorial(3)
             → 5 * 4 * 3 * factorial(2)
             → 5 * 4 * 3 * 2 * factorial(1)
             → 5 * 4 * 3 * 2 * 1 = 120
```

> 💡 **INSIGHT:** Every recursive solution can be written
> as a loop. Recursion is chosen when it makes the logic
> cleaner — for example, when traversing trees.

---

## 🧱 BRICK 2 – Common Recursive Patterns

**① Summing a list**
```python
def sum_list(lst):
    if not lst:              # base: empty list
        return 0
    return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4]))   # 10
```

**② Fibonacci numbers**
```python
def fib(n):
    if n <= 1:                # base: n=0 or n=1
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(6))   # 8   (sequence: 0,1,1,2,3,5,8)
```

> ⚠️ **WARNING:** Python has a recursion limit
> (default ~1000 calls). If a recursive function
> exceeds this, you get a `RecursionError`. Always
> ensure your base case is reachable.

**③ Directory tree traversal (conceptual)**
Recursion shines when exploring nested structures
like folders, JSON trees, or organizational charts.
You will use it heavily in later modules.

---

## 📌 Key Takeaway
- Recursion = a function that calls itself.
- Every recursion needs a **base case** to stop.
- The **recursive case** must move toward the base.
- Use recursion when the problem has a naturally
  self‑similar structure (trees, graphs, fractals).