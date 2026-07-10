# L34 Solution – else, finally & Complete Cleanup

## 🟢 Easy 1 – else Block on Success
```python
try:
    x = 1
except:
    pass
else:
    print('success')
```

## 🟢 Easy 2 – finally Always Runs
```python
try:
    1 / 0
except ZeroDivisionError:
    print('error')
finally:
    print('cleanup')
```

## 🟡 Medium 1 – Full Pattern (success case)
```python
try:
    print('try')
except:
    pass
else:
    print('else')
finally:
    print('finally')
```

## 🟡 Medium 2 – File Handling with finally
```python
f = None
try:
    print('opened')
finally:
    print('closed')
```

## 🔴 Hard 1 – finally Overrides Return
```python
def demo():
    try:
        return 'try'
    finally:
        return 'finally'
print(demo())
```

## 🔴 Hard 2 – Complete Error Handling with Logging
```python
def process(data):
    try:
        int(data)
    except ValueError:
        print('Invalid')
    finally:
        print('Done')
process('abc')
```