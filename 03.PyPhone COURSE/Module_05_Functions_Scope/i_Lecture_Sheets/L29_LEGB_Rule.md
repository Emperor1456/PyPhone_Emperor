# 📘 PyPhone Emperor v3.0 · Module 5
# 📖 L‑29 – LEGB Rule – Local, Enclosing, Global, Built‑in

---

## 🎯 OBJECTIVE — What You Will Master

> Where variables live and how Python finds them.

- 🌐 **LEGB** – Local → Enclosing → Global → Built‑in (lookup order)
- 🏠 **Local** – inside current function
- 🏢 **Enclosing** – in outer (nested) functions
- 🌍 **Global** – at module level
- 🧰 **Built‑in** – Python’s own names (`print`, `len`, etc.)

---

## 🧱 DEMONSTRATING LEGB

```python
x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)   # local
    inner()
outer()
```

Python searches inward‑out, stopping at the first match.

---

## 🧱 MODIFYING GLOBAL VARIABLES

```python
counter = 0
def increment():
    global counter
    counter += 1
increment()
print(counter)   # 1
```

Without `global`, `counter += 1` would create a local variable and crash.

---

## 🧱 MODIFYING ENCLOSING VARIABLES (`nonlocal`)

```python
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()
print(outer())   # 1
```

---

## 💡 Real‑world Usage

**Banking – global interest rate**
```python
RATE = 0.05
def apply_interest(bal):
    return bal * (1 + RATE)
```

**E‑commerce – config constant**
```python
MAX_ITEMS = 100
def add_to_cart(cart, item):
    if len(cart) < MAX_ITEMS:
        cart.append(item)
```

**Logistics – built‑in `len` used everywhere**
```python
print(len([1,2,3]))   # built‑in
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Use `global` to change a variable outside a function. | `x=10; def change(): global x; x=20; change(); print(x)` |
| Medium | Define `outer()` with local `x=10`, inner `set_x()` that changes `x` via `nonlocal`, return `x`. | `def outer(): x=10; def inner(): nonlocal x; x=20; inner(); return x` |
| Hard | Predict and print a variable from LEGB: define global, enclosing, local; print from inner. | Nested functions |

Run the coach:
```bash
python ii_Practice_Sheets/L29_LEGB_Rule.py
```

---

## 📌 Key Takeaway
- Python resolves names using LEGB order.
- Use `global` to modify global; `nonlocal` for enclosing.
- Avoid overusing globals; prefer parameter passing.

*For Emperor.*