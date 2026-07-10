# 📘 PyPhone Emperor v3.0 · Module 5
# 📖 L‑26 – Return Values & Early Return Pattern

---

## 🎯 OBJECTIVE — What You Will Master

> Send results back from functions and exit early when needed.

- 🔙 **`return`** – send a value back to the caller
- ⏪ **Early return** – exit function immediately under certain conditions
- 📦 **Multiple returns** – return a tuple of values
- 🧪 **`None` return** – functions without `return` yield `None`

---

## 🧱 BASIC RETURN

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)   # 5
```

---

## 🧱 EARLY RETURN

Stop execution as soon as a condition is met.

```python
def safe_divide(a, b):
    if b == 0:
        return None
    return a / b
```

---

## 🧱 RETURNING MULTIPLE VALUES

```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4,1,9,3])
print(low, high)   # 1 9
```

> ⚠️ **WARNING:** Code after `return` in the same block is dead code and will never execute.

---

## 💡 Real‑world Usage

**Banking – withdraw with guard**
```python
def withdraw(balance, amount):
    if amount > balance:
        return None
    return balance - amount
```

**E‑commerce – calculate order total**
```python
def total(items):
    if not items:
        return 0.0
    return sum(item["price"] for item in items)
```

**Logistics – validate shipment**
```python
def validate(tracking_id):
    if not tracking_id:
        return False, "Missing ID"
    return True, "Valid"
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Define `double(x)` returning `2*x`. Call with 5. | `def double(x): return 2*x` |
| Medium | Define `absolute(x)` returning `x if x>=0 else -x`. Call with -7. | `def absolute(x): ...` |
| Hard | Define `is_even(n)` returning `True` if even. Call with 8. | `def is_even(n): return n%2==0` |

Run the coach:
```bash
python ii_Practice_Sheets/L26_Return_Values_Early_Return.py
```

---

## 📌 Key Takeaway
- `return` sends a value back and ends the function.
- Use early returns to handle edge cases cleanly.
- Return multiple values as a tuple.

*For Emperor.*