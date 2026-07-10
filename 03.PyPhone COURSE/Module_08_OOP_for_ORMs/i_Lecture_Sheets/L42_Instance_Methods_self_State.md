# 📘 PyPhone Emperor v3.0 · Module 8
# 📖 L‑42 – Instance Methods, `self` & State Management

---

## 🎯 OBJECTIVE — What You Will Master

> Give objects behaviour that reads and changes their own data.

- 🔧 **Instance methods** – functions defined inside a class
- 🧠 **`self`** – the automatic reference to the calling object
- ✏️ **Mutators** – methods that modify state
- 🔍 **Accessors** – methods that return information without changing state

---

## 🧱 DEFINING METHODS

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):    # mutator
        self.count += 1

    def value(self):        # accessor
        return self.count

c = Counter()
c.increment()
print(c.value())   # 1
```

---

## 🧱 BUSINESS EXAMPLE – BANK ACCOUNT

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

acc = BankAccount("Emperor", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.balance)   # 1300
```

> 💡 **INSIGHT:** Always use `self.attr` to read/write instance data. Forgetting `self.` creates a local variable inside the method — a common bug.

---

## 💡 Real‑world Usage

**E‑commerce – shopping cart**
```python
class Cart:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def total(self):
        return len(self.items)
```

**Logistics – package tracker**
```python
class Package:
    def __init__(self, tracking):
        self.tracking = tracking
        self.status = "pending"
    def ship(self):
        self.status = "shipped"
    def deliver(self):
        self.status = "delivered"
```

**HR – employee record**
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def give_raise(self, amount):
        self.salary += amount
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Define a `Dog` class with `speak()` returning "Woof! I am " + name. |
| Medium | Define a `Counter` class that increments and prints its count. |
| Hard | Define a `Calculator` class with an `add` method. |

Run the coach:
```bash
python ii_Practice_Sheets/L42_Instance_Methods_self_State.py
```

---

## 📌 Key Takeaway
- Instance methods operate on an object's own data via `self`.
- Mutators change state; accessors return state.
- Always use `self.` to access attributes inside methods.

*For Emperor.*