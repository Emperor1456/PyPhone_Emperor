# 📘 PyPhone Emperor · Module 1  
# 📖 L‑07 – Comparison Operators

---

## 🎯 OBJECTIVE
Learn to compare values using Python's
comparison operators.
These operators return a **boolean** value:
`True` or `False`.
Comparison is the foundation of all
decision‑making in programs.

---

## 🧱 BRICK 1 – The Six Comparison Operators

Python provides exactly six operators to compare
any two values. They work on numbers, strings,
and many other types.

| Operator | Meaning                  |
|----------|--------------------------|
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

**Examples with numbers:**
```python
print(10 == 10)    # True
print(10 == 5)     # False
print(10 != 5)     # True
print(10 > 5)      # True
print(10 < 5)      # False
print(10 >= 10)    # True
print(10 <= 5)     # False
```

> 💡 **NOTE:** `==` compares value equality. Do not confuse with `=` (assignment).

---

## 🧱 BRICK 2 – Comparing Different Types

### Comparing strings
Strings are compared **lexicographically**
(like a dictionary, by Unicode order).
Capital letters come **before** lowercase letters.

```python
print("apple" == "apple")     # True
print("apple" == "banana")    # False
print("apple" < "banana")     # True  (a before b)
print("apple" > "Apple")      # True  (lowercase > uppercase)
print("Z" < "a")              # True  (all capitals < lowercase)
```

### Comparing variables
```python
age = 18
limit = 21
print(age >= limit)   # False
print(age < limit)    # True
```

### Chaining comparisons (Python‑only feature)
```python
x = 5
print(1 < x < 10)     # True  (same as: 1 < x and x < 10)
print(10 < x < 20)    # False
```

> 💡 **INSIGHT:** Chaining comparisons is elegant and exclusive to Python. Use it to check ranges.

---

## 💡 Real‑world Usage
Comparisons drive every business rule.

```python
# Check if transaction amount exceeds threshold
amount = 15000
threshold = 10000
is_flagged = amount > threshold
print("Flagged:", is_flagged)

# Validate a username is not empty
username = "Emperor"
is_valid = username != ""
print("Valid:", is_valid)
```

---

## 🔍 Practice Preview (for later coding)
```python
a = 42
b = 42
c = 99

print("a == b:", a == b)
print("a == c:", a == c)
print("a != c:", a != c)
print("a < c :", a < c)
print("a >= c:", a >= c)
print("a <= b:", a <= b)

# String comparison
print("'cat' < 'dog':", "cat" < "dog")

# Chained comparison
age = 18
print("Between 13 and 19?", 13 <= age <= 19)
```

---

## 📌 Key Takeaway
- Six operators: `==`, `!=`, `>`, `<`, `>=`, `<=`.
- They always return `True` or `False`.
- Strings compare alphabetically; case matters.
- Chained comparisons are clean and Pythonic.