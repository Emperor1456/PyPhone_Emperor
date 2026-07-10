# 📘 PyPhone Emperor v3.0 · Module 8
# 📖 L‑43 – Class Variables vs Instance Variables

---

## 🎯 OBJECTIVE — What You Will Master

> Share data across all instances, or keep it unique per object.

- 🌐 **Class variable** – defined in the class body, shared by all instances
- 🧍 **Instance variable** – defined with `self.`, unique per object
- ⚠️ **Shadowing** – an instance variable can hide a class variable
- 🧪 **Use cases** – constants, counters, default values

---

## 🧱 CLASS VARIABLES

```python
class Employee:
    company = "PyPhone Corp"   # class variable

    def __init__(self, name):
        self.name = name       # instance variable

e1 = Employee("Emperor")
e2 = Employee("Rahim")
print(e1.company)   # PyPhone Corp
print(e2.company)   # PyPhone Corp
```

Change the class variable through the **class**, not an instance:

```python
Employee.company = "New Corp"
print(e1.company)   # New Corp
print(e2.company)   # New Corp
```

---

## 🧱 INSTANCE SHADOWING

If you assign to `self.company`, you create a **new instance variable** that hides the class variable for that specific object.

```python
e1.company = "Freelance"
print(e1.company)          # Freelance (instance)
print(e2.company)          # New Corp (class)
print(Employee.company)    # New Corp
```

> ⚠️ **WARNING:** Reading via `instance.attr` checks the instance first, then the class. Writing always creates an instance variable.

---

## 💡 Real‑world Usage

**Banking – shared interest rate**
```python
class SavingsAccount:
    rate = 0.05   # class variable
    def __init__(self, balance):
        self.balance = balance
```

**E‑commerce – default currency**
```python
class Product:
    currency = "USD"
    def __init__(self, name, price):
        self.name = name
        self.price = price
```

**Logistics – max weight for all packages**
```python
class Package:
    max_weight = 50
    def __init__(self, weight):
        if weight > Package.max_weight:
            raise ValueError("Overweight")
        self.weight = weight
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Define a class with a class variable and print it via the class name. |
| Medium | Create two instances and print the shared class variable from both. |
| Hard | Create an instance that shadows the class variable with its own value and print both. |

Run the coach:
```bash
python ii_Practice_Sheets/L43_Class_vs_Instance_Variables.py
```

---

## 📌 Key Takeaway
- Class variables are shared; instance variables are unique.
- Reading through an instance searches instance → class.
- Assigning via `self.` creates an instance variable, even if a class variable exists.

*For Emperor.*