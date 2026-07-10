# L05 Solution – User Input, CLI Arguments & sys.argv

## 🟢 Easy 1 – Default Value
```python
import sys
if len(sys.argv) > 1:
    print(sys.argv[1])
else:
    print('none')
```

## 🟢 Easy 2 – Argument Count
```python
import sys
print(len(sys.argv))
```

## 🟡 Medium 1 – Uppercase Converter
```python
import sys
if len(sys.argv) == 2:
    print(sys.argv[1].upper())
else:
    print('usage')
```

## 🟡 Medium 2 – Greeting
```python
import sys
name = sys.argv[1] if len(sys.argv) > 1 else 'Guest'
print(f'Hello, {name}')
```

## 🔴 Hard 1 – Admin Check
```python
import sys
if len(sys.argv) > 1 and sys.argv[1] == 'admin':
    print('Access granted')
else:
    print('Access denied')
```

## 🔴 Hard 2 – Sum Checker
```python
import sys
if len(sys.argv) == 3:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    print(a + b)
else:
    print('error')
```
