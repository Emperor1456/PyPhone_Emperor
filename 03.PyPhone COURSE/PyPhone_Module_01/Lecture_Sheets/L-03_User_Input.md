# 📘 PyPhone Emperor · Module 1  
# 📖 L‑03 – User Input

---

## 🎯 OBJECTIVE
Learn to receive data from the user at runtime
using the `input()` function.
Understand that all input arrives as a string,
and how to convert it for further use.
This is the bridge between your program
and the outside world.

---

## 🧱 BRICK 1 – The `input()` Function

`input()` makes your program pause and wait
for the user to type something and press Enter.
The typed value is always returned as a **string**.

```python
variable = input("Prompt message: ")
```

**Example:**
```python
name = input("What is your name? ")
print("Hello, " + name + "!")
```

If the user types `Emperor`, then `name` holds
the string `"Emperor"`.

### Important points
- The prompt is optional: `input()` works without it.
- The prompt goes inside the parentheses, in quotes.
- The cursor waits on the same line after the prompt.
- Everything the user types is captured as **text**.
  Even if they type `42`, you get `"42"` (a string).

> 💡 **INSIGHT:** `input()` is the simplest way to make a program interactive. Every real application uses some form of input.

---

## 🧱 BRICK 2 – Converting Input to Numbers

Since `input()` always returns a string,
you must **typecast** it to do any maths.

**Two‑step approach (safe):**
```python
① raw = input("Enter your age: ")   # string
② age = int(raw)                    # integer
③ next_year = age + 1
④ print("Next year you will be", next_year)
```

**One‑liner (shortcut):**
```python
age = int(input("Enter your age: "))
```

### Handling decimal input
```python
height = float(input("Height in metres: "))
```

> ⚠️ **WARNING:** If the user types something that cannot be converted (`"hello"` for `int`), the program will crash with a `ValueError`. We will learn error handling in Module 6. For now, assume correct input.

---

## 💡 Real‑world Pattern
In enterprise software, user input is often
validated and cleaned before processing.

```python
# Simple order system
product  = input("Product name: ")
quantity = int(input("Quantity: "))
price    = float(input("Unit price: "))
total    = quantity * price
print("Total cost:", total)
```

Here, `product` stays a string, but the numbers
are converted so arithmetic works.

---

## 🔍 Practice Preview (for later coding)
```python
# Collect three pieces of information
name = input("Your name: ")
age  = int(input("Your age: "))
city = input("Your city: ")

# Print a summary
print("Name:", name)
print("Age next year:", age + 1)
print("City:", city)

# Try entering a float for age and see what happens
```

---

## 📌 Key Takeaway
- `input()` always returns a **string**.
- Convert with `int()` or `float()` to do maths.
- The prompt is a string inside the parentheses.
- Without conversion, `age + 1` will crash.