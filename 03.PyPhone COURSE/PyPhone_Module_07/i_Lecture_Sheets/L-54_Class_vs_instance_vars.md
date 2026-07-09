# 📘 PyPhone Emperor · Module 7  
# 📖 L‑54 – Class Variables vs Instance Variables (Shared vs Unique Data)

---

## 🎯 OBJECTIVE  
Master the distinction between **class variables** (shared across all instances) and **instance variables** (unique per object). Use class variables for constants, defaults, and counters; instance variables for per‑object state.

---

## 🧱 BRICK 1 – Class Variables

Define a variable directly inside the class body, outside any method. It belongs to the class, and all instances see the same value.

```python
class Employee:
    company = 'PyPhone'

print(Employee.company)   # 'PyPhone'
```

**① Shared company name (Easy practice)**
```python
class Employee:
    company = 'PyPhone'

print(Employee.company)   # PyPhone
```
Access through the class or through any instance — the value is the same.

**② Two instances share the class variable (Medium practice)**
```python
e1 = Employee()
e2 = Employee()
print(e1.company, e2.company)   # PyPhone PyPhone
```
Both `e1` and `e2` see `'PyPhone'` because they read the class variable.

**③ Car with class variable for wheels (Hard practice)**
```python
class Car:
    wheels = 4

c = Car()
print(c.wheels)   # 4
```

> 💡 **INSIGHT:** Class variables are stored on the class object, not on each instance. This saves memory and ensures consistency.

---

## 🧱 BRICK 2 – Instance Variables and Shadowing

Instance variables are created inside methods using `self.attr`. If an instance variable has the same name as a class variable, it **shadows** (hides) the class variable for that instance.

**④ Instance variable shadows class variable**
```python
class Employee:
    company = 'PyPhone'

e1 = Employee()
e1.company = 'Freelance'         # creates instance variable
print(e1.company)                # 'Freelance' (instance)
print(Employee.company)          # 'PyPhone' (class unchanged)
```

**⑤ Modifying class variable through the class**
```python
Employee.company = 'NewCorp'
print(e2.company)   # 'NewCorp' — all instances see the change unless they have their own instance variable
```

> ⚠️ **WARNING:** Reading `obj.attr` checks the instance first, then the class. Writing always creates an instance variable, even if a class variable with that name exists.

> 💡 **ADVANCED TIP – Shared counters:** Use a class variable as a counter for all instances: increment it in `__init__` via `ClassName.counter += 1`.

---

## 💡 Real‑world Usage

**Banking – interest rate as class variable**
```python
class SavingsAccount:
    interest_rate = 0.05

    def __init__(self, balance):
        self.balance = balance

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
```

**E‑commerce – default currency**
```python
class Product:
    currency = 'USD'

    def __init__(self, name, price):
        self.name = name
        self.price = price

print(Product.currency)   # 'USD'
```

**Logistics – max weight for all packages**
```python
class Package:
    max_weight = 50   # kg

    def __init__(self, weight):
        if weight > Package.max_weight:
            raise ValueError('Overweight')
        self.weight = weight
```

**HR – company policy shared across employees**
```python
class Employee:
    company = 'PyPhone Corp'
    vacation_days = 20

e = Employee()
print(e.vacation_days)   # 20
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Define `Employee` with class variable `company='PyPhone'`. Print `Employee.company`. | `PyPhone` |
| Medium | Create two Employee instances and print both share the same `company` value. | `PyPhone PyPhone` |
| Hard   | Define `Car` with class variable `wheels=4`. Create instance `c` and print `c.wheels`. | `4` |

Run the coach:
```bash
python ii_Practice_Sheets/L-54_Class_vs_Instance_Variables.py
```

---

## 📌 Key Takeaway
- Class variable: defined outside methods, shared by all instances.
- Instance variable: defined with `self.` inside methods, unique per object.
- Access via `Class.var` or `instance.var`; write creates an instance variable.
- Use class variables for constants, defaults, and shared data.