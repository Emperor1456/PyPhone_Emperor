# 📘 Module 08 – OOP for ORMs · Revision Note

---

## L41 – Classes, Objects & `__init__`
- `class Name:` defines a blueprint; `obj = Name()` creates an instance.
- `__init__(self, ...)` initialises attributes.
- `self` refers to the current instance.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
```

---

## L42 – Instance Methods & `self`
- Methods are functions inside a class; first parameter always `self`.
- Access instance attributes with `self.attr`.
- Mutators modify state; accessors return information.

```python
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
```

---

## L43 – Class Variables vs Instance Variables
- Class variable: defined in the class body, shared by all instances.
- Instance variable: defined with `self.`, unique to each object.
- Instance variable shadows class variable if same name is used.

```python
class Employee:
    company = "PyPhone"   # class variable
    def __init__(self, name):
        self.name = name  # instance variable
```

---

## L44 – Inheritance & `super()`
- `class Child(Parent):` inherits all methods and attributes.
- Child can override or extend parent methods.
- `super().__init__(...)` calls the parent constructor.

```python
class Animal:
    def speak(self): return "?"
class Dog(Animal):
    def speak(self): return "Woof"
```

---

## L45 – Method Overriding & Polymorphism
- Overriding replaces a parent method with a child’s version.
- Polymorphism: different classes respond to the same method call.
- Duck typing: "if it quacks like a duck, treat it like a duck."

```python
def make_sound(animal):
    print(animal.speak())
```

---

## L46 – Special Methods (`__str__`, `__repr__`, `__len__`)
- `__str__` – user‑friendly string (for `print()`).
- `__repr__` – developer‑focused representation.
- `__len__` – enables `len(obj)`.
- `__eq__`, `__add__` – operator overloading.

```python
class Book:
    def __str__(self): return f"{self.title} by {self.author}"
    def __len__(self): return 1
```

---

## L47 – `@property`, Setters & Getters
- `@property` turns a method into a read‑only attribute.
- `@name.setter` adds write access with validation.
- Encapsulation without ugly getter/setter boilerplate.

```python
class Circle:
    def __init__(self, radius): self._radius = radius
    @property
    def diameter(self): return 2 * self._radius
```

---

## L48 – `Enum` – Database Constants
- `Enum` creates a fixed set of symbolic names for values.
- Prevents typos and invalid values.
- Enums map directly to database column constraints.

```python
from enum import Enum
class Status(Enum):
    PENDING = 1
    ACTIVE = 2
```

---

*Quick Test:*  
- What is `self`?  
- How to call a parent method from a child?  
- Class variable vs instance variable?  
- When to use `@property`?