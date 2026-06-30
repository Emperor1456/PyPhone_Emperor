# 📘 PyPhone Emperor · Module 4  
# 🗃️ Comprehensive Note – Functions & Scope

---

## 🎯 Scope
This note covers every essential concept from Module 4: defining and calling functions, parameters, return values, default parameters, `*args` and `**kwargs`, scope (LEGB rule), lambda functions, and recursion.  
All code fits a phone screen; no sideways scrolling.

---

## 🧱 1. Defining and Calling Functions

```python
def function_name(parameters):
    # indented body
    return value
```

- `def` creates a function; the body is indented (4 spaces).
- A function does nothing until **called**.
- Use the function name with parentheses to call it.

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Emperor"))   # Hello, Emperor!
```

---

## 🧱 2. Parameters & Arguments
- **Parameters** – placeholders in the `def` line.
- **Arguments** – actual values passed when calling.

### Positional Arguments
Matched by order.

```python
def add(a, b):
    return a + b

add(3, 5)   # 8
```

### Keyword Arguments
Pass by name; order doesn’t matter.

```python
def describe(name, age, city):
    print(f"{name} is {age} and lives in {city}")

describe(age=18, city="Dhaka", name="Emperor")
```

- Positional arguments must come **before** keyword arguments.

---

## 🧱 3. Return Values
`return` sends a value back to the caller and exits the function.  
If there is no `return`, the function returns `None`.

```python
def square(x):
    return x ** 2

result = square(4)   # 16
```

Multiple return values are packed into a tuple.

```python
def min_max(lst):
    return min(lst), max(lst)

low, high = min_max([4, 1, 9, 3])   # low=1, high=9
```

---

## 🧱 4. Default Parameters
Assign default values with `=` in the `def` line.  
If the caller omits the argument, the default is used.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Emperor")   # Hello, Emperor!
greet()            # Hello, Guest!
```

- Parameters with defaults must come **after** parameters without defaults.
- **Never use mutable defaults** like `[]`. Use `None` instead and create the object inside.

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

## 🧱 5. `*args` and `**kwargs`
### `*args` — Variable Positional Arguments
Collects extra positional arguments into a tuple.

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1,2,3))        # 6
print(sum_all(10,20,30,40))  # 100
```

### `**kwargs` — Variable Keyword Arguments
Collects extra keyword arguments into a dictionary.

```python
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_details(name="Emperor", age=18, city="Dhaka")
```

**Order when combining:**  
`def func(a, b=10, *args, **kwargs):`

---

## 🧱 6. Scope and the LEGB Rule
Where a variable can be accessed.

- **Local** – inside the current function.
- **Enclosing** – in the outer function (if nested).
- **Global** – at module level.
- **Built‑in** – names like `print`, `len`.

Python searches for names in that order: **L → E → G → B**.

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)    # local
    inner()

outer()
```

### Modifying a Global Variable
Use the `global` keyword inside the function.

```python
counter = 0

def increment():
    global counter
    counter += 1
```

Without `global`, `counter += 1` would create a new local variable and raise an error.

---

## 🧱 7. Lambda Functions
A `lambda` is an anonymous, one‑expression function.

```python
square = lambda x: x ** 2
print(square(5))   # 25
```

- No `def`, no `return` – the expression is automatically returned.
- Can take multiple arguments: `lambda a, b: a + b`.
- Often used with `map()`, `filter()`, `sorted()`.

```python
nums = [1,2,3,4]
evens = list(filter(lambda x: x % 2 == 0, nums))
# [2,4]
```

---

## 🧱 8. Recursion
A function that calls itself.

**Requirements:**
- A **base case** that stops the recursion.
- A **recursive case** that moves toward the base case.

```python
def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)  # recursive case

print(factorial(5))   # 120
```

- Python has a default recursion limit (~1000 calls). Exceeding it raises `RecursionError`.

---

## 💡 Quick Reference
```python
# Define and call
def add(a, b):
    return a + b

add(2, 3)                # 5

# Default parameter
def greet(name="Guest"):
    print(f"Hi, {name}")

greet()                  # Hi, Guest

# *args and **kwargs
def mix(a, *args, **kwargs):
    print(a, args, kwargs)

mix(1, 2, 3, x=4)        # 1 (2,3) {'x':4}

# Lambda
double = lambda x: x * 2
double(5)                # 10

# Recursion (factorial)
def fact(n):
    if n <= 1: return 1
    return n * fact(n - 1)

# LEGB example
x = "global"
def f():
    x = "local"
    print(x)
```

---

## 📌 Key Takeaway
- Functions are defined with `def` and called with `()`.
- Use parameters to pass data; use `return` to get results back.
- `*args` and `**kwargs` allow flexible argument lists.
- Scope follows LEGB; use `global` to modify global variables.
- Lambdas are short, throwaway functions.
- Recursion is a powerful pattern when a problem naturally divides into smaller copies of itself.

*Study this sheet. Recall it from memory. Then practice.*