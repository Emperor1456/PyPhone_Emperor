# 📘 PyPhone Emperor v3.0 · Module 5
# 📖 L‑27 – Default Parameters & Mutable Pitfall

---

## 🎯 OBJECTIVE — What You Will Master

> Set fallback values for parameters, and avoid the most insidious Python bug.

- 🧷 **Default parameters** – provide a value when none is given
- ⚠️ **Mutable default trap** – why `def f(lst=[])` is dangerous
- ✅ **Safe pattern** – use `None` as default, create mutable inside
- 🧪 **Business use** – optional flags, configuration

---

## 🧱 DEFAULT PARAMETERS IN ACTION

```python
def power(base, exp=2):
    return base ** exp

print(power(3))      # 9 (3²)
print(power(3, 3))   # 27
```

Non‑default parameters must come **before** defaults.

---

## 🧱 THE MUTABLE DEFAULT PITFALL

```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))   # [1]
print(add_item(2))   # [1, 2]  ← unexpected!
```

The list is created **once** at function definition, not each call.

---

## 🧱 THE FIX – NONE SENTINEL

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

Now each call gets a fresh list when needed.

> 💡 **INSIGHT:** This pattern is used everywhere in production Python.

---

## 💡 Real‑world Usage

**Banking – new account with default balance**
```python
def create_account(name, balance=0.0):
    return {"name": name, "balance": balance}
```

**E‑commerce – add to cart with default quantity**
```python
def add_to_cart(cart, product, qty=1):
    cart.append({"product": product, "qty": qty})
    return cart
```

**Logistics – default shipping method**
```python
def ship(order_id, method="standard"):
    print(f"Shipping {order_id} via {method}")
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Define `greet(name='Guest')` returning "Hello " + name. Call with no argument. | `def greet(name='Guest'): return 'Hello '+name` |
| Medium | Using the same `greet`, call with `'Emperor'` and print result. | `print(greet('Emperor'))` |
| Hard | Define `power(x,exp=2)` returning `x**exp`. Call with 2 (default) and 3,2; print each. | `def power(x,exp=2): return x**exp` |

Run the coach:
```bash
python ii_Practice_Sheets/L27_Default_Parameters_Mutable_Pitfall.py
```

---

## 📌 Key Takeaway
- Defaults make arguments optional.
- Never use mutable objects directly as defaults; use `None`.
- The order of parameters matters.

*For Emperor.*