# 📘 PyPhone Emperor · Module 2  
# 📖 L‑17 – Nested Conditionals (Multi‑step Business Rules)

---

## 🎯 OBJECTIVE  
Master **nested conditionals** — `if` statements inside other `if` blocks — to implement multi‑stage business checks. A secondary condition is tested only after a primary condition passes. This is the logic behind login gates, access levels, and discount engines.

---

## 🧱 BRICK 1 – Nesting for Two‑stage Verification

A nested `if` sits inside the indented body of an outer `if`. The inner block runs only when **both** the outer and inner conditions are `True`.

```python
if outer_condition:
    # outer block
    if inner_condition:
        # inner block — runs only when both are True
    else:
        # runs when outer True, inner False
else:
    # runs when outer False
```

**① Access control — admin panel visibility**
```python
is_logged_in = True
is_admin     = False

if is_logged_in:
    print("Welcome back")
    if is_admin:
        access = 'full'
    else:
        access = 'limited'
else:
    access = 'none'
print(access)   # 'limited'
```
- Outer: user must be logged in.
- Inner: only admins get full access.
- A regular user (`is_admin = False`) gets `'limited'`.
- A visitor (`is_logged_in = False`) gets `'none'`.

> 💡 **INSIGHT:** The outer `if` acts as a gatekeeper. Without it, you’d have to repeat `is_logged_in` checks everywhere. Nesting keeps logic tidy.

**② Driving eligibility — age gate, then license & ban status**
```python
age        = 22
has_license = True
is_banned   = False

if age >= 18:
    if has_license and not is_banned:
        can_drive = True
    else:
        can_drive = False
else:
    can_drive = False
print(can_drive)   # True
```
- Outer: must be at least 18.
- Inner: needs a license and no ban.
- If age < 18, `can_drive` is immediately `False`.
- If age >= 18 but lacks license, also `False`.

> ⚠️ **WARNING:** Always provide an `else` for each level. In the driving example, forgetting the inner `else` would leave `can_drive` undefined when `has_license` is `False`.

---

## 🧱 BRICK 2 – Deeper Nesting and the Flattening Principle

Nesting can go deeper, but code quickly becomes a staircase. Most business rules can be simplified.

**③ Tiered discount — member status, then purchase amount**
```python
member   = True
purchase = 150

if member:
    if purchase > 100:
        discount = 0.2
    else:
        discount = 0.1
else:
    discount = 0.0
print(discount)   # 0.2
```
- Outer: `member` flag.
- Inner: `purchase > 100` gives premium discount.
- Non‑members get no discount, regardless of spend.

This three‑level logic is clear. But imagine adding "VIP members", "holiday season", "first‑time buyer" — the nest grows quickly.

**④ Flattening with `and` / `or` (advanced)**
A deeply nested chain like:
```python
if a:
    if b:
        if c:
            result = True
```
can often be rewritten as:
```python
if a and b and c:
    result = True
```
The flattened version is shorter and less error‑prone.

> 💡 **ADVANCED TIP – Short‑circuit flattening:**
> ```python
> if (
>     is_logged_in
>     and is_admin
>     and not is_suspended
> ):
>     show_admin_panel()
> ```
> Python evaluates `and` chains left‑to‑right. The moment one condition is `False`, the rest are skipped. This gives the same effect as nested `if`s but keeps the code flat and readable.

**When to use nesting vs. flattening:**
- Nest when the logic is naturally hierarchical (e.g., "only if member, then check purchase").
- Flatten when all conditions must be true for a single action.
- Never go beyond 2–3 levels of nesting; refactor instead.

---

## 💡 Real‑world Usage

**Banking – withdrawal with balance check and daily limit**
```python
is_authenticated = True
withdrawal       = 200
balance          = 500
daily_limit      = 300

if is_authenticated:
    if withdrawal <= balance:
        if withdrawal <= daily_limit:
            status = 'Approved'
        else:
            status = 'Exceeds daily limit'
    else:
        status = 'Insufficient funds'
else:
    status = 'Login required'
print(status)
```

**E‑commerce – special coupon after membership check**
```python
is_premium = True
cart_total = 80

if is_premium:
    if cart_total > 50:
        shipping = 0
    else:
        shipping = 5
else:
    if cart_total > 100:
        shipping = 0
    else:
        shipping = 10
print(shipping)
```

**HR – bonus eligibility (department + performance)**
```python
department = 'Sales'
performance_score = 85

if department == 'Sales':
    if performance_score >= 80:
        bonus = 5000
    else:
        bonus = 2000
elif department == 'Engineering':
    if performance_score >= 90:
        bonus = 7000
    else:
        bonus = 3000
else:
    bonus = 1000
print(bonus)
```

---

## 🔍 Practice Preview
You will write three nested conditionals that mirror real business logic.

| Level | Task | Expected Outcome |
|-------|------|------------------|
| Easy  | `is_logged_in=True`, `is_admin=False`. Set `access='full'` if both True, else `'limited'` (outer True, inner False). | `access = 'limited'` |
| Medium| `age=22`, `has_license=True`, `is_banned=False`. Write nested `if` that sets `can_drive=True` only if age≥18 and `has_license and not is_banned`; otherwise `False`. | `can_drive = True` |
| Hard  | `member=True`, `purchase=150`. Set `discount=0.2` if member and purchase>100; `0.1` if member but purchase≤100; `0.0` if not member. | `discount = 0.2` |

Run the coach:
```bash
python ii_Practice_Sheets/L-17_Nested_Conditionals.py
```
Type the nested blocks exactly as described; the engine checks the final variable value.

---

## 📌 Key Takeaway
- Nesting places a secondary `if` inside a primary one.
- Inner block only runs if outer condition is already `True`.
- Always provide `else` branches at each level to avoid missing assignments.
- Limit nesting to 2‑3 levels; use `and`/`or` to flatten when possible.
- Real business rules (access, eligibility, discount tiers) rely on nested logic daily.