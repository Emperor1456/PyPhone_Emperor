# L31 Solution – Recursion & Memoization

## 🟢 Easy 1 – Recursive Factorial
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
print(factorial(4))
```

## 🟢 Easy 2 – Recursive Sum of List
```python
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])
print(sum_list([1,2,3]))
```

## 🟡 Medium 1 – Fibonacci Recursive
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(5))
```

## 🟡 Medium 2 – Countdown Recursive
```python
def countdown(n):
    if n <= 0:
        return []
    return [n] + countdown(n-1)
print(countdown(5))
```

## 🔴 Hard 1 – Memoized Fibonacci
```python
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(10))
```

## 🔴 Hard 2 – Recursive Power
```python
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp-1)
print(power(2, 5))
```