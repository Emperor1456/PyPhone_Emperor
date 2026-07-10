# L54 Solution – Generator Expressions & yield

## 🟢 Easy 1 – Generator Expression Sum
```python
total = sum(x*x for x in range(1, 6))
print(total)
```

## 🟢 Easy 2 – List from Generator
```python
gen = (x*2 for x in range(3))
print(list(gen))
```

## 🟡 Medium 1 – Simple yield Function
```python
def gen():
    yield 1
    yield 2
    yield 3
print(list(gen()))
```

## 🟡 Medium 2 – Fibonacci Generator
```python
def fib_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
print(list(fib_gen(5)))
```

## 🔴 Hard 1 – Countdown Generator
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
print(list(countdown(5)))
```

## 🔴 Hard 2 – Read File Lines Generator
```python
def read_lines():
    for line in ['Hello', 'World']:
        yield line
print(list(read_lines()))
```