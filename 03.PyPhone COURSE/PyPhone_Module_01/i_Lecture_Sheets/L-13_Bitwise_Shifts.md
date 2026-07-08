# 📘 PyPhone Emperor · Module 1  
# 📖 L‑13 – Bitwise Shifts in Resource Packing

---

## 🎯 OBJECTIVE
Learn the bitwise shift operators `<<` (left shift)
and `>>` (right shift).
These operators move the bits of an integer
left or right, which is equivalent to multiplying
or dividing by powers of two.
Shifts are used in low‑level data packing,
color manipulation, efficient arithmetic,
and anywhere memory or speed is critical.

---

## 🧱 BRICK 1 – Left Shift (`<<`)

The left shift operator `<<` moves every bit
of a number to the left by a specified number
of positions. Each left shift **multiplies**
the number by `2`.

```python
x = 8
y = x << 2   # shift left by 2
print(y)     # 32  (8 × 2² = 32)
```

**How it works, bit by bit (8 << 2):**
```
  8  =  0000 1000  (binary)
<< 2  =  0010 0000  (shift left 2)
      =  32
```

### Multiplying by powers of two
- `x << 1` = `x * 2`
- `x << 2` = `x * 4`
- `x << 3` = `x * 8`

### Business example – packing multiple small values

Imagine you need to store a person's age (0‑63),
security level (0‑15), and score (0‑7) in a single
integer to save memory or send over a network.
You can pack them using left shifts.

```python
age   = 25     # 6 bits max
level = 12     # 4 bits max
score = 5      # 3 bits max

packed = (age << 7) | (level << 3) | score
# age shifted left 7, level shifted left 3, score stays
print(packed)
```

Each value occupies its own field inside the
packed integer, with no overlap.

> 💡 `<<` is the fastest way to multiply by powers of two
> in performance‑critical code and the standard way
> to create space for more bits.

---

## 🧱 BRICK 2 – Right Shift (`>>`)

The right shift operator `>>` moves every bit
to the right. Each right shift **divides**
the number by `2` (integer division).

```python
x = 8
y = x >> 2   # shift right by 2
print(y)     # 2  (8 ÷ 2² = 2)
```

**How it works, bit by bit (8 >> 2):**
```
  8  =  0000 1000  (binary)
>> 2  =  0000 0010  (shift right 2)
      =  2
```

### Dividing by powers of two (integer division)
- `x >> 1` = `x // 2`
- `x >> 2` = `x // 4`
- `x >> 3` = `x // 8`

### Business example – extracting packed data

From the packed integer above, you can recover
the original values using right shifts and
a bitmask.

```python
packed = 10245   # example packed value
age   = packed >> 7               # extract age (shift right 7)
level = (packed >> 3) & 0b1111    # extract level (4 bits)
score = packed & 0b111            # extract score (3 bits)
print(age, level, score)
```

The right shift pushes the relevant bits down
to the least significant positions;
the mask keeps only the bits you want.

> 💡 `>>` is the fastest way to perform integer division
> by powers of two, and the standard way to
> extract fields from packed integers.

---

## 💡 Real‑world Usage

### Color manipulation (RGB packing)
24‑bit colors are a classic use case.
Each component (red, green, blue) is 8 bits,
packed into a single integer.

```python
red   = 200
green = 150
blue  = 100

packed = (red << 16) | (green << 8) | blue
print(packed)

r = (packed >> 16) & 0xFF
g = (packed >> 8) & 0xFF
b = packed & 0xFF
print(r, g, b)   # 200 150 100
```

### Network packet encoding
Protocol headers often pack multiple fields
into a single 32‑bit word. You build the header
with left shifts and parse it with right shifts.

### Embedded systems
Microcontrollers with limited RAM use bit‑packing
to store sensor data, flags, and counters
in as few bytes as possible.

---

## 🔍 Practice Preview
You will perform four shift operations.

- **Easy:** Print the result of `8 << 2`.
- **Medium:** Print the result of `8 >> 2`.
- **Hard:** Print the result of `10 << 2` on the first line,
  and `20 >> 2` on the second line.

Run the practice coach:
```bash
python ii_Practice_Sheets/L-13_Bitwise_Shifts.py
```

Choose your level, type the script, and the engine will verify.

---

## 📌 Key Takeaway
- `<< n` multiplies by `2**n`.
- `>> n` floor‑divides by `2**n`.
- Left shifts create space; right shifts extract.
- The bit‑shifting pattern is universal: from RGB colors
  to network protocols, from databases to embedded systems.