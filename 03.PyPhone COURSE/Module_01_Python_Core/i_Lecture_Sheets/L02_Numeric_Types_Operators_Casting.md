# 📘 PyPhone Emperor v3.0 · Module 1
# 📖 L‑02 – Numeric Types, Operators & Type Casting

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, every number in Python will obey you.

- 🔢 **Numeric Types:** `int`, `float`, `complex` — when and why.
- 🧮 **Arithmetic Operators:** `+`, `-`, `*`, `/`, `//`, `%`, `**`.
- 🔄 **Type Casting:** `int()`, `float()`, `complex()` — safe and explicit conversion.
- ⚡ **Operator Precedence:** PEMDAS in Python.
- 🐍 **Edge Cases:** Division by zero, float precision, overflow (or lack thereof).

---

## 🧱 THE CORE CONCEPT – Python’s Three Numeric Types

Python has three built‑in numeric types. You will use `int` and `float` daily;
`complex` appears in scientific and engineering applications.

| Type | Example | Description |
|------|---------|-------------|
| `int` | `42`, `-7`, `0` | Whole numbers, arbitrary precision |
| `float` | `3.14`, `-0.001`, `1.5e3` | Decimal numbers, 64‑bit IEEE |
| `complex` | `2+3j`, `-1j` | Real + imaginary component |

### Integer Precision
Python integers have **no maximum size** (unlike C/Java).
```python
big = 2 ** 1000   # a number with 302 digits — works perfectly
print(big)
```

### Float Precision
Floats are 64‑bit IEEE 754 — about 15‑17 decimal digits of precision.
```python
print(0.1 + 0.2)   # 0.30000000000000004 — classic floating‑point artifact
```

> 💡 **INSIGHT:** For money, never use `float`. Use `int` (cents) or the `decimal` module.
> We’ll cover this in error handling when dealing with financial data.

---

## 🧱 ARITHMETIC OPERATORS – The Full Arsenal

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | True Division | `5 / 2` | `2.5` (always float) |
| `//` | Floor Division | `5 // 2` | `2` (integer quotient) |
| `%` | Modulo | `5 % 2` | `1` (remainder) |
| `**` | Exponentiation | `2 ** 10` | `1024` |

```python
print(10 / 3)    # 3.3333333333333335
print(10 // 3)   # 3
print(10 % 3)    # 1
print(2 ** 8)    # 256
```

> ⚠️ **WARNING:** Division `/` always returns a `float`, even if the result is a whole number.
> Use `//` when you need an integer quotient, but be careful with negative numbers:
> `-5 // 2` returns `-3` (floor, not truncation).

---

## 🧱 TYPE CASTING – Explicit Conversion

Python never implicitly converts numbers to strings or vice versa.
You must cast explicitly.

```python
x = 42
y = "100"

# int to float
print(float(x))         # 42.0

# string to int
print(int(y))           # 100

# int to string
print(str(x) + "px")    # "42px"

# float to int (truncates, does NOT round)
print(int(3.9))         # 3
print(int(-3.9))        # -3
```

### Safe Casting
```python
user_input = "  15  "
cleaned = int(user_input.strip())   # 15
```

Invalid conversions raise `ValueError`:
```python
int("abc")   # ValueError
```

> 💡 **INSIGHT:** Always sanitise user input before casting.
> Use `.strip()` and validation logic. We’ll handle this formally in error handling (Module 6).

---

## 🧱 OPERATOR PRECEDENCE (PEMDAS)

Python follows mathematical precedence:
1. **P**arentheses
2. **E**xponentiation (`**`)
3. **M**ultiplication / **D**ivision / Floor / Modulo
4. **A**ddition / **S**ubtraction

```python
print(2 + 3 * 4)       # 14, not 20
print((2 + 3) * 4)     # 20
print(2 ** 3 ** 2)     # 512 (right‑associative: 2 ** (3 ** 2) = 2 ** 9)
```

> ⚠️ **WARNING:** Exponentiation is right‑associative. When chaining `**`, the rightmost group evaluates first.

---

## 💡 Real‑world Usage

**Banking – calculate simple interest**
```python
principal = 10000
rate = 0.05
years = 3
interest = principal * rate * years
print(interest)   # 1500.0
```

**E‑commerce – apply discount and compute tax**
```python
price = 2499.99
discount_percent = 20
tax_rate = 0.10

discounted = price * (1 - discount_percent / 100)
total = discounted * (1 + tax_rate)
print(round(total, 2))   # 2199.99
```

**Logistics – containers needed**
```python
total_items = 250
items_per_box = 24
boxes = total_items // items_per_box
leftover = total_items % boxes
print(f"{boxes} full boxes, {leftover} items left")
```

---

## 🔍 Practice Preview
You will:
- Perform all seven arithmetic operations on business data.
- Cast a string input to an integer for a stock count.
- Compute compound expressions using operator precedence.
- Handle a string‑to‑float conversion for a product price.

Run the coach:
```bash
python ii_Practice_Sheets/L02_Numeric_Types_Operators_Casting.py
```

---

## 📌 Key Takeaway
- Python has `int`, `float`, `complex` — `int` has unlimited precision.
- Use `//` for integer quotient, `%` for remainder, `/` always returns float.
- Cast explicitly with `int()`, `float()`, `str()` — never rely on automatic conversion.
- Respect PEMDAS; use parentheses for clarity.
- Money should be in cents (int) or use `decimal`.

*For Emperor.*
