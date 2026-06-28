# 📘 PyPhone Emperor · Module 1  
# 📖 L‑10 – Compound Assignments (All)

---

## 🎯 OBJECTIVE
Complete your mastery of all compound
assignment operators in Python:
`*=`, `/=`, `//=`, `%=`, `**=`.
These operators let you perform an
operation and assign the result in
one compact step.

---

## 🧱 BRICK 1 – Multiply, Divide, Floor Divide

### Multiply‑and‑assign `*=`
```python
x = 4
x *= 3        # same as: x = x * 3
print(x)      # 12
```

### Divide‑and‑assign `/=`
```python
x = 20
x /= 4        # same as: x = x / 4
print(x)      # 5.0  (division always gives float)
```

### Floor‑divide‑and‑assign `//=`
```python
x = 20
x //= 3       # same as: x = x // 3
print(x)      # 6
```

> ⚠️ **WARNING:** `//=` floors the result, so `-20 //= 3` gives `-7` (not `-6`).

---

## 🧱 BRICK 2 – Modulus and Power

### Modulus‑and‑assign `%=`
```python
x = 17
x %= 5        # same as: x = x % 5
print(x)      # 2  (remainder of 17 ÷ 5)
```

### Power‑and‑assign `**=`
```python
x = 2
x **= 5       # same as: x = x ** 5
print(x)      # 32  (2⁵)
```

---

## 💡 Complete Reference Table

| Operator | Equivalent To      |
|----------|--------------------|
| `x += y` | `x = x + y`        |
| `x -= y` | `x = x - y`        |
| `x *= y` | `x = x * y`        |
| `x /= y` | `x = x / y`        |
| `x //= y`| `x = x // y`       |
| `x %= y` | `x = x % y`        |
| `x **= y`| `x = x ** y`       |

---

## 💡 Real‑world Usage
```python
# Compound interest calculation
principal = 1000
rate = 1.05    # 5% growth
principal *= rate   # year 1
principal *= rate   # year 2
principal *= rate   # year 3
print("After 3 years:", principal)

# Extracting digits with modulo
number = 1234
last_digit = number % 10    # 4
number //= 10               # remove last digit
print("Remaining:", number) # 123
```

---

## 🔍 Practice Preview (for later coding)
```python
# Test all compound assignments
x = 10
print("Start:", x)

x += 5
print("+= 5:", x)    # 15

x -= 3
print("-= 3:", x)    # 12

x *= 2
print("*= 2:", x)    # 24

x /= 4
print("/= 4:", x)    # 6.0

x //= 2
print("//= 2:", x)   # 3.0

x **= 3
print("**= 3:", x)   # 27.0

x %= 7
print("%= 7:", x)    # 6.0
```

---

## 📌 Key Takeaway
- Compound operators combine an operation with assignment.
- All seven follow the same pattern: `op=`.
- `//=` and `%=` are especially useful for integer algorithms.
- `/=` always produces a float.