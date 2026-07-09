# 📘 PyPhone Emperor · Module 4  
# 📖 L‑31 – Return Values (Sending Results Back)

---

## 🎯 OBJECTIVE  
Master the `return` statement to send computed values back from functions.  
A function that returns a value becomes a reusable processor — it can feed results into variables,  
expressions, or other functions. This is how enterprise code builds data pipelines.

---

## 🧱 BRICK 1 – The `return` Statement

`return` exits the function immediately and hands a value to the caller.  
Without `return`, the function defaults to `None`.

**① Doubling a value – price markup**
```python
def double(x):
    return 2 * x

result = double(5)
print(result)   # 10
```
`double(5)` computes 10 and sends it back.  
The caller captures it in `result` or uses it directly in `print()`.

**② Absolute value – distance from zero**
```python
def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

val = absolute(-7)
print(val)   # 7
```
Negative inputs flip to positive; positive inputs pass through unchanged.  
This is the Medium practice task — a classic validation helper.

**③ Even/odd check – transaction ID validation**
```python
def is_even(n):
    return n % 2 == 0

check = is_even(8)
print(check)   # True
```
The expression `n % 2 == 0` evaluates to `True` or `False`,  
and that boolean is returned directly. This is the Hard practice task.

> 💡 **INSIGHT:** A function can have multiple `return` statements.  
> The first one reached ends the function — code after it is ignored.

---

## 🧱 BRICK 2 – Using Return Values in Business Logic

**④ Tax calculation**
```python
def tax(amount, rate=0.1):
    return amount * rate

price = 200
total_price = price + tax(price)
print(total_price)   # 220.0
```

**⑤ Validation with early return**
```python
def safe_divide(a, b):
    if b == 0:
        return None   # early exit on invalid input
    return a / b

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # None
```

**⑥ Chain function calls**
```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result = multiply(add(2, 3), 4)   # (2+3) * 4 = 20
print(result)   # 20
```

> ⚠️ **WARNING:** Code after `return` in the same block is dead — it never runs.

> 💡 **ADVANCED TIP:** Return values make functions **composable**.  
> You can nest calls, build pipelines, and test each function independently.

---

## 💡 Real‑world Usage

**Banking – calculate interest**
```python
def interest(principal, rate, years):
    return principal * rate * years

print(interest(1000, 0.05, 2))   # 100.0
```

**E‑commerce – compute discount**
```python
def discount(price, percent):
    return price * (percent / 100)

print(discount(500, 10))   # 50.0
```

**Logistics – fuel cost**
```python
def fuel_cost(distance, efficiency, price_per_liter):
    return (distance / efficiency) * price_per_liter

print(fuel_cost(300, 15, 1.2))   # 24.0
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Define `double(x)` returning `2*x`. Call with 5 and print. | `10` |
| Medium | Define `absolute(x)` returning `x if x>=0 else -x`. Call with -7 and print. | `7` |
| Hard   | Define `is_even(n)` returning `True if n%2==0 else False`. Call with 8 and print. | `True` |

Run the coach:
```bash
python ii_Practice_Sheets/L-31_Return_Values.py
```

---

## 📌 Key Takeaway
- `return` sends a value back to the caller and ends the function.
- Functions without `return` evaluate to `None`.
- Multiple `return` statements allow early exits.
- Return values enable function chaining and composability.