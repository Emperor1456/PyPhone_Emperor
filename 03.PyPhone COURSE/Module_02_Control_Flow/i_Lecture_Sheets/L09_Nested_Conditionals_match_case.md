# 📘 PyPhone Emperor v3.0 · Module 2
# 📖 L‑09 – Nested Conditionals & `match`‑`case`

---

## 🎯 OBJECTIVE — What You Will Master

> Multi‑level decisions and modern pattern matching.

- 🧩 **Nested `if`** – decisions inside decisions
- ⚡ **Flattening** – when to use `and`/`or` instead of deep nesting
- 🧪 **`match`‑`case`** – Python 3.10’s elegant alternative to long `if‑elif` chains
- 🧱 **Guards & destructuring** – adding conditions inside cases, matching data structures

---

## 🧱 NESTED CONDITIONALS

An `if` inside another `if`. The inner block only runs when **both** conditions are true.

```python
is_logged_in = True
is_admin = False
if is_logged_in:
    if is_admin:
        print("Admin panel")
    else:
        print("User dashboard")
else:
    print("Please log in")
```

**Business rule – discount with membership & purchase amount**
```python
member = True
purchase = 150
if member:
    if purchase > 100:
        discount = 0.2
    else:
        discount = 0.1
else:
    discount = 0.0
```

> 💡 **INSIGHT:** Nesting beyond 2‑3 levels makes code hard to read. Use `and`/`or` to flatten simple conjunctions.

---

## 🧱 `match`‑`case` – CLEANER THAN `elif`

When you compare **one variable** against many possible values, `match` is clearer than a chain of `if‑elif`.

```python
command = "stop"
match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case "pause":
        print("Pausing")
    case _:
        print("Unknown")
```

`_` is the wildcard (like `else`).

**Business example – HTTP status handler**
```python
code = 200
match code:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown")
```

**Advanced – guard (if) and destructuring**
```python
value = 12
match value:
    case x if x < 0:
        print("Negative")
    case x if x > 0:
        print("Positive")
    case 0:
        print("Zero")
```

Tuple destructuring:
```python
point = (0, 5)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y‑axis at {y}")
    case (x, 0):
        print(f"X‑axis at {x}")
    case _:
        print("Somewhere")
```

> ⚠️ **WARNING:** `match` requires Python 3.10+. Verify with `python --version` in Termux.

---

## 💡 Real‑world Usage

**Banking – transaction classification**
```python
amount = 15000
match amount:
    case a if a > 10000:
        print("Large – review")
    case a if a > 5000:
        print("Medium – process")
    case _:
        print("Small – auto")
```

**E‑commerce – order status**
```python
status = "shipped"
match status:
    case "pending":
        action = "Awaiting"
    case "shipped":
        action = "In transit"
    case "delivered":
        action = "Completed"
    case _:
        action = "Unknown"
```

**Logistics – package weight category**
```python
weight = 8
match weight:
    case w if w > 20:
        print("Heavy")
    case w if w > 10:
        print("Medium")
    case _:
        print("Light")
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Use `match` to translate a number (1,2,3) to words ("one","two","three"). | `match num: case 1: …` |
| Medium | A banking menu: given a code, match "deposit", "withdraw", "balance", else "invalid". | `match action: case …` |
| Hard | Classify a shipment using nested `if` (temperature & humidity) then flatten with `match` and guards. | Combine concepts |

Run the coach:
```bash
python ii_Practice_Sheets/L09_Nested_Conditionals_match_case.py
```

---

## 📌 Key Takeaway
- Nested `if` handles multi‑step decisions; avoid deep nesting.
- `match`‑`case` is ideal for multiple fixed values or patterns.
- Use guards (`if`) and destructuring for complex conditions.

*For Emperor.*