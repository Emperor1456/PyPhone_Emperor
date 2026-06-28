# 📘 PyPhone Emperor · Module 7
# 📖 L‑56 – Overriding Methods

---

## 🎯 OBJECTIVE
Learn to **override** a parent class method in a child class.
Overriding lets you replace or extend inherited behaviour
with a version tailored specifically to the child class,
while still optionally calling the original parent method.

---

## 🧱 BRICK 1 – Replacing a Method Entirely

If a child defines a method with the exact same name as
one in the parent, the child version **completely replaces**
the parent version when called on a child instance.

```python
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        return "Hello from Child"

p = Parent()
c = Child()
print(p.greet())   # Hello from Parent
print(c.greet())   # Hello from Child
```

The child’s `greet` has **overridden** the parent’s.
The parent object still uses its original method.

> 💡 **INSIGHT:** Overriding is the primary way to
> specialise behaviour in child classes.

---

## 🧱 BRICK 2 – Extending a Method with `super()`

Often you don’t want to replace the parent method entirely —
you want to **add** behaviour while still running the parent’s
original code. Use `super().method()` to call the parent’s
version.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        return f"{self.name} earns {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def details(self):
        base = super().details()
        return f"{base}, manages {self.department}"
```

Now `Manager.details()` builds on top of
`Employee.details()` instead of rewriting it
from scratch.

> ⚠️ **WARNING:** Forgetting to call `super()` in
> `__init__` when the parent does important setup
> can cause subtle bugs — always call it when you
> override the constructor.

---

## 📌 Key Takeaway
- Override: define a method with the same name in the child.
- The child version replaces the parent version for that class.
- Use `super().method()` to call the parent’s version.
- Perfect for extending behaviour, not just replacing it.