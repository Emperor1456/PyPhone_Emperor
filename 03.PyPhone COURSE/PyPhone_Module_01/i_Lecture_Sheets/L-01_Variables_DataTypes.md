# 📘 PyPhone Emperor · Module 1  
# 📖 L‑01 – Variables & Data Types in Inventory

---

## 🎯 OBJECTIVE
Learn to store business data in variables,
recognise the three fundamental data types,
and output a simple product label.
This is the first brick of every business program.

---

## 🧱 BRICK 1 – What Is a Variable?

A variable is a **named box in memory**.
You assign it with the equals sign:

```python
variable_name = value
```

**Inventory example – three core types:**

```python
product_name = "Wireless Mouse"   # text (str)
unit_price   = 24.99              # decimal (float)
stock        = 150                # whole number (int)
```

Now `product_name` holds the text,
`unit_price` holds the decimal,
and `stock` holds the integer.

### Naming rules (enforced by Python)
- Must start with a letter (a–z, A–Z) or underscore `_`
- Cannot start with a digit
- Can contain letters, digits, underscores
- Case‑sensitive: `Stock`, `stock`, `STOCK` are three different variables
- No spaces, no hyphens, no special characters
- Must not be a Python keyword (`if`, `for`, `class`, etc.)

**Valid:** `unit_price`, `item2`, `_qty`  
**Invalid:** `2day`, `total-price`, `user name`

> 💡 Use **snake_case** – lowercase words joined by underscores.  
> `product_name` is professional; `pn` is not.

---

## 🧱 BRICK 2 – Three Core Data Types

Python sets the type automatically when you assign a value.

| Type    | Meaning               | Inventory example          |
|---------|-----------------------|----------------------------|
| `str`   | text                  | `"Wireless Mouse"`         |
| `int`   | whole number          | `150` (stock count)        |
| `float` | number with decimals  | `24.99` (price in dollars) |

### Printing values – the `print()` function
To output the product details, use `print()`.

```python
product_name = "Wireless Mouse"
unit_price   = 24.99
stock        = 150

print(product_name)    # Wireless Mouse
print(unit_price)      # 24.99
print(stock)           # 150
```

### Dynamic typing (Preview)
A variable can change type later – that’s dynamic typing.

```python
x = 1234          # int
x = "1234"        # now a str
print(type(x))    # <class 'str'>
```

> ⚠️ **WARNING:** Python’s dynamic typing is powerful but
> can hide bugs. Always know the current type of a variable.

---

## 💡 Real‑world Usage
Every inventory system, from a corner shop to a
warehouse, starts with variables that describe the
products. The same `product_name`, `price`, `stock`
pattern runs on servers, in spreadsheets, and in
your phone’s apps.

---

## 🔍 Practice Preview
You are an inventory clerk. Create three variables:

- `product_name = 'Wireless Mouse'`
- `unit_price = 24.99`
- `stock = 150`

Then print them on separate lines.

In Termux, run the practice coach:
```bash
python ii_Practice_Sheets/L-01_Variables_Data_Types.py
```

Choose **Easy** and type exactly those lines.  
The engine will verify your output instantly.

---

## 📌 Key Takeaway
- A variable is a named box for a value.
- The three core types are `str` (text), `int` (whole number), `float` (decimal).
- Use `print()` to display any variable.
- Python sets the type for you, but you must stay aware of it.
- Professional code uses descriptive, snake_case names.