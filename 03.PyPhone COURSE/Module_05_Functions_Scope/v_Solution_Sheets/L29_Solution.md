# L29 Solution – LEGB Rule – Local, Enclosing, Global, Built‑in

## 🟢 Easy 1 – Global Variable Access
```python
x = 10
def print_x():
    print(x)
print_x()
```

## 🟢 Easy 2 – Local Variable
```python
def set_local():
    y = 5
    print(y)
set_local()
```

## 🟡 Medium 1 – Modify Global with `global`
```python
counter = 0
def increment():
    global counter
    counter += 1
increment()
print(counter)
```

## 🟡 Medium 2 – Enclosing Scope with `nonlocal`
```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    return x
print(outer())
```

## 🔴 Hard 1 – LEGB Order Demonstration
```python
x = 'global'
def outer():
    x = 'enclosing'
    def inner():
        print(x)
    inner()
outer()
```

## 🔴 Hard 2 – Shadowing Global
```python
x = 100
def shadow():
    x = 200
    print(x)
shadow()
print(x)
```