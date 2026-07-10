# L01 Solution – Variables, Memory & Dynamic Typing

## 🟢 Easy 1 – Product Record
```python
product_name = 'Wireless Mouse'
unit_price = 24.99
stock = 150
print(product_name, unit_price, stock, sep=', ')
```

## 🟢 Easy 2 – Naming Conventions
```python
MAX_RETRIES = 5
_internal = 'secret'
print(MAX_RETRIES)
print(_internal)
```

## 🟡 Medium 1 – Dynamic Typing
```python
x = 42
x = 'Emperor'
print(type(x).__name__)
```

## 🟡 Medium 2 – Swapping
```python
a = 10
b = 20
a, b = b, a
print(a, b)
```

## 🔴 Hard 1 – Integer Caching
```python
a = 100
b = 100
c = 300
d = 300
print(a is b, c is not d)
```

## 🔴 Hard 2 – Mutable Identity
```python
a = [1, 2]
b = [1, 2]
print(a == b, a is b)
```
