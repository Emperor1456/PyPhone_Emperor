# 📘 PyPhone Emperor · Module 1  
# 📖 L‑08 – Logical Operators in Business Rules

---

## 🎯 OBJECTIVE
Learn to combine and invert conditions using
Python’s three logical operators: `and`, `or`, `not`.
These operators allow you to build complex
business rules from simple comparisons.
They are the backbone of every decision in
a professional application.

---

## 🧱 BRICK 1 – The `and` and `or` Operators

Logical operators combine multiple comparisons
into a single condition that evaluates to
`True` or `False`.

### `and` – both sides must be True

```python
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False
```

**Business example:** A transaction is valid only if
the amount is positive **and** the status is "paid".

```python
amount = 500
status = "paid"
is_valid = amount > 0 and status == "paid"
print(is_valid)   # True
```

### `or` – at least one side must be True

```python
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False
```

**Business example:** A customer qualifies for a discount
if they are a premium member **or** the order exceeds $200.

```python
is_premium = False
order_total = 250
qualifies = is_premium or order_total > 200
print(qualifies)   # True
```

### Short‑circuit evaluation
Python stops evaluating as soon as the result is known.

- In `A and B`, if A is `False`, B is never checked.
- In `A or B`, if A is `True`, B is never checked.

This is efficient and can prevent errors in later checks.

> 💡 **INSIGHT:** Use `and` when **all** conditions must be met.
> Use `or` when **any** condition is enough.

---

## 🧱 BRICK 2 – The `not` Operator and Combining All Three

### `not` – negates a condition

```python
print(not True)    # False
print(not False)   # True
```

**Business example:** Flag a user if they are **not** active.

```python
is_active = False
needs_review = not is_active
print(needs_review)   # True
```

### Mixing `not`, `and`, `or`

When you combine operators, use parentheses to
make the logic crystal clear.

```python
# Check if x is between 10 and 20
x = 15
in_range = x > 10 and x < 20
print(in_range)   # True

# Complex business rule:
# Valid if (paid or subscribed) AND not banned
paid = True
subscribed = False
banned = False
can_access = (paid or subscribed) and not banned
print(can_access)   # True
```

### Precedence (evaluation order)
Python evaluates `not` first, then `and`, then `or`.
But always use parentheses – it makes your intention
obvious and avoids subtle bugs.

```python
# Without parentheses (harder to read):
result = True or False and False   # True (and first: False and False = False, then True or False = True)

# With parentheses (clearer):
result = True or (False and False)   # True
```

> ⚠️ **WARNING:** Never rely on your reader knowing
> the precedence rules. Use parentheses.
> `A and B or C` should always be written as
> `(A and B) or C` or `A and (B or C)`.

---

## 💡 Real‑world Usage
Logical operators are the nervous system of
every business application.

**Example 1 – Access control**
```python
role = "admin"
is_logged_in = True
can_edit = is_logged_in and role == "admin"
print(can_edit)   # True
```

**Example 2 – Discount eligibility**
```python
is_student = True
purchase_amount = 75
gets_discount = is_student or purchase_amount >= 100
print(gets_discount)   # True (student, even though amount < 100)
```

**Example 3 – Error flagging**
```python
has_errors = False
is_empty = True
needs_attention = has_errors or is_empty
print(needs_attention)   # True
```

---

## 🔍 Practice Preview
You will evaluate three logical expressions.

- **Easy:** Print the result of `(True and False) or (not False)`.
- **Medium:** Set `x=15`, then print whether `x` is between 10 and 20
  (use `x > 10 and x < 20`).
- **Hard:** Print the result of `not (10 < 5 or 5 > 1)`.

Run the practice coach:
```bash
python ii_Practice_Sheets/L-08_Logical_Operators.py
```

Choose your level, type the script, and the engine will verify.

---

## 📌 Key Takeaway
- `and` requires both conditions to be `True`.
- `or` requires at least one condition to be `True`.
- `not` negates a single condition.
- Use parentheses to make complex logic readable.
- Logical operators are the foundation of every business rule in code.