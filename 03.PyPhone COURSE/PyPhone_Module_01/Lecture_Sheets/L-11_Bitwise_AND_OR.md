# 📘 PyPhone Emperor · Module 1  
# 📖 L‑11 – Bitwise AND (`&`) and OR (`|`)

---

## 🎯 OBJECTIVE
Learn to operate on numbers at the **bit level**
using the bitwise AND (`&`) and OR (`|`) operators.
These are essential for low‑level programming,
permissions, flags, and hardware interaction.

---

## 🧱 BRICK 1 – Understanding Bits

Computers store numbers in **binary** (base‑2).
A bit is a single 0 or 1.
A byte is 8 bits.

**Example: the number 5 in binary**
```
5  →  0 1 0 1   (4‑bit representation)
      8 4 2 1   (place values: 8, 4, 2, 1)
```
5 = 4 + 1 → bits at positions 4 and 1 are set.

### Common binary values
```
Decimal:  0   1   2   3   4   5   6   7
Binary:   000 001 010 011 100 101 110 111
```

> 💡 **TIP:** Think of bits as light switches — 1 is ON, 0 is OFF.

---

## 🧱 BRICK 2 – Bitwise AND (`&`) and OR (`|`)

### Bitwise AND `&`
Compares each pair of bits.
Result bit is **1 only if both input bits are 1**.
Otherwise, 0.

```
  5  =  1 0 1
& 3  =  0 1 1
─────────────
  1  =  0 0 1
```
```python
print(5 & 3)   # 1
```

### Bitwise OR `|`
Compares each pair of bits.
Result bit is **1 if at least one input bit is 1**.
Only 0 when both are 0.

```
  5  =  1 0 1
| 3  =  0 1 1
─────────────
  7  =  1 1 1
```
```python
print(5 | 3)   # 7
```

> 💡 **INSIGHT:** `&` is like a strict filter — both bits must be set. `|` is generous — any set bit passes.

---

## 💡 Real‑world Usage

### Permission flags (Unix‑style)
```python
READ    = 4   # binary 100
WRITE   = 2   # binary 010
EXECUTE = 1   # binary 001

# User has read + write
user_perm = READ | WRITE   # 6  (binary 110)

# Check if user has write
has_write = (user_perm & WRITE) != 0
print("Can write:", has_write)   # True

# Check if user has execute
has_exec = (user_perm & EXECUTE) != 0
print("Can execute:", has_exec)  # False
```

### Setting and checking flags
- Use `|` to **combine** flags.
- Use `&` to **check** if a flag is set.

---

## 🔍 Practice Preview (for later coding)
```python
# Bitwise AND
a = 12    # binary 1100
b = 10    # binary 1010
print("12 & 10 =", a & b)   # 8 (binary 1000)

# Bitwise OR
print("12 | 10 =", a | b)   # 14 (binary 1110)

# Permission system
READ = 4
WRITE = 2
EXEC = 1

my_perm = READ | EXEC          # 5
print("Has READ?", (my_perm & READ) != 0)
print("Has WRITE?", (my_perm & WRITE) != 0)
print("Has EXEC?", (my_perm & EXEC) != 0)
```

---

## 📌 Key Takeaway
- `&` returns bits that are 1 in **both** operands.
- `|` returns bits that are 1 in **either** operand.
- Used for flags, permissions, and low‑level data packing.
- Decimal numbers are automatically handled in binary by Python.