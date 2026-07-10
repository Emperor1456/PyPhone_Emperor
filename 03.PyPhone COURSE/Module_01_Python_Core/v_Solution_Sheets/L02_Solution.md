# L02 Solution – Numeric Types, Operators & Casting

## 🟢 Easy 1 – Precedence
```python
print(10 + 3 * 4)
```

## 🟢 Easy 2 – Box Packing
```python
boxes = 250 // 24
left = 250 % 24
print(boxes, left)
```

## 🟡 Medium 1 – Type Casting
```python
raw = '  42  '
stock = int(raw.strip())
print(stock)
```

## 🟡 Medium 2 – Float Precision
```python
price = 24.99
qty = 3
total = price * qty
print(f'{total:.2f}')
```

## 🔴 Hard 1 – Exponentiation
```python
print(2 ** 10)
```

## 🔴 Hard 2 – Casting Chain
```python
temp_str = '98.6'
temp_float = float(temp_str)
temp_int = int(temp_float)
print(temp_int)
```
