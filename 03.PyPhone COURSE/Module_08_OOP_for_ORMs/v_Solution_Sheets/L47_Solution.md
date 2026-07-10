# L47 Solution – @property, Setters & Getters

## 🟢 Easy 1 – Read‑Only Property
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius
c = Circle(5)
print(c.diameter)
```

## 🟢 Easy 2 – Fahrenheit Property
```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    @property
    def fahrenheit(self):
        return self.celsius * 9/5 + 32
t = Temperature(0)
print(t.fahrenheit)
```

## 🟡 Medium 1 – Setter for Radius
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError('Positive only')
        self._radius = value
    @property
    def diameter(self):
        return 2 * self._radius
c = Circle(5)
c.radius = 10
print(c.diameter)
```

## 🟡 Medium 2 – Setter for Celsius
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self, value):
        self._celsius = value
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
t = Temperature(0)
t.celsius = 100
print(t.fahrenheit)
```

## 🔴 Hard 1 – Bank Account Property
```python
class Account:
    def __init__(self, balance):
        self._balance = balance
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError('Negative not allowed')
        self._balance = amount
acc = Account(100)
acc.balance = 200
print(acc.balance)
```

## 🔴 Hard 2 – Password Validation with Property
```python
class User:
    def __init__(self):
        self._password = ''
    @property
    def password(self):
        return '****'
    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise ValueError('Too short')
        self._password = value
u = User()
u.password = 'secure123'
print('Set')
```