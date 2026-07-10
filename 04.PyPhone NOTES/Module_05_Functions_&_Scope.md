# 📘 Module 05 – Functions & Scope · Revision Note

---

## L24 – def – Functions, Docstrings & Type Hints
- `def name(params):` creates a reusable block.
- Docstring: triple‑quoted string after `def`.
- Type hints: `def add(a: int, b: int) -> int:`.

```python
def multiply(x: float, y: float) -> float:
    """Return the product of two floats."""
    return x * y
```

---

## L25 – Parameters, Arguments & `__name__ == "__main__"`
- Parameters are placeholders; arguments are actual values.
- Positional arguments matched by order; keyword by name.
- `if __name__ == "__main__":` guards script execution.

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
    if b == 0: return None
    return a / b
```

---

## L27 – Default Parameters & Mutable Pitfall
- Defaults make arguments optional: `def f(x=10)`.
- Never use mutable objects as defaults – use `None`.

```python
def add_item(item, items=None):
    if items is None: items = []
    items.append(item)
    return items
```

---

## L28 – *args, **kwargs & Unpacking
- `*args` collects positional arguments into a tuple.
- `**kwargs` collects keyword arguments into a dict.
- Unpack with `*` (iterables) and `**` (dicts).

```python
def log_event(event, **details):
    print(f"[{event}] {details}")
```

---

## L29 – LEGB Rule (Variable Scope)
- Lookup order: **L**ocal → **E**nclosing → **G**lobal → **B**uilt‑in.
- `global` modifies global variable inside function.
- `nonlocal` modifies variable in enclosing (nested) function.

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
- `lambda args: expression` – anonymous one‑liner.
- `map(func, iterable)` – apply function to all items.
- `filter(func, iterable)` – keep items where func is True.
- `sorted(iterable, key=func)` – sort using custom key.

```python
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=lambda w: len(w))
```

---

## L31 – Recursion & Memoization
- Function calling itself; must have base case.
- `functools.lru_cache` caches results for speed.

```python
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
```

---

*Quick Test:*  
- Parameter vs argument?  
- Why never use empty list as default?  
- When to use `*args`?  
- Purpose of `__name__ == "__main__"`?