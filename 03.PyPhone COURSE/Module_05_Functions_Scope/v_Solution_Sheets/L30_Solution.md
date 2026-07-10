# L30 Solution – Lambda Functions, `map()`, `filter()`, `sorted(key=)`

## 🟢 Easy 1 – Lambda – Double a Number
```python
double = lambda x: x * 2
print(double(5))
```

## 🟢 Easy 2 – Lambda – Add Two Numbers
```python
add = lambda a, b: a + b
print(add(3, 5))
```

## 🟡 Medium 1 – `map()` – Square a List
```python
nums = [1,2,3]
squared = list(map(lambda x: x**2, nums))
print(squared)
```

## 🟡 Medium 2 – `filter()` – Even Numbers
```python
nums = [1,2,3,4,5,6]
evens = list(filter(lambda x: x%2==0, nums))
print(evens)
```

## 🔴 Hard 1 – `sorted()` with Key
```python
words = ['banana','cherry','apple']
sorted_words = sorted(words, key=lambda w: w[1])
print(sorted_words)
```

## 🔴 Hard 2 – Lambda in Function
```python
def make_multiplier(factor):
    return lambda x: x * factor
triple = make_multiplier(3)
print(triple(5))
```