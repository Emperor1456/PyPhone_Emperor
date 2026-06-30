# 📘 PyPhone Emperor · Module 1  
# 🗃️ Comprehensive Note – Python Fundamentals

---

## 🎯 Scope
This note covers every essential concept from Module 1.  
It is designed as a single‑page reference for revision and practice.  
Every keyword, operator, and built‑in function you need is here.

---

## 🧱 1. Variables & Data Types
A **variable** is a named container for a value.  
Python is dynamically typed — you don’t declare the type.

```python
name = "Emperor"        # str
age = 18                # int
pi = 3.14               # float
```

- `type(x)` returns the type of `x`.
- Common types: `str`, `int`, `float`, `bool`, `list`, `dict`, etc.

---

## ⌨️ 2. User Input
`input("Prompt")` reads a line from the user as a **string**.

```python
name = input("Your name? ")
```

- Always cast to the desired type before doing maths.

---

## 🔁 3. Typecasting
Convert between types using:

| Function  | Purpose               |
|-----------|-----------------------|
| `int(x)`  | to integer            |
| `float(x)`| to floating‑point     |
| `str(x)`  | to string             |

```python
num = int("42")         # 42
pi = float("3.14")      # 3.14
msg = str(100)          # "100"
```

---

## ⚡ 4. Operators – Arithmetic
| Operator | Meaning            | Example       |
|----------|--------------------|---------------|
| `+`      | addition           | `3 + 2 → 5`   |
| `-`      | subtraction        | `3 - 2 → 1`   |
| `*`      | multiplication     | `3 * 2 → 6`   |
| `/`      | division (float)   | `3 / 2 → 1.5` |
| `//`     | floor division     | `3 // 2 → 1`  |
| `%`      | modulus (remainder)| `3 % 2 → 1`   |
| `**`     | exponentiation     | `2 ** 3 → 8`  |

---

## 🔍 5. Operators – Comparison
Return `True` or `False`.

| Operator | Meaning                  |
|----------|--------------------------|
| `==`     | equal                    |
| `!=`     | not equal                |
| `>`      | greater than             |
| `<`      | less than                |
| `>=`     | greater than or equal to |
| `<=`     | less than or equal to    |

---

## 🧠 6. Operators – Logical
Combine conditions.

| Operator | Description                                |
|----------|--------------------------------------------|
| `and`    | True if **both** conditions are True        |
| `or`     | True if **at least one** condition is True  |
| `not`    | Reverses the boolean value                 |

```python
(age >= 18) and (has_license)   # both must be True
```

---

## 📝 7. Operators – Assignment
Shorthand to update a variable.

| Operator | Equivalent  |
|----------|-------------|
| `=`      | assign      |
| `+=`     | `x = x + a` |
| `-=`     | `x = x - a` |
| `*=`     | `x = x * a` |
| `/=`     | `x = x / a` |
| `//=`    | `x = x // a`|
| `%=`     | `x = x % a` |
| `**=`    | `x = x ** a`|

---

## 🧮 8. Operators – Bitwise
Operate on bits of integers.

| Op  | Meaning        | Example (5 & 3) |
|-----|----------------|-----------------|
| `&` | AND            | `5 & 3 → 1`     |
| `\|`| OR             | `5 \| 3 → 7`    |
| `^` | XOR            | `5 ^ 3 → 6`     |
| `~` | NOT (invert)   | `~5 → -6`       |
| `<<`| left shift     | `5 << 1 → 10`   |
| `>>`| right shift    | `5 >> 1 → 2`    |

---

## ✨ 9. Escape Sequences
Special characters inside strings.

| Sequence | Meaning             |
|----------|---------------------|
| `\n`     | new line            |
| `\t`     | tab                 |
| `\\`     | backslash           |
| `\"`     | double quote        |
| `\'`     | single quote        |

```python
print("Hello\nWorld")   # prints two lines
```

---

## 💡 Quick Reference
```python
# Variables & Casting
x = 10
y = float(x)
name = input("Name: ")
age = int(input("Age: "))

# Arithmetic
div = 17 // 5          # 3
rem = 17 % 5           # 2
pwr = 2 ** 5           # 32

# Comparison & Logic
check = (10 > 5) and (10 < 20)   # True
toggle = not True                # False

# Compound assignment
total = 0
total += 5            # total = 5
total *= 2            # total = 10

# Bitwise
flags = 0b1010
mask  = 0b0100
result = flags & mask  # bitwise AND

# Escape
path = "C:\\Users\\Emperor"
quote = "He said, \"Hello\""
```

---

## 📌 Key Takeaway
- Python is dynamically typed; use `type()` to inspect.
- `input()` always returns a string – cast before maths.
- Operators exist for arithmetic, comparison, logic, assignment, and bitwise manipulation.
- Escape sequences let you include special characters in strings.
- Master these fundamentals — they are the bedrock of everything that follows.

*Study this sheet. Recall it from memory. Then practice.*