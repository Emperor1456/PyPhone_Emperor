# L55 Solution – Decorators – Wrapping Functions

## 🟢 Easy 1 – Simple Decorator
```python
def bold(func):
    def wrapper():
        return f'<b>{func()}</b>'
    return wrapper

@bold
def say():
    return 'Hi'

print(say())
```

## 🟢 Easy 2 – Uppercase Decorator
```python
def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet():
    return 'hello'

print(greet())
```

## 🟡 Medium 1 – Logging Decorator
```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} returned {result}')
        return result
    return wrapper

@log
def add(a, b):
    return a + b

print(add(3, 5))
```

## 🟡 Medium 2 – Stacking Decorators
```python
def bold(func):
    def wrapper():
        return f'<b>{func()}</b>'
    return wrapper

def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

@bold
@uppercase
def message():
    return 'hi'

print(message())
```

## 🔴 Hard 1 – Timer Decorator
```python
import time

def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f'Took {end-start:.4f}s')
        return result
    return wrapper

@timer
def compute():
    return 42

print(compute())
print('Fast')
```

## 🔴 Hard 2 – Retry Decorator
```python
def retry(max_attempts):
    def decorator(func):
        def wrapper():
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func()
                except:
                    attempts += 1
            return func()
        return wrapper
    return decorator

counter = [0]

@retry(3)
def unstable():
    counter[0] += 1
    if counter[0] < 3:
        raise ValueError('fail')
    return 'OK'

print(unstable())
```