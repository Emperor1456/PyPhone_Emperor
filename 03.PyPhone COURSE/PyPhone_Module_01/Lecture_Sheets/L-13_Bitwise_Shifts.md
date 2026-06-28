# 📘 PyPhone Emperor · Module 1  
# 📖 L‑13 – Bitwise Shifts (`<<` and `>>`)

---

## 🎯 OBJECTIVE
Learn to shift bits left and right using
`<<` and `>>`. These operators efficiently
multiply or divide by powers of two and
are used in graphics, compression,
and low‑level data packing.

---

## 🧱 BRICK 1 – Left Shift `<<`

Shifts all bits to the **left** by a given
number of positions. Zeros fill the right side.
Each left shift **multiplies** the number by 2.

```python
x = 5       # binary: 101
print(x << 1)   # 10   (101 → 1010 = 10)
print(x << 2)   # 20   (101 → 10100 = 20)
print(x << 3)   # 40   (101 → 101000 = 40)
```

### Visual representation
```
5      =     1 0 1
5 << 1 =   1 0 1 0   = 10
5 << 2 = 1 0 1 0 0   = 20
```

### General rule
```
x << n  =  x * (2 ** n)
```
```python
print(5 << 3)           # 40
print(5 * (2 ** 3))     # 40  (same)
```

> 💡 **INSIGHT:** Left shift is a fast way to double a number repeatedly.

---

## 🧱 BRICK 2 – Right Shift `>>`

Shifts all bits to the **right** by a given
number of positions. Bits shifted past the
rightmost position are **discarded**.
Each right shift **divides** (floors) by 2.

```python
x = 40      # binary: 101000
print(x >> 1)   # 20   (101000 → 10100 = 20)
print(x >> 2)   # 10   (101000 → 1010 = 10)
print(x >> 3)   # 5    (101000 → 101 = 5)
print(x >> 4)   # 2    (101000 → 10 = 2)
```

### Visual representation
```
40       = 1 0 1 0 0 0
40 >> 1  =   1 0 1 0 0   = 20
40 >> 2  =     1 0 1 0   = 10
40 >> 3  =       1 0 1   = 5
```

### General rule
```
x >> n  =  x // (2 ** n)
```
```python
print(40 >> 3)          # 5
print(40 // (2 ** 3))   # 5  (same)
```

> ⚠️ **WARNING:** For negative numbers, right shift fills with 1s on the left (arithmetic shift), preserving sign.

---

## 💡 Shifts vs Multiplication/Division

Bit shifts are **faster** than multiplication
or division, though Python optimises both.
They are essential in:
- Embedded systems and microcontrollers
- Graphics programming (pixel manipulation)
- Hash functions and checksums
- Network packet encoding

---

## 💡 Real‑world Usage

### Packing RGB values into a single integer
```python
# Each color: 0–255 (8 bits)
red   = 200
green = 150
blue  = 100

# Pack into one 24‑bit integer
packed = (red << 16) | (green << 8) | blue
print(packed)

# Extract colors back
r = (packed >> 16) & 0xFF
g = (packed >> 8) & 0xFF
b = packed & 0xFF
print(r, g, b)   # 200 150 100
```

### Fast multiplication/division by powers of 2
```python
value = 1
value <<= 10    # 1 * 2^10 = 1024
print(value)    # 1024
value >>= 5     # 1024 // 32 = 32
print(value)    # 32
```

---

## 🔍 Practice Preview (for later coding)
```python
x = 1

# Left shifts (multiply by 2 each time)
print("Left shifts:")
for i in range(5):
    shifted = x << i
    print(f"1 << {i} = {shifted}")

# Right shifts (divide by 2 each time)
y = 64
print("\nRight shifts:")
for i in range(5):
    shifted = y >> i
    print(f"64 >> {i} = {shifted}")

# Pack and unpack RGB
r, g, b = 255, 128, 64
packed = (r << 16) | (g << 8) | b
print("\nPacked:", packed)
print("Unpacked:", (packed >> 16) & 0xFF,
                   (packed >> 8) & 0xFF,
                   packed & 0xFF)
```

---

## 📌 Key Takeaway
- `<< n` multiplies by `2**n`.
- `>> n` floor‑divides by `2**n`.
- Bits shifted off the end are lost.
- Essential for data packing, graphics, and fast arithmetic.