# 📘 PyPhone Emperor · Module 2
# 📖 L‑18 – `match-case` (Pattern Matching)

---

## 🎯 OBJECTIVE
Learn Python’s modern **`match`** statement,
introduced in Python 3.10.
It compares a value against a series of **patterns**
and executes the first matching block.
Think of it as a cleaner `if‑elif‑elif` chain
when you are checking the same variable repeatedly.

---

## 🧱 BRICK 1 – Basic Syntax

```python
match variable:
    case pattern1:
        # runs if variable matches pattern1
    case pattern2:
        # runs if variable matches pattern2
    case _:
        # runs if no other pattern matched
```

`_` is a **wildcard** — it matches anything.
It works like `else` in an `if` chain.

**Example:**
```python
command = "stop"
match command:
    case "start":
        print("Engine started")
    case "stop":
        print("Engine stopped")
    case "pause":
        print("Engine paused")
    case _:
        print("Unknown command")
```
Output: `Engine stopped`

> 💡 **INSIGHT:** `match` checks patterns **top to bottom**.
> The first matching case executes; later cases are ignored.

---

## 🧱 BRICK 2 – Patterns Beyond Simple Values

`match` is powerful — it can destructure data,
match types, and use guard clauses (`if` inside cases).

**Matching with a guard:**
```python
value = 12
match value:
    case x if x < 0:
        print("Negative")
    case x if x == 0:
        print("Zero")
    case x if x > 0:
        print("Positive")
```

**Matching data structures:**
```python
point = (0, 5)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On Y-axis at {y}")
    case (x, 0):
        print(f"On X-axis at {x}")
    case (x, y):
        print(f"Point at ({x}, {y})")
```
Here `point` matches the second case, printing `On Y-axis at 5`.

> ⚠️ **WARNING:** `match` requires Python 3.10+.
> Your Termux Python is likely recent enough, but verify with
> `python --version` if you get a SyntaxError.

---

## 📌 Key Takeaway
- `match` compares a value against multiple patterns.
- `case _` is the fallback, like `else`.
- Guards (`if`) add conditions to a pattern.
- Destructuring works on tuples, lists, and more.