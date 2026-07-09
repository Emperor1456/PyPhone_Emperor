# 📘 PyPhone Emperor · Module 2  
# 📖 L‑16 – The `if-elif-else` Chain (Multi‑way Decisions)

---

## 🎯 OBJECTIVE  
Master the `if-elif-else` ladder to handle multiple exclusive paths in a business rule. Python checks conditions from top to bottom; the first `True` branch executes, and the rest are skipped entirely. If no condition is `True`, the `else` block catches everything else.

---

## 🧱 BRICK 1 – The Ladder Syntax and a Grading Engine

```python
if condition1:
    # block 1
elif condition2:
    # block 2
elif condition3:
    # block 3
else:
    # fallback block
```

Only **one** block ever runs — the first whose condition is `True`. The `else` is optional, but in business logic it acts as a safety net.

**① Customer scoring – performance grade**
```python
score = 65
if score >= 80:
    print('A')
elif score >= 70:
    print('B')
elif score >= 60:
    print('C')
else:
    print('D')
```
- Check order:  
  - `65 >= 80`? No → skip.  
  - `65 >= 70`? No → skip.  
  - `65 >= 60`? Yes → print `'C'` → stop.

If `score` were `85`, the first `if` would catch it. If `score` were `55`, the `else` would print `'D'`.

> 💡 **INSIGHT:** The ladder works like a filter cascade. Always place the most specific (highest) threshold first, then gradually widen the range.

**② Loyalty points – tier assignment**
```python
points = 75
if points >= 90:
    print('A')
elif points >= 75:
    print('B')
elif points >= 60:
    print('C')
else:
    print('F')
```
`75 >= 90`? No. `75 >= 75`? Yes → `'B'`.

**Flow:**
```
       ┌─────────────┐
       │  condition1? │
       └──────┬──────┘
        False │ True
       ┌──────▼──────┐ ┌───────┐
       │  condition2? │ │block1 │
       └──────┬──────┘ └───────┘
        False │ True
       ┌──────▼──────┐ ┌───────┐
       │  condition3? │ │block2 │
       └──────┬──────┘ └───────┘
        False │ True
       ┌──────▼──────┐ ┌───────┐
       │   else      │ │block3 │
       └─────────────┘ └───────┘
```

---

## 🧱 BRICK 2 – Business Classification with Real Data

**③ Equipment temperature monitoring**
```python
temp = 55
if temp > 100:
    status = 'Hot'
elif temp > 70:
    status = 'Warm'
elif temp > 40:
    status = 'Medium'
else:
    status = 'Cold'
print(status)   # Medium
```
- `55 > 100`? No.  
- `55 > 70`? No.  
- `55 > 40`? Yes → `'Medium'`.

This logic classifies machine health in a factory. A temperature of 105 would yield `'Hot'`, triggering an alarm.

**④ Order quantity discount tiers**
```python
quantity = 30
if quantity >= 100:
    price_per_unit = 8
elif quantity >= 50:
    price_per_unit = 9
elif quantity >= 20:
    price_per_unit = 10
else:
    price_per_unit = 12
print(price_per_unit)   # 10
```

**⑤ Age‑based risk classification (insurance)**
```python
age = 55
if age < 18:
    risk = 'Low'
elif age < 50:
    risk = 'Medium'
elif age < 70:
    risk = 'High'
else:
    risk = 'Critical'
print(risk)   # High
```

> ⚠️ **WARNING – Order is everything:**  
> If you write `elif temp > 40` before `temp > 70`, a temperature of 80 would wrongly be classified as `'Medium'` because the first true branch (`> 40`) would fire.  
> Always place tighter (higher) thresholds first.

> 💡 **ADVANCED TIP – Short‑circuit evaluation:**  
> Python stops checking as soon as one `if` or `elif` condition is `True`. This is why order matters and also saves processing time when the chain is long.

---

## 💡 Real‑world Usage

**Transaction amount classification (banking)**
```python
amount = 12000
if amount > 10000:
    action = 'Flag for compliance review'
elif amount > 5000:
    action = 'Approve with manager'
elif amount > 1000:
    action = 'Auto‑approve'
else:
    action = 'Instant settlement'
print(action)
```

**Delivery time estimation (logistics)**
```python
distance_km = 45
if distance_km > 200:
    eta = '2 days'
elif distance_km > 100:
    eta = '1 day'
elif distance_km > 50:
    eta = 'Same day'
else:
    eta = 'Within 4 hours'
print(eta)
```

**Salary band assignment (HR)**
```python
experience_years = 6
if experience_years >= 10:
    band = 'Senior'
elif experience_years >= 5:
    band = 'Mid‑level'
elif experience_years >= 2:
    band = 'Junior'
else:
    band = 'Trainee'
print(band)
```

---

## 🔍 Practice Preview
You will build three decision chains, exactly as the practice engine expects:

| Level  | Task                                                                 | Expected Output |
|--------|----------------------------------------------------------------------|-----------------|
| Easy   | `score=65`. Print grade: A>=80, B>=70, C>=60, else D.               | `C`             |
| Medium | `points=75`. A>=90, B>=75, C>=60, else F.                           | `B`             |
| Hard   | `temp=55`. Hot>100, Warm>70, Medium>40, else Cold.                  | `Medium`        |

Run the coach:
```bash
python ii_Practice_Sheets/L-16_if_elif_else.py
```
Choose `1`, `2`, or `3`. Type the ladder; the engine checks your output.

---

## 📌 Key Takeaway
- `if-elif-else` chains multiple exclusive conditions.
- Only the **first** true branch executes; rest are skipped.
- `else` is a fallback for when none match.
- Order conditions from strictest to loosest.
- Used everywhere: grading, pricing tiers, risk bands, temperature alerts.