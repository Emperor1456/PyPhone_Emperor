# 📘 PyPhone Emperor · Module 2
# 📖 L‑15 – `if-else`

---

## 🎯 OBJECTIVE
Learn to handle both outcomes of a decision
using the **`if-else`** statement.
When the condition is `True`, the `if` block runs;
when it’s `False`, the `else` block runs instead.
Exactly one of the two paths executes — never both.

---

## 🧱 BRICK 1 – The Two‑Way Branch

```python
if condition:
    # runs when condition is True
    statement
else:
    # runs when condition is False
    statement
```

**Example:**
```python
temperature = 28
if temperature > 30:
    print("Hot day")
else:
    print("Not too hot")
```
If `temperature` is 28, `28 > 30` is `False`,
so the `else` block executes.

> 💡 **INSIGHT:** `if-else` guarantees that **something** always happens — the program never falls through silently.

---

## 🧱 BRICK 2 – Real‑world Patterns

**① Validation**
```python
password = "secret123"
if len(password) >= 8:
    print("Password accepted")
else:
    print("Password too short")
```

**② Simple business logic**
```python
order_total = 75
if order_total >= 50:
    shipping = 0
else:
    shipping = 5.99
print("Shipping:", shipping)
```

**③ Assigning values with `if-else`**
```python
is_member = True
discount = 10 if is_member else 0   # ternary (shortcut)
```

> ⚠️ **WARNING:** The `else` block **must** be indented exactly like the `if` block. Both share the same parent.

---

## 🔍 Practice Preview (for later coding)
```python
age = 16
if age >= 18:
    print("Adult")
else:
    print("Minor")

score = 55
if score >= 60:
    print("Pass")
else:
    print("Fail")
```

---

## 📌 Key Takeaway
- `if-else` gives a two‑way decision.
- Exactly one block runs — never both.
- The `else` block has no condition of its own.
- Use for validation, branching, and clean logic.