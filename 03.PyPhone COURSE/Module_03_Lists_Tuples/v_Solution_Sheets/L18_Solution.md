# L18 Solution – Sequence Comparison & zip() Deep Dive

## 🟢 Easy 1 – Compare Lists
```python
print([1,2,3] == [1,2,3])
```

## 🟢 Easy 2 – Zip Two Lists
```python
names = ['Emperor', 'Rahim']
scores = [95, 88]
print(list(zip(names, scores)))
```

## 🟡 Medium 1 – Zip and Iterate
```python
products = ['Widget', 'Gadget']
prices = [9.99, 19.99]
for p, pr in zip(products, prices):
    print(f'{p}: ${pr:.2f}')
```

## 🟡 Medium 2 – Unzip a List of Tuples
```python
pairs = [('A', 1), ('B', 2), ('C', 3)]
letters, numbers = zip(*pairs)
print(list(letters), list(numbers))
```

## 🔴 Hard 1 – Compare Sequences Lexicographically
```python
print([1,2,3] < [1,2,4])
```

## 🔴 Hard 2 – Zip with Different Lengths
```python
from itertools import zip_longest
a = [1,2,3]
b = ['x','y']
result = list(zip_longest(a, b, fillvalue='?'))
print(result)
```