# 📘 PyPhone Emperor · Module 4
# 📖 L‑33 – `*args` & `**kwargs`

---

## 🎯 OBJECTIVE
Learn to write functions that accept **any number**
of positional or keyword arguments using the special
parameters `*args` and `**kwargs`.
These are essential for building flexible APIs,
wrappers, and decorators.

---

## 🧱 BRICK 1 – `*args` (Variable Positional Arguments)

A parameter prefixed with a single asterisk `*args`
collects any extra **positional** arguments into a tuple.
The name `args` is a convention — you can use any name,
but `args` is standard.

```python
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))       # 6
print(sum_all(10, 20, 30, 40)) # 100
```

You can combine `*args` with normal parameters:
```python
def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet("Hello", "Emperor", "Python", "World")
# Hello, Emperor!
# Hello, Python!
# Hello, World!
```

> 💡 **INSIGHT:** `*args` is an ordinary tuple inside
> the function — you can iterate, index, and slice it.

---

## 🧱 BRICK 2 – `**kwargs` (Variable Keyword Arguments)

A parameter prefixed with double asterisks `**kwargs`
collects any extra **keyword** arguments into a dictionary.
Again, `kwargs` is the conventional name.

```python
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_details(name="Emperor", age=18, city="Dhaka")
# name: Emperor
# age: 18
# city: Dhaka
```

### Order when combining all four kinds
```python
def full_func(a, b=10, *args, **kwargs):
    pass
```
① positional (a)  
② default (b)  
③ `*args`  
④ `**kwargs`  

This order is **enforced** by Python.

> ⚠️ **WARNING:** `*args` and `**kwargs` are unpacking
> operators. Using them incorrectly (e.g., `**` on a list)
> raises a `TypeError`.

---

## 📌 Key Takeaway
- `*args` collects extra positional arguments into a tuple.
- `**kwargs` collects extra keyword arguments into a dict.
- The order must be: regular, default, `*args`, `**kwargs`.
- Use them for wrappers, logging, and extensible functions.