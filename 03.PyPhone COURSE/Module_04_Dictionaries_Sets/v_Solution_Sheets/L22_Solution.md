# L22 Solution – Sets – Uniqueness, Membership, Operations

## 🟢 Easy 1 – Create a Set from List
```python
nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)
print(unique)
```

## 🟢 Easy 2 – Membership Test
```python
s = {'apple', 'banana', 'cherry'}
print('apple' in s)
```

## 🟡 Medium 1 – Add and Remove Elements
```python
s = {1, 2, 3}
s.add(4)
s.discard(2)
print(s)
```

## 🟡 Medium 2 – Unique Characters
```python
word = 'hello'
unique = set(word)
print(unique)
```

## 🔴 Hard 1 – Set Update
```python
s = {1, 2}
s.update([3, 4], {5, 6})
print(s)
```

## 🔴 Hard 2 – Deduplicate and Sort
```python
nums = [5, 3, 5, 1, 3, 2]
unique_sorted = sorted(set(nums))
print(unique_sorted)
```