# 📘 PyPhone Emperor · Module 4
# 📖 L‑34 – Local vs Global Scope (LEGB Rule)

---

## 🎯 OBJECTIVE
Learn where variables live and how Python resolves
their names using the **LEGB rule** — Local, Enclosing,
Global, Built‑in. Understanding scope is critical for
writing bug‑free functions and managing data flow.

---

## 🧱 BRICK 1 – Local and Global Variables

- **Local variable:** defined inside a function;
  visible only within that function.
- **Global variable:** defined outside any function;
  visible throughout the file.

```python
x = "global"

def demo():
    x = "local"
    print("Inside:", x)

demo()              # Inside: local
print("Outside:", x) # Outside: global
```

The local `x` shadows the global `x` inside the function,
but does **not** modify it. They are two separate variables.

> 💡 **INSIGHT:** A function can **read** a global variable
> directly, but to **modify** it you must use `global`.

---

## 🧱 BRICK 2 – The `global` Keyword and the LEGB Rule

### Modifying a global variable
```python
counter = 0

def increment():
    global counter
    counter += 1
    print(counter)

increment()   # 1
print(counter) # 1
```

Without `global counter`, `counter += 1` would create
a new local variable and crash (UnboundLocalError).

### The LEGB rule – name lookup order
Python searches for a variable name in this order:
① **L**ocal – inside the current function  
② **E**nclosing – in the outer function, if nested  
③ **G**lobal – at module level  
④ **B**uilt‑in – Python’s built‑in names (like `print`, `len`)

```python
name = "Global"

def outer():
    name = "Enclosing"
    def inner():
        name = "Local"
        print(name)     # Local (innermost wins)
    inner()

outer()
```

> ⚠️ **WARNING:** Overusing `global` makes code hard to
> debug. Prefer passing values through parameters and
> return statements.

---

## 📌 Key Takeaway
- Variables inside a function are local by default.
- Global variables can be read, but need `global` to modify.
- LEGB defines the search order: Local → Enclosing → Global → Built‑in.
- Limit global usage; prefer passing data via arguments.