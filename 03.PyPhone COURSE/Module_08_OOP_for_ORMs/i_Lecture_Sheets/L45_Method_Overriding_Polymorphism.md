# 📘 PyPhone Emperor v3.0 · Module 8
# 📖 L‑45 – Method Overriding & Polymorphism

---

## 🎯 OBJECTIVE — What You Will Master

> Same interface, different behaviour — the heart of flexible design.

- 🧬 **Overriding** – child replaces a parent's method entirely
- 🎭 **Polymorphism** – different classes respond to the same method call
- 🧪 **Duck typing** – "if it quacks like a duck, it's a duck"
- 🧱 **Business context** – processing different payment types, notifications

---

## 🧱 OVERRIDING A METHOD

```python
class Payment:
    def process(self):
        return "Processing generic payment"

class CreditCard(Payment):
    def process(self):
        return "Processing credit card payment"

class PayPal(Payment):
    def process(self):
        return "Processing PayPal payment"
```

Each subclass provides its own implementation of `process()`.

---

## 🧱 POLYMORPHISM IN ACTION

```python
def handle_payment(payment: Payment):
    print(payment.process())

handle_payment(CreditCard())   # Processing credit card payment
handle_payment(PayPal())       # Processing PayPal payment
```

The same function works with any `Payment` subclass — no changes needed.

---

## 💡 Real‑world Usage

**Banking – transaction types**
```python
class Transfer:
    def execute(self): return "Transferring funds"

class Withdrawal:
    def execute(self): return "Dispensing cash"
```

**E‑commerce – shipping methods**
```python
class StandardShipping:
    def cost(self, weight): return weight * 5

class ExpressShipping:
    def cost(self, weight): return weight * 10
```

**Logistics – vehicle routing**
```python
class Truck:
    def deliver(self): return "Road delivery"

class Drone:
    def deliver(self): return "Air delivery"
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Override a parent method in a child class and print the child's result. |
| Medium | Create a list of different objects and call the same method on each. |
| Hard | Write a function that accepts any object with a specific method and calls it. |

Run the coach:
```bash
python ii_Practice_Sheets/L45_Method_Overriding_Polymorphism.py
```

---

## 📌 Key Takeaway
- Overriding replaces a parent method with a child's version.
- Polymorphism lets you write code that works with any class sharing an interface.
- This is the foundation of plugin systems and interchangeable components.

*For Emperor.*