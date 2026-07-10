# 📘 PyPhone Emperor v3.0 · Module 8
# 📖 L‑41 – Classes, Objects & `__init__`

---

## 🎯 OBJECTIVE — What You Will Master

> Blueprint your own data types with classes and constructors.

- 🏗️ **Class** – a blueprint for creating objects
- 🧱 **Object** – an instance of a class
- ⚙️ **`__init__`** – the constructor that initialises new objects
- 🧪 **Attributes** – data stored on the instance via `self`

---

## 🧱 DEFINING A CLASS

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

p = Product("Laptop", 999.99)
print(p.name)   # Laptop
print(p.price)  # 999.99
```

`self` refers to the specific instance being created. It must be the first parameter of every method.

---

## 🧱 WHY CLASSES MATTER

Classes group data (attributes) and behaviour (methods) together. They are the foundation of Object‑Relational Mapping (ORM) — the bridge between Python and SQL databases.

```python
class Customer:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
```

---

## 💡 Real‑world Usage

**Banking – account blueprint**
```python
class Account:
    def __init__(self, account_id, balance=0):
        self.account_id = account_id
        self.balance = balance
```

**E‑commerce – order model**
```python
class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items
```

**Logistics – shipment record**
```python
class Shipment:
    def __init__(self, tracking_id, destination):
        self.tracking_id = tracking_id
        self.destination = destination
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Define a class `Dog` with a method `bark` that prints "Woof!". Create an instance and call `bark()`. |
| Medium | Define a class `Cat` with `__init__` setting `self.name`. Create an instance and print `name`. |
| Hard | Define a class `Book` with `__init__(title, author)`. Create an instance and print both attributes. |

Run the coach:
```bash
python ii_Practice_Sheets/L41_Classes_Objects_init.py
```

---

## 📌 Key Takeaway
- `class Name:` defines a new type.
- `__init__` sets initial state; `self` binds values to the instance.
- Classes model real‑world entities — the backbone of ORMs.

*For Emperor.*