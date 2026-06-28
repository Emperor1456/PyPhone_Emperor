# 📘 PyPhone Emperor · Module 1  
# 📖 L‑08 – Logical Operators

---

## 🎯 OBJECTIVE
Learn to combine multiple conditions using
the logical operators `and`, `or`, and `not`.
These operators let you build complex
decision logic from simple comparisons.

---

## 🧱 BRICK 1 – `and` and `or`

### `and` — Both conditions must be `True`
The whole expression is `True` only if
**both** the left and the right side are `True`.

```python
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False
```

**Real example:**
```python
age = 25
has_license = True
can_drive = (age >= 18) and has_license
print(can_drive)        # True
```

### `or` — At least one condition must be `True`
The whole expression is `True` if **either**
the left or the right side (or both) is `True`.

```python
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False
```

**Real example:**
```python
is_weekend = True
is_holiday = False
can_sleep_in = is_weekend or is_holiday
print(can_sleep_in)     # True
```

> 💡 **INSIGHT:** `and` is like a strict gate — all conditions must pass. `or` is lenient — only one needs to pass.

---

## 🧱 BRICK 2 – `not` and Short‑Circuiting

### `not` — Reverses a boolean
`not True` becomes `False`, `not False` becomes `True`.

```python
print(not True)         # False
print(not False)        # True
```

**Real example:**
```python
is_raining = False
should_go_out = not is_raining
print(should_go_out)    # True
```

### Combining all three
```python
age = 20
has_permission = False
is_admin = False

can_enter = (age >= 18 and has_permission) or is_admin
print(can_enter)        # False
```

### Short‑circuit evaluation (important!)
Python stops evaluating as soon as the result
is certain. This is efficient and can prevent errors.

- `False and anything()` → `False` (stops immediately)
- `True or anything()` → `True` (stops immediately)

```python
# The second condition is never checked
# because the first is already False
result = False and (10 / 0 == 0)   # No ZeroDivisionError
print(result)   # False
```

> ⚠️ **WARNING:** Short‑circuiting can hide errors if you rely on side effects in the second condition. Write clean, side‑effect‑free conditions.

---

## 💡 Real‑world Usage
```python
# Loan approval logic
income = 50000
credit_score = 720
has_debt = False

approved = (income >= 40000 and credit_score >= 700) and not has_debt
print("Loan approved:", approved)
```

---

## 🔍 Practice Preview (for later coding)
```python
# AND: both must be true
temperature = 22
is_sunny = True
print("Good weather?", temperature > 20 and is_sunny)

# OR: at least one true
is_manager = False
is_supervisor = True
print("Can approve?", is_manager or is_supervisor)

# NOT: reverse
print("Not true:", not True)

# Complex: eligible for discount
age = 65
is_member = False
discount = (age >= 60) or is_member
print("Gets discount:", discount)
```

---

## 📌 Key Takeaway
- `and` requires **both** sides true.
- `or` requires **at least one** side true.
- `not` flips the boolean.
- Python short‑circuits — stops early when answer is known.