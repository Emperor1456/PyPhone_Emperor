# 📘 PyPhone Emperor · Module 4  
# 📖 L‑30 – Parameters & Arguments (Feeding Data into Functions)

---

## 🎯 OBJECTIVE  
Master **parameters** and **arguments** — the mechanism that lets functions receive input.  
Parameters are placeholders in the definition; arguments are the actual values you supply when calling.  
With them, a single function can process different transaction amounts, compute custom powers,  
or build full names from first and last strings — exactly the kind of logic that powers Companion's memory engine.

---

## 🧱 BRICK 1 – Positional Arguments (Order Matters)

When you define a function with parameters inside the parentheses,  
you must pass matching arguments when calling it.  
Arguments are assigned to parameters **by position** — the first argument goes to the first parameter,  
second to second, and so on.

**① Adding two numbers – financial sum**
```python
def add(a, b):
    return a + b

total = add(3, 5)
print(total)   # 8
```
Here `a` receives 3, `b` receives 5.  
This is exactly the Easy practice task — think of it as summing two deposit amounts.

**② Combining first and last name – customer record**
```python
def full_name(first, last):
    return first + ' ' + last

name = full_name('Emperor', 'PyPhone')
print(name)   # 'Emperor PyPhone'
```
The function takes two strings and returns a properly spaced full name.  
This matches the Medium practice task; in business systems, such a function would build a display name from database fields.

**③ Computing a power – compound growth factor**
```python
def power(base, exp):
    return base ** exp

result = power(2, 10)
print(result)   # 1024
```
`base` is 2, `exp` is 10 → returns 2¹⁰ = 1024.  
Financial models use powers for compound interest or exponential growth;  
this is the Hard practice task.

> 💡 **INSIGHT:** Parameter names should clearly describe the expected input.  
> `add(a, b)` is fine, but `add(amount1, amount2)` is even better in real code.

---

## 🧱 BRICK 2 – Multiple Parameters and Business Logic

You can define functions with any number of parameters.  
The calling code must provide exactly that many arguments, in the correct order.

**④ Invoice total from quantity and unit price**
```python
def invoice_total(quantity, unit_price):
    return quantity * unit_price

print(invoice_total(5, 12.50))   # 62.5
```

**⑤ Shipping cost with dimensions**
```python
def shipping_cost(weight, length, width, height):
    volume = length * width * height
    return weight * 0.5 + volume * 0.01

cost = shipping_cost(10, 20, 15, 10)
print(cost)   # 5.0 + 3.0 = 8.0
```

**⑥ Format an account summary**
```python
def summary(account_id, balance, status):
    return f"Account {account_id}: ${balance} ({status})"

print(summary('A100', 2500, 'Active'))
```

> ⚠️ **WARNING:** Mismatching the number of arguments and parameters raises a `TypeError`.  
> If you define `def f(x, y):` and call `f(5)`, Python will complain.  
> Count your arguments carefully.

> 💡 **ADVANCED TIP – Keyword arguments (preview):**  
> You can also pass arguments by name, not by position:  
> `full_name(last='PyPhone', first='Emperor')` works the same.  
> This is useful when a function has many parameters and you want to be explicit.  
> You will master keyword arguments in a future lesson; for now, stick to positional matching.

---

## 💡 Real‑world Usage

**Banking – transfer between accounts**
```python
def transfer(sender, receiver, amount):
    return f"Transferring ${amount} from {sender} to {receiver}"

print(transfer('A123', 'B456', 500))
```

**E‑commerce – generate product label**
```python
def product_label(product_name, sku):
    return f"{product_name} [{sku}]"

print(product_label('Wireless Mouse', 'SKU-001'))
```

**Logistics – calculate delivery days**
```python
def delivery_est(distance_km, speed_kmh):
    return distance_km / speed_kmh

days = delivery_est(500, 60) / 24
print(f"Delivery in {days:.1f} days")
```

**HR – build employee record string**
```python
def employee_record(id, name, department):
    return f"ID: {id}, Name: {name}, Dept: {department}"

print(employee_record(101, 'Emperor', 'Engineering'))
```

**Reporting – sum monthly expenses**
```python
def sum_monthly(rent, utilities, groceries):
    return rent + utilities + groceries

total = sum_monthly(500, 120, 300)
print(f"Monthly total: ${total}")
```

---

## 🔍 Practice Preview
You will write three functions that take parameters and return results.

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Define `add(a,b)` returning `a+b`. Call with 3,5 and print. | `8`             |
| Medium | Define `full_name(first,last)` returning `'first last'`. Call with `'Emperor','PyPhone'` and print. | `Emperor PyPhone` |
| Hard   | Define `power(base,exp)` returning `base**exp`. Call with 2,10 and print. | `1024`          |

Run the coach:
```bash
python ii_Practice_Sheets/L-30_Parameters_Arguments.py
```
Choose `1`, `2`, or `3`. Type your function definition and call; the engine checks output.

---

## 📌 Key Takeaway
- Parameters are placeholders (defined in `def`); arguments are actual values (passed at call).
- Positional arguments match by order — first to first, second to second.
- Functions with multiple parameters handle diverse business inputs.
- Use clear parameter names to make your function self‑documenting.
- This is the gateway to building reusable business modules — the exact pattern you’ll use for Companion’s logic.