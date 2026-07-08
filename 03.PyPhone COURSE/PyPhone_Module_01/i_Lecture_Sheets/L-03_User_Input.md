# 📘 PyPhone Emperor · Module 1  
# 📖 L‑03 – User Input in Customer Interactions

---

## 🎯 OBJECTIVE
Learn to receive data from the user at runtime
using `input()`, and convert it to numbers
so you can process orders and personalise responses.
This connects your program to the outside world.

---

## 🧱 BRICK 1 – The `input()` Function

`input()` pauses your program and waits for the user
to type something and press Enter.
The result is **always a string**.

```python
variable = input("Prompt message: ")
```

### Greeting a customer

```python
name = input("Enter your name: ")
print("Hello, " + name)
```

If the user types `Emperor`, `name` holds
the string `"Emperor"`, and the program prints a
personalised greeting.

**Key points:**
- The prompt is optional: `input()` works without it.
- The cursor waits on the same line after the prompt.
- Even if the user types `4`, you get `"4"` (a string).

---

## 🧱 BRICK 2 – Converting Input for Calculations

Since `input()` returns a string,
you must **typecast** it to do any maths.

### Reading a single number

```python
age_str = input("Enter your age: ")    # user types 18
age = int(age_str)                     # 18 (int)
print("In 10 years you will be", age + 10)
```

### Reading a decimal value

```python
price_str = input("Enter the price: ")  # user types 9.99
price = float(price_str)                # 9.99 (float)
print("Twice the price:", price * 2)
```

### Reading two numbers on one line

When the user enters two values separated by a space,
you can split them and convert each one.

```python
data = input("Enter two numbers: ")   # user types "5 7"
a_str, b_str = data.split()           # ["5", "7"]
a = int(a_str)
b = int(b_str)
print("Sum:", a + b)                  # 12
```

`.split()` breaks a string into a list at spaces.
You can then convert each piece individually.

> ⚠️ **WARNING:** If the user types something that cannot
> be converted (`"hello"` for `int`), the program will crash.
> We’ll learn error handling in Module 6. For now, assume
> correct input.

---

## 💡 Real‑world Usage
Every interactive system – from ATMs to online shops –
uses `input()` to collect data from the user.
The same pattern appears again and again:

```python
name    = input("Customer name: ")
product = input("Product: ")
qty     = int(input("Quantity: "))
price   = float(input("Unit price: "))
total   = qty * price
print(f"Thank you, {name}! Total: ${total:.2f}")
```

---

## 🔍 Practice Preview
You will interact with a customer order system.

- **Easy:** Ask for a name and print a greeting.
- **Medium:** Ask for an age, convert to `int`, print age in 10 years.
- **Hard:** Read two numbers on one line, split them, convert to ints, and print their sum.

Run the practice coach:
```bash
python ii_Practice_Sheets/L-03_User_Input.py
```

Choose your level, type the script, and the engine will verify.

---

## 📌 Key Takeaway
- `input()` always returns a **string**.
- Convert with `int()` or `float()` to do maths.
- Use `.split()` to read multiple values on one line.
- Without conversion, arithmetic on strings fails.