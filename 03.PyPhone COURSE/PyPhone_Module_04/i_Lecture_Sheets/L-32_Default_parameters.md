# 📘 PyPhone Emperor · Module 4  
# 📖 L‑32 – Default Parameters (Flexible Function Signatures)

---

## 🎯 OBJECTIVE  
Master **default parameters** — values that fill in when an argument is omitted.  
They make functions more flexible, reduce caller burden, and provide sensible fallbacks  
for optional business data like default greeting names, tax rates, or power exponents.

---

## 🧱 BRICK 1 – Defining Defaults

Assign a value with `=` in the function signature.  
If the caller skips that argument, the default is used.

**① Greeting with a fallback name**
```python
def greet(name='Guest'):
    return 'Hello ' + name

print(greet())          # 'Hello Guest'  (default used)
print(greet('Emperor')) # 'Hello Emperor'
```
This is the Easy practice task: call `greet()` with no arguments and get `'Hello Guest'`.

**② Power function with default exponent**
```python
def power(x, exp=2):
    return x ** exp

print(power(2))    # 4   (2²)
print(power(3, 2)) # 9   (3²)
```
`exp` defaults to 2 — perfect for squaring, but you can override it.  
This matches the Hard practice task.

> 💡 **INSIGHT:** Default parameters make functions **backward‑compatible**.  
> Existing code that calls `power(5)` still works even after you add more parameters.

---

## 🧱 BRICK 2 – Rules and the Mutable Trap

**③ Multiple defaults**
```python
def format_currency(amount, symbol='$', decimals=2):
    return f"{symbol}{amount:.{decimals}f}"

print(format_currency(100))         # $100.00
print(format_currency(100, '€', 1)) # €100.0
```

**④ Mutable default pitfall**
```python
# BAD — shared list across calls
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))   # [1]
print(add_item(2))   # [1, 2]  ← unexpected
```

**⑤ Safe pattern with `None`**
```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))   # [1]
print(add_item(2))   # [2]     ← correct
```

> ⚠️ **WARNING:** Non‑default parameters must come **before** default ones.  
> `def f(a=1, b):` is a syntax error.

> 💡 **ADVANCED TIP:** Use `None` as a sentinel for mutable defaults.  
> This is the Pythonic standard — it prevents subtle, hard‑to‑find bugs.

---

## 💡 Real‑world Usage

**Banking – transfer with default currency**
```python
def transfer(amount, currency='BDT'):
    return f"Transferring {amount} {currency}"

print(transfer(500))            # BDT
print(transfer(100, 'USD'))     # USD
```

**E‑commerce – shipping with default method**
```python
def ship(order_id, method='Standard'):
    return f"Order {order_id} via {method}"

print(ship('A001'))              # Standard
print(ship('A002', 'Express'))   # Express
```

**Logistics – delivery time with default speed**
```python
def eta(distance, speed=60):
    return distance / speed

print(eta(120))      # 2.0 hours
print(eta(120, 80))  # 1.5 hours
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Define `greet(name='Guest')` returning `'Hello '+name`. Call with no arguments and print. | `Hello Guest` |
| Medium | Using same `greet`, call with `'Emperor'` and print. | `Hello Emperor` |
| Hard   | Define `power(x,exp=2)` returning `x**exp`. Call with 2 (default) and 3,2; print each on a separate line. | `4`<br>`9` |

Run the coach:
```bash
python ii_Practice_Sheets/L-32_Default_Parameters.py
```

---

## 📌 Key Takeaway
- Default values make arguments optional.
- Non‑default parameters must come first in the signature.
- Never use mutable objects (`[]`, `{}`) as defaults — use `None` instead.
- Defaults provide sensible fallbacks and keep function calls clean.