# 📘 PyPhone Emperor · Module 7  
# 🗃️ Comprehensive Note – Object‑Oriented Programming (OOP)

---

## 🎯 Scope
This note covers the full OOP toolkit from Module 7: classes, objects, the `__init__` constructor, instance methods and `self`, class vs instance variables, inheritance, method overriding, special methods (`__str__`, `__repr__`, `__len__`), and property decorators (`@property`, `@setter`).  
All code fits a phone screen; no sideways scrolling.

---

## 🧱 1. Classes and Objects
A **class** is a blueprint for creating objects.  
An **object** (instance) is a concrete entity built from the class.

```python
class User:
    pass          # empty class placeholder

u1 = User()       # instantiate an object
u2 = User()
```

You can attach **attributes** to instances with dot notation, but the proper way is via `__init__`.

---

## 🧱 2. The `__init__` Constructor
`__init__` is a special method that runs automatically when a new object is created.  
It initializes instance attributes using the `self` reference.

```python
class User:
    def __init__(self, name, age):
        self.name = name   # instance variable
        self.age = age

u1 = User("Emperor", 18)
print(u1.name, u1.age)     # Emperor 18
```

- `self` must be the first parameter.
- **Never** use mutable default arguments like `def __init__(self, items=[])`.  
  Use `None` and create the object inside the method.

---

## 🧱 3. Instance Methods & `self`
An **instance method** is a function defined inside a class.  
It always has `self` as its first parameter, giving access to instance data.

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
```

- **Accessor** methods only read data; **mutator** methods modify it.
- Without `self.`, you’re working with a local variable, not an attribute.

---

## 🧱 4. Class Variables vs Instance Variables
- **Class variable**: defined directly inside the class body, shared by all instances.
- **Instance variable**: defined with `self.` inside methods, unique to each object.

```python
class Employee:
    company = "PyPhone"        # class variable

    def __init__(self, name):
        self.name = name        # instance variable

e1 = Employee("Emperor")
e2 = Employee("Guest")

print(e1.company)   # PyPhone
print(e2.company)   # PyPhone

Employee.company = "New Corp"   # change class variable for all
print(e1.company, e2.company)   # New Corp New Corp

e1.company = "Freelance"        # creates instance variable, shadows class variable
print(e1.company, e2.company)   # Freelance New Corp
```

---

## 🧱 5. Inheritance (Parent & Child Classes)
A child class **inherits** all attributes and methods from a parent class.  
Use `class Child(Parent):` syntax.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    pass                        # Dog inherits everything

d = Dog("Buddy")
print(d.name)        # Buddy
print(d.speak())     # Some sound
```

### Adding or Overriding in Child
- **Override** a method by redefining it with the same name in the child.
- **Call the parent’s version** with `super()`.

```python
class Cat(Animal):
    def speak(self):
        return "Meow"

class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)       # call parent __init__
        self.can_fly = can_fly
```

---

## 🧱 6. Method Overriding
When a child provides its own version of a method, that method **overrides** the parent’s.  
Use `super().method()` to **extend** the parent behaviour instead of replacing it entirely.

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

---

## 🧱 7. Special Methods (Dunder Methods)
Special methods let your objects work with built‑in Python operators and functions.

- `__str__(self)` – called by `print()` and `str()`. Returns a human‑readable string.
- `__repr__(self)` – called by `repr()` and in the interactive shell. Returns an unambiguous representation, ideally code to recreate the object.
- `__len__(self)` – called by `len()`. Returns a custom length.
- `__eq__(self, other)` – called by `==`. Defines equality.
- `__add__(self, other)` – called by `+`. Defines addition.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (${self.price:.2f})"

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

p = Product("Laptop", 799.99)
print(str(p))      # Laptop ($799.99)
print(repr(p))     # Product('Laptop', 799.99)
```

If `__str__` is not defined, Python falls back to `__repr__`.

---

## 🧱 8. Property Decorators (`@property`)
Properties allow you to manage attribute access with getter, setter, and deleter methods, while still using simple `obj.attr` syntax.

### Read‑only Property
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

c = Circle(5)
print(c.diameter)   # 10   (no parentheses!)
```

### Getter & Setter (Controlled Access)
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius    # internal attribute (protected)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

c = Circle(5)
c.radius = 10        # setter is called
print(c.radius)      # getter is called
```

- Use `@property` for computed attributes or to add validation.
- The internal attribute `_radius` is a convention to signal “protected” (not enforced by Python).

---

## 💡 Quick Reference
```python
# Class & Object
class MyClass:
    class_var = "shared"

    def __init__(self, param):
        self.inst_var = param

    def method(self):
        return self.inst_var

# Inheritance
class Child(Parent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# Special methods
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self): return f"({self.x},{self.y})"
    def __repr__(self): return f"Point({self.x},{self.y})"
    def __len__(self): return 2   # arbitrary
    def __eq__(self, o): return self.x == o.x and self.y == o.y
    def __add__(self, o): return Point(self.x+o.x, self.y+o.y)

# Property
class Circle:
    def __init__(self, r):
        self._r = r
    @property
    def radius(self):
        return self._r
    @radius.setter
    def radius(self, val):
        if val < 0: raise ValueError
        self._r = val
```

---

## 📌 Key Takeaway
- A **class** is a template; an **object** is an instance of that template.
- `__init__` sets up initial instance state – always use `self` to store attributes.
- Instance methods receive `self`; they can read or modify instance data.
- **Class variables** are shared; **instance variables** are unique per object.
- **Inheritance** models “is‑a” relationships; use `super()` to call parent methods.
- **Special methods** (`__str__`, `__len__`, `__eq__`) integrate your objects with Python’s built‑in behaviour.
- **Properties** (`@property` and `@setter`) provide controlled attribute access without changing the public API.

*Study this sheet. Recall it from memory. Then practice.*