# L45 Solution – Method Overriding & Polymorphism

## 🟢 Easy 1 – Override Method
```python
class Parent:
    def show(self):
        return 'Parent'
class Child(Parent):
    def show(self):
        return 'Child'
c = Child()
print(c.show())
```

## 🟢 Easy 2 – GrandChild Inherits Override
```python
class Parent:
    def show(self):
        return 'Parent'
class Child(Parent):
    def show(self):
        return 'Child'
class GrandChild(Child):
    pass
gc = GrandChild()
print(gc.show())
```

## 🟡 Medium 1 – GrandChild Overrides Again
```python
class GrandChild(Child):
    def show(self):
        return 'GrandChild'
gc = GrandChild()
print(gc.show())
```

## 🟡 Medium 2 – Polymorphic List
```python
objs = [Parent(), Child(), GrandChild()]
for obj in objs:
    print(obj.show())
```

## 🔴 Hard 1 – Payment Polymorphism
```python
class CreditCard:
    def pay(self):
        return 'Card payment'
class PayPal:
    def pay(self):
        return 'PayPal payment'
def process(payment):
    print(payment.pay())
process(CreditCard())
process(PayPal())
```

## 🔴 Hard 2 – Animal Sounds Polymorphism
```python
class Dog:
    def speak(self):
        return 'Woof'
class Cat:
    def speak(self):
        return 'Meow'
class Bird:
    def speak(self):
        return 'Tweet'
animals = [Dog(), Cat(), Bird()]
for a in animals:
    print(a.speak())
```