# 📘 PyPhone Emperor · Module 7
# 📖 L‑55 – Inheritance (Parent & Child Classes)

---

## 🎯 OBJECTIVE
Learn to create new classes based on existing ones
using **inheritance**. The child class automatically
receives all attributes and methods of the parent,
allowing you to reuse, extend, or modify behaviour
without rewriting code.

---

## 🧱 BRICK 1 – Basic Inheritance

To inherit, put the parent class name in parentheses
after the child class name.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    pass   # Dog inherits everything from Animal

d = Dog("Buddy")
print(d.name)      # Buddy
print(d.speak())   # Some sound
```

Here `Dog` is the **child** (subclass) and `Animal` is
the **parent** (superclass). `Dog` automatically has
`__init__` and `speak` without defining them.

> 💡 **INSIGHT:** Inheritance models an **"is‑a"**
> relationship – a Dog is an Animal.

---

## 🧱 BRICK 2 – Adding and Overriding in Child

The child can add new methods or override existing
ones by redefining them.

```python
class Cat(Animal):
    def speak(self):
        return "Meow"          # override

    def purr(self):
        return "Purrr"         # new method
```

If the child overrides `__init__`, it can still
call the parent's `__init__` via `super()`.

```python
class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)   # call parent __init__
        self.can_fly = can_fly
```

`super()` gives access to the parent class,
letting you reuse its logic seamlessly.

> ⚠️ **WARNING:** Python supports multiple inheritance
> (`class C(A, B)`). Use with caution – the method
> resolution order (MRO) can become complex.

---

## 📌 Key Takeaway
- `class Child(Parent):` inherits all methods and attributes.
- Child can add new methods or override existing ones.
- `super().__init__(...)` calls the parent constructor.
- Inheritance promotes code reuse and logical hierarchy.