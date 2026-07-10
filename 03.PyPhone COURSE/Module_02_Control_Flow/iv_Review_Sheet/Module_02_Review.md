# 📘 Module 02 – Control Flow · Revision Guide

---

## L08 – if, elif, else – Business Rules

- `if` executes a block only when the condition is `True`.
- `else` runs when the condition is `False`.
- `elif` chains multiple exclusive conditions; the first match wins.
- Order matters: put the strictest condition first.

```python
income = 45000
if income >= 50000:
    print("High tax")
elif income >= 20000:
    print("Medium tax")
else:
    print("Low tax")
```

---

## L09 – Nested Conditionals & match‑case

- Nested `if` tests secondary conditions only after the primary passes.
- Use `and`/`or` to flatten when possible.
- `match`‑`case` (Python 3.10+) is a cleaner alternative to long `if‑elif` chains.
- Use guards (`if`) and wildcard (`_`) for complex patterns.

```python
choice = 2
match choice:
    case 1: print("Balance inquiry")
    case 2: print("Cash withdrawal")
    case _: print("Invalid")
```

---

## L10 – while Loops – Sentinel‑Controlled Repetition

- `while condition:` repeats as long as the condition is `True`.
- Always update the controlling variable to avoid infinite loops.
- Sentinel pattern: stop when a special value is encountered.
- `while True` + `break` is common for interactive menus.

```python
total = 0
i = 1
while i <= 4:
    total += i
    i += 1
print(total)   # 10
```

---

## L11 – for Loops, range(), enumerate(), zip()

- `for item in iterable:` visits each element.
- `range(start, stop, step)` generates integer sequences.
- `enumerate(seq, start)` provides index and value.
- `zip(seq1, seq2)` pairs elements; stops at the shortest.

```python
items = ['Laptop', 'Mouse', 'Keyboard']
for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")
```

---

## L12 – Loop Control – break, continue, pass

- `break` exits the loop immediately.
- `continue` skips the rest of the current iteration and moves to the next.
- `pass` is a no‑op placeholder.
- Use `break` for early exit, `continue` for filtering.

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)   # prints 1..4
```

---

**Quick Test:**  
- What is the difference between `elif` and a nested `if`?  
- How can you avoid an infinite `while` loop?  
- When would you use `enumerate()` instead of a simple `for` loop?  
- What happens if you forget `break` in a `while True` loop?

*Review complete. You are now ready for the Module 02 Practice Review.*