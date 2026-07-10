# L03 Solution – Strings: Indexing, Slicing & Immutability

## 🟢 Easy 1 – First Character
```python
code = 'Emperor'
print(code[0])
```

## 🟢 Easy 2 – Last Character
```python
order_id = 'ORD-123-X'
print(order_id[-1])
```

## 🟡 Medium 1 – Substring
```python
sku = 'PyPhone'
print(sku[1:5])
```

## 🟡 Medium 2 – Domain Extractor
```python
email = 'emperor@pyphone.com'
at_pos = email.find('@')
domain = email[at_pos+1:]
print(domain)
```

## 🔴 Hard 1 – Palindrome
```python
s = 'radar'
if s == s[::-1]:
    print('Palindrome')
else:
    print('Not Palindrome')
```

## 🔴 Hard 2 – Masking
```python
acct = '1234567890123456'
masked = '****' + acct[-4:]
print(masked)
```
