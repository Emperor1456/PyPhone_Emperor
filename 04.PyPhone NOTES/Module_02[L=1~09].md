# 📘 PyPhone Emperor · Module 2  
# 🗃️ Comprehensive Note – Control Flow & Loops

---

## 🎯 Scope
This note covers every decision‑making and repetition tool from Module 2.  
It is a single‑page reference for `if`, `elif`, `else`, `match‑case`, `while`, `for`, `break`, `continue`, and `pass`.  
All code fits a phone screen; no sideways scrolling.

---

## 🧱 1. `if` Statement
Executes a block only when the condition is `True`.

```python
if temperature > 30:
    print("Hot day")
```
- Indentation is mandatory (4 spaces is the standard).
- The condition can be any expression that evaluates to `True` or `False`.

---

## 🧱 2. `if‑else`
Provides a two‑way branch.  
One block runs when the condition is `True`, the other when it is `False`.

```python
if score >= 60:
    print("Pass")
else:
    print("Fail")
```
- Exactly one of the two blocks runs.

---

## 🧱 3. `if‑elif‑else` Chain
Tests multiple conditions in order.  
The first `True` branch runs; the rest are ignored.

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```
- You can have as many `elif` blocks as needed.
- Order matters – put the most restrictive conditions first.

---

## 🧱 4. Nested Conditionals
An `if` (or any conditional) inside another `if`.

```python
if is_logged_in:
    if is_admin:
        print("Admin panel")
    else:
        print("User dashboard")
```
- Inner block runs only when outer condition is already `True`.
- Deep nesting harms readability; prefer logical operators where possible.

---

## 🧱 5. `match‑case` (Pattern Matching)
A modern way to compare a value against multiple patterns (Python 3.10+).

```python
match command:
    case "start":
        print("Starting…")
    case "stop":
        print("Stopping…")
    case _:
        print("Unknown")
```
- `_` is a wildcard that matches anything (like `else`).
- Can destructure tuples, lists, and use guard clauses (`if` inside a case).

---

## 🔁 6. `while` Loop
Repeats a block while a condition is `True`.

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```
- The loop must eventually make the condition `False`, or it will run forever.
- Use `Ctrl+C` to interrupt an infinite loop.

---

## 🔁 7. `for` Loop
Iterates over a sequence (range, string, list, etc.).

```python
for i in range(1, 6):
    print(i)
```
- `range(start, stop, step)` generates a sequence of integers.
- Can iterate directly over any iterable.

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

---

## 🛑 8. `break` and `continue`
- **`break`** – exits the loop immediately.
- **`continue`** – skips the rest of the current iteration and moves to the next.

```python
for i in range(1, 10):
    if i == 5:
        break          # stops at 4
    if i % 2 == 0:
        continue       # skips evens
    print(i)           # prints only odds
```

---

## ⏸️ 9. `pass` Statement
A placeholder that does nothing.  
Used when syntax requires an indented block but you have no code yet.

```python
if True:
    pass          # no action, just a placeholder
```

---

## 💡 Quick Reference
```python
# if-elif-else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

# match-case
command = "start"
match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case _:
        print("Unknown")

# while loop
total = 0
while total < 10:
    total += 1

# for loop
for i in range(1, 6):
    print(i)

# break & continue
for n in range(10):
    if n == 3:
        continue
    if n == 8:
        break
    print(n)

# pass
def future_feature():
    pass
```

---

## 📌 Key Takeaway
- Conditionals (`if`, `elif`, `else`, `match`) control the flow of decisions.
- Loops (`while`, `for`) repeat code; use `break` to stop early and `continue` to skip steps.
- `pass` is a silent placeholder for unfinished blocks.
- Indentation is the only way to define blocks in Python — keep it consistent.

*Study this sheet. Recall it from memory. Then practice.*