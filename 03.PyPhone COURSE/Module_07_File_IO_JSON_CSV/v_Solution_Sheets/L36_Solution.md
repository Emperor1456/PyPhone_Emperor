# L36 Solution – Reading Text Files

## 🟢 Easy 1 – Read Entire File
```python
with open('test.txt', 'r') as f:
    content = f.read()
print(content)
```

## 🟢 Easy 2 – Read All Lines
```python
with open('test.txt', 'r') as f:
    lines = f.readlines()
print(lines)
```

## 🟡 Medium 1 – Read First Line and Strip
```python
with open('test.txt', 'r') as f:
    first = f.readline().strip()
print(first)
```

## 🟡 Medium 2 – Iterate Over Lines
```python
with open('test.txt', 'r') as f:
    for line in f:
        print(line.strip())
```

## 🔴 Hard 1 – Read File into a List Comprehension
```python
with open('test.txt', 'r') as f:
    lines = [line.strip() for line in f]
print(lines)
```

## 🔴 Hard 2 – Count Lines
```python
with open('test.txt', 'r') as f:
    count = sum(1 for _ in f)
print(count)
```