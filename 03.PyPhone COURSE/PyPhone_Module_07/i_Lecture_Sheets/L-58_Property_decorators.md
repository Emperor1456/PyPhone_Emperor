# 📘 PyPhone Emperor · Module 7
# 📖 L‑58 – Property Decorators (`@property`)

---

## 🎯 OBJECTIVE
Learn to control attribute access with **property
decorators**. `@property` turns a method into a
readable attribute, while `@name.setter` adds
controlled write access. This is Python’s elegant
way to implement getters and setters without
breaking the simple `obj.attr` syntax.

---

## 🧱 BRICK 1 – Read‑Only Properties with `@property`

A method decorated with `@property` can be accessed
like an attribute — no parentheses needed. Use it
when the value is derived from internal data.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

c = Circle(5)
print(c.diameter)   # 10   (not c.diameter()!)
```

The property looks like data, but it runs a method
each time you access it. The internal `radius` is
still a normal attribute.

> 💡 **INSIGHT:** Properties let you start with simple
> public attributes, and later add logic without
> changing the interface used by external code.

---

## 🧱 BRICK 2 – Setters and Deleters

If you want to allow assignment to a property,
add a **setter** with `@name.setter`. You can
validate or transform the value before storing it.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius    # internal storage

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
```

Now `c.radius = 10` triggers the setter,
and `c.radius = -1` raises a clean error.

Optionally add a **deleter** with `@name.deleter`:
```python
@radius.deleter
def radius(self):
    del self._radius
```

> ⚠️ **WARNING:** The internal attribute (`_radius`)
> is a convention to signal “protected”. Python does
> not enforce true privacy, but properties give you
> clean control over access.

---

## 📌 Key Takeaway
- `@property` makes a method callable without `()`.
- Use properties for computed attributes.
- `@name.setter` adds controlled write access.
- Properties preserve the simple `obj.attr` syntax
  while enabling validation and logic.