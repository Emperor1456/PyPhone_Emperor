# L19 Solution – Dictionary – Key‑Value Pairs & Hash Tables

## 🟢 Easy 1 – Create a Dictionary
```python
user = {'name': 'Emperor', 'age': 18}
print(user)
```

## 🟢 Easy 2 – Access a Value by Key
```python
d = {'name': 'Emperor', 'age': 18}
print(d['name'])
```

## 🟡 Medium 1 – Safe Access with .get()
```python
d = {'name': 'Emperor'}
print(d.get('phone', 'Not found'))
```

## 🟡 Medium 2 – Add and Update
```python
d = {'name': 'Emperor', 'age': 18}
d['city'] = 'Dhaka'
d['age'] = 19
print(d)
```

## 🔴 Hard 1 – Remove with pop()
```python
d = {'name': 'Emperor', 'age': 18, 'city': 'Dhaka'}
popped = d.pop('age')
print(popped)
print(d)
```

## 🔴 Hard 2 – Check Key Existence
```python
d = {'name': 'Emperor'}
if 'email' in d:
    print('Exists')
else:
    print('Missing')
```