# 📘 PyPhone Emperor · Module 8  
# 🗃️ Comprehensive Note – Advanced Python

---

## 🎯 Scope
This note covers the advanced tools from Module 8: comprehensions (list, dict, set), generator expressions and `yield`, basic decorators, error‑handling best practices, working with CSV files, virtual environments in Termux, and automated testing with `assert` and `unittest`.  
All code fits a phone screen; no sideways scrolling.

---

## 🧱 1. Advanced Comprehensions
Comprehensions create collections in a single, readable line.

### List Comprehension
```python
[expr for item in iterable if condition]
```

**Examples:**
```python
squares = [x**2 for x in range(10)]          # 0,1,4,…,81
evens = [x for x in range(20) if x%2==0]    # 0,2,4,…,18
labels = ["even" if x%2==0 else "odd" for x in range(1,6)]
# ['odd','even','odd','even','odd']
```

### Dictionary Comprehension
```python
{key: value for item in iterable if condition}
```

```python
square_map = {x: x**2 for x in range(5)}     # {0:0,1:1,2:4,…}
filtered = {k:v for k,v in d.items() if v>10}
```

### Set Comprehension
```python
{expr for item in iterable if condition}
```

```python
unique_lengths = {len(w) for w in ["a","ab","abc","a"]}  # {1,2,3}
```

---

## 🧱 2. Generator Expressions & `yield`

### Generator Expression – Lazy Evaluation
Uses `()` instead of `[]`. Produces items one at a time, saving memory.

```python
gen = (x**2 for x in range(10))
next(gen)   # 0
next(gen)   # 1
list(gen)   # consume the rest
```

Ideal for large data or infinite sequences.

### `yield` – Generator Function
A function with `yield` returns a generator. Execution pauses at each `yield` and resumes on the next iteration.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num)   # 3,2,1
```

Generators are **exhausted** after one pass; recreate them to reuse.

---

## 🧱 3. Decorators (Basic)
A decorator is a function that wraps another function to extend its behaviour, without modifying the original code.

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)
# Output:
# Calling add
# Returned 8
```

- `@decorator` applies the wrapper automatically.
- Use `functools.wraps` (in production) to preserve metadata.
- Decorators can accept parameters (nested decorator pattern).

---

## 🧱 4. Error Handling Best Practices
- **Catch specific exceptions** – never bare `except:`.
- **Keep `try` blocks small** – wrap only the risky line(s).
- **Use `else`** for logic that runs only on success.
- **Use `finally`** for cleanup (close files, release locks).
- **Log errors** – never silence them silently.

```python
import logging

try:
    value = int(user_input)
except ValueError:
    logging.exception("Invalid input")
    value = 0
else:
    print("Input processed successfully.")
finally:
    print("Operation complete.")
```

- Avoid using exceptions for normal flow control (they are slower than `if` checks).

---

## 🧱 5. `try-except-else-finally` Review
Execution order:  
① `try` block  
② `except` (if an error occurs) – skips `else`  
③ `else` (only if no error)  
④ `finally` (always, even after `return`, `break`, `continue`)

```python
try:
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result = {result}")
finally:
    print("Done.")
```

**Pitfall:** A `return` inside `finally` overrides any previous `return` or exception – avoid it.

---

## 🧱 6. Working with CSV Files
The `csv` module handles comma‑separated values.

### Reading
```python
import csv

# Read as list of rows
with open("data.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Read as dicts (header from first row)
with open("data.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["Age"])
```

### Writing
```python
# Write lists
with open("out.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name","Age"])
    writer.writerow(["Emperor",18])

# Write dicts
with open("out.csv","w",newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Name","Age"])
    writer.writeheader()
    writer.writerow({"Name":"Emperor","Age":18})
```

- Always use `newline=""` to prevent blank lines on some systems.
- Custom delimiters: `delimiter="|"`.

---

## 🧱 7. Virtual Environments in Termux
A virtual environment isolates project dependencies.

**Create & activate:**
```bash
python -m venv .venv
source .venv/bin/activate
```

Now `pip install` goes into that environment.  
**Deactivate:**
```bash
deactivate
```

- Always add `.venv/` to `.gitignore`.
- This keeps your system Python clean and prevents version conflicts.

---

## 🧱 8. Introduction to Testing

### `assert` – Quick Check
```python
def double(n):
    return n * 2

assert double(3) == 6    # passes silently
assert double(0) == 0    # passes
```

- Great for sanity checks and development.
- Assertions can be disabled with the `-O` flag; do **not** use for production input validation.

### `unittest` – Structured Testing
Create a test class inheriting from `unittest.TestCase`.  
Test methods start with `test_`.

```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2,3), 5)
    def test_negative(self):
        self.assertEqual(add(-1,-1), -2)

if __name__ == "__main__":
    unittest.main()
```

- **Common assertions:** `assertEqual`, `assertTrue`, `assertRaises`.
- Use `setUp()` / `tearDown()` for shared pre‑/post‑test logic.
- Tests must be independent – order doesn’t matter.

---

## 💡 Quick Reference
```python
# List comprehension
[x**2 for x in range(5)]                     # [0,1,4,9,16]

# Dict comprehension
{x: x**2 for x in range(3)}                  # {0:0,1:1,2:4}

# Generator expression
gen = (x**2 for x in range(1000))            # lazy

# Decorator template
def my_dec(func):
    def wrapper(*a, **kw):
        # before
        res = func(*a, **kw)
        # after
        return res
    return wrapper

# CSV
import csv
with open('f.csv','r') as f:
    reader = csv.DictReader(f)
    for row in reader: ...

# venv
# python -m venv .venv && source .venv/bin/activate

# Testing
import unittest
class MyTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1, 1)
```

---

## 📌 Key Takeaway
- Use comprehensions for concise, readable data transformations.
- Generators (`yield` and `()`) save memory and enable pipelines.
- Decorators are a powerful pattern for extending function behaviour.
- Robust error handling follows strict rules: be specific, use `else`/`finally`, and never silence errors silently.
- The `csv` module is your go‑to for tabular data; virtual environments keep dependencies isolated.
- Automated testing (`assert` and `unittest`) ensures code correctness and supports fearless refactoring.

*Study this sheet. Recall it from memory. Then practice.*