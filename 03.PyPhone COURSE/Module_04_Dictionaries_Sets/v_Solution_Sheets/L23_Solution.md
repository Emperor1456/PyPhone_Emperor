# L23 Solution – dataclass & namedtuple – Clean Data

## 🟢 Easy 1 – Namedtuple – Book Record
```python
from collections import namedtuple
Book = namedtuple('Book', ['title', 'author'])
b = Book('1984', 'Orwell')
print(b.title)
```

## 🟢 Easy 2 – Dataclass – Student Record
```python
from dataclasses import dataclass
@dataclass
class Student:
    name: str
    grade: float
s = Student('Emperor', 95.0)
print(s)
```

## 🟡 Medium 1 – Compare Namedtuples
```python
from collections import namedtuple
Book = namedtuple('Book', ['title', 'author'])
b1 = Book('A', 'X')
b2 = Book('A', 'X')
print(b1 == b2)
```

## 🟡 Medium 2 – Dataclass with Default
```python
from dataclasses import dataclass
@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0
p = Product('Widget', 9.99)
print(p)
```

## 🔴 Hard 1 – Frozen Dataclass
```python
from dataclasses import dataclass
@dataclass(frozen=True)
class Point:
    x: int
    y: int
p = Point(5, 10)
print(p.x)
```

## 🔴 Hard 2 – Namedtuple – Multiple Return
```python
from collections import namedtuple
MinMax = namedtuple('MinMax', ['min', 'max'])
def get_min_max(lst):
    return MinMax(min(lst), max(lst))
result = get_min_max([3,1,9,4])
print(result.min, result.max)
```