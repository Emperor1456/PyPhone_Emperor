# 📘 PyPhone Emperor · Module 1  
# 📖 L‑12 – Bitwise XOR (`^`) and NOT (`~`)

---

## 🎯 OBJECTIVE
Complete your bitwise operator toolkit
with XOR (`^`) and NOT (`~`).
These operators unlock bit‑toggling,
encryption basics, and bit‑flipping.

---

## 🧱 BRICK 1 – Bitwise XOR `^`

XOR means **exclusive OR**.
Result bit is **1 only if the two bits are different**.
If both bits are the same, result is 0.

### Truth table per bit
```
0 ^ 0  =  0
0 ^ 1  =  1
1 ^ 0  =  1
1 ^ 1  =  0
```

### Example with binary diagram
```
  12  =  1 1 0 0
^ 10  =  1 0 1 0
───────────────
   6  =  0 1 1 0
```
```python
print(12 ^ 10)   # 6
```

### Key property: toggling
XOR with 1 flips a bit.  
XOR with 0 leaves it unchanged.  
XOR with itself gives 0.

```python
x = 42
print(x ^ x)     # 0  (anything XOR itself = 0)
print(x ^ 0)     # 42 (XOR with 0 = unchanged)
```

> 💡 **INSIGHT:** XOR is reversible: `(A ^ B) ^ B = A`. This is the basis of many simple ciphers.

---

## 🧱 BRICK 2 – Bitwise NOT `~`

The NOT operator flips **every bit**:
0 becomes 1, 1 becomes 0.
In Python, `~` returns the **two's complement**,
which is `-x - 1`.

```python
print(~5)    # -6
print(~0)    # -1
print(~-1)   # 0
```

### Why `~5 = -6`?
Python uses signed integers with infinite bits
in theory. Flipping all bits of `5` (binary `...0101`)
gives `...1010`, which is the two's complement
representation of `-6`.

### Practical shortcut
```
~x  =  -x - 1
```
```python
# Check the formula
x = 10
print(~x)          # -11
print(-x - 1)      # -11 (matches)
```

> ⚠️ **WARNING:** Bitwise NOT in Python behaves differently than in languages with fixed‑width integers. Always remember `~x = -x - 1`.

---

## 💡 Real‑world Usage

### Toggle a flag with XOR
```python
flag = 0b1010       # binary: 1010
mask = 0b0100       # bit to toggle (3rd bit)
flag ^= mask        # now flag = 0b1110
flag ^= mask        # toggle again → 0b1010 (back to original)
```

### Simple encryption (XOR cipher)
```python
message = 65        # ASCII 'A'
key = 42
encrypted = message ^ key
decrypted = encrypted ^ key
print(decrypted)    # 65 (original message)
```

---

## 🔍 Practice Preview (for later coding)
```python
a = 12    # 1100
b = 10    # 1010

# XOR
print("12 ^ 10 =", a ^ b)    # 6  (0110)
print("12 ^ 12 =", a ^ a)    # 0
print("12 ^ 0  =", a ^ 0)    # 12

# NOT
print("~5  =", ~5)            # -6
print("~0  =", ~0)            # -1
print("~-1 =", ~-1)           # 0

# Toggling a flag
flag = 0b1010     # binary
mask = 0b0001     # toggle last bit
print("Original:", bin(flag))
flag ^= mask
print("Toggled :", bin(flag))
flag ^= mask
print("Back    :", bin(flag))
```

---

## 📌 Key Takeaway
- `^` sets bits to 1 where inputs **differ**.
- `~` flips all bits; in Python, `~x = -x - 1`.
- XOR with 1 toggles; XOR with self gives 0.
- XOR is the core of many encryption schemes.