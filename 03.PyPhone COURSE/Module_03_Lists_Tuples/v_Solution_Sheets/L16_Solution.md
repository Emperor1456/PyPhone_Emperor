# L16 Solution – List Comprehension & Generator Expressions

## 🟢 Easy 1 – Squares with Comprehension
```python
squares = [x*x for x in [1, 2, 3]]
print(squares)
```

## 🟢 Easy 2 – Even Numbers Filter
```python
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)
```

## 🟡 Medium 1 – Map with Comprehension
```python
prices = [100, 200, 300]
with_tax = [p * 1.1 for p in prices]
print(with_tax)
```

## 🟡 Medium 2 – Generator Expression Sum
```python
total = sum(x*x for x in range(1, 6))
print(total)
```

## 🔴 Hard 1 – Nested Comprehension – Flatten Matrix
```python
matrix = [[1,2],[3,4],[5,6]]
flat = [num for row in matrix for num in row]
print(flat)
```

## 🔴 Hard 2 – Conditional Expression in Comprehension
```python
result = [x**2 if x%2==0 else x for x in range(1, 7)]
print(result)
```