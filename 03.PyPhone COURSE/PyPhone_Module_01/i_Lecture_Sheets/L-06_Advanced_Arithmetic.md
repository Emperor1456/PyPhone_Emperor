# 📘 PyPhone Emperor · Module 1  
# 📖 L‑06 – Advanced Arithmetic Operators

---

## 🎯 OBJECTIVE
Learn the four advanced arithmetic operators
in Python that go beyond basic `+`, `-`, `*`, `/`.
These are essential for integer division,
remainders, exponentiation, and algorithms.

---

## 🧱 BRICK 1 – Floor Division and Modulus

### Floor Division `//`
Divides and **chops off** the decimal part
(always rounds down, even for negatives).

```python
print(10 // 3)   # 3
print(15 // 4)   # 3
print(-10 // 3)  # -4  (rounds down, not toward zero)
print(10.5 // 3) # 3.0
```

### Modulus `%`
Returns the **remainder** of a division.

```python
print(10 % 3)    # 1   (3×3=9, remainder 1)
print(15 % 4)    # 3
print(10 % 2)    # 0   (even number)
print(11 % 2)    # 1   (odd number)
```

### Relationship between `//` and `%`
For any integers `a` and `b`:
```python
a == (a // b) * b + (a % b)
```

> 💡 **INSIGHT:** `% 2` is the classic way to test if a number is even or odd.

---

## 🧱 BRICK 2 – Exponentiation

### Exponentiation `**`
Raises a number to a power.

```python
print(2 ** 3)    # 8   (2 × 2 × 2)
print(5 ** 2)    # 25  (5 squared)
print(10 ** 0)   # 1   (anything to power 0 is 1)
print(2 ** -1)   # 0.5 (negative exponent = reciprocal)
print(4 ** 0.5)  # 2.0 (square root)
```

### Operator precedence (PEMDAS)
Python evaluates in this order:
1. `**` (right to left)
2. `*`, `/`, `//`, `%` (left to right)
3. `+`, `-` (left to right)

```python
print(2 ** 3 ** 2)   # 2 ** (3 ** 2) = 2 ** 9 = 512
print(10 + 5 * 2)    # 10 + 10 = 20
print((10 + 5) * 2)  # 15 * 2 = 30
```

> ⚠️ **COMMON PITFALL:** `**` is right‑associative. `2**3**2` means `2**(3**2)`, not `(2**3)**2`.

---

## 💡 Real‑world Usage
Floor division and modulus are used everywhere
in scheduling, hashing, and page‑number calculations.

```python
# Calculate pages needed for a report
total_lines = 47
lines_per_page = 10
pages = total_lines // lines_per_page
if total_lines % lines_per_page != 0:
    pages += 1
print("Pages needed:", pages)
```

---

## 🔍 Practice Preview (for later coding)
```python
# Floor division and modulus
dividend = 17
divisor = 5
print("Floor division:", dividend // divisor)  # 3
print("Remainder:", dividend % divisor)        # 2

# Exponentiation
base = 2
power = 10
print("2^10 =", base ** power)

# Check even/odd
number = 42
print("Is even?", number % 2 == 0)

# Square root
print("Square root of 25:", 25 ** 0.5)
```

---

## 📌 Key Takeaway
- `//` divides and floors (rounds down).
- `%` gives the remainder after division.
- `**` raises to a power; use `** 0.5` for square root.
- Know the precedence: `**` first, then `* / // %`, then `+ -`.