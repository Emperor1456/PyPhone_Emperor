# 📘 PyPhone Emperor v3.0 · Module 8
# 📖 L‑46 – Special Methods – `__str__`, `__repr__`, `__len__`

---

## 🎯 OBJECTIVE — What You Will Master

> Make your objects behave like built‑in types.

- 🖨️ `__str__` – called by `print()` and `str()` (user‑friendly)
- 🛠️ `__repr__` – called by `repr()` (developer‑focused, unambiguous)
- 📏 `__len__` – called by `len()`
- ⚖️ `__eq__` – called by `==` (object equality)
- 🧪 **Operator overloading** – `+`, `-`, etc.

---

## 🧱 `__str__` AND `__repr__`

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name} (${self.price:.2f})"
    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

p = Product("Laptop", 999.99)
print(p)        # Laptop ($999.99)
print(repr(p))  # Product('Laptop', 999.99)
```

---

## 🧱 `__len__` AND `__eq__`

```python
class Playlist:
    def __init__(self, songs):
        self.songs = songs
    def __len__(self):
        return len(self.songs)
    def __eq__(self, other):
        return self.songs == other.songs

pl = Playlist(["A", "B"])
print(len(pl))        # 2
print(pl == Playlist(["A", "B"]))  # True
```

> 💡 **INSIGHT:** Always define `__repr__` so that it returns a string that could recreate the object. If `__str__` is missing, Python uses `__repr__`.

---

## 💡 Real‑world Usage

**Banking – account representation**
```python
class Account:
    def __str__(self):
        return f"Account({self.id}): ${self.balance}"
```

**E‑commerce – product comparison**
```python
class Product:
    def __eq__(self, other):
        return self.sku == other.sku
```

**Logistics – package weight**
```python
class Package:
    def __len__(self):
        return int(self.weight)
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Define `__str__` for a Book class and print `str(book)`. |
| Medium | Define `__len__` for a class returning 0. |
| Hard | Define `__eq__` to compare two objects. |

Run the coach:
```bash
python ii_Practice_Sheets/L46_Special_Methods_str_repr_len.py
```

---

## 📌 Key Takeaway
- Special methods make your objects integrate with Python syntax.
- `__str__` for users, `__repr__` for developers.
- `__len__`, `__eq__`, and others enable built‑in behaviours.

*For Emperor.*