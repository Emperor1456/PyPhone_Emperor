# L06 Solution – Boolean Logic, Truthiness & is vs ==

## 🟢 Easy 1 – Stock Check
```python
stock = 12
print(stock > 0)
```

## 🟢 Easy 2 – Loan Qualifier
```python
age = 25
income = 2100
print(age > 18 and income > 2000)
```

## 🟡 Medium 1 – Truthiness
```python
empty_list = []
non_empty = 'hello'
print(bool(empty_list), bool(non_empty))
```

## 🟡 Medium 2 – Short‑Circuit
```python
divisor = 5
dividend = 10
if divisor != 0 and dividend / divisor > 0:
    print('safe')
else:
    print('unsafe')
```

## 🔴 Hard 1 – List Identity
```python
a = [1, 2]
b = [1, 2]
print(a == b, a is b)
```

## 🔴 Hard 2 – None Check
```python
reading = None
if reading is None:
    print('No data')
else:
    print('Data present')
```
