# 📘 PyPhone Emperor v3.0 · Module 9
# 📖 L‑49 – Modules & `import` (math, random, etc.)

---

## 🎯 OBJECTIVE — What You Will Master

> Unlock Python's built‑in arsenal and organize your own code into reusable files.

- 📦 **Modules** – `.py` files containing functions and variables
- 🔌 **`import`** – bring modules into your script
- 🎲 **`random`** – generate random numbers and choices
- 🧮 **`math`** – mathematical constants and functions
- 📅 **`datetime`** – date and time handling
- 🧪 **`os`** – interact with the operating system

---

## 🧱 IMPORTING MODULES

```python
import math
print(math.sqrt(16))   # 4.0

from math import pi, sin
print(pi)              # 3.141592653589793

import random as rnd
print(rnd.randint(1, 10))  # random integer 1‑10
```

---

## 🧱 KEY MODULE FUNCTIONS

**`random`:**
```python
import random
print(random.random())         # float 0.0‑1.0
print(random.choice(["a","b"]))# pick one
```

**`math`:**
```python
print(math.ceil(3.2))   # 4
print(math.floor(3.8))  # 3
```

**`datetime`:**
```python
from datetime import datetime
print(datetime.now())
```

**`os`:**
```python
import os
print(os.getcwd())   # current working directory
```

---

## 🧱 CREATING YOUR OWN MODULE

Save a file `calculator.py`:
```python
def add(a, b):
    return a + b
```

Then in another script:
```python
import calculator
print(calculator.add(2, 3))
```

---

## 💡 Real‑world Usage

**Banking – generate account numbers**
```python
import random
acc_id = f"ACC-{random.randint(1000,9999)}"
```

**E‑commerce – timestamp orders**
```python
from datetime import datetime
order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

**Logistics – list files in a directory**
```python
import os
for file in os.listdir("shipments"):
    print(file)
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Import `math` and print the value of `pi`. |
| Medium | Use `random.randint()` to simulate a dice roll (1‑6). |
| Hard | Write a function that uses `os.listdir()` and returns the number of files in a given directory. |

Run the coach:
```bash
python ii_Practice_Sheets/L49_Modules_import.py
```

---

## 📌 Key Takeaway
- Modules extend Python's capabilities; `import` brings them in.
- Use standard modules (`math`, `random`, `datetime`, `os`) for common tasks.
- You can create your own modules to organize reusable code.

*For Emperor.*