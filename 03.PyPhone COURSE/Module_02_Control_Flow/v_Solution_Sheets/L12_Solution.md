# L12 Solution – Loop Control – break, continue, pass

## 🟢 Easy 1 – Break
```python
for x in [1, 2, 3, 4]:
    if x == 3:
        print('Found')
        break
```

## 🟢 Easy 2 – Continue
```python
for i in range(1, 7):
    if i % 2 == 0:
        continue
    print(i)
```

## 🟡 Medium 1 – Process Active
```python
statuses = ['active', 'inactive', 'active', 'suspended']
for status in statuses:
    if status != 'active':
        continue
    print('Sending statement')
```

## 🟡 Medium 2 – Early Stop Sum
```python
res = 0
i = 1
while i <= 10:
    res += i
    if res > 30:
        break
    i += 1
print(res)
```

## 🔴 Hard 1 – Pass Placeholder
```python
for i in range(5):
    if i == 2:
        pass
    else:
        print(i)
print('Done')
```

## 🔴 Hard 2 – Validate & Retry
```python
num = -5
while True:
    if num <= 0:
        print('Invalid')
        num = 10
    else:
        print('Valid')
        break
```