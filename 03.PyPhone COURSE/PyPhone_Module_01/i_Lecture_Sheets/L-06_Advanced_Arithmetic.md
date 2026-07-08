# 📘 PyPhone Emperor · Module 1  
# 📖 L‑06 – Advanced Arithmetic in Reports

---

## 🎯 OBJECTIVE
Learn the three advanced arithmetic operators
that go beyond `+`, `-`, `*`, `/`.
These are essential for calculating pages,
checking remainders, and computing powers
in business reports and data analysis.

---

## 🧱 BRICK 1 – Floor Division and Modulus

### Floor Division `//`
Divides and **chops off** the decimal part,
always rounding down. This is useful when you need
a whole‑number result.

```python
full_pages = 31 // 4   # 7  (4×7=28, remainder 3)
```

### Modulus `%`
Returns the **remainder** after division.
Often used to check if something is exactly divisible.

```python
leftover = 31 % 4      # 3   (because 31 = 7×4 + 3)
```

### A real‑world example: pagination
```python
total_lines = 31
lines_per_page = 4
pages      = total_lines // lines_per_page   # 7
extra      = total_lines % lines_per_page    # 3
print(pages)
print(extra)
```

> 💡 `% 2` is the classic way to test if a number is even or odd.

---

## 🧱 BRICK 2 – Exponentiation `**`

Raises a number to a power.

```python
size = 2 ** 10   # 1024
print(size)
```

### Why it matters
- Models compound growth or memory sizes.
- `number ** 0.5` gives the square root.
- Operator precedence: `**` is right‑associative.
  `2 ** 3 ** 2` means `2 ** (3 ** 2) = 512`.

### A business example: doubling a value
```python
start = 1
days = 10
final = start * (2 ** days)   # 1024
print(final)
```

> ⚠️ **COMMON PITFALL:** `**` is right‑associative.  
> Use parentheses if you need left‑to‑right grouping.

---

## 💡 Real‑world Usage
Every analytics report uses floor division and modulus.
For example, splitting a dataset into chunks,
distributing items evenly, or calculating compound
interest all rely on these operators.

```python
# Total items and batch size
total_items = 31
batch_size = 4
full_batches = total_items // batch_size   # 7
remaining   = total_items % batch_size    # 3
print("Full batches:", full_batches)
print("Leftover:", remaining)
```

---

## 🔍 Practice Preview
You will compute three values for an analytics report.

- Floor division: `31 // 4`
- Remainder: `31 % 4`
- Exponentiation: `2 ** 10`

Run the practice coach:
```bash
python ii_Practice_Sheets/L-06_Advanced_Arithmetic.py
```

Choose your level, type the script, and the engine will verify.

---

## 📌 Key Takeaway
- `//` gives the whole‑number result of division.
- `%` gives the remainder after division.
- `**` raises a number to a power; use `** 0.5` for square root.
- Use them together to solve real problems like pagination or growth calculations.