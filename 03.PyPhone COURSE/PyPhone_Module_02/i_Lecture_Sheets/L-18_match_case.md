# 📘 PyPhone Emperor · Module 2  
# 📖 L‑18 – The `match-case` Statement (Pattern Matching for Business Rules)

---

## 🎯 OBJECTIVE  
Master Python’s modern `match` statement (Python 3.10+).  
It compares a value against a set of **patterns** and runs the first matching block.  
Use it to replace long `if‑elif‑elif` chains when testing the same variable against many values.  
Think: menu dispatchers, HTTP status handlers, payment classifiers — every business rule that pivots on a single variable.

---

## 🧱 BRICK 1 – Basic Syntax and Simple Value Matching

```python
match variable:
    case pattern1:
        # runs when variable matches pattern1
    case pattern2:
        # runs when variable matches pattern2
    case _:
        # wildcard – runs if nothing else matched
```

`_` is the fallback, just like `else` in an `if` chain.  
Patterns are checked **top to bottom**; only the **first match** executes.

**① Menu dispatcher – banking transaction choice**
```python
option = 1
match option:
    case 1:
        print('one')
    case 2:
        print('two')
    case _:
        print('other')
```
`option` is 1 → prints `'one'`.  
If the user picked 2, it would print `'two'`; anything else prints `'other'`.  
This is the core of a simple text‑menu system.

**② Color code translator – UI theme selector**
```python
color = 'r'
match color:
    case 'r':
        print('Red')
    case 'g':
        print('Green')
    case 'b':
        print('Blue')
    case _:
        print('Unknown color')
```
Here `color = 'r'` matches the first case and prints `'Red'`.  
Use exactly this logic when converting short codes to human‑readable labels.

**③ HTTP status handler – API response interpreter**
```python
code = 200
match code:
    case 200:
        print('Success')
    case 404:
        print('Not Found')
    case 500:
        print('Server Error')
    case _:
        print('Unknown')
```
`code` is 200 → prints `'Success'`.  
A 404 would print `'Not Found'`; 500 gives `'Server Error'`; anything else falls back to `'Unknown'`.

> 💡 **INSIGHT:** `match` shines when you have one variable and many possible concrete values.  
> It’s more readable than a cascade of `if‑elif` because the tested variable is written only once.

---

## 🧱 BRICK 2 – Guards and Destructuring for Deeper Business Logic

`match` goes far beyond simple values.  
You can add **guards** (`if` conditions inside a case) and **destructure** data structures.

**④ Transaction classifier with a guard**
```python
amount = 1500
match amount:
    case x if x > 10000:
        risk = 'High – compliance review'
    case x if x > 5000:
        risk = 'Medium – manager approval'
    case x if x > 1000:
        risk = 'Low – auto‑approved'
    case _:
        risk = 'Minimal – instant settlement'
print(risk)
```
Each case captures the value in `x` and then applies a condition.  
`amount = 1500` matches the third case because `1500 > 1000` is `True`.  
This is perfect for tiered risk scoring, discount bands, or tax brackets.

**⑤ Order status tuple – destructuring**
```python
order = ('shipped', '2026-06-15')
match order:
    case ('pending', _):
        action = 'Awaiting warehouse'
    case ('shipped', date):
        action = f'Dispatched on {date}'
    case ('delivered', date):
        action = f'Arrived on {date}'
    case _:
        action = 'Unknown status'
print(action)  # 'Dispatched on 2026-06-15'
```
Here the tuple is broken into its components.  
The second case matches `('shipped', date)` and binds `date` to `'2026-06-15'`.

**⑥ Coordinating services – matching a tuple with a guard**
```python
service = ('transfer', 1200)
match service:
    case ('transfer', amount) if amount < 1000:
        fee = 0
    case ('transfer', amount):
        fee = 5
    case ('payment', _):
        fee = 2
    case _:
        fee = 10
print(fee)   # 5
```
A transfer of 1200 (≥1000) falls to the second case, so a $5 fee applies.

> ⚠️ **WARNING:** `match` requires Python 3.10 or later.  
> Termux usually ships a recent Python, but run `python --version` if you see a SyntaxError.  
> Also, do **not** put a condition directly after `case x` without `if` — that’s invalid syntax.

> 💡 **ADVANCED TIP:** Guards (`if`) let you keep complex business rules inside the pattern matching itself,  
> reducing the need for extra nested `if` blocks and making the code self‑documenting.

---

## 💡 Real‑world Usage

**Payment status handler**
```python
payment_status = 'paid'
match payment_status:
    case 'pending':
        send_reminder()
    case 'paid':
        generate_receipt()
    case 'failed':
        notify_user()
    case _:
        log_error()
```

**API response router**
```python
response = (200, '{"user": "Emperor"}')
match response:
    case (200, body):
        parse_success(body)
    case (401, _):
        redirect_to_login()
    case (500, _):
        show_server_error()
    case _:
        show_generic_error()
```

**Order dispatch decision**
```python
order = ('express', 2)   # (shipping_type, item_count)
match order:
    case ('express', count) if count <= 5:
        courier = 'Bike'
    case ('express', count):
        courier = 'Van'
    case ('standard', _):
        courier = 'Truck'
    case _:
        courier = 'Standard post'
print(courier)
```

---

## 🔍 Practice Preview
You will write three `match`‑based mini‑programs that mirror real business dispatchers.

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | `x=1`. Use `match` to print `'one'` for 1, `'two'` for 2, else `'other'`. | `one`           |
| Medium | `color='r'`. Match `'r'` → `'Red'`, `'g'` → `'Green'`, `'b'` → `'Blue'`. | `Red`           |
| Hard   | `code=200`. Match 200 → `'Success'`, 404 → `'Not Found'`, wildcard → `'Unknown'`. | `Success`       |

Run the coach:
```bash
python ii_Practice_Sheets/L-18_match_case.py
```
Choose `1`, `2`, or `3`. Type the `match` block; the engine checks your output.

---

## 📌 Key Takeaway
- `match` compares one value against many patterns.
- `case _` is the wildcard fallback, like `else`.
- Use guards (`if`) to add business conditions inside a case.
- Destructure tuples, lists, and more to extract data cleanly.
- `match` replaces long `if‑elif` chains when checking the same variable repeatedly.
- Make sure your Python is 3.10+.