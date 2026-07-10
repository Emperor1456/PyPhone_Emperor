# L43 Solution – Class Variables vs Instance Variables

## 🟢 Easy 1 – Class Variable
```python
class Employee:
    company = 'PyPhone'
print(Employee.company)
```

## 🟢 Easy 2 – Two Instances Share Class Var
```python
class Employee:
    company = 'PyPhone'
e1 = Employee(); e2 = Employee()
print(e1.company, e2.company)
```

## 🟡 Medium 1 – Class Variable with Instance
```python
class Car:
    wheels = 4
c = Car()
print(c.wheels)
```

## 🟡 Medium 2 – Shadow Class Variable
```python
class Employee:
    company = 'PyPhone'
e1 = Employee()
e1.company = 'Freelance'
print(e1.company)
print(Employee.company)
```

## 🔴 Hard 1 – Shared Counter
```python
class User:
    count = 0
    def __init__(self):
        User.count += 1
u1 = User(); u2 = User()
print(User.count)
```

## 🔴 Hard 2 – Default Config via Class Var
```python
class AppConfig:
    theme = 'dark'
config = AppConfig()
config.theme = 'light'
print(config.theme)
print(AppConfig.theme)
```