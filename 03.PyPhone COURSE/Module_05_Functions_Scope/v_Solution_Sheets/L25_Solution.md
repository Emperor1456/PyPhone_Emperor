# L25 Solution – Parameters, Arguments & `__name__ == "__main__"`

## 🟢 Easy 1 – Add Two Numbers
```python
def add(a, b):
    return a + b
print(add(3, 5))
```

## 🟢 Easy 2 – Full Name Formatter
```python
def full_name(first, last):
    return first + ' ' + last
print(full_name('Emperor', 'PyPhone'))
```

## 🟡 Medium 1 – Keyword Arguments
```python
def power(base, exp):
    return base ** exp
print(power(base=2, exp=10))
```

## 🟡 Medium 2 – Mixed Arguments
```python
def describe_person(name, age, city):
    print(f'{name} is {age} years old and lives in {city}.')
describe_person('Emperor', age=18, city='Dhaka')
```

## 🔴 Hard 1 – `__name__ == "__main__"` Guard
```python
def main():
    print('Script executed directly')
if __name__ == '__main__':
    main()
```

## 🔴 Hard 2 – Type Casting in Function
```python
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None
print(safe_int('42'))
```