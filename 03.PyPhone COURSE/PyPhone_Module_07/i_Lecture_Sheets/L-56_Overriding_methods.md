# 📘 PyPhone Emperor · Module 7  
# 📖 L‑56 – Overriding Methods (Tailoring Parent Behaviour)

---

## 🎯 OBJECTIVE  
Master **method overriding** — redefining a parent class method in the child to specialise its behaviour. Combine with `super()` to extend instead of replace. This is how you build flexible, layered business logic.

---

## 🧱 BRICK 1 – Simple Override (Replacement)

**① Child overrides parent (Easy practice)**
```python
class Parent:
    def show(self):
        return 'Parent'

class Child(Parent):
    def show(self):
        return 'Child'

c = Child()
print(c.show())   # 'Child'
```
The child completely replaces the parent's `show`.

**② Grandchild inherits overridden method (Medium practice)**
```python
class GrandChild(Child):
    pass

gc = GrandChild()
print(gc.show())   # 'Child' — inherits Child's version
```
`GrandChild` doesn't define `show`, so it uses the one from `Child`.

**③ Grandchild overrides again (Hard practice)**
```python
class GrandChild(Child):
    def show(self):
        return 'GrandChild'

gc = GrandChild()
print(gc.show())   # 'GrandChild'
```
Now `GrandChild` replaces `show` yet again.

> 💡 **INSIGHT:** Overriding is the primary way to specialise behaviour in a class hierarchy. Each level can refine or completely change what a method does.

---

## 🧱 BRICK 2 – Extending with `super()`

Often you want to **add** to the parent's behaviour, not replace it entirely.

**④ Extending a greeting**
```python
class Person:
    def greet(self):
        return 'Hello'

class Employee(Person):
    def greet(self):
        return super().greet() + ', welcome to the team!'

e = Employee()
print(e.greet())   # 'Hello, welcome to the team!'
```

**⑤ Financial instrument – base tax calculation, overridden with surcharge**
```python
class Transaction:
    def tax(self, amount):
        return amount * 0.05

class InternationalTransaction(Transaction):
    def tax(self, amount):
        base = super().tax(amount)
        return base + amount * 0.02   # additional surcharge
```

> ⚠️ **WARNING:** If you override `__init__`, call `super().__init__()` unless you intentionally want to skip the parent's setup — skipping it often leads to missing attributes.

> 💡 **ADVANCED TIP – Abstract methods:** Use `@abstractmethod` from `abc` to force children to override specific methods. This is the design‑by‑contract pattern.

---

## 💡 Real‑world Usage

**Banking – different fee calculations**
```python
class Account:
    def monthly_fee(self):
        return 5

class PremiumAccount(Account):
    def monthly_fee(self):
        return 0   # premium accounts have no fee
```

**E‑commerce – shipping for different regions**
```python
class Shipping:
    def cost(self, weight):
        return weight * 10

class InternationalShipping(Shipping):
    def cost(self, weight):
        return super().cost(weight) * 1.5   # 50% extra
```

**Logistics – vehicle fuel calculation**
```python
class Vehicle:
    def fuel_needed(self, distance):
        return distance / 10

class Truck(Vehicle):
    def fuel_needed(self, distance):
        return super().fuel_needed(distance) * 1.2   # 20% more fuel
```

**HR – manager role overrides employee**
```python
class Employee:
    def role(self):
        return 'Staff'

class Manager(Employee):
    def role(self):
        return 'Manager'
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Define `Parent` with method `show` returning `'Parent'`. Define `Child(Parent)` overriding `show` to return `'Child'`. Create instance `c` and print `c.show()`. | `Child` |
| Medium | Create `GrandChild(Child)` without overriding. Print `show()` – should return `'Child'`. | `Child` |
| Hard   | Override `show` in `GrandChild` to return `'GrandChild'`. Print the result. | `GrandChild` |

Run the coach:
```bash
python ii_Practice_Sheets/L-56_Overriding_Methods.py
```

---

## 📌 Key Takeaway
- Override: define a method with the same name in the child.
- The child version replaces the parent version for that class.
- `super().method()` calls the parent's version — use it to extend behaviour.
- Each level in the hierarchy can refine or replace methods.