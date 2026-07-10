# 📘 PyPhone Emperor v3.0 · Module 8
# 📖 L‑47 – `@property`, Setters & Getters

---

## 🎯 OBJECTIVE — What You Will Master

> Control attribute access with clean, Pythonic syntax.

- 🔒 **`@property`** – turn a method into a read‑only attribute
- ✏️ **`@name.setter`** – add write access with validation
- 🧹 **`@name.deleter`** – intercept deletion of the property
- 🧪 **Why properties** – encapsulation without ugly getter/setter methods

---

## 🧱 READ‑ONLY PROPERTY

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

c = Circle(5)
print(c.diameter)   # 10
# c.diameter = 20   # AttributeError: can't set attribute
```

---

## 🧱 PROPERTY WITH SETTER

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

c = Circle(5)
c.radius = 10   # uses setter
print(c.radius) # 10
```

---

## 💡 Real‑world Usage

**Banking – balance validation**
```python
class Account:
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount
```

**E‑commerce – discount price**
```python
class Product:
    @property
    def final_price(self):
        return self.price * (1 - self.discount)
```

**Logistics – dimensional weight**
```python
class Package:
    @property
    def dim_weight(self):
        return (self.l * self.w * self.h) / 5000
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Define a `@property` that computes `diameter` from `radius`. |
| Medium | Add a setter that validates the radius is positive. |
| Hard | Compute `fahrenheit` from `celsius` using a property. |

Run the coach:
```bash
python ii_Practice_Sheets/L47_property_Setters_Getters.py
```

---

## 📌 Key Takeaway
- `@property` makes methods look like attributes.
- Setters enable validation without changing the interface.
- Encapsulation keeps your data safe and your API clean.

*For Emperor.*