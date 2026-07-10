# L28 Solution – `*args`, `**kwargs` & Unpacking

## 🟢 Easy 1 – Sum All – `*args`
```python
def sum_all(*args):
    return sum(args)
print(sum_all(1,2,3,4))
```

## 🟢 Easy 2 – Print Info – `**kwargs`
```python
def print_info(**kwargs):
    return ', '.join(f'{k}: {v}' for k,v in kwargs.items())
print(print_info(name='Emperor', age=18))
```

## 🟡 Medium 1 – Mixed `*args` and `**kwargs`
```python
def mixed(*args, **kwargs):
    if not kwargs:
        return sum(args)
    return str(kwargs)
print(mixed(1,2,3))
```

## 🟡 Medium 2 – Unpacking List into Function
```python
def add(a,b,c):
    return a+b+c
nums = [1,2,3]
print(add(*nums))
```

## 🔴 Hard 1 – Kwargs as Dict
```python
print(mixed(name='Emperor'))
```

## 🔴 Hard 2 – Combine Unpacking
```python
def show(a,b,c):
    print(a, b, c)
nums = [1,2]
kwargs = {'c': 3}
show(*nums, **kwargs)
```