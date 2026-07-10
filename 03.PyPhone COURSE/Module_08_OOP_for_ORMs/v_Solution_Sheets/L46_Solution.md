# L46 Solution – Special Methods (__str__, __repr__, __len__)

## 🟢 Easy 1 – __str__ Method
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f'{self.title} by {self.author}'
b = Book('1984', 'Orwell')
print(str(b))
```

## 🟢 Easy 2 – __len__ Method
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f'{self.title} by {self.author}'
    def __len__(self):
        return 0
b = Book('1984','Orwell')
print(len(b))
```

## 🟡 Medium 1 – __repr__ Method
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
p = Point(3, 4)
print(repr(p))
```

## 🟡 Medium 2 – __eq__ Method
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
p1 = Point(1,2); p2 = Point(1,2)
print(p1 == p2)
```

## 🔴 Hard 1 – __add__ Operator Overloading
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
v1 = Vector(2,3); v2 = Vector(4,5)
v3 = v1 + v2
print(v3.x)
print(v3.y)
```

## 🔴 Hard 2 – __str__ for Product
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f'{self.name} (${self.price:.2f})'
p = Product('Laptop', 999.99)
print(p)
```