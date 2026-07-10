# L21 Solution – Nested Dictionaries & defaultdict

## 🟢 Easy 1 – Create Nested Dictionary
```python
company = {'employees': {'emp1': {'name': 'Emperor', 'dept': 'Engineering'}}}
print(company)
```

## 🟢 Easy 2 – Access Nested Value
```python
print(company['employees']['emp1']['dept'])
```

## 🟡 Medium 1 – Modify Nested Dict
```python
company = {'employees': {'emp1': {'name': 'Emperor', 'dept': 'Engineering'}}}
company['employees']['emp2'] = {'name': 'Rahim', 'dept': 'Sales'}
print(company)
```

## 🟡 Medium 2 – defaultdict – Group by First Letter
```python
from collections import defaultdict
words = ['apple', 'banana', 'avocado', 'cherry']
by_letter = defaultdict(list)
for w in words:
    by_letter[w[0]].append(w)
print(dict(by_letter))
```

## 🔴 Hard 1 – Nested Dict Counting
```python
data = [('A',100),('B',200),('A',50)]
summary = {}
for cat, amt in data:
    if cat not in summary:
        summary[cat] = {'total':0, 'count':0}
    summary[cat]['total'] += amt
    summary[cat]['count'] += 1
print(summary)
```

## 🔴 Hard 2 – defaultdict(int) – Character Frequency
```python
from collections import defaultdict
counts = defaultdict(int)
for ch in 'mississippi':
    counts[ch] += 1
print(dict(counts))
```