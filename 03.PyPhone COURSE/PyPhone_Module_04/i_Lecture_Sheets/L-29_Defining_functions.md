# 📘 PyPhone Emperor · Module 4  
# 📖 L‑29 – Defining a Function (`def`) (Reusable Business Logic)

---

## 🎯 OBJECTIVE  
Master the `def` statement to create reusable, callable blocks of code.  
Functions are the building blocks of enterprise software — they encapsulate  
logic for greetings, calculations, validations, and business rules,  
making your code modular, testable, and maintainable.

---

## 🧱 BRICK 1 – The `def` Statement and Basic Calls

A function is defined with `def`, a name, parentheses, and a colon.  
The indented body executes only when the function is **called**.

```python
def function_name():
    # body – runs when called
```

**① Customer greeting message**
```python
def hello():
    print('Hello, Emperor')

hello()   # prints 'Hello, Emperor'
```
This mirrors the Easy practice task: define a simple function that prints a business greeting.

**② Logging a standard confirmation**
```python
def confirm():
    print('Transaction completed.')

confirm()   # 'Transaction completed.'
confirm()   # can be called repeatedly
```
Reuse the same logic anywhere without rewriting `print` statements.

> 💡 **INSIGHT:** A function is inert until called.  
> `def` creates the function; `function_name()` executes it.

> ⚠️ **WARNING:** The function must be defined **before** it’s called.  
> Python reads code top‑to‑bottom, so place your `def` blocks above the first call.

---

## 🧱 BRICK 2 – Functions with Return Values

A function can send a value back to the caller using `return`.  
This makes it a mini‑processor that can be used inside other expressions.

**③ Personalized greeting with return (Medium practice)**
```python
def greet(name):
    return 'Hi, ' + name

message = greet('Emperor')
print(message)   # 'Hi, Emperor'
```
The function computes a string and hands it back.  
You can use the result directly in `print()` or assign it to a variable.

**④ Business calculation – square of a number (Hard practice)**
```python
def square(x):
    return x * x

result = square(5)
print(result)   # 25
```
This is a typical utility function for financial or engineering calculations.

**⑤ Combining function calls**
```python
print(square(3) + square(4))   # 9 + 16 = 25
```
Because `square()` returns a value, it can be used inside arithmetic expressions.

> 💡 **ADVANCED TIP – Functions as building blocks:**  
> Enterprise code is built by assembling many small, well‑named functions.  
> Each function does **one thing** — greet, calculate, validate.  
> When you build Companion, you’ll write functions for memory retrieval,  
> emotion detection, and response generation.

> ⚠️ **WARNING:** If a function has no `return` statement, it returns `None` by default.  
> Don’t accidentally `print` where you meant to `return`.

---

## 💡 Real‑world Usage

**Banking – log a standard alert**
```python
def fraud_alert():
    print('Alert: Suspicious activity detected.')

fraud_alert()
```

**E‑commerce – calculate tax**
```python
def calculate_tax(price):
    return price * 0.05

tax = calculate_tax(200)
print(f"Tax: {tax}")
```

**Logistics – generate a tracking prefix**
```python
def tracking_prefix():
    return 'TRK-'

track_id = tracking_prefix() + '12345'
print(track_id)   # 'TRK-12345'
```

**HR – standard employee ID formatter**
```python
def format_id(number):
    return 'EMP-' + str(number)

print(format_id(42))   # 'EMP-42'
```

**Reporting – a reusable header**
```python
def print_header(report_name):
    print(f"=== {report_name} ===")

print_header('Sales Q3')
print_header('Inventory')
```

---

## 🔍 Practice Preview
You will write three function‑definition mini‑programs.

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Define a function `hello()` that prints `'Hello, Emperor'`. Call it. | `Hello, Emperor` |
| Medium | Define `greet(name)` returning `'Hi, '+name`. Call with `'Emperor'` and print the result. | `Hi, Emperor` |
| Hard   | Define `square(x)` returning `x*x`. Call with `5` and print the result. | `25` |

Run the coach:
```bash
python ii_Practice_Sheets/L-29_Defining_Function.py
```
Choose `1`, `2`, or `3`. Type your function and call; the engine checks output.

---

## 📌 Key Takeaway
- `def function_name():` creates a reusable code block.
- Call the function with `function_name()` to execute it.
- Use `return` to send a value back to the caller.
- Functions reduce repetition, improve readability, and enable testing.
- Every Companion module will be built from functions — this is the foundation.