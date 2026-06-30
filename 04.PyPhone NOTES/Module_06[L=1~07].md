# 📘 PyPhone Emperor · Module 6  
# 🗃️ Comprehensive Note – File Handling & Exceptions

---

## 🎯 Scope
This note covers the complete toolkit for working with files and handling errors gracefully.  
You will learn to read, write, and append files, use the `json` module for data interchange, and build robust error‑handling with `try`, `except`, `else`, and `finally`.  
All code fits a phone screen; no sideways scrolling.

---

## 🧱 1. Opening & Reading Files

### The `with` Statement (Industry Standard)
Opens a file and automatically closes it when the block ends, even if errors occur.

```python
with open("data.txt", "r") as f:
    content = f.read()
```

### Reading Methods
- `f.read()` → whole file as a single string.
- `f.readline()` → next line (including `\n`).
- `f.readlines()` → list of all lines.

```python
with open("data.txt", "r") as f:
    first_line = f.readline()
    all_lines = f.readlines()
```

### Iterating Over Lines (Memory‑Efficient)
```python
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())
```

---

## 🧱 2. Writing to Files

### Mode `'w'` – Overwrite or Create
Erases existing content if the file exists; creates a new file if not.

```python
with open("output.txt", "w") as f:
    f.write("Hello, Emperor!\n")
    f.write("Line 2\n")
```

### Writing Multiple Lines
```python
lines = ["First\n", "Second\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)
```

**Warning:** `'w'` destroys previous content silently. Use it only when you need a fresh file.

---

## 🧱 3. Appending to Files

### Mode `'a'` – Add to the End
New content is written **after** the existing file data. Creates the file if it doesn’t exist.

```python
with open("log.txt", "a") as f:
    f.write("[INFO] New entry\n")
```

### Real‑World Pattern – Logging
```python
from datetime import datetime
ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("app.log", "a") as f:
    f.write(f"[{ts}] User logged in\n")
```

---

## 🧱 4. Working with JSON

JSON is the universal data‑exchange format. Python’s `json` module converts dictionaries ↔ JSON seamlessly.

### Writing Python → JSON File
```python
import json

user = {"name": "Emperor", "age": 18, "active": True}
with open("user.json", "w") as f:
    json.dump(user, f, indent=4)
```

### Reading JSON File → Python
```python
with open("user.json", "r") as f:
    data = json.load(f)
print(data["name"])   # Emperor
```

### Working with JSON Strings (Not Files)
- `json.dumps(obj)` → returns a JSON string.
- `json.loads(string)` → parses JSON string into a dict.

```python
json_str = '{"name":"Emperor"}'
user = json.loads(json_str)
```

---

## 🧱 5. Introduction to Exceptions

### Basic `try`/`except`
Place risky code inside `try`. If an error occurs, the matching `except` block runs.

```python
try:
    num = int(input("Number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("That's not a valid number.")
```

### Catching the Error Object
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
```

**Never use a bare `except:`** – it catches even system‑exit signals and hides bugs.

---

## 🧱 6. Handling Multiple Exceptions

You can have several `except` blocks, each for a different error type.  
Python checks them **top to bottom**; the first match wins.

```python
try:
    data = {"name": "Emperor"}
    print(data["age"])
except KeyError:
    print("Key missing.")
except Exception:
    print("Something else went wrong.")
```

### Catching Multiple Errors Together
Group exceptions in a tuple if they share the same handler.

```python
try:
    risky_op()
except (ValueError, TypeError) as e:
    print(f"Invalid input: {e}")
```

**Order matters:** More specific exceptions must come **before** generic ones.

---

## 🧱 7. `else` and `finally`

### `else` – Runs Only on Success
The `else` block executes **only if no exception occurred** in the `try` block.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero.")
else:
    print(f"Result is {result}")
```

### `finally` – Always Runs
The `finally` block runs **no matter what** – even if an exception was raised or a `return` was used.

```python
f = None
try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File missing.")
finally:
    if f:
        f.close()
    print("Cleanup complete.")
```

**Best practice:** Use `finally` for cleanup (closing files, releasing locks). Never `return` inside `finally` – it can swallow exceptions.

---

## 💡 Quick Reference
```python
# Reading
with open("f.txt","r") as f:
    text = f.read()

# Writing (overwrite)
with open("f.txt","w") as f:
    f.write("data\n")

# Appending
with open("f.txt","a") as f:
    f.write("more data\n")

# JSON
import json
data = {"key":"val"}
json.dump(data, open("f.json","w"))
loaded = json.load(open("f.json"))

# Exception basic
try:
    risky()
except ValueError:
    print("Wrong value")
except:
    print("Other error")
else:
    print("Success")
finally:
    print("Always runs")
```

---

## 📌 Key Takeaway
- Use `with open(...)` for all file operations – it guarantees proper closure.
- `'r'` for reading, `'w'` for writing (overwrites), `'a'` for appending.
- `json.dump()` and `json.load()` are your bridges to structured data.
- Catch specific exceptions; avoid bare `except:`.
- `else` lets you separate success‑only logic; `finally` is for mandatory cleanup.
- Short `try` blocks and precise `except` clauses create maintainable, professional code.

*Study this sheet. Recall it from memory. Then practice.*