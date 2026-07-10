# 📘 Module 05 – Functions & Scope · Revision Guide

---

## L24 – Defining Functions, Docstrings & Type Hints

- `def name(params):` creates a reusable block.
- Docstring: triple‑quoted string right after the `def` line.
- Type hints: `def add(a: int, b: int) -> int:` (optional but powerful).

```python
def multiply(x: float, y: float) -> float:
    """Return the product of two floats."""
    return x * y
```

---

## L25 – Parameters, Arguments & `__name__ == "__main__"`

- Parameters are placeholders; arguments are actual values.
- Positional arguments matched by order; keyword arguments by name.
- `if __name__ == "__main__":` runs code only when script is executed directly.

```python
def greet(name, title="Mr."):
    print(f"Hello, {title} {name}")
if __name__ == "__main__":
    greet("Emperor")
```

---

## L26 – Return Values & Early Return Pattern

- `return` sends a value back and ends the function.
- Early return handles edge cases first.
- Multiple values returned as a tuple.

```python
def safe_divide(a, b):
    if b == 0:
        return None
    return a / b
```

---

## L27 – Default Parameters & Mutable Pitfall

- Defaults make arguments optional: `def f(x=10)`.
- Never use mutable objects as defaults; use `None` and create inside.

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

## L28 – `*args`, `**kwargs` & Unpacking

- `*args` collects extra positional arguments into a tuple.
- `**kwargs` collects extra keyword arguments into a dict.
- Unpack with `*` (iterables) and `**` (dicts).

```python
def log_event(event, **details):
    print(f"[{event}] {details}")
```

---

## L29 – LEGB Rule (Variable Scope)

- Lookup order: **L**ocal → **E**nclosing → **G**lobal → **B**uilt‑in.
- `global` modifies a global variable inside a function.
- `nonlocal` modifies a variable in the enclosing (nested) function.

```python
x = "global"
def outer():
    x = "enclosing"
    def inner():
        nonlocal x
        x = "inner"
    inner()
    return x
```

---

## L30 – Lambda Functions, map(), filter(), sorted()

- `lambda args: expression` creates anonymous functions.
- `map(func, iterable)` applies a function to every item.
- `filter(func, iterable)` keeps items for which func returns True.
- `sorted(iterable, key=func)` sorts using a custom key.

```python
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=lambda w: len(w))
```

---

## L31 – Recursion & Memoization

- A function calling itself.
- Must have a base case to stop recursion.
- `functools.lru_cache` caches results for speed.

```python
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n-1)
```

---

**Quick Test:**  
- What is the difference between a parameter and an argument?  
- Why should you never use an empty list as a default argument?  
- When would you use `*args` instead of a regular parameter?  
- What is the purpose of `__name__ == "__main__"`?

*Review complete. You are now ready for the Module 05 Practice Review.*