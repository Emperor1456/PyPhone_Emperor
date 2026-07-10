# L32 Solution – try/except – Catching Specific Exceptions

## 🟢 Easy 1 – Catch ValueError
```python
try:
    int('abc')
except ValueError:
    print('error')
```

## 🟢 Easy 2 – Catch ZeroDivisionError
```python
try:
    10 / 0
except ZeroDivisionError:
    print('caught')
```

## 🟡 Medium 1 – Catch FileNotFoundError
```python
try:
    open('nofile.txt')
except FileNotFoundError:
    print('missing')
```

## 🟡 Medium 2 – Multiple Exceptions
```python
try:
    int('abc')
except ValueError:
    print('value error')
except ZeroDivisionError:
    print('zero error')
```

## 🔴 Hard 1 – Catch Exception and Print Type
```python
try:
    print(x)
except Exception as e:
    print(type(e).__name__)
```

## 🔴 Hard 2 – Validation with try/except
```python
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None
print(safe_int('42'))
```