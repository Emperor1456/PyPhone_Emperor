# L20 Solution – Dictionary Methods, Iteration & Counting

## 🟢 Easy 1 – List All Keys
```python
d = {'name': 'Emperor', 'age': 18}
print(list(d.keys()))
```

## 🟢 Easy 2 – List All Values
```python
print(list(d.values()))
```

## 🟡 Medium 1 – Iterate Over Items
```python
d = {'name': 'Emperor', 'age': 18}
for k, v in d.items():
    print(f'{k}: {v}')
```

## 🟡 Medium 2 – Counting Pattern
```python
words = ['apple', 'banana', 'apple', 'cherry']
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts)
```

## 🔴 Hard 1 – Merge Two Dictionaries
```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d1.update(d2)
print(d1)
```

## 🔴 Hard 2 – Pop and Clear
```python
d = {'x': 10, 'y': 20, 'z': 30}
last = d.popitem()
print(last)
d.clear()
print(d)
```