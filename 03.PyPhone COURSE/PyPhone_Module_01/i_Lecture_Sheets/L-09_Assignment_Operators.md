# 📘 PyPhone Emperor · Module 1  
# 📖 L‑09 – Assignment Operators

---

## 🎯 OBJECTIVE
Learn how to assign values to variables
and how to update variables using
assignment operators.
These are the most frequently used
operators in all of programming.

---

## 🧱 BRICK 1 – Basic Assignment and `+=`, `-=`

### Basic assignment `=`
The equals sign puts a value into a variable.
It does **not** mean mathematical equality.

```python
x = 10        # x is now 10
name = "Emperor"
is_active = True
```

### Add‑and‑assign `+=`
Adds a value to the variable, then stores
the result back in the same variable.

```python
x = 10
x += 5        # same as: x = x + 5
print(x)      # 15

# Works with strings too
msg = "Hello"
msg += " World"
print(msg)    # Hello World
```

### Subtract‑and‑assign `-=`
Subtracts a value from the variable.

```python
x = 20
x -= 7        # same as: x = x - 7
print(x)      # 13
```

> 💡 **NOTE:** Compound assignment operators are syntactic sugar — they make code shorter and often clearer.

---

## 🧱 BRICK 2 – Why Use Compound Assignment

### Cleaner, more readable code
Instead of:
```python
counter = counter + 1
total = total - discount
```
Write:
```python
counter += 1
total -= discount
```

### Enterprise example — accumulating totals
```python
# Track daily sales
daily_total = 0
daily_total += 150.00    # morning sale
daily_total += 89.50     # afternoon sale
daily_total += 320.00    # evening sale
print("Daily total:", daily_total)
```

### Multiple assignments in one line
Python allows assigning to multiple variables
at once:
```python
a, b, c = 10, 20, 30
print(a, b, c)   # 10 20 30

# Swap values in one line
x, y = 5, 10
x, y = y, x
print(x, y)      # 10 5
```

> 💡 **INSIGHT:** Swapping variables without a temporary variable is uniquely simple in Python: `x, y = y, x`.

---

## 💡 Important: Variables are references
When you do `x += 5`, Python reads the current
value of `x`, adds 5, and makes `x` point to
the new value. The original value is discarded.

For immutable types (numbers, strings),
a new object is created each time you modify.

---

## 🔍 Practice Preview (for later coding)
```python
# Basic assignments
score = 0
print("Initial:", score)

score += 10   # earned points
print("After bonus:", score)

score -= 3    # penalty
print("After penalty:", score)

# String accumulation
log = ""
log += "[INFO] System started\n"
log += "[INFO] Processing data\n"
log += "[WARN] Low memory\n"
print(log)

# Multiple assignment
width, height, depth = 1920, 1080, 256
print("Resolution:", width, "x", height)
```

---

## 📌 Key Takeaway
- `=` assigns a value; `+=` adds and assigns; `-=` subtracts and assigns.
- Compound operators make code cleaner.
- Multiple assignment works in one line.
- Variables point to values; reassigning changes the pointer.