# L41 Solution – Classes, Objects & __init__

## 🟢 Easy 1 – Define a Simple Class
```python
class Dog:
    def bark(self):
        print('Woof!')
d = Dog()
d.bark()
```

## 🟢 Easy 2 – Class with __init__
```python
class Cat:
    def __init__(self, name):
        self.name = name
c = Cat('Whiskers')
print(c.name)
```

## 🟡 Medium 1 – Book Class with Two Attributes
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
b = Book('1984', 'Orwell')
print(b.title, b.author)
```

## 🟡 Medium 2 – Bank Account Class
```python
class BankAccount:
    def __init__(self):
        self.balance = 0
acc = BankAccount()
print(acc.balance)
```

## 🔴 Hard 1 – Product Class with Validation
```python
class Product:
    def __init__(self, name, price):
        if price <= 0:
            raise ValueError('Price must be positive')
        self.name = name
        self.price = price
p = Product('Widget', 10)
print(p.name)
```

## 🔴 Hard 2 – User with Default Values
```python
class User:
    def __init__(self, name, active=True):
        self.name = name
        self.active = active
u = User('Emperor')
print(u.active)
```