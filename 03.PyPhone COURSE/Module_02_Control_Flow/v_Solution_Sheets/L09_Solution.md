# L09 Solution – Nested Conditionals & match‑case

## 🟢 Easy 1 – Access Control
```python
is_logged_in = True
is_admin = False
if is_logged_in:
    if is_admin:
        print('Admin panel')
    else:
        print('User dashboard')
else:
    print('Please log in')
```

## 🟢 Easy 2 – Discount Engine
```python
member = True
purchase = 150
if member:
    if purchase > 100:
        print('20% off')
    else:
        print('10% off')
else:
    print('No discount')
```

## 🟡 Medium 1 – ATM Menu
```python
choice = 2
match choice:
    case 1:
        print('Balance inquiry')
    case 2:
        print('Cash withdrawal')
    case 3:
        print('Deposit')
    case _:
        print('Invalid')
```

## 🟡 Medium 2 – Language Selector
```python
lang = 'fr'
match lang:
    case 'en':
        print('Hello')
    case 'fr':
        print('Bonjour')
    case 'es':
        print('Hola')
    case _:
        print('Unknown language')
```

## 🔴 Hard 1 – Lab Result
```python
value = 12
match value:
    case x if x < 0:
        print('Negative')
    case 0:
        print('Zero')
    case x if x > 0:
        print('Positive')
```

## 🔴 Hard 2 – Warehouse Classification
```python
weight = 15
destination = 'international'
if destination == 'domestic':
    if weight <= 10:
        print('Standard domestic')
    else:
        print('Heavy domestic')
elif destination == 'international':
    if weight <= 10:
        print('Standard international')
    else:
        print('Heavy international')
else:
    print('Unknown destination')
```