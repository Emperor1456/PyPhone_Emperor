# 📘 PyPhone Emperor · Module 7
# 📖 L‑57 – Special Methods (`__str__`, `__repr__`, `__len__`)

---

## 🎯 OBJECTIVE
Learn to define **special methods** (also called
dunder methods) that give your objects built‑in
Python behaviour. `__str__` controls the
human‑readable string, `__repr__` the developer
representation, and `__len__` the length.
Mastering them makes your classes feel like
first‑class citizens of the language.

---

## 🧱 BRICK 1 – `__str__` and `__repr__`

### `__str__` — for users
Called by `print()` and `str()`. It should return
a readable, friendly description of the object.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (${self.price:.2f})"

p = Product("Laptop", 799.99)
print(p)   # Laptop ($799.99)
```

### `__repr__` — for developers
Called by `repr()` and shown in the interactive
shell. It should return an unambiguous string,
ideally code that could recreate the object.

```python
class Product:
    # ... __init__ ...

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

p = Product("Laptop", 799.99)
print(repr(p))   # Product('Laptop', 799.99)
```

If `__str__` is missing, Python falls back to `__repr__`.
Always define at least `__repr__` for debugging.

---

## 🧱 BRICK 2 – `__len__` and Other Common Special Methods

### `__len__` — length of an object
Called by `len()`. Works only if your object logically
has a size.

```python
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

p = Playlist(["Song A", "Song B"])
print(len(p))   # 2
```

### Other useful special methods
- `__bool__` → called by `bool(obj)`; return `True`/`False`.
- `__eq__` → called by `==`; define object equality.
- `__add__`, `__sub__`, etc. → operator overloading.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
```

> 💡 **INSIGHT:** Special methods make your objects
> integrate seamlessly with Python’s core syntax.

---

## 📌 Key Takeaway
- `__str__` = friendly to users; `print()` uses it.
- `__repr__` = unambiguous to developers; fallback for `__str__`.
- `__len__` = lets you call `len(obj)`.
- Define special methods to give your classes Pythonic behaviour.