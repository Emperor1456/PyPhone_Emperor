# L37 Solution – Writing & Appending Files

## 🟢 Easy 1 – Write to a File
```python
with open('output.txt', 'w') as f:
    f.write('Emperor')
print(open('output.txt').read())
```

## 🟢 Easy 2 – Overwrite a File
```python
with open('output.txt', 'w') as f:
    f.write('PyPhone')
print(open('output.txt').read())
```

## 🟡 Medium 1 – Write Multiple Lines
```python
lines = ['First\n', 'Second\n']
with open('lines.txt', 'w') as f:
    f.writelines(lines)
print(open('lines.txt').read().strip())
```

## 🟡 Medium 2 – Append to File
```python
with open('log.txt', 'w') as f:
    f.write('line1')
with open('log.txt', 'a') as f:
    f.write('\nline2')
print(open('log.txt').read().strip())
```

## 🔴 Hard 1 – Write Numbers as CSV
```python
nums = [1,2,3]
with open('numbers.txt', 'w') as f:
    f.write(','.join(map(str, nums)))
print(open('numbers.txt').read())
```

## 🔴 Hard 2 – Write Dictionary as Key‑Value Pairs
```python
d = {'name':'Emperor', 'age':'18'}
with open('config.txt', 'w') as f:
    for k,v in d.items():
        f.write(f'{k}={v}\n')
print(open('config.txt').read().strip())
```