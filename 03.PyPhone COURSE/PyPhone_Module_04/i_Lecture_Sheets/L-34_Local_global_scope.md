# 📘 PyPhone Emperor · Module 4  
# 📖 L‑34 – Local vs Global Scope (LEGB Rule)

---

## 🎯 OBJECTIVE  
Master **variable scope** — where variables live and how Python resolves names.  
Understanding scope prevents bugs where a function accidentally shadows or modifies data.  
The LEGB rule (Local → Enclosing → Global → Built‑in) is the map every Python developer follows.

---

## 🧱 BRICK 1 – Local vs Global Variables

- **Local:** defined inside a function; visible only there.
- **Global:** defined outside any function; visible throughout the file.

**① Modifying a global variable with `global`**
```python
x = 10

def change():
    global x
    x = 20

change()
print(x)   # 20
```
Without `global x`, the assignment `x = 20` would create a new local variable, leaving the global `x` unchanged.  
This is the Easy practice task.

**② Incrementing a global counter**
```python
counter = 5

def increment():
    global counter
    counter += 1

increment()
print(counter)   # 6
```
The `global` keyword tells Python: "use the variable from the global scope, not a local one."  
This is the Medium practice task.

> 💡 **INSIGHT:** A function can **read** a global variable without `global`.  
> You only need `global` when you want to **assign** to it inside the function.

---

## 🧱 BRICK 2 – The LEGB Rule and `nonlocal`

Python searches for names in this order: **L**ocal → **E**nclosing → **G**lobal → **B**uilt‑in.

**③ Enclosing scope with `nonlocal`**
```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    return x

print(outer())   # 20
```
`nonlocal x` tells Python: "x belongs to the enclosing function, not to `inner()` or the global scope."  
This is the Hard practice task.

**④ LEGB demonstration**
```python
name = 'Global'

def outer():
    name = 'Enclosing'
    def inner():
        name = 'Local'
        print(name)   # 'Local' (innermost wins)
    inner()

outer()
```

**⑤ Built‑in scope**
```python
print(len)   # <built-in function len> — always available
```

> ⚠️ **WARNING:** Overusing `global` makes code hard to debug and test.  
> Prefer passing values through parameters and return statements.

> 💡 **ADVANCED TIP:** Use `nonlocal` in nested functions (closures) to modify outer variables.  
> This is critical for decorators and factory functions you'll write later.

---

## 💡 Real‑world Usage

**Banking – global interest rate**
```python
rate = 0.05

def apply_interest(balance):
    return balance * (1 + rate)

print(apply_interest(1000))   # 1050.0
```

**E‑commerce – global discount flag**
```python
sale_active = True

def get_price(item_price):
    if sale_active:
        return item_price * 0.8
    return item_price

print(get_price(100))   # 80.0
```

**HR – counter for employee IDs**
```python
next_id = 1000

def new_employee(name):
    global next_id
    emp_id = next_id
    next_id += 1
    return f"{name}: EMP-{emp_id}"

print(new_employee('Emperor'))   # Emperor: EMP-1000
print(new_employee('Rahim'))     # Rahim: EMP-1001
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | `x=10`. Define a function that uses `global x` to change x to 20. Call it, then print x. | `20` |
| Medium | `counter=5`. Define `increment()` that increments global counter by 1. Call it, then print counter. | `6` |
| Hard   | Define `outer()` with local x=10, inner function that uses `nonlocal x` to set x=20, calls inner, and returns x. Print the returned value. | `20` |

Run the coach:
```bash
python ii_Practice_Sheets/L-34_Local_Global_Scope.py
```

---

## 📌 Key Takeaway
- Local variables live inside functions; global ones live at module level.
- Use `global` to assign to a global variable from inside a function.
- Use `nonlocal` to modify a variable in the enclosing scope (nested functions).
- LEGB defines the lookup order: Local → Enclosing → Global → Built‑in.
- Prefer parameter passing over global state for cleaner, testable code.