# 📘 PyPhone Emperor · Module 7
# 📖 L‑54 – Class Variables vs Instance Variables

---

## 🎯 OBJECTIVE
Learn the difference between **class variables**
(shared by all objects of a class) and **instance
variables** (unique to each object). Understanding
this distinction is critical for designing clean,
memory‑efficient classes.

---

## 🧱 BRICK 1 – Class Variables

A class variable is defined directly inside the
class body, outside any method. It belongs to the
class itself, not to any particular instance.
All instances share the **same** class variable.

```python
class Employee:
    company = "PyPhone Corp"   # class variable

    def __init__(self, name):
        self.name = name       # instance variable

e1 = Employee("Emperor")
e2 = Employee("Guest")

print(e1.company)   # PyPhone Corp
print(e2.company)   # PyPhone Corp
```

Changing a class variable through the **class**
affects all instances that haven't overridden it:

```python
Employee.company = "New Corp"
print(e1.company)   # New Corp
print(e2.company)   # New Corp
```

> 💡 **INSIGHT:** Class variables are perfect for
> constants, default settings, or counters that
> should be shared across all instances.

---

## 🧱 BRICK 2 – Instance Variables and Shadowing

Instance variables are created with `self.` inside
methods (usually `__init__`). Each object gets its
own copy, independent of other objects.

If you assign to `self.company` on an instance,
you **shadow** the class variable — a new instance
variable is created that hides the class one for
that specific object.

```python
e1.company = "Freelance"      # creates instance variable
print(e1.company)             # Freelance  (instance)
print(e2.company)             # New Corp   (class variable still)
print(Employee.company)       # New Corp
```

Now `e1` has its own `company`, while `e2` still
accesses the class variable.

> ⚠️ **WARNING:** Reading a variable via `self.`
> checks the instance first, then the class. Writing
> always creates an instance variable, even if a
> class variable with the same name exists.

---

## 📌 Key Takeaway
- Class variables are shared; defined without `self.`
- Instance variables are unique per object; defined
  with `self.` inside methods.
- `obj.attr` reads instance first, then class.
- Assignment via `obj.attr` creates/overwrites an
  instance variable, leaving the class variable intact.