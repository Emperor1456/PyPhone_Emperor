# 📘 PyPhone Emperor v3.0 · Module 1
# 📖 L‑05 – User Input, CLI Arguments & sys.argv

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, your programs will talk to the outside world.

- ⌨️ `input()` – interactive user prompts
- 🧹 Sanitizing input – strip, validate, cast
- 📟 Command‑line arguments – `sys.argv`
- 🧰 Building simple CLI tools
- ⚠️ Handling missing or invalid input gracefully

---

## 🧱 USER INPUT WITH `input()`

`input()` pauses your program and waits for the user to type something.
It always returns a **string**.

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

Convert to numbers explicitly:

```python
age_str = input("Enter your age: ")
age = int(age_str.strip())
print(f"Next year you will be {age + 1}.")
```

> ⚠️ **WARNING:** `int("abc")` raises `ValueError`. Always validate before casting.
> We'll handle this formally with `try/except` in Module 6.

---

## 🧱 COMMAND‑LINE ARGUMENTS WITH `sys.argv`

`sys.argv` is a list of words typed after the script name in the terminal.

```python
import sys
print(sys.argv)
```

If you run:
```bash
python script.py Emperor 18
```
`sys.argv[0]` is `"script.py"`.
`sys.argv[1]` is `"Emperor"`.
`sys.argv[2]` is `"18"`.

Check the number of arguments:

```python
if len(sys.argv) < 2:
    print("Usage: python script.py <name>")
else:
    name = sys.argv[1]
    print(f"Hello, {name}!")
```

> 💡 **INSIGHT:** `sys.argv` is how real CLI tools receive input.
> It's faster than `input()` for automation and scripting.

---

## 🧱 BUILDING A SIMPLE CLI TOOL

**Example: Inventory Checker**

```python
import sys

if len(sys.argv) != 3:
    print("Usage: python inventory.py <product> <quantity>")
else:
    product = sys.argv[1]
    qty = int(sys.argv[2])
    threshold = 20
    if qty < threshold:
        print(f"REORDER {product} — only {qty} left!")
    else:
        print(f"{product} stock OK ({qty}).")
```

Run it:
```bash
python inventory.py "Wireless Mouse" 15
# Output: REORDER Wireless Mouse — only 15 left!
```

---

## 💡 Real‑world Usage

**Banking – enter transaction amount**
```python
amount = float(input("Enter amount: ").strip())
print(f"Processing ${amount:.2f}...")
```

**E‑commerce – SKU lookup from CLI**
```python
import sys
sku = sys.argv[1] if len(sys.argv) > 1 else input("SKU: ")
print(f"Looking up {sku}...")
```

**Logistics – shipment weight from command line**
```python
import sys
weight = float(sys.argv[1]) if len(sys.argv) > 1 else 0.0
print(f"Weight: {weight}kg")
```

**HR – employee search tool**
```python
import sys
name = sys.argv[1] if len(sys.argv) > 1 else input("Name: ")
print(f"Searching for {name}...")
```

---

## 🔍 Practice Preview
You will:
- Prompt a user for product details with `input()`.
- Read a stock count from command‑line arguments.
- Build a small CLI inventory checker.
- Handle missing arguments gracefully with a usage message.

Run the coach:
```bash
python ii_Practice_Sheets/L05_User_Input_CLI_Args_sysargv.py
```

---

## 📌 Key Takeaway
- `input()` always returns a string – cast to the type you need.
- `sys.argv` captures command‑line arguments as a list.
- Always check `len(sys.argv)` before accessing indices.
- CLI tools are the backbone of automation and backend scripting.

*For Emperor.*