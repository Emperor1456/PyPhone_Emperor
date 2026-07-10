# L44 Solution – Inheritance & super()

## 🟢 Easy 1 – Simple Inheritance
```python
class Animal:
    def speak(self):
        return '?'
class Dog(Animal):
    def speak(self):
        return 'Woof'
d = Dog()
print(d.speak())
```

## 🟢 Easy 2 – Another Child
```python
class Animal:
    def speak(self):
        return '?'
class Cat(Animal):
    def speak(self):
        return 'Meow'
c = Cat()
print(c.speak())
```

## 🟡 Medium 1 – Child Without Override
```python
class Animal:
    def speak(self):
        return '?'
class Bird(Animal):
    pass
b = Bird()
print(b.speak())
```

## 🟡 Medium 2 – Using super().__init__
```python
class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
d = Dog('Rex')
print(d.name)
```

## 🔴 Hard 1 – Account Hierarchy
```python
class Account:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
class SavingsAccount(Account):
    def __init__(self, id, balance, rate):
        super().__init__(id, balance)
        self.rate = rate
sa = SavingsAccount('A1', 1000, 0.05)
print(sa.balance)
```

## 🔴 Hard 2 – Method Override with super()
```python
class Employee:
    def info(self):
        return 'Employee'
class Manager(Employee):
    def info(self):
        return super().info() + ' Manager'
m = Manager()
print(m.info())
```