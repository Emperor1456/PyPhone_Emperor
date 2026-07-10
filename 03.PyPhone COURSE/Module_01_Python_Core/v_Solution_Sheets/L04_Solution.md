# L04 Solution – String Methods & f‑strings

## 🟢 Easy 1 – Strip
```python
code = '   EMP-101   '
clean = code.strip()
print(clean)
```

## 🟢 Easy 2 – Search & Count
```python
email = 'emperor@pyphone.com'
pos = email.find('@')
cnt = email.count('o')
print(pos, cnt)
```

## 🟡 Medium 1 – Split & Join
```python
data = 'laptop,mouse,keyboard,monitor'
items = data.split(',')
result = ' | '.join(items)
print(result)
```

## 🟡 Medium 2 – Replace & Case
```python
slug = 'wireless_mouse_pro'
slug = slug.replace('_', '-').upper()
print(slug)
```

## 🔴 Hard 1 – Receipt
```python
item = 'Laptop'
price = 999.99
qty = 2
total = price * qty
print(f'{qty} x {item} = ${total:.2f}')
```

## 🔴 Hard 2 – Column Formatting
```python
print(f"{'Mouse':10} ${24.99:6.2f}")
print(f"{'Keyboard':10} ${49.99:6.2f}")
```
