# 📘 PyPhone Emperor · Module 7
# 📖 L‑52 – `__init__` Method (Constructor)

---

## 🎯 OBJECTIVE
Learn to initialise objects automatically at the
moment of creation using the special `__init__` method.
This is the constructor — it runs every time a new
instance is born, setting up its initial state.

---

## 🧱 BRICK 1 – The `__init__` Method

`__init__` is a method you define inside the class.
It must have `self` as its first parameter, followed
by any other parameters you want to pass when
creating the object.

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

When you call `User("Emperor", 18)`, Python:
① Creates an empty `User` object.
② Calls `__init__` on that object, passing `"Emperor"`
   and `18` as arguments.
③ `self.name = name` attaches the name to the instance.
④ The fully initialised object is returned.

```python
u1 = User("Emperor", 18)
print(u1.name)   # Emperor
print(u1.age)    # 18
```

> 💡 **INSIGHT:** `__init__` is not the "first" method
> called — the object is created first, then `__init__`
> customises it. The actual constructor is `__new__`,
> which you rarely need to touch.

---

## 🧱 BRICK 2 – Setting Defaults in `__init__`

You can provide default values for parameters,
making them optional when creating objects.

```python
class User:
    def __init__(self, name, age=18, active=True):
        self.name = name
        self.age = age
        self.active = active

u1 = User("Emperor")                    # uses defaults
u2 = User("Guest", 25, False)           # overrides all
```

This is the standard way to create flexible,
production‑ready classes. Every instance gets a
predictable set of attributes, which eliminates
the ad‑hoc attribute assignment from L‑51.

> ⚠️ **WARNING:** Never use mutable default values like
> `def __init__(self, items=[])`. Use `None` and create
> the mutable object inside, just as you learned with
> default parameters in functions.

---

## 📌 Key Takeaway
- `__init__(self, ...)` initialises new objects.
- `self` refers to the specific instance being created.
- Parameters passed to `Class(...)` go to `__init__`.
- Use default values for optional attributes.