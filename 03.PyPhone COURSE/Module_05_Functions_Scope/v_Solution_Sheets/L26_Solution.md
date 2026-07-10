# L26 Solution – Return Values & Early Return Pattern

## 🟢 Easy 1 – Return a Value
```python
def double(x):
    return 2 * x
print(double(5))
```

## 🟢 Easy 2 – Return Sum
```python
def add(a, b):
    return a + b
print(add(3, 5))
```

## 🟡 Medium 1 – Early Return – Absolute Value
```python
def absolute(x):
    if x >= 0:
        return x
    return -x
print(absolute(-7))
```

## 🟡 Medium 2 – Early Return – Safe Division
```python
def safe_divide(a, b):
    if b == 0:
        return None
    return a / b
print(safe_divide(10, 2))
```

## 🔴 Hard 1 – Return Multiple Values
```python
def min_max(lst):
    return min(lst), max(lst)
low, high = min_max([4,1,9,3])
print(low)
print(high)
```

## 🔴 Hard 2 – Return Boolean – Even Check
```python
def is_even(n):
    return n % 2 == 0
print(is_even(8))
```