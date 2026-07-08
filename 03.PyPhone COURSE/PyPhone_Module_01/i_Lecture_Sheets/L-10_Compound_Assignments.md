# 📘 PyPhone Emperor · Module 1  
# 📖 L‑10 – Compound Assignment Operators in Data Updates

---

## 🎯 OBJECTIVE
Extend your mastery of assignment operators
to include multiplication, division, floor division,
modulus, and exponentiation assignment.
These compound operators are essential for
scaling prices, distributing batches, and
applying complex business rules with minimal code.

---

## 🧱 BRICK 1 – Multiplication and Division Assignments

### `*=` – multiply and assign
Multiplies the variable by a value and stores the result.

```python
x = 10
x *= 5        # x = 10 * 5 = 50
print(x)
```

**Business example – scaling a price by a factor:**
```python
base_price = 20
multiplier = 3
base_price *= multiplier   # 60
print(base_price)
```

### `/=` – divide and assign (float result)
Divides the variable and stores the result as a float.

```python
y = 10
y /= 3        # y = 3.3333333333333335
print(y)
```

**Business example – splitting a bill:**
```python
total_bill = 100
people = 3
total_bill /= people   # 33.333...
print(total_bill)
```

> 💡 `/=` always produces a float, even if the division is exact.

---

## 🧱 BRICK 2 – Floor Division, Modulus, and Exponentiation Assignments

### `//=` – floor divide and assign
Divides the variable, chops off the decimal, and stores the integer.

```python
a = 5
a //= 2       # a = 2 (5 // 2 = 2)
print(a)
```

**Business example – items per box:**
```python
total_items = 23
box_capacity = 5
boxes_needed = total_items
boxes_needed //= box_capacity   # 4 (full boxes, ignoring remainder)
print(boxes_needed)
```

### `%=` – modulus and assign
Stores the **remainder** after division.

```python
b = 5
b %= 3        # b = 2 (5 % 3 = 2)
print(b)
```

**Business example – leftover items after packing:**
```python
total_items = 23
box_capacity = 5
leftover = total_items
leftover %= box_capacity       # 3
print(leftover)
```

### `**=` – exponentiation and assign
Raises the variable to a power and stores the result.

```python
c = 3
c **= 2       # c = 9
print(c)
```

**Business example – compound interest over one period:**
```python
principal = 1000
rate = 0.05
principal *= (1 + rate)    # 1050.0
principal **= 1            # same
```

> ⚠️ **WARNING:** `**=` is rarely used in everyday code,
> but it’s critical in scientific or mathematical scripts.

---

## 💡 Real‑world Usage
These operators combine two steps into one,
making your code cleaner and less error‑prone.

### Inventory restock with partial boxes
```python
total_items = 23
box_size = 5
full_boxes = total_items
full_boxes //= box_size      # 4
remaining = total_items
remaining %= box_size        # 3
print("Full boxes:", full_boxes)
print("Leftover:", remaining)
```

### Adjusting a score with a multiplier
```python
score = 100
multiplier = 1.5
score *= multiplier          # 150.0
print(score)
```

### Distributing discount equally
```python
price = 200
discount = 50
price -= discount            # 150
price /= 2                   # 75.0
print(price)
```

---

## 🔍 Practice Preview
You will apply compound assignments to update
several variables.

- **Easy:** Start with `x = 10`, then multiply by 5 using `*=` and print `x`.
- **Medium:** Start with `y = 10`, divide by 3 using `/=` and print the result
  (it should show `3.33` after rounding).
- **Hard:** Start with `a = 5`, floor‑divide by 2 using `//=` and print.
  Then start with `b = 5`, modulus by 3 using `%=` and print.
  The output must show `2` on the first line and `2` on the second.

Run the practice coach:
```bash
python ii_Practice_Sheets/L-10_Compound_Assignments.py
```

Choose your level, type the script, and the engine will verify.

---

## 📌 Key Takeaway
- `*=`, `/=`, `//=`, `%=`, `**=` combine arithmetic with assignment.
- `/= ` always yields a float; `//=` yields an integer.
- `%= ` gives the remainder.
- `**=` raises to a power.
- Use them to make your code concise and business‑logic clear.