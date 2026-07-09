# 📘 PyPhone Emperor · Module 8  
# 📖 L‑61 – Decorators (Basic) – Wrapping Business Functions with Logging & Validation

---

## 🎯 OBJECTIVE  
Master **decorators** — functions that modify other functions without changing their code.  
Use them to add logging, authentication, performance measurement, or output formatting to any business function.  
The `@decorator` syntax is the gateway to clean, reusable middleware in Python.

---

## 🧱 BRICK 1 – Functions as Objects

In Python, functions can be passed around, returned, and assigned — they are first‑class objects.

```python
def greet():
    return "Hello"

say = greet
print(say())   # Hello
```

A function can accept a function as an argument:
```python
def execute(func):
    return func()

print(execute(greet))   # Hello
```

A function can return a function (closure):
```python
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
print(double(5))   # 10
```

> 💡 **INSIGHT:** This ability to treat functions as data is what makes decorators possible.

---

## 🧱 BRICK 2 – Creating and Using Decorators

A decorator is a function that takes a function, defines an inner `wrapper` that adds extra behaviour, and returns the wrapper.

**① Bold decorator (Easy practice)**
```python
def bold(func):
    def wrapper():
        return f'<b>{func()}</b>'
    return wrapper

@bold
def say():
    return 'Hi'

print(say())   # <b>Hi</b>
```
The `@bold` syntax is equivalent to `say = bold(say)`. The wrapper adds HTML tags around the original result.

**② Uppercase decorator (Medium practice)**
```python
def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet():
    return 'hello'

print(greet())   # HELLO
```

**③ Stacking decorators (Hard practice)**
```python
@bold
@uppercase
def message():
    return 'hi'

print(message())   # <b>HI</b>
```
Decorators are applied bottom‑up: `@uppercase` runs first, then `@bold` wraps the result. The final output is the bold, uppercase string.

**④ Decorator for logging**
```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

print(add(3, 5))
# Output: Calling add / add returned 8 / 8
```

> ⚠️ **WARNING:** The wrapper hides the original function’s name and docstring. Use `functools.wraps(func)` inside the wrapper to preserve metadata in production.

> 💡 **ADVANCED TIP – Decorator factories:**  
> A function returning a decorator allows parameterised decorators, e.g., `@repeat(3)` to run a function three times.

---

## 💡 Real‑world Usage

**Banking – authentication decorator**
```python
def authenticated(func):
    def wrapper(user, *args, **kwargs):
        if not user.get('logged_in'):
            raise PermissionError("Authentication required")
        return func(user, *args, **kwargs)
    return wrapper

@authenticated
def view_balance(user):
    return user['balance']
```

**E‑commerce – discount application**
```python
def apply_discount(func):
    def wrapper(price, discount):
        return func(price, discount * 1.1)   # boost discount
    return wrapper

@apply_discount
def final_price(price, discount):
    return price - discount
```

**Logistics – measure execution time**
```python
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time()-start:.4f}s")
        return result
    return wrapper
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Define a decorator `bold` that wraps the return value of a function in `<b>..</b>`. Apply it to a function `say()` returning `'Hi'`. Print the result of calling `say()`. | `<b>Hi</b>` |
| Medium | Define a decorator `uppercase` that converts the string return value to uppercase. Apply to a function `greet` returning `'hello'`. Print the result. | `HELLO` |
| Hard   | Stack both decorators on a function `message` returning `'hi'`. The bold should be applied first (outermost). Print result. | `<b>HI</b>` |

Run the coach:
```bash
python ii_Practice_Sheets/L-61_Decorators.py
```

---

## 📌 Key Takeaway
- Decorators wrap functions to extend behaviour without modification.
- `@decorator` applies the wrapper at definition time.
- Stacking applies bottom‑up: the first `@` is outermost.
- Use `*args, **kwargs` to make wrappers compatible with any function signature.
- Essential for middleware: logging, access control, output formatting.