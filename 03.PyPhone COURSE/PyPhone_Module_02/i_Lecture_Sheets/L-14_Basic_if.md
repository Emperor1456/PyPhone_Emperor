# 📘 PyPhone Emperor · Module 2  
# 📖 L‑14 – Basic `if` Statement in Business Decisions

---

## 🎯 OBJECTIVE
Learn to make decisions in Python using the **`if`** statement.  
When a condition is `True`, the indented code block runs.  
When it’s `False`, the block is skipped entirely.  
We’ll apply this to transaction validation and grade assignment –  
the foundation of every business rule engine.

---

## 🧱 BRICK 1 – Syntax and Indentation

An `if` statement consists of three parts:

① The keyword `if`  
② A condition that evaluates to `True` or `False`  
③ A colon `:` followed by an **indented block** of code  

```python
if condition:
    # this line runs only if condition is True
    statement
    statement
```

**Crucial:** The indented lines must be indented **exactly the same amount** (4 spaces is the standard).  
If you mix spaces and tabs, Python will crash.

**Minimal business example – approve a transaction:**
```python
amount = 1500
limit  = 1000

if amount <= limit:
    print("Transaction approved")
```
If `amount` is 1500 and `limit` is 1000, the condition `1500 <= 1000` is `False`, so nothing prints.  
If `amount` were 900, the message would appear.

---

## 🧱 BRICK 2 – Adding `else` for a Two‑Way Decision

Often you want to do one thing if the condition is true,
and a different thing if it’s false.
Use `else`:

```python
if condition:
    # runs when condition is True
else:
    # runs when condition is False
```

**Business example – validate an order:**
```python
x = 10   # order quantity
if x > 5:
    print("OK")
else:
    print("NO")
```
Here, because 10 > 5, the program prints `"OK"`.

**Another example – check if a number is even:**
```python
num = 4
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```
The expression `num % 2 == 0` checks the remainder after division by 2.
If zero, it’s even; otherwise, odd.

### The flow of an `if‑else` statement:
```
       ┌─────────────┐
       │  condition? │
       └──────┬──────┘
          True│False
      ┌───────┐   ┌───────┐
      │ block │   │ block │
      └───────┘   └───────┘
```

> 💡 **INSIGHT:** An `if` without `else` simply does nothing when the condition is false.  
> Adding `else` ensures **something** always happens.

---

## 💡 Real‑world Usage

**Transaction validation:**
```python
balance  = 500
withdraw = 300

if withdraw <= balance:
    balance -= withdraw
    print("Withdrawal successful")
    print("Remaining balance:", balance)
else:
    print("Insufficient funds")
```

**Grading system (multi‑branch preview):**
```python
score = 75
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```
The `elif` (short for “else if”) lets you check multiple conditions in order.
Only the first true branch runs. Here, `score` is 75, so "C" prints.

> ⚠️ **WARNING:** The order of `if` / `elif` / `else` matters.  
> Python stops at the **first** true condition.  
> If you wrote `if score >= 70` first, it would print "C" even for a 95.

---

## 🔍 Practice Preview
You will write small decision‑making scripts.

- **Easy:** Given `x = 10`, print `"OK"` if `x > 5`, otherwise `"NO"`.
- **Medium:** Given `num = 4`, print `"Even"` if it’s even, `"Odd"` otherwise.
- **Hard:** Given `score = 75`, print the letter grade:
  `A` (>=90), `B` (>=80), `C` (>=70), else `F`.

Run the practice coach:
```bash
python ii_Practice_Sheets/L-14_Basic_if.py
```

Choose your level, type the script, and the engine will verify your output.

---

## 📌 Key Takeaway
- `if condition:` runs the indented block only when the condition is `True`.
- Use `else` to define what happens when the condition is `False`.
- Use `elif` for multiple conditions checked in order.
- Always indent consistently (4 spaces).
- Business rules are built by chaining these simple decisions.