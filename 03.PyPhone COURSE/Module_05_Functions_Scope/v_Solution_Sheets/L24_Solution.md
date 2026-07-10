# L24 Solution – def – Functions, Docstrings, Type Hints

## 🟢 Easy 1 – Define a Simple Function
```python
def hello():
    print('Hello, Emperor')
hello()
```

## 🟢 Easy 2 – Function with Docstring
```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
print(add(3, 5))
```

## 🟡 Medium 1 – Function with Type Hints
```python
def multiply(x: float, y: float) -> float:
    """Multiply two floats."""
    return x * y
print(multiply(2.5, 4.0))
```

## 🟡 Medium 2 – Function with Multiple Returns
```python
def min_max(numbers):
    return min(numbers), max(numbers)
low, high = min_max([4, 1, 9, 3])
print(low, high)
```

## 🔴 Hard 1 – Function with Validation
```python
def safe_divide(a, b):
    if b == 0:
        return None
    return a / b
print(safe_divide(10, 2))
```

## 🔴 Hard 2 – Recursive Function – Sum of List
```python
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])
print(sum_list([1, 2, 3, 4]))
```