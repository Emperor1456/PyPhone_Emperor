# 📘 PyPhone Emperor · Module 1  
# 📖 L‑02 – Typecasting

---

## 🎯 OBJECTIVE
Learn to convert values from one data type to another
using the built‑in functions `int()`, `float()`, and `str()`.
Typecasting is essential when reading user input
or combining numbers with strings.

---

## 🧱 BRICK 1 – Converting to Integer and Float

`int(value)`   → turns a value into an integer  
`float(value)` → turns a value into a float  

**Examples:**
```python
a = "42"         # a is a string
b = int(a)       # b is 42 (int)
c = float(a)     # c is 42.0 (float)
d = int(9.9)     # d is 9 (decimal part is cut off, not rounded)
e = float(7)     # e is 7.0
```

### Rules to remember
- `int()` works on strings that look like whole numbers, e.g. `"42"`.
- `int("3.14")` **will crash** → cannot convert a float‑looking string directly to int.
- `float()` works on strings like `"3.14"` or `"42"`.
- When you convert a float to an int, the decimal part is **truncated**, not rounded.

> ⚠️ **COMMON PITFALL:** `int("3.14")` raises `ValueError`. Always convert to `float` first if the string may contain a decimal point.

---

## 🧱 BRICK 2 – Converting to String

`str(value)` → turns any value into its string representation  

**Why use it?**  
You cannot join a string and a number with `+`.
The number must be converted to a string first.

```python
age = 18
msg = "I am " + str(age) + " years old."
print(msg)   # I am 18 years old.
```

Without `str(age)`, Python would throw a `TypeError`.

### Converting other types to string
```python
print(str(3.14))    # "3.14"
print(str(True))    # "True"
```

> 💡 **INSIGHT:** `str()` is the safest conversion — everything in Python can be turned into a string.

---

## 💡 Typecasting and User Input (important!)
When you use `input()`, everything you get back is a **string**,
even if the user types a number.

```python
raw_age = input("Your age: ")    # raw_age is "18"
age = int(raw_age)               # age is 18 (int)
next_year = age + 1              # 19
```

If you forget to cast, `age + 1` would cause a TypeError.

---

## 🔍 Practice Preview (for later coding)
```python
raw_age   = input("Your age: ")
age_int   = int(raw_age)
age_float = float(raw_age)

print("Integer:", age_int)
print("Float  :", age_float)
print("Next birthday:", age_int + 1)

# What happens if the user types "17.5"?
# Uncomment the next line and test it:
# age_int = int(raw_age)   # will it crash?
```

---

## 📌 Key Takeaway
- Use `int()`, `float()`, and `str()` to switch types.
- `input()` always returns a string – cast it before doing maths.
- `int()` truncates a float (no rounding).
- Always know the type you are working with.