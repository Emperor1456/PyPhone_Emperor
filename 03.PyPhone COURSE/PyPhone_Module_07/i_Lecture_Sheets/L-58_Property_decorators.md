# 📘 PyPhone Emperor · Module 7  
# 📖 L‑58 – Property Decorators (`@property`) – Controlled Attribute Access

---

## 🎯 OBJECTIVE  
Master `@property` to create methods that behave like read‑only attributes, and `@name.setter` to add controlled write access. Properties keep the simple `obj.attr` syntax while enabling validation, computed values, and data hiding.

---

## 🧱 BRICK 1 – Read‑only Properties

Decorate a method with `@property` to make it accessible without parentheses, like a data attribute.

**① Circle diameter from radius (Easy practice)**
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
print(c.diameter)   # 10  (not c.diameter())
```
`diameter` is computed live from `radius`; no parentheses needed.

**② Temperature conversion to Fahrenheit (Medium practice)**
```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

t = Temperature(0)
print(t.fahrenheit)   # 32.0
```

**③ Same property at a different temperature (Hard practice)**
```python
t = Temperature(100)
print(t.fahrenheit)   # 212.0
```

> 💡 **INSIGHT:** Properties give you the best of both worlds: the clean syntax of attributes with the flexibility of methods. Later you can add validation without changing external code.

---

## 🧱 BRICK 2 – Setters for Controlled Write Access

Add `@name.setter` to allow assignment with validation.

**④ Radius with validation**
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius   # internal storage

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Radius cannot be negative')
        self._radius = value

c = Circle(5)
c.radius = 10      # uses setter
print(c.radius)    # 10
```

**⑤ Bank account with balance validation**
```python
class Account:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError('Balance cannot be negative')
        self._balance = amount
```

> ⚠️ **WARNING:** The internal attribute naming convention `_name` signals "protected". It's not enforced by Python, but it's a strong convention. Properties let you change the internal representation later without affecting external code.

> 💡 **ADVANCED TIP – Deleter:** Add `@name.deleter` to intercept `del obj.attr` for cleanup logic.

---

## 💡 Real‑world Usage

**Banking – account status derived from balance**
```python
class Account:
    def __init__(self, balance):
        self.balance = balance

    @property
    def is_overdrawn(self):
        return self.balance < 0

acc = Account(-50)
print(acc.is_overdrawn)   # True
```

**E‑commerce – product discount price**
```python
class Product:
    def __init__(self, price, discount=0):
        self.price = price
        self.discount = discount

    @property
    def final_price(self):
        return self.price * (1 - self.discount)

p = Product(100, 0.2)
print(p.final_price)   # 80.0
```

**Logistics – package dimensional weight**
```python
class Package:
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h

    @property
    def dim_weight(self):
        return (self.l * self.w * self.h) / 5000

p = Package(50, 40, 30)
print(p.dim_weight)   # 12.0
```

**HR – full name from first and last**
```python
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

e = Employee('Emperor', 'PyPhone')
print(e.full_name)   # Emperor PyPhone
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Define `Circle` with `__init__(radius)` and `@property` `diameter` returning `2*radius`. Create `c` with radius=5 and print `c.diameter`. | `10` |
| Medium | Define `Temperature` with `__init__(celsius)` and `@property` `fahrenheit` returning `celsius*9/5+32`. Create `t` with celsius=0 and print `t.fahrenheit`. | `32.0` |
| Hard   | Using same Temperature class, create instance with celsius=100 and print fahrenheit. | `212.0` |

Run the coach:
```bash
python ii_Practice_Sheets/L-58_Property_Decorators.py
```

---

## 📌 Key Takeaway
- `@property` turns a method into a read‑only attribute.
- `@name.setter` adds write access with optional validation.
- Properties preserve the clean `obj.attr` interface.
- Use them for computed values, validation, and future‑proofing attribute access.