# 📘 PyPhone Emperor · Module 4
# 📖 L‑30 – Parameters & Arguments

---

## 🎯 OBJECTIVE
Learn to pass data into functions using **parameters**
(placeholders) and **arguments** (actual values).
Parameters make functions flexible and reusable
with different inputs.

---

## 🧱 BRICK 1 – Parameters and Positional Arguments

**Parameter:** a variable listed inside the parentheses
in the `def` statement.
**Argument:** the actual value you supply when calling
the function.

```python
def greet(name):          # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Emperor")          # "Emperor" is an argument
greet("World")
```

Multiple parameters are separated by commas:
```python
def add(a, b):
    print(a + b)

add(3, 5)      # prints 8
add(10, 20)    # prints 30
```

Arguments are matched to parameters **by position** — the
first argument goes to the first parameter, second to second.

> 💡 **INSIGHT:** Use descriptive parameter names to make
> the function’s purpose obvious.

---

## 🧱 BRICK 2 – Keyword Arguments and Mixing

You can also pass arguments by **name**, not position.
Keyword arguments improve readability and allow you to
skip default order.

```python
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

describe_person(age=18, city="Dhaka", name="Emperor")
```

Rules when mixing positional and keyword arguments:
- Positional arguments must come **before** keyword arguments.
- Each parameter can only receive one value.

```python
# Valid
describe_person("Emperor", age=18, city="Dhaka")

# Invalid – positional after keyword
# describe_person(name="Emperor", 18, "Dhaka")
```

> ⚠️ **WARNING:** Never assign a parameter more than once
> (e.g., `f(1, a=2)`) — it raises a `TypeError`.

---

## 📌 Key Takeaway
- Parameters are placeholders; arguments are actual values.
- Positional arguments are matched by order.
- Keyword arguments use parameter names for clarity.
- Positionals first, then keyword arguments.