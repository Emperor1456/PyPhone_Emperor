# 📘 PyPhone Emperor · Module 7  
# 📖 L‑55 – Inheritance (Parent & Child Classes) – Reusing Business Logic

---

## 🎯 OBJECTIVE  
Master **inheritance** — the mechanism that lets a child class automatically receive all attributes and methods from a parent class. This promotes code reuse and models "is‑a" relationships (a Dog is an Animal, a Cat is an Animal).

---

## 🧱 BRICK 1 – Basic Inheritance and Overriding

Define a parent class with shared behaviour, then create child classes that inherit and override.

```python
class Animal:
    def speak(self):
        return '?'

class Dog(Animal):
    def speak(self):
        return 'Woof'
```

**① Dog overrides speak (Easy practice)**
```python
class Animal:
    def speak(self):
        return '?'

class Dog(Animal):
    def speak(self):
        return 'Woof'

d = Dog()
print(d.speak())   # 'Woof'
```
`Dog` inherits everything from `Animal` but replaces `speak` with its own version.

**② Cat overrides speak (Medium practice)**
```python
class Cat(Animal):
    def speak(self):
        return 'Meow'

c = Cat()
print(c.speak())   # 'Meow'
```

**③ Bird does NOT override – uses parent method (Hard practice)**
```python
class Bird(Animal):
    pass

b = Bird()
print(b.speak())   # '?' — inherits parent's speak
```
`Bird` is a child with no changes; it uses `Animal`'s `speak` directly.

> 💡 **INSIGHT:** Inheritance captures "is‑a" relationships. Use it when the child is a specialised version of the parent.

---

## 🧱 BRICK 2 – Extending with `super()`

Child classes can call parent methods using `super()`, which is common in `__init__`.

**④ Animal with name**
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} makes a sound'

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)    # call parent constructor
        self.breed = breed

    def speak(self):
        return f'{self.name} barks'

d = Dog('Rex', 'German Shepherd')
print(d.speak())   # 'Rex barks'
print(d.breed)     # 'German Shepherd'
```

**⑤ Financial hierarchy – Account and SavingsAccount**
```python
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def info(self):
        return f'{self.owner}: ${self.balance}'

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
```

> ⚠️ **WARNING:** Always call `super().__init__()` if the parent's `__init__` sets critical attributes. Forgetting it leaves the object partially uninitialised.

> 💡 **ADVANCED TIP – Method Resolution Order (MRO):** Python searches for methods in a specific order; you can see it with `ClassName.__mro__`.

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
    interest = 0.05
    def add_interest(self):
        self.balance *= (1 + self.interest)
```

**E‑commerce – product variants**
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class DigitalProduct(Product):
    def download(self):
        return f'Downloading {self.name}'
```

**Logistics – vehicle types**
```python
class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

class Truck(Vehicle):
    def load(self, weight):
        return weight <= self.capacity
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Define `Animal` with method `speak` returning `'?'`. Define `Dog(Animal)` overriding `speak` to return `'Woof'`. Create `d=Dog()` and print `d.speak()`. | `Woof` |
| Medium | Add another subclass `Cat` overriding `speak` to return `'Meow'`. Create `c=Cat()` and print `c.speak()`. | `Meow` |
| Hard   | Define `Bird(Animal)` that does NOT override speak. Create instance and print `speak()`. Should return `'?'`. | `?` |

Run the coach:
```bash
python ii_Practice_Sheets/L-55_Inheritance.py
```

---

## 📌 Key Takeaway
- `class Child(Parent):` inherits all methods and attributes.
- Child can override (replace) methods or add new ones.
- Use `super()` to call parent methods, especially `__init__`.
- Inheritance promotes reuse and models natural hierarchies.