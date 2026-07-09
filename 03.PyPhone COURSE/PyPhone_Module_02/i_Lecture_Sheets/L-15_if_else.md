# 📘 PyPhone Emperor · Module 2  
# 📖 L‑15 – `if-else` in Binary Decisions

---

## 🎯 OBJECTIVE
Learn to use the `if-else` statement to make
two‑way decisions in Python.
When the condition is `True`, one block runs;
otherwise, the `else` block runs.
This is the backbone of every binary business rule,
from approving orders to classifying customers.

---

## 🧱 BRICK 1 – The `if-else` Structure

An `if-else` statement gives your program exactly two paths.

```python
if condition:
    # runs when condition is True
else:
    # runs when condition is False
```

**Crucial:** Only **one** of the two blocks ever executes.
The indentation must be consistent (4 spaces per level).

**Simple business example – customer status:**
```python
a = 3
if a > 0:
    print("A")
else:
    print("B")
```
Because `3 > 0` is `True`, the program prints `"A"`.
If `a` were `-1`, it would print `"B"`.

**The flow:**
```
       ┌─────────────┐
       │  condition? │
       └──────┬──────┘
          True│False
      ┌───────┐   ┌───────┐
      │  if   │   │ else  │
      └───────┘   └───────┘
```

> 💡 **INSIGHT:** An `if` without `else` simply does nothing
> when the condition is false. Adding `else` guarantees
> that **exactly one** of the two branches executes.

---

## 🧱 BRICK 2 – Using `if-else` for Multiple Checks

You can write several independent `if-else` statements
one after another to test different conditions.
Each is evaluated separately.

**Business example – categorise a number by sign and parity:**
```python
n = 8

# Check parity (even or odd)
if n % 2 == 0:
    parity = "Even"
else:
    parity = "Odd"

# Check sign (positive or negative)
if n >= 0:
    sign = "Positive"
else:
    sign = "Negative"

print(parity)    # Even
print(sign)      # Positive
```

`n = 8` is even and non‑negative, so the output is:
```
Even
Positive
```

**Another example – check a transaction limit:**
```python
amount = 2500
limit  = 2000

if amount <= limit:
    print("Approved")
else:
    print("Declined")
```
Here, `2500 <= 2000` is `False`, so `"Declined"` prints.

> ⚠️ **WARNING:** Do **not** confuse `=` (assignment) with
> `==` (equality). An `if x = 5:` is a syntax error.
> Always use `==` inside conditions.

---

## 💡 Real‑world Usage

Every business rule that has only two possible outcomes
is built with `if-else`.

**Inventory check:**
```python
stock = 10
order = 15

if order <= stock:
    print("Order fulfilled")
else:
    print("Out of stock")
```

**Credit card verification:**
```python
balance = 300
purchase = 250

if purchase <= balance:
    balance -= purchase
    print("Payment successful")
else:
    print("Insufficient funds")
```

**Customer tier:**
```python
points = 1200
if points >= 1000:
    print("Gold member")
else:
    print("Silver member")
```

---

## 🔍 Practice Preview
You will write three small decision scripts.

- **Easy:** Given `a = 3`, print `"A"` if `a > 0`, otherwise `"B"`.
- **Medium:** Given `x = -5`, print `"Positive"` if `x >= 0`, otherwise `"Negative"`.
- **Hard:** Given `n = 8`, print `"Even"` or `"Odd"` on the first line,
  and `"Positive"` or `"Negative"` on the second line.

Run the practice coach:
```bash
python ii_Practice_Sheets/L-15_if_else.py
```

Choose your level, type the script, and the engine will verify your output.

---

## 📌 Key Takeaway
- `if-else` creates exactly two execution paths.
- The `else` block runs when the `if` condition is `False`.
- You can use multiple independent `if-else` statements to check different properties.
- Always indent consistently and use `==` for comparisons.
- This is the simplest and most common business rule pattern.