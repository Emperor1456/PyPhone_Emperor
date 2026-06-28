# 📘 PyPhone Emperor · Module 8
# 📖 L‑59 – Advanced List & Dictionary Comprehensions

---

## 🎯 OBJECTIVE
Deepen your mastery of **comprehensions** — concise expressions
that build lists, dictionaries, and sets from iterables.
You'll go beyond basics and learn nested comprehensions,
conditionals in expressions, and multi‑variable patterns.

---

## 🧱 BRICK 1 – List Comprehensions with Conditionals

The classic list comprehension syntax:
```python
[expression for item in iterable if condition]
```

**Conditional at the end (filtering):**
```python
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

**Conditional in the expression (ternary mapping):**
```python
labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 6)]
# ['odd', 'even', 'odd', 'even', 'odd']
```

**Nested loops in a comprehension:**
```python
matrix = [[1,2],[3,4],[5,6]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6]
```
The loops are evaluated **left to right** — outer first.

---

## 🧱 BRICK 2 – Dictionary and Set Comprehensions

### Dictionary comprehensions
```python
{key_expr: value_expr for item in iterable if condition}
```

**Example – mapping squares:**
```python
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

**Example – filtering:**
```python
scores = {"Ana": 85, "Bob": 92, "Emperor": 78}
high = {name: score for name, score in scores.items() if score >= 80}
# {'Ana': 85, 'Bob': 92}
```

### Set comprehensions
```python
{expression for item in iterable if condition}
```

**Example – unique lengths:**
```python
words = ["apple", "banana", "cherry", "apple"]
lengths = {len(w) for w in words}
# {5, 6}
```

> ⚠️ **WARNING:** Although comprehensions are elegant, deep nesting
> harms readability. If logic is complex, use a regular `for` loop.

---

## 📌 Key Takeaway
- List comprehension: `[expr for var in iterable if cond]`
- Dict comprehension: `{key: val for var in iterable if cond}`
- Set comprehension: `{expr for var in iterable if cond}`
- Use nested loops left‑to‑right, conditionals at end or in expression.