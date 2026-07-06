# 📘 PyPhone Emperor · Module 1  
# 📖 L‑01 – Variables & Data Types

---

## 🎯 OBJECTIVE
Learn to store data in memory using variables,
and recognise the three fundamental data types
in Python: **string**, **integer**, and **float**.
This is the first building block of every program.

---

## 🧱 BRICK 1 – What Is a Variable?

A variable is a labelled box in memory.
You assign it with the equals sign:

```python
variable_name = value
```

**Example:**
```python
name = "Emperor"
age  = 18
```

Now `name` holds the text `"Emperor"`,
and `age` holds the integer `18`.

### Rules for naming variables
- Must start with a letter (a–z, A–Z) or underscore `_`
- Cannot start with a digit
- Can contain letters, digits, underscores
- Case‑sensitive: `age`, `Age`, `AGE` are three different variables
- No spaces, no special characters (like `@`, `$`)
- Must not be a Python keyword (`if`, `for`, `class`, etc.)

**Valid:** `total_price`, `user2`, `_count`  
**Invalid:** `2day`, `total-price`, `user name`

> 💡 **NOTE:** A variable name should be descriptive — `customer_name` not `cn`.

---

## 🧱 BRICK 2 – Three Core Data Types

Python automatically sets the type when you assign a value.

| Type  | Description                     | Examples         |
|-------|---------------------------------|------------------|
| `str` | text, inside `" "` or `' '`     | `"hello"`, `'A'` |
| `int` | whole number, positive/negative | `42`, `-7`, `0`  |
| `float`| number with a decimal point     | `3.14`, `-0.5`   |

### Checking types with `type()`

```python
>>> type("hello")
<class 'str'>
>>> type(100)
<class 'int'>
>>> type(99.9)
<class 'float'>
```

### Mixing types in operations
- `int * float` → `float` (e.g., `5 * 2.0` = `10.0`)
- `int + int` → `int`
- `str + int` → **TypeError** (must convert first)

> ⚠️ **WARNING:** Python is **dynamically typed** — a variable can change type later. Always know your current type.

---

## 🔍 Practice Preview (for later coding)
```python
product  = "Laptop"
quantity = 5
price    = 799.99

print(type(product))
print(type(quantity))
print(type(price))
# What do you think this prints?
print(type(quantity * price))
```

---

## 📌 Key Takeaway
- A variable stores a value with a name.
- The three core types are `str`, `int`, `float`.
- Use `type()` to inspect any value.
- Python sets the type for you, but you must stay aware of it.