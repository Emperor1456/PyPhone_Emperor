# L11 Solution – for Loops, range(), enumerate(), zip()

## 🟢 Easy 1 – Sum a List
```python
sales = [1, 2, 3, 4, 5]
total = 0
for sale in sales:
    total += sale
print(total)
```

## 🟢 Easy 2 – Print Characters
```python
code = 'Emperor'
for ch in code:
    print(ch)
```

## 🟡 Medium 1 – Enumerate
```python
items = ['Laptop', 'Mouse', 'Keyboard']
for i, item in enumerate(items, start=1):
    print(f'{i}. {item}')
```

## 🟡 Medium 2 – Zip Products & Prices
```python
products = ['Widget', 'Gadget']
prices = [9.99, 19.99]
for product, price in zip(products, prices):
    print(f'{product}: ${price:.2f}')
```

## 🔴 Hard 1 – Even Numbers from 1 to 10
```python
evens = []
for i in range(1, 11):
    if i % 2 == 0:
        evens.append(i)
print(evens)
```

## 🔴 Hard 2 – Monthly Report
```python
months = ['Jan', 'Feb', 'Mar']
sales = [1500, 2300, 1800]
for i, (month, sale) in enumerate(zip(months, sales), start=1):
    print(f'{i}: {month} sales ${sale}')
```