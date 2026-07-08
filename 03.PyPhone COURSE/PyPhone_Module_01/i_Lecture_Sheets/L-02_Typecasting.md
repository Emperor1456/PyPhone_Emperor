# 📘 PyPhone Emperor · Module 1  
# 📖 L‑02 – Typecasting in Data Pipelines

---

## 🎯 OBJECTIVE
Learn to convert values between types
using `int()`, `float()`, and `str()`.
Typecasting is essential when you read data
that arrives as text and must be processed as numbers.
We’ll apply it to a customer data import.

---

## 🧱 BRICK 1 – Converting Strings to Numbers

Data often arrives as text – from files, APIs, or `input()`.
You must convert it before doing arithmetic.

### `int()` – turn a string into an integer

```python
age_str = "25"          # raw data, always text
age_int = int(age_str)  # 25 (integer)
print(age_int)
```

### `float()` – turn a string into a float

```python
pi_str = "3.14"
pi = float(pi_str)      # 3.14
print(pi)
```

**Rules:**
- `int()` works only on strings that look like whole numbers.
- `int("3.14")` **crashes** – use `float()` first.
- `float()` accepts `"3.14"` or `"42"`.
- Converting a float to an int **truncates** the decimal:
  `int(9.9)` → `9` (not 10).

> ⚠️ **COMMON PITFALL:** `int()` does not round.  
> For rounding, use `round(value)`.

---

## 🧱 BRICK 2 – Converting Between Other Types

### Number → String with `str()`

```python
pi = 3.14
pi_str = str(pi)        # "3.14"
print(pi_str)
```

`str()` works on **anything** – it’s the safest conversion.

### Converting a whole list of strings

Often you have a list of numeric strings that need
to become actual numbers.

```python
vals = ["1", "2", "3"]
nums = [int(v) for v in vals]   # [1, 2, 3]
print(nums)
```

This uses a **list comprehension** (we’ll study later),
but the idea is simple: apply `int()` to every element.

### Dynamic typing in action

A variable can change type – that’s dynamic typing.

```python
x = 1234          # int
x = str(x)        # "1234"
print(type(x))    # <class 'str'>
```

---

## 💡 Real‑world Usage
A typical data pipeline reads a CSV file where every
field is a string. Before you can compute totals or
averages, you cast the columns to `int` or `float`.

```python
raw_age = "18"
raw_price = "9.99"
age = int(raw_age)
price = float(raw_price)
total = price * 2
print(total)       # 19.98
```

---

## 🔍 Practice Preview
You will perform three data conversions.

- **Easy:** Convert the string `"25"` to an integer and print it.
- **Medium:** Convert the float `3.14` to a string and print it.
- **Hard:** Convert the list `["1","2","3"]` into a list of integers and print it.

Run the practice coach:
```bash
python ii_Practice_Sheets/L-02_Typecasting.py
```

Choose your level, type the script, and the engine will verify.

---

## 📌 Key Takeaway
- `int()` converts to integer; `float()` to decimal; `str()` to text.
- `input()` and file data are always strings – convert before math.
- `int()` truncates, never rounds.
- Use list comprehensions to convert a whole collection at once.