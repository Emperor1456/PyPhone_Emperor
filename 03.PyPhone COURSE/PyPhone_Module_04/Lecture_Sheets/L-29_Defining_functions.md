# 📘 PyPhone Emperor · Module 4
# 📖 L‑29 – Defining a Function (`def`)

---

## 🎯 OBJECTIVE
Learn to create reusable blocks of code called **functions**
using the `def` keyword. Functions are the foundation of
structured programming — they reduce repetition, improve
readability, and make code testable.

---

## 🧱 BRICK 1 – The `def` Statement

A function is defined with `def`, a name, parentheses `()`,
and a colon `:`. The indented body that follows runs whenever
the function is **called**.

```python
def function_name():
    # indented body
    statement
```

**Minimal example:**
```python
def greet():
    print("Hello, Emperor!")

greet()   # calls the function → prints "Hello, Emperor!"
```

Without the call `greet()`, nothing runs. Defining a function
does not execute it — only calling does.

> 💡 **INSIGHT:** Function names follow the same rules as
> variable names: lowercase, underscores for spaces,
> no leading digits.

---

## 🧱 BRICK 2 – Why Functions Matter

**① Reuse logic without copy‑paste**
```python
def show_menu():
    print("1. Start")
    print("2. Settings")
    print("3. Quit")

show_menu()
show_menu()   # call as many times as needed
```

**② Organise code logically**
```python
def validate_email(email):
    return "@" in email and "." in email

def register_user(name, email):
    if validate_email(email):
        print(f"User {name} registered.")
    else:
        print("Invalid email.")
```

**③ Test behaviour in isolation**
Each function can be tested independently, which is
critical for enterprise‑grade software.

> ⚠️ **NOTE:** A function must be defined **before** it
> is called. Python reads files top to bottom.

---

## 📌 Key Takeaway
- `def name():` creates a function; indented lines are its body.
- A function does nothing until **called** with `name()`.
- Functions eliminate repetition and improve structure.