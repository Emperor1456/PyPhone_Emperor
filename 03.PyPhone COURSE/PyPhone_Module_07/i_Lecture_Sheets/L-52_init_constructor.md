# 📘 PyPhone Emperor · Module 7  
# 📖 L‑52 – `__init__` Method (Constructor for Reliable Object Creation)

---

## 🎯 OBJECTIVE  
Master the `__init__` constructor to initialise objects predictably. Every instance gets its attributes set at creation time — no ad‑hoc assignment. This is how professional code guarantees every object starts in a valid state.

---

## 🧱 BRICK 1 – The `__init__` Method Signature

`__init__` is a special method that Python calls automatically after object creation. It must have `self` as the first parameter.

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person('Emperor')
print(p.name)   # 'Emperor'
```

**① Person with required name (Easy practice)**
```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person('Emperor')
print(p.name)   # Emperor
```

**② Car with multiple attributes (Medium practice)**
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

c = Car('Toyota', 'Corolla')
print(c.make, c.model)   # Toyota Corolla
```

**③ BankAccount with default balance (Hard practice)**
```python
class BankAccount:
    def __init__(self):
        self.balance = 0

acc = BankAccount()
print(acc.balance)   # 0
```
Even without arguments, `__init__` ensures every account starts with a clean balance.

> 💡 **INSIGHT:** Use `__init__` to guarantee that essential attributes exist on every instance. This prevents `AttributeError` later.

---

## 🧱 BRICK 2 – Default Values in `__init__`

Make parameters optional by supplying defaults, exactly like regular function defaults.

**④ Account with optional opening balance**
```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

a1 = BankAccount()       # uses default 0
a2 = BankAccount(500)    # overrides to 500
print(a1.balance, a2.balance)   # 0 500
```

**⑤ Product with default category**
```python
class Product:
    def __init__(self, name, price, category='General'):
        self.name = name
        self.price = price
        self.category = category

p = Product('Mouse', 19.99)
print(p.category)   # 'General'
```

> ⚠️ **WARNING:** Never use mutable defaults like `[]` or `{}` in `__init__`. Use `None` and create the object inside.

> 💡 **ADVANCED TIP – `@dataclass`:** For simple data classes, `from dataclasses import dataclass` can auto‑generate `__init__` and other methods, reducing boilerplate.

---

## 💡 Real‑world Usage

**Banking – new account with owner name**
```python
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
acc = Account('Emperor', 1000)
print(acc.owner)
```

**E‑commerce – order with items list**
```python
class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []  # mutable default handled safely
o = Order('ORD-1')
print(o.order_id)
```

**Logistics – package with dimensions**
```python
class Package:
    def __init__(self, weight, length, width, height):
        self.weight = weight
        self.length = length
        self.width = width
        self.height = height
p = Package(5, 20, 15, 10)
print(p.weight)
```

**HR – employee with department**
```python
class Employee:
    def __init__(self, name, dept='Engineering'):
        self.name = name
        self.dept = dept
e = Employee('Emperor')
print(e.dept)
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Define `Person` with `__init__` setting `self.name`. Create `p` with name `'Emperor'` and print `p.name`. | `Emperor` |
| Medium | Define `Car` with `__init__` taking make and model. Create `c` with make=`'Toyota'`, model=`'Corolla'` and print both. | `Toyota Corolla` |
| Hard   | Define `BankAccount` with `__init__` setting `self.balance=0`. Create instance `acc`, then print `acc.balance`. | `0` |

Run the coach:
```bash
python ii_Practice_Sheets/L-52_init_Method.py
```

---

## 📌 Key Takeaway
- `__init__` guarantees every instance starts with the right attributes.
- `self` binds the values to the instance; always first parameter.
- Default parameter values make arguments optional.
- Use `None` for mutable defaults to avoid shared‑state bugs.