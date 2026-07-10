# 📘 PyPhone Emperor v3.0 · Module 9
# 📖 L‑55 – Decorators – Wrapping Functions

---

## 🎯 OBJECTIVE — What You Will Master

> Modify or enhance functions without changing their code.

- 🧵 **Decorator** – a function that takes a function and returns a new one
- 🎁 **`@decorator` syntax** – apply a decorator to a function
- 🧪 **Why decorators** – logging, timing, access control
- 🛠️ **`functools.wraps`** – preserve original function metadata

---

## 🧱 A SIMPLE DECORATOR

```python
def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

@bold
def greet():
    return "Hello"

print(greet())   # <b>Hello</b>
```

---

## 🧱 LOGGING DECORATOR

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

add(3, 5)
# Output:
# Calling add
# add returned 8
```

---

## 🧱 PRESERVING METADATA

```python
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

---

## 💡 Real‑world Usage

**Banking – authentication decorator**
```python
def authenticated(func):
    def wrapper(user, *args, **kwargs):
        if not user.is_authenticated:
            raise PermissionError("Login required")
        return func(user, *args, **kwargs)
    return wrapper
```

**E‑commerce – timing decorator**
```python
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Took {time.time()-start:.2f}s")
        return result
    return wrapper
```

**Logistics – retry decorator**
```python
def retry(max_attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts-1:
                        raise
                    print(f"Retrying... ({attempt+1})")
        return wrapper
    return decorator
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Create a decorator that wraps output in `<b>..</b>`. |
| Medium | Create a decorator that converts return value to uppercase. |
| Hard | Stack two decorators on a function and print the combined result. |

Run the coach:
```bash
python ii_Practice_Sheets/L55_Decorators_Wrapping_Functions.py
```

---

## 📌 Key Takeaway
- Decorators wrap functions, adding behavior before/after.
- Use `@decorator` to apply; stack them bottom‑up.
- Always use `@wraps` to preserve the original function's name and docstring.

*For Emperor.*