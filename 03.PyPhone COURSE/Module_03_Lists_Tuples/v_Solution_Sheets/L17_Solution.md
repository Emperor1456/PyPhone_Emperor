# L17 Solution – Tuples – Immutable Sequences

## 🟢 Easy 1 – Create a Tuple
```python
t = (1, 2, 3)
print(t)
```

## 🟢 Easy 2 – Access Tuple Elements
```python
t = (10, 20, 30)
print(t[0])
```

## 🟡 Medium 1 – Unpack a Tuple
```python
point = (5, 8)
x, y = point
print(x, y)
```

## 🟡 Medium 2 – Swap Variables with Tuple
```python
a, b = 10, 20
a, b = b, a
print(a, b)
```

## 🔴 Hard 1 – Tuple as Dictionary Key
```python
d = {(1, 2): 'point A'}
print(d[(1, 2)])
```

## 🔴 Hard 2 – Multiple Return Values
```python
def min_max(lst):
    return min(lst), max(lst)
low, high = min_max([4,1,9,3])
print(low)
print(high)
```