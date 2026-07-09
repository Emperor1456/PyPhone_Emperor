# 📘 PyPhone Emperor · Module 7  
# 📖 L‑53 – Instance Methods & `self` (Giving Objects Behaviour)

---

## 🎯 OBJECTIVE  
Master instance methods — functions inside a class that operate on the object's own data. They always take `self` as the first parameter, giving them access to the instance's attributes. This is where objects gain behaviour.

---

## 🧱 BRICK 1 – Methods That Return Strings

A method can use `self` to access attributes and return a formatted result.

**① Dog that speaks its name (Easy practice)**
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return 'Woof! I am ' + self.name

d = Dog('Rex')
print(d.speak())   # 'Woof! I am Rex'
```
The method uses `self.name` to personalise the bark.

**② Calculator with add method (Hard practice)**
```python
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(3, 5))   # 8
```
Even though `add` doesn't use instance attributes, it's still an instance method — often a design choice for grouping utility functions.

---

## 🧱 BRICK 2 – Methods That Modify State (Mutators)

**③ Counter that increments (Medium practice)**
```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

c = Counter()
c.increment()
print(c.count)   # 1
```
`increment()` changes the object's internal state — a classic mutator pattern.

**④ Bank account with deposit**
```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

acc = BankAccount(100)
acc.deposit(50)
print(acc.balance)   # 150
```

> 💡 **INSIGHT:** Methods that only read data are **accessors**; methods that change data are **mutators**. Both are instance methods when they use `self`.

> ⚠️ **WARNING:** Forget `self.` and you create a local variable inside the method — the attribute remains unchanged, a very common OOP bug.

> 💡 **ADVANCED TIP – Chaining methods:** Return `self` from mutator methods to enable method chaining: `obj.deposit(50).withdraw(20)`.

---

## 💡 Real‑world Usage

**Banking – account with withdraw**
```python
class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

acc = Account(200)
acc.withdraw(50)
print(acc.balance)   # 150
```

**E‑commerce – shopping cart**
```python
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total(self):
        return len(self.items)

cart = Cart()
cart.add_item('Laptop')
print(cart.total())   # 1
```

**Logistics – package status update**
```python
class Package:
    def __init__(self, tracking):
        self.tracking = tracking
        self.status = 'Pending'

    def ship(self):
        self.status = 'Shipped'

    def deliver(self):
        self.status = 'Delivered'

p = Package('TRK-1')
p.ship()
print(p.status)   # 'Shipped'
```

**HR – employee raise**
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

e = Employee('Emperor', 50000)
e.give_raise(5000)
print(e.salary)   # 55000
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Define `Dog` with `__init__` setting `self.name`, and method `speak` returning `'Woof! I am '+name`. Create `d` with name `'Rex'`, call `d.speak()` and print. | `Woof! I am Rex` |
| Medium | Define `Counter` with `__init__` setting `self.count=0`, method `increment` that adds 1. Create `c`, call `c.increment()`, then print `c.count`. | `1` |
| Hard   | Define `Calculator` with method `add(self,a,b)` returning `a+b`. Create instance, call `add(3,5)` and print result. | `8` |

Run the coach:
```bash
python ii_Practice_Sheets/L-53_Instance_Methods.py
```

---

## 📌 Key Takeaway
- Instance methods always take `self` and access the object's own data.
- They can return values (accessors) or modify the object (mutators).
- `self.attr` is mandatory to read/write attributes; without it you create a local variable.
- Methods define what objects can **do** — the behaviour half of OOP.