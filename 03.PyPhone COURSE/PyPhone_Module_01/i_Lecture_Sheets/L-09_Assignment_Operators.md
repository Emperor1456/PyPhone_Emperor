# 📘 PyPhone Emperor · Module 1  
# 📖 L‑09 – Assignment Operators in Data Updates

---

## 🎯 OBJECTIVE
Learn to use Python’s assignment operators
to store and modify values efficiently.
Beyond the basic `=` sign, compound assignment
operators combine arithmetic with assignment,
allowing you to write cleaner, more concise
code for updating business variables like
stock levels, salaries, and account balances.

---

## 🧱 BRICK 1 – The Basic Assignment Operator `=`

The equals sign `=` assigns the value on its right
to the variable on its left.
It is not a mathematical equality statement;
it is an instruction to **store**.

```python
x = 10          # x now holds 10
name = "Emperor"   # name now holds "Emperor"
```

You can reassign a variable to a different value,
even of a different type, at any time.

```python
x = 10
x = x + 5       # x becomes 15 (old value + 5)
```

> 💡 **NOTE:** In Python, `=` is assignment; `==` is equality check.
> Never confuse them.

---

## 🧱 BRICK 2 – Compound Assignment Operators

Compound operators perform an arithmetic operation
**and** assign the result back to the same variable.
They make your code shorter and more readable.

| Operator | Equivalent to      | Example    | Result |
|----------|--------------------|------------|--------|
| `+=`     | `x = x + value`    | `x += 5`   | adds 5 |
| `-=`     | `x = x - value`    | `x -= 3`   | subtracts 3 |
| `*=`     | `x = x * value`    | `x *= 2`   | doubles x |
| `/=`     | `x = x / value`    | `x /= 2`   | halves x (float) |
| `//=`    | `x = x // value`   | `x //= 3`  | floor‑divides x |
| `%=`     | `x = x % value`    | `x %= 2`   | remainder of x÷2 |
| `**=`    | `x = x ** value`   | `x **= 2`  | squares x |

### Updating business variables

**Example – adjusting stock after a sale:**
```python
stock = 150
sold = 4
stock -= sold      # stock = stock - sold → 146
print(stock)
```

**Example – applying a percentage increase:**
```python
salary = 50000
raise_pct = 0.10
salary *= (1 + raise_pct)   # salary = 55000.0
print(salary)
```

**Example – scaling a value:**
```python
points = 3
points **= 2      # points = 9
print(points)
```

**Example – integer division update:**
```python
y = 9
y //= 3          # y = 3
print(y)
```

**Example – modulus update:**
```python
a = 5
a %= 2           # a = 1 (remainder of 5÷2)
print(a)
```

These are the very patterns used in payroll
calculations, inventory management, and
game scoring systems.

---

## 💡 Real‑world Usage
Compound assignment operators are everywhere
in real software because they reduce repetition
and make the intention clear at a glance.

```python
# Inventory restock
current_stock = 20
delivery = 50
current_stock += delivery   # now 70

# Discount application
price = 100
discount = 0.15
price *= (1 - discount)    # now 85.0

# Depreciation calculation
value = 10000
depreciation_rate = 0.10
value *= (1 - depreciation_rate)   # 9000.0
```

---

## 🔍 Practice Preview
You will update variables using compound operators.

- **Easy:** Start with `x = 10`, then add 5 using `+=` and print `x`.
- **Medium:** Start with `y = 9`, use `//=` to divide by 3 and print.
  Then set `z = 3`, use `**=` to square it and print.
- **Hard:** Start with `a = 5`, use `%=` to get remainder by 2 and print.
  Then set `b = 5`, use `//=` to divide by 2 and print.

Run the practice coach:
```bash
python ii_Practice_Sheets/L-09_Assignment_Operators.py
```

Choose your level, type the script, and the engine will verify.

---

## 📌 Key Takeaway
- `=` assigns a value; compound operators (`+=`, `-=`, `*=`, etc.) update it.
- They make code shorter and more readable.
- The operator works on the current value of the variable.
- Always ensure the variable is defined before using a compound assignment.