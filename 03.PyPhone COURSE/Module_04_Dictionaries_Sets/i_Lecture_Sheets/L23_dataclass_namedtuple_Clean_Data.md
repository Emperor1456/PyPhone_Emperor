# 📘 PyPhone Emperor v3.0 · Module 4
# 📖 L‑23 – `dataclass` & `namedtuple` – Clean Data Containers

---

## 🎯 OBJECTIVE — What You Will Master

> Modern Python data classes that replace boilerplate code.

- 📦 **`namedtuple`** – lightweight, immutable data objects
- 🧪 **`dataclass`** – auto‑generated `__init__`, `__repr__`, and more
- 🚀 **Type hints** – integrate with data classes for clarity
- 🧱 **When to use** – configuration, records, ORM models

---

## 🧱 `namedtuple` – FROM `collections`

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)   # 10 20
print(p[0])       # 10
```

Immutable – cannot assign to `p.x` after creation.

---

## 🧱 `dataclass` – MODERN PYTHON (3.7+)

```python
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

p = Product("Laptop", 999.99, 5)
print(p)   # Product(name='Laptop', price=999.99, quantity=5)
```

Auto‑generated `__init__`, `__repr__`, `__eq__`.

**Comparison with `namedtuple`:**
- `dataclass` is mutable by default (can add `frozen=True` for immutability).
- `dataclass` allows default values and more complex logic.

---

## 🧱 BUSINESS USAGE

**Banking – transaction record**
```python
from dataclasses import dataclass

@dataclass
class Transaction:
    id: int
    amount: float
    type: str

tx = Transaction(1, 250.0, "deposit")
```

**E‑commerce – product catalog**
```python
Product = namedtuple("Product", ["sku", "name", "price"])
p1 = Product("SKU-1", "Mouse", 24.99)
```

> ⚠️ **WARNING:** `namedtuple` is a tuple, so you can still use indexing, but that can break readability. Prefer attribute access.

---

## 💡 Real‑world Usage

**Banking – account summary**
```python
@dataclass
class Account:
    id: str
    balance: float
    status: str = "active"
```

**E‑commerce – order line item**
```python
LineItem = namedtuple("LineItem", ["product", "qty", "price"])
```

**Logistics – shipment manifest**
```python
@dataclass
class Shipment:
    tracking: str
    weight: float
    destination: str
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Create a `namedtuple` for a book (title, author) and print its attributes. | `Book=namedtuple("Book",["title","author"]); b=Book("1984","Orwell"); print(b.title)` |
| Medium | Define a `dataclass` for a student (name, grade) and create an instance. | `@dataclass class Student: name: str; grade: float; s=Student("Emperor",95); print(s)` |
| Hard | Compare two `namedtuple` instances with `==` (should be True if fields equal). | `b1=Book(...); b2=Book(...); print(b1==b2)` |

Run the coach:
```bash
python ii_Practice_Sheets/L23_dataclass_namedtuple_Clean_Data.py
```

---

## 📌 Key Takeaway
- `namedtuple` for simple immutable records.
- `dataclass` for richer, mutable data containers with less boilerplate.
- Both integrate with type hints for professional code.

*For Emperor.*