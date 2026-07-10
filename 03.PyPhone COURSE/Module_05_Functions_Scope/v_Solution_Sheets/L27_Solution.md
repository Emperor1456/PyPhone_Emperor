# L27 Solution – Default Parameters & Mutable Pitfall

## 🟢 Easy 1 – Greeting with Default
```python
def greet(name='Guest'):
    return 'Hello ' + name
print(greet())
```

## 🟢 Easy 2 – Power with Default Exponent
```python
def power(x, exp=2):
    return x ** exp
print(power(2))
```

## 🟡 Medium 1 – Override Default
```python
print(greet('Emperor'))
```

## 🟡 Medium 2 – Default with Type Casting
```python
def increment(n, step=1):
    return n + step
print(increment(10))
print(increment(10, 5))
```

## 🔴 Hard 1 – Avoid Mutable Default
```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
print(add_item('A'))
print(add_item('B'))
```

## 🔴 Hard 2 – Default with Validation
```python
def connect(host, port=None):
    if port is None:
        port = 5432
    print(f'{host}:{port}')
connect('localhost')
```