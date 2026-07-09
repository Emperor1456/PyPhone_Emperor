# 📘 PyPhone Emperor · Module 7  
# 📖 L‑57 – Special Methods (`__str__`, `__repr__`, `__len__`, `__add__`) – Pythonic Business Objects

---

## 🎯 OBJECTIVE  
Master **special methods** (dunder methods) to make your objects behave like built‑in types.  
`__str__` controls `print()` output, `__len__` enables `len()`, and `__add__` enables the `+` operator.  
These methods integrate your classes seamlessly with Python's core syntax — a hallmark of professional code.

---

## 🧱 BRICK 1 – `__str__` for Human‑readable Output

`__str__` is called by `print()` and `str()`. Return a friendly, readable string.

**① Book with title and author (Easy practice)**
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'{self.title} by {self.author}'

b = Book('1984', 'Orwell')
print(str(b))   # '1984 by Orwell'
```

**② Adding `__len__` (Medium practice)**
```python
class Book:
    # ... __init__ and __str__ ...
    def __len__(self):
        return 0   # simplistic; in real code maybe number of pages

b = Book('1984', 'Orwell')
print(len(b))   # 0
```

> 💡 **INSIGHT:** Always define at least `__repr__` for debugging; if `__str__` is missing, Python uses `__repr__`. Rule: `__repr__` for developers (unambiguous), `__str__` for users (readable).

---

## 🧱 BRICK 2 – Operator Overloading with `__add__`

Define arithmetic on your objects by implementing `__add__`, `__sub__`, etc.

**③ Vector addition with `+` (Hard practice)**
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3.x)   # 6
print(v3.y)   # 8
```
Now `v1 + v2` works naturally.

**④ Financial example – Money with `__add__`**
```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f'${self.amount:.2f}'

m1 = Money(10)
m2 = Money(15.50)
print(m1 + m2)   # $25.50
```

> ⚠️ **WARNING:** Overloading operators is powerful but should follow intuitive semantics. Don't make `+` do something unexpected.

> 💡 **ADVANCED TIP – Full comparison suite:**  
> Implement `__eq__` (equals), `__lt__` (less than), etc., to make your objects sortable and comparable, which is essential for business data processing.

---

## 💡 Real‑world Usage

**Banking – account with `__str__`**
```python
class Account:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance

    def __str__(self):
        return f'Account {self.id}: ${self.balance}'

a = Account('A100', 5000)
print(a)   # Account A100: $5000
```

**E‑commerce – cart total with `__add__`**
```python
class Cart:
    def __init__(self, total):
        self.total = total

    def __add__(self, other):
        return Cart(self.total + other.total)

c1 = Cart(30)
c2 = Cart(45)
print((c1 + c2).total)   # 75
```

**Logistics – package weight with comparisons**
```python
class Package:
    def __init__(self, weight):
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

p1 = Package(5)
p2 = Package(10)
print(p1 < p2)   # True
```

**HR – employee with `__repr__`**
```python
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"Employee('{self.name}', {self.id})"

e = Employee('Emperor', 101)
print(repr(e))   # Employee('Emperor', 101)
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Define `Book` with `__init__(title,author)` and `__str__` returning `'title by author'`. Create `b` for `'1984','Orwell'` and print `str(b)`. | `1984 by Orwell` |
| Medium | Add `__len__` to `Book` that returns 0. Print `len(b)`. | `0` |
| Hard   | Define `Vector` with x,y and `__add__` to add two vectors. Create v1=(2,3), v2=(4,5), print (v1+v2).x and (v1+v2).y on separate lines. | `6`<br>`8` |

Run the coach:
```bash
python ii_Practice_Sheets/L-57_Special_Methods.py
```

---

## 📌 Key Takeaway
- `__str__`: human‑friendly string for `print()` and `str()`.
- `__len__`: enable `len(obj)`.
- `__add__`: enable `obj1 + obj2` (operator overloading).
- Special methods make your classes feel like built‑in types.