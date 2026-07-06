# 📘 PyPhone Emperor · Module 8
# 📖 L‑61 – Decorators (Basic)

---

## 🎯 OBJECTIVE
Learn to write and use **decorators** — functions that wrap
other functions to add behaviour before and/or after the
original call, without modifying the original function’s code.
Decorators are the foundation of middleware, logging,
authentication, and performance measurement.

---

## 🧱 BRICK 1 – Functions as Objects

In Python, functions are **first‑class citizens**: you can
pass them as arguments, return them from other functions,
and assign them to variables.

```python
def greet():
    return "Hello"

say = greet             # assign function to variable
print(say())            # Hello
```

A function can **accept a function** as a parameter:

```python
def execute(func):
    return func()

print(execute(greet))   # Hello
```

A function can **return a new function**:

```python
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
print(double(5))        # 10
```

> 💡 **INSIGHT:** This ability to treat functions as data
> is what makes decorators possible.

---

## 🧱 BRICK 2 – Building a Decorator

A decorator is a function that takes a function, defines
an inner **wrapper** that adds logic, and returns the wrapper.

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper
```

Apply the decorator with `@syntax`:

```python
@logger
def add(a, b):
    return a + b

print(add(3, 5))
# Output:
# Calling add
# add returned 8
# 8
```

Without `@`, the same effect is:
```python
add = logger(add)
```

### Decorators with parameters (advanced concept):
```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello!")
```
This is a **decorator factory** — it returns a decorator.

> ⚠️ **WARNING:** The wrapper’s name and docstring become
> those of the wrapper, not the original. Use
> `functools.wraps` to preserve metadata in production code.

---

## 📌 Key Takeaway
- Functions are objects; they can be passed and returned.
- A decorator is a function that wraps another function.
- `@decorator` applies the wrapper automatically.
- Use decorators for cross‑cutting concerns like logging.