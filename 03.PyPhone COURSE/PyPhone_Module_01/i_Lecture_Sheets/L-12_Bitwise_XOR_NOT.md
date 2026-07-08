# 📘 PyPhone Emperor · Module 1  
# 📖 L‑12 – Bitwise XOR & NOT in Permission and Encryption

---

## 🎯 OBJECTIVE
Complete your bitwise operator toolkit
with XOR (`^`) and NOT (`~`).
These operators unlock bit‑toggling,
permission removal, and simple encryption
techniques that appear in real systems.

---

## 🧱 BRICK 1 – Bitwise XOR (`^`)

XOR means **exclusive OR**.
A result bit is `1` **only if the two bits differ**.
If both bits are the same, the result bit is `0`.

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

### Key property: toggling bits
XOR with `1` flips a bit; XOR with `0` leaves it unchanged.

```python
print(5 ^ 3)    # 6  (101 ^ 011 = 110)
```

### Business example – toggling a permission flag

Imagine each bit represents a user permission.
You can **toggle** a specific permission (turn it on or off)
with XOR and a mask.

```python
READ  = 0b100   # 4
WRITE = 0b010   # 2
EXEC  = 0b001   # 1

user_perms = READ | WRITE   # 0b110 → 6 (Read+Write)

# Toggle WRITE permission
mask = WRITE
user_perms ^= mask          # 6 ^ 2 = 4 → only Read
user_perms ^= mask          # 4 ^ 2 = 6 → back to Read+Write
print(user_perms)
```

> 💡 **INSIGHT:** XOR is reversible:
> `(A ^ B) ^ B` always returns `A`.
> This property is used in simple ciphers and hash mixing.

---

## 🧱 BRICK 2 – Bitwise NOT (`~`)

The NOT operator flips **every bit** of the integer:
`0` becomes `1`, `1` becomes `0`.
In Python, `~` returns the two’s complement,
which equals `-x - 1`.

```python
print(~5)    # -6   (because -5 - 1 = -6)
print(~0)    # -1
print(~-1)   # 0
```

### Why `~5 = -6`?

Python uses signed integers with (theoretically)
infinite bits. Flipping all bits of `5` (binary `...0101`)
produces `...1010`, which is the two’s complement
representation of `-6`.

### Practical shortcut

```python
x = 10
print(~x)          # -11
print(-x - 1)      # -11 (matches)
```

### Business example – clearing a permission bit

You can use `~` with `&` to **clear** a specific bit
(remove a permission) while leaving others unchanged.

```python
READ  = 0b100   # 4
WRITE = 0b010   # 2

user_perms = READ | WRITE   # 0b110 → 6 (Read+Write)

# Clear WRITE permission
user_perms &= ~WRITE        # 6 & ~2 = 6 & -3 = 4 (only Read)
print(user_perms)
```

> ⚠️ **WARNING:** Bitwise NOT in Python behaves
> differently than in languages with fixed‑width
> integers. Always remember `~x = -x - 1`.

---

## 💡 Real‑world Usage

### Toggle a flag with XOR
```python
flag = 0b1010       # binary: 1010
mask = 0b0100       # bit to toggle (3rd bit)
flag ^= mask        # now flag = 0b1110
flag ^= mask        # toggle again → 0b1010 (original)
```

### Simple encryption (XOR cipher)
```python
message = 65        # ASCII 'A'
key = 42
encrypted = message ^ key
decrypted = encrypted ^ key
print(decrypted)    # 65 (original message)
```

### Clearing bits in a hardware register
```python
status = 0b1111    # all bits set
# turn off bit 2 (value 4)
status &= ~0b0100  # now 0b1011
print(bin(status))
```

---

## 🔍 Practice Preview
You will compute four bitwise expressions.

- **Easy:** Print the result of `5 ^ 3`.
- **Medium:** Print the result of `~5`.
- **Hard:** Print the result of `4 ^ 5` on the first line,
  and `~3` on the second line.

Run the practice coach:
```bash
python ii_Practice_Sheets/L-12_Bitwise_XOR_NOT.py
```

Choose your level, type the script, and the engine will verify.

---

## 📌 Key Takeaway
- `^` sets bits to `1` where inputs **differ**.
- `~` flips all bits; in Python, `~x = -x - 1`.
- XOR with 1 toggles; XOR with self gives 0.
- NOT, combined with AND, clears specific bits.
- Both operators are used in permission systems, encryption, and low‑level programming.