# L15 Solution – List Slicing & Slice Assignment

## 🟢 Easy 1 – Basic Slicing
```python
nums = [1, 2, 3, 4, 5]
print(nums[1:4])
```

## 🟢 Easy 2 – Copy Entire List
```python
original = [10, 20, 30]
copy = original[:]
print(copy)
```

## 🟡 Medium 1 – Replace Middle
```python
data = [0, 1, 2, 3, 4]
data[1:4] = [10, 20]
print(data)
```

## 🟡 Medium 2 – Insert with Empty Slice
```python
data = [0, 10, 20, 4]
data[2:2] = [100]
print(data)
```

## 🔴 Hard 1 – Delete with Slice Assignment
```python
data = [0, 10, 100, 20, 4]
data[1:3] = []
print(data)
```

## 🔴 Hard 2 – Every Second Element
```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[::2])
```