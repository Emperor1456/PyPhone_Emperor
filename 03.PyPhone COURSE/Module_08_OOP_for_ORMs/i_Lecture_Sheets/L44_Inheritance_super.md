# 📘 PyPhone Emperor v3.0 · Module 8
# 📖 L‑44 – Inheritance & `super()`

---

## 🎯 OBJECTIVE — What You Will Master

> Reuse and extend existing classes — the DRY principle applied to OOP.

- 🧬 **Inheritance** – child class inherits from parent
- 🏛️ **`super()`** – call parent methods from child
- 🧪 **`isinstance()`** – check object type in the hierarchy
- 🧱 **Why inheritance** – models "is‑a" relationships (a Dog is an Animal)

---

## 🧱 BASIC INHERITANCE

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

d = Dog()
print(d.speak())   # Woof!
```

`Dog` inherits everything from `Animal`; it can **override** methods.

---

## 🧱 USING `super()` IN `__init__`

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call parent constructor
        self.breed = breed

d = Dog("Rex", "German Shepherd")
print(d.name, d.breed)   # Rex German Shepherd
```

> ⚠️ **WARNING:** Always call `super().__init__()` if the parent sets critical attributes. Forgetting it leaves the object partially uninitialised.

---

## 💡 Real‑world Usage

**Banking – different account types**
```python
class Account:
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

class CheckingAccount(Account):
    def withdraw(self, amount):
        self.balance -= amount

class SavingsAccount(Account):
    def add_interest(self):
        self.balance *= 1.05
```

**E‑commerce – product variants**
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class DigitalProduct(Product):
    def download(self):
        return f"Downloading {self.name}"
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Parent class with a method; child overrides it and prints the child's version. |
| Medium | Add another child that overrides differently. |
| Hard | Child that extends parent `__init__` with `super()` and adds new attribute. |

Run the coach:
```bash
python ii_Practice_Sheets/L44_Inheritance_super.py
```

---

## 📌 Key Takeaway
- `class Child(Parent):` inherits all methods and attributes.
- Child can override (replace) or extend parent methods.
- `super()` lets you call the parent's version.

*For Emperor.*