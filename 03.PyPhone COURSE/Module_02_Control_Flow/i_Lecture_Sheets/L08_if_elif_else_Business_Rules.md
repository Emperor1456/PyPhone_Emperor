# 📘 PyPhone Emperor v3.0 · Module 2
# 📖 L‑08 – if, elif, else – Business Rule Engines

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, you will build decision engines that run banks, warehouses, and empires.

- 🧠 **if** – execute a block only when a condition is true
- 🔁 **else** – handle the opposite case
- 📊 **elif** – chain multiple exclusive conditions
- 🧪 **Real business rules** – loan approvals, inventory alerts, tax brackets
- 🚫 **Common pitfalls** – indentation, order, and missing cases

---

## 🧱 THE `if` STATEMENT – THE GATEKEEPER

The simplest decision tool. The indented block runs **only if** the condition evaluates to `True`.

```python
stock = 10
if stock > 0:
    print("In stock")
```

If `stock` is 0 or negative, nothing prints. The gate stays closed.

**Business example – overdraft alert:**
```python
balance = -50
if balance < 0:
    print("Overdrawn!")
```

---

## 🧱 `if‑else` – TWO ROADS

Always execute one block or the other.

```python
temperature = 28
if temperature > 30:
    print("Hot day")
else:
    print("Not too hot")
```

**Business example – loan eligibility:**
```python
income = 25000
if income >= 20000:
    print("Approved")
else:
    print("Denied")
```

---

## 🧱 `if‑elif‑else` – THE FULL DECISION TREE

Chain multiple conditions. The **first** `True` branch executes; the rest are skipped. `else` catches everything else.

```python
score = 82
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(grade)   # B
```

**Business example – shipping cost by weight:**
```python
weight_kg = 12
if weight_kg > 20:
    cost = 30
elif weight_kg > 10:
    cost = 20
elif weight_kg > 5:
    cost = 10
else:
    cost = 5
print(f"Shipping: ${cost}")
```

> ⚠️ **WARNING:** Order matters. Put the most restrictive condition first. If you check `weight_kg > 5` before `weight_kg > 20`, the heavy package would get the wrong rate.

> 💡 **INSIGHT:** `elif` is just a cleaner way of writing nested `if‑else` inside the `else` block. Use it whenever you have three or more exclusive paths.

---

## 💡 Real‑world Usage

**Banking – transaction category:**
```python
amount = 15000
if amount > 10000:
    print("Large transaction – flag for review")
elif amount > 5000:
    print("Medium transaction – process normally")
else:
    print("Small transaction – auto‑approve")
```

**E‑commerce – discount tier:**
```python
spent = 250
if spent >= 500:
    discount = 20
elif spent >= 200:
    discount = 10
elif spent >= 100:
    discount = 5
else:
    discount = 0
print(f"Discount: {discount}%")
```

**Logistics – delivery priority:**
```python
distance_km = 45
if distance_km > 100:
    priority = "Low"
elif distance_km > 50:
    priority = "Medium"
else:
    priority = "High"
```

**HR – salary band:**
```python
experience = 6
if experience >= 10:
    band = "Senior"
elif experience >= 5:
    band = "Mid"
elif experience >= 2:
    band = "Junior"
else:
    band = "Trainee"
```

---

## 🔍 Practice Preview
You will build decision engines for real business logic.

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Check if a product is in stock and print "Available" or "Out of stock". | `if stock > 0: … else: …` |
| Medium | Assign a tax rate based on income brackets using `if‑elif‑else`. | `if income >= … elif … else` |
| Hard | Classify a shipment by weight and distance, printing the exact cost category. | Nested conditions or chained `if‑elif` |

Run the coach:
```bash
python ii_Practice_Sheets/L08_if_elif_else_Business_Rules.py
```

---

## 📌 Key Takeaway
- `if` evaluates a condition; `else` handles the opposite.
- `elif` chains multiple exclusive checks – first match wins.
- Order of conditions determines the outcome; place stricter rules first.
- Business rules are simply well‑written conditionals.

*For Emperor.*