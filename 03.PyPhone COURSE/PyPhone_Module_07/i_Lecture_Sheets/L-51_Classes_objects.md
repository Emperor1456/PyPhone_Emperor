# 📘 PyPhone Emperor · Module 7
# 📖 L‑51 – Classes & Objects

---

## 🎯 OBJECTIVE
Learn to define your own **classes** and create
**objects** from them. A class is a blueprint —
an object is a concrete instance built from that
blueprint. This is the foundation of
Object‑Oriented Programming.

---

## 🧱 BRICK 1 – Defining a Class

A class is defined with the `class` keyword, a name
(by convention `PascalCase`), and a colon. Inside,
you write **methods** — functions that belong to
the class.

```python
class User:
    """A simple user account."""
    pass   # placeholder for an empty class
```

You create an **object** (instance) by calling the
class like a function:

```python
u1 = User()
u2 = User()
print(type(u1))   # <class '__main__.User'>
```

Every object is independent — `u1` and `u2` are two
distinct instances of the same class.

---

## 🧱 BRICK 2 – Adding Attributes

You can attach data directly to instances using
dot notation, even without a constructor.

```python
u1.name = "Emperor"
u1.age = 18

u2.name = "Guest"
u2.age = 25

print(u1.name)   # Emperor
print(u2.name)   # Guest
```

However, this is ad‑hoc and error‑prone. In L‑52
you'll learn `__init__` to properly initialise
objects at creation time.

> 💡 **INSIGHT:** A class is a **type**. When you write
> `int`, `str`, `list`, you're using built‑in classes.
> Now you're building your own.

---

## 📌 Key Takeaway
- `class Name:` defines a new type.
- `Name()` creates an instance (object) of that class.
- Objects can hold their own data via attributes.
- Classes let you model real‑world entities in code.