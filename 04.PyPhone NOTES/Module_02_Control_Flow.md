# 📘 Module 02 – Control Flow · Revision Note

---

## L08 – if, elif, else – Business Rules
- `if condition:` executes block when `True`.
- `else:` runs when condition is `False`.
- `elif:` chains exclusive conditions; first match wins.
- Order matters: strictest condition first.

```python
income = 45000
if income >= 50000:     print("High tax")
elif income >= 20000:   print("Medium tax")
else:                   print("Low tax")
```

---

## L09 – Nested Conditionals & match‑case
- Nested `if` tests secondary conditions only after primary passes.
- Flatten with `and`/`or` when possible.
- `match`‑`case` (Python 3.10+) is cleaner than long `if‑elif`.
- Use guards (`if`) and wildcard `_`.

```python
choice = 2
match choice:
    case 1: print("Balance inquiry")
    case 2: print("Cash withdrawal")
    case _: print("Invalid")
```

---

## L10 – while Loops – Sentinel‑Controlled Repetition
- `while condition:` repeats as long as `True`.
- Always update the controlling variable.
- Sentinel: stop when a special value is reached.
- `while True` + `break` for interactive menus.

```python
total, i = 0, 1
while i <= 4:
    total += i
    i += 1
print(total)   # 10
```

---

## L11 – for Loops, range(), enumerate(), zip()
- `for item in iterable:` visits each element.
- `range(start, stop, step)` generates integer sequences.
- `enumerate(seq, start)` provides index + value.
- `zip(seq1, seq2)` pairs elements; stops at shortest.

```python
items = ["Laptop", "Mouse", "Keyboard"]
for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")
```

---

## L12 – Loop Control – break, continue, pass
- `break` exits the loop immediately.
- `continue` skips the rest of this iteration.
- `pass` is a no‑op placeholder.

```python
for i in range(1, 10):
    if i == 5: break
    print(i)   # prints 1..4
```

---

*Quick Test:*  
- Difference between `elif` and nested `if`?  
- How to avoid infinite `while`?  
- When to use `enumerate()`?  
- What happens if you forget `break` in `while True`?