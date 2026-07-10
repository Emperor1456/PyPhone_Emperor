# L42 Solution – Instance Methods, self & State

## 🟢 Easy 1 – Dog with speak method
```python
class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return 'Woof! I am ' + self.name
d = Dog('Rex')
print(d.speak())
```

## 🟢 Easy 2 – Counter with increment
```python
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
c = Counter()
c.increment()
print(c.count)
```

## 🟡 Medium 1 – Calculator with add method
```python
class Calculator:
    def add(self, a, b):
        return a + b
calc = Calculator()
print(calc.add(3, 5))
```

## 🟡 Medium 2 – Bank Account with deposit
```python
class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
acc = BankAccount()
acc.deposit(100)
print(acc.balance)
```

## 🔴 Hard 1 – Safe Withdrawal
```python
class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('Insufficient')
acc = BankAccount()
acc.deposit(100)
acc.withdraw(150)
print(acc.balance)
```

## 🔴 Hard 2 – Stats Tracker
```python
class Stats:
    def __init__(self):
        self.numbers = []
    def add(self, num):
        self.numbers.append(num)
    def average(self):
        return sum(self.numbers)/len(self.numbers) if self.numbers else 0
s = Stats()
s.add(10); s.add(20); s.add(30)
print(s.average())
```