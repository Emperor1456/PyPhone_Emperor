# 📘 PyPhone Emperor · Module 1  
# 📖 L‑11 – Bitwise AND & OR in Permission Systems

---

## 🎯 OBJECTIVE
Learn the bitwise operators `&` (AND) and `|` (OR).
These operators work directly on the binary
representation of integers, treating each bit
as a separate flag.
They are essential for permission systems,
low‑level data processing, and hardware control,
but also appear in everyday programming puzzles
and optimisations.

---

## 🧱 BRICK 1 – Bitwise AND (`&`)

The `&` operator compares two integers bit by bit.
A bit in the result is `1` only if **both** corresponding
bits are `1`.

```python
a = 5   # binary: 101
b = 3   # binary: 011
c = a & b   # binary: 001 → decimal 1
print(c)
```

**How it works, bit by bit:**

| bit of a | bit of b | result |
|----------|----------|--------|
| 1        | 0        | 0      |
| 0        | 1        | 0      |
| 1        | 1        | 1      |

So `5 & 3` equals `1`.

### Real‑world analogy – permission check

Imagine a user has a set of permissions stored as bits:
- Read = 4 (binary 100)
- Write = 2 (binary 010)
- Execute = 1 (binary 001)

To check if a user has **Read** permission, you `&` their
permissions with the Read flag. If the result is non‑zero,
they have it.

```python
READ = 4
user_permissions = 6   # 110 → Read + Write
has_read = user_permissions & READ   # 6 & 4 = 4 (non‑zero → True)
print(has_read)
```

> 💡 `&` is perfect for testing if a specific flag is set
> inside a packed integer.

---

## 🧱 BRICK 2 – Bitwise OR (`|`)

The `|` operator sets a bit in the result to `1` if
**at least one** of the corresponding bits is `1`.

```python
a = 5   # binary: 101
b = 3   # binary: 011
c = a | b   # binary: 111 → decimal 7
print(c)
```

**How it works, bit by bit:**

| bit of a | bit of b | result |
|----------|----------|--------|
| 1        | 0        | 1      |
| 0        | 1        | 1      |
| 1        | 1        | 1      |

So `5 | 3` equals `7`.

### Real‑world analogy – combining permissions

To **grant** a new permission to a user, you `|` their
current permissions with the new flag.

```python
READ = 4
WRITE = 2
user_permissions = 0
user_permissions = user_permissions | READ    # 4
user_permissions = user_permissions | WRITE   # 4 | 2 = 6
print(user_permissions)   # 6 (Read + Write)
```

> 💡 `|` is used to merge several flag values into one.

---

## 💡 Real‑world Usage

Bitwise operations are not just academic – they appear
in real systems every day.

- **Linux file permissions:** `chmod 755` uses octal
  numbers where each digit is a 3‑bit permission set.
- **Network masks:** subnet masks use bitwise AND to
  determine network addresses.
- **Hardware registers:** microcontrollers use bitwise
  operations to turn on/off specific device features.
- **Game development:** storing multiple player states
  in a single integer saves memory and processing.

Even if you never write low‑level code, understanding
`&` and `|` deepens your grasp of how computers actually
represent and manipulate data.

---

## 🔍 Practice Preview
You will compute two bitwise operations.

- **Easy:** Print the result of `5 & 3`.
- **Medium:** Print the result of `5 | 3`.
- **Hard:** Print the result of `6 & 3` on the first line,
  and `6 | 3` on the second line.

Run the practice coach:
```bash
python ii_Practice_Sheets/L-11_Bitwise_AND_OR.py
```

Choose your level, type the script, and the engine will verify.

---

## 📌 Key Takeaway
- `&` (AND) keeps bits only where both are `1`.
- `|` (OR) sets bits where either is `1`.
- They are the building blocks of permission systems,
  flags, and low‑level data packing.
- Each operator works directly on the binary form of integers.