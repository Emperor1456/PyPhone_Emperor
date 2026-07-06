# 📘 PyPhone Emperor · Module 7
# 📖 L‑53 – Instance Methods & `self`

---

## 🎯 OBJECTIVE
Learn to write functions that belong to an object —
**instance methods**. Every instance method has `self`
as its first parameter, giving it access to the
object's own data. This is how objects gain behaviour.

---

## 🧱 BRICK 1 – Defining an Instance Method

An instance method is a function defined inside a
class. Its first parameter is **always** `self`,
which refers to the specific object calling the method.

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, I am {self.name}."

u1 = User("Emperor", 18)
print(u1.greet())   # Hello, I am Emperor.
```

When you call `u1.greet()`, Python automatically
passes `u1` as the `self` argument. You never
write it explicitly.

> 💡 **INSIGHT:** `self` is not a keyword — you could
> use any name, but `self` is the ironclad convention.

---

## 🧱 BRICK 2 – Methods That Modify State

Instance methods can read **and** change the object's
attributes, giving objects dynamic behaviour.

```python
class BankAccount:
    def __init__(self, owner, balance):
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

Methods that modify attributes are called **mutators**.
Methods that only read data are **accessors**.

> ⚠️ **WARNING:** Forgetting `self.` inside a method
> creates a local variable, not an attribute — a very
> common bug.

---

## 📌 Key Takeaway
- Instance methods take `self` as their first parameter.
- `self` gives access to the object's own attributes.
- Methods define what an object **can do**.
- `self.attr` refers to instance data; without it you
  create a temporary local variable.