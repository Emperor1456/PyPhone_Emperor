# 📘 PyPhone Emperor · Module 7  
# 📖 L‑51 – Classes & Objects (Blueprint for Business Entities)

---

## 🎯 OBJECTIVE  
Master **classes** and **objects** — the core of object‑oriented programming. A class is a blueprint; an object is a concrete instance. Use them to model real‑world entities like dogs, cats, books, and bank accounts with their own data and behaviour.

---

## 🧱 BRICK 1 – Defining a Class and Creating Objects

A class is defined with `class Name:` followed by methods (functions inside the class). You create an object by calling the class.

```python
class Dog:
    def bark(self):
        print('Woof!')

d = Dog()
d.bark()   # prints 'Woof!'
```

**① Animal behaviour – dog barks (Easy practice)**
```python
class Dog:
    def bark(self):
        print('Woof!')

d = Dog()
d.bark()
```
Output: `Woof!`. The class gives every dog instance the ability to bark.

**② Pet with a name – cat initialisation (Medium practice)**
```python
class Cat:
    def __init__(self, name):
        self.name = name

c = Cat('Whiskers')
print(c.name)   # 'Whiskers'
```
`__init__` sets the cat's name at creation; `self.name` stores it on the instance.

**③ Business entity – book details (Hard practice)**
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

b = Book('1984', 'Orwell')
print(b.title, b.author)   # '1984 Orwell'
```
A `Book` object now carries both title and author as instance attributes.

> 💡 **INSIGHT:** `self` refers to the specific instance. Every method must have `self` as its first parameter, so it knows which object it's working on.

---

## 🧱 BRICK 2 – Attributes and Methods in Business Context

**④ Person record**
```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person('Emperor')
print(p.name)   # 'Emperor'
```

**⑤ Car specification**
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

c = Car('Toyota', 'Corolla')
print(c.make, c.model)   # 'Toyota Corolla'
```

**⑥ Bank account with default balance**
```python
class BankAccount:
    def __init__(self):
        self.balance = 0

acc = BankAccount()
print(acc.balance)   # 0
```

> ⚠️ **WARNING:** Without `self.`, a variable inside a method is just a local variable — gone after the method ends. Always use `self.attr` for data that should persist with the object.

> 💡 **ADVANCED TIP – Class documentation:** Use docstrings (`"""..."""`) right after the class definition to describe its purpose. This is essential for maintainable enterprise code.

---

## 💡 Real‑world Usage

**Banking – customer account**
```python
class Customer:
    def __init__(self, name, account_id):
        self.name = name
        self.account_id = account_id
cust = Customer('Emperor', 'A100')
print(cust.account_id)
```

**E‑commerce – product listing**
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
item = Product('Mouse', 24.99)
print(item.name)
```

**Logistics – shipment record**
```python
class Shipment:
    def __init__(self, tracking_id):
        self.tracking_id = tracking_id
s = Shipment('TRK-123')
print(s.tracking_id)
```

**HR – employee badge**
```python
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
emp = Employee(101, 'Emperor')
print(emp.name)
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Define class `Dog` with method `bark` that prints `'Woof!'`. Create instance `d` and call `d.bark()`. | `Woof!` |
| Medium | Define class `Cat` with `__init__` setting `self.name`. Create instance `c` with name `'Whiskers'` and print `c.name`. | `Whiskers` |
| Hard   | Define class `Book` with `__init__(self,title,author)`. Create instance `b` with title `'1984'` and author `'Orwell'`. Print both attributes separated by a space. | `1984 Orwell` |

Run the coach:
```bash
python ii_Practice_Sheets/L-51_Classes_Objects.py
```

---

## 📌 Key Takeaway
- `class Name:` defines a blueprint; `Name()` creates an instance.
- `__init__(self, ...)` initialises new objects with attributes.
- `self.attr` stores data on the instance; methods always start with `self`.
- Classes model real‑world business entities — accounts, products, shipments.