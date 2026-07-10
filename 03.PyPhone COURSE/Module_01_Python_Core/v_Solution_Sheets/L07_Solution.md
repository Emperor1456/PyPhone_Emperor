# L07 Solution – None, Optional Typing & Sentinels

## 🟢 Easy 1 – Sensor Reading
```python
reading = None
if reading is None:
    print('No data')
else:
    print('Data found')
```

## 🟢 Easy 2 – Missing Record
```python
def find_item():
    return None
result = find_item()
if result is None:
    print('Missing')
else:
    print('Found')
```

## 🟡 Medium 1 – Mutable Default Fix
```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
print(add_item('A'))
```

## 🟡 Medium 2 – Default Config
```python
def connect(host, port=None):
    if port is None:
        port = 5432
    print(f'{host}:{port}')
connect('localhost')
```

## 🔴 Hard 1 – Safe Division
```python
def safe_divide(a, b):
    if b == 0:
        return None
    return a / b
print(safe_divide(10, 2))
```

## 🔴 Hard 2 – User Lookup
```python
def find_user(user_id):
    users = {1: 'Emperor', 2: 'Rahim'}
    return users.get(user_id)
print(find_user(1))
```
