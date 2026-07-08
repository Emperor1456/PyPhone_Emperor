# 📘 PyPhone Emperor · Module 1  
# 📖 L‑07 – Comparison Operators in Business Rules

---

## 🎯 OBJECTIVE
Learn to compare values using Python's
six comparison operators.
These operators return a **boolean** value:
`True` or `False`.
Comparison is the foundation of all
decision‑making in programs.
We’ll apply them to validate transactions
and enforce business constraints.

---

## 🧱 BRICK 1 – The Six Comparison Operators

Python provides exactly six operators to compare
any two values. They work on numbers, strings,
and many other types.

| Operator | Meaning                  | Example        | Result  |
|----------|--------------------------|----------------|---------|
| `==`     | Equal to                 | `10 == 10`     | `True`  |
| `!=`     | Not equal to             | `10 != 5`      | `True`  |
| `>`      | Greater than             | `10 > 5`       | `True`  |
| `<`      | Less than                | `10 < 5`       | `False` |
| `>=`     | Greater than or equal to | `10 >= 10`     | `True`  |
| `<=`     | Less than or equal to    | `5 <= 10`      | `True`  |

### Using comparisons on numbers

```python
amount = 1500
limit  = 1000

print(amount > limit)    # True  – exceeds the limit
print(amount == limit)   # False – not equal
print(amount != limit)   # True  – different values
print(amount >= 1500)    # True  – at least the threshold
print(amount <= 2000)    # True  – within upper bound
```

### Comparing strings

Strings are compared lexicographically (dictionary order),
based on Unicode values. Capital letters come before
lowercase letters.

```python
print("apple" == "apple")     # True
print("apple" == "Apple")     # False – case matters
print("apple" < "banana")     # True  (a before b)
print("apple" > "Apple")      # True  (lowercase > uppercase)
print("Z" < "a")              # True  (all capitals < lowercase)
```

> 💡 **INSIGHT:** Use `.lower()` or `.upper()` if you need
> case‑insensitive comparisons.

---

## 🧱 BRICK 2 – Chaining and Combining Comparisons

### Chaining (Python‑only feature)

Python lets you write a range check in one clean expression.

```python
x = 5
print(1 < x < 10)      # True  (same as: 1 < x and x < 10)
print(10 < x < 20)     # False
```

### Combining with `and`, `or`, `not`

Often a business rule requires multiple conditions.

```python
amount = 500
status = "paid"

# Both conditions must be true
is_valid = amount > 100 and status == "paid"
print(is_valid)        # True

# At least one condition must be true
is_eligible = status == "paid" or amount > 1000
print(is_eligible)     # True

# Negate a condition
is_empty = not (amount > 0)
print(is_empty)        # False
```

### Full transaction validation example

```python
amount = 2500
status = "pending"

# Rule: amount must be between 10 and 5000, and status must be "paid"
is_approved = (10 <= amount <= 5000) and status == "paid"
print(is_approved)     # False (status is not paid)
```

> ⚠️ **WARNING:** Do not confuse `==` (equality) with `=` (assignment).
> `if x = 5:` is a syntax error. Always use `if x == 5:`.

---

## 💡 Real‑world Usage
Comparisons drive every business rule in software.

**Example 1 – Fraud detection**
```python
transaction_amount = 15000
fraud_threshold = 10000
is_suspicious = transaction_amount > fraud_threshold
print("Flagged:", is_suspicious)
```

**Example 2 – Inventory reorder**
```python
current_stock = 15
reorder_level = 20
needs_reorder = current_stock <= reorder_level
print("Reorder needed:", needs_reorder)
```

**Example 3 – User access control**
```python
user_role = "admin"
is_admin = user_role == "admin"
print("Access granted:", is_admin)
```

---

## 🔍 Practice Preview
You will verify some simple business rules.

- **Easy:** Print whether `10 > 5`.
- **Medium:** Print whether `5 == 5`.
- **Hard:** Print whether `10 != 5 and 10 > 5 and 5 <= 10`
  (all three conditions must be true).

Run the practice coach:
```bash
python ii_Practice_Sheets/L-07_Comparison_Operators.py
```

Choose your level, type the script, and the engine will verify.

---

## 📌 Key Takeaway
- Six operators: `==`, `!=`, `>`, `<`, `>=`, `<=`.
- They always return `True` or `False`.
- Strings compare lexicographically; case matters.
- Chained comparisons (`1 < x < 10`) are clean and Pythonic.
- Combine with `and`/`or`/`not` for complex business logic.