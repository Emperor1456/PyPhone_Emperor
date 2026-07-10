# 📘 PyPhone Emperor v3.0 · Module 5
# 📖 L‑24 – `def` – Functions, Docstrings & Type Hints

---

## 🎯 OBJECTIVE — What You Will Master

> Create reusable logic blocks with clear documentation and type annotations.

- 🔧 **`def` keyword** – define your own callable functions
- 📝 **Docstrings** – document what the function does
- 🏷️ **Type hints** – annotate parameter and return types
- 🧪 **Why functions matter** – DRY principle, testability, readability

---

## 🧱 DEFINING A SIMPLE FUNCTION

```python
def greet():
    print("Hello, Emperor!")
greet()   # calls the function
```

Functions must be defined **before** they are called.

---

## 🧱 ADDING DOCSTRINGS

A docstring explains the function’s purpose and usage.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
print(add(2, 3))   # 5
```

Access the docstring: `help(add)` or `add.__doc__`.

---

## 🧱 TYPE HINTS (OPTIONAL BUT POWERFUL)

```python
def multiply(x: float, y: float) -> float:
    """Multiply two floats and return the product."""
    return x * y
```

Hints improve readability and enable tooling (linters, IDE autocomplete). They are not enforced at runtime.

---

## 💡 Real‑world Usage

**Banking – interest calculation**
```python
def calc_interest(principal: float, rate: float, years: int) -> float:
    """Compute simple interest."""
    return principal * rate * years
```

**E‑commerce – tax calculator**
```python
def add_tax(price: float, tax_rate: float = 0.10) -> float:
    """Return price with tax added."""
    return price * (1 + tax_rate)
```

**Logistics – shipping cost**
```python
def shipping_cost(weight: float, distance: float) -> float:
    """Calculate shipping cost based on weight and distance."""
    return weight * 0.5 + distance * 0.02
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Define a function `hello()` that prints "Hello, Emperor" and call it. | `def hello(): print(...)` |
| Medium | Define `greet(name)` returning "Hi, " + name. Call with "Emperor". | `def greet(n): return "Hi, "+n` |
| Hard | Define `square(x: int) -> int` with a docstring and type hints. Call with 5. | `def square(x: int) -> int: ...` |

Run the coach:
```bash
python ii_Practice_Sheets/L24_def_Functions_Docstrings_Type_Hints.py
```

---

## 📌 Key Takeaway
- Functions encapsulate logic; use `def`.
- Document with docstrings; annotate types for clarity.
- Define once, call many times – the heart of DRY.

*For Emperor.*