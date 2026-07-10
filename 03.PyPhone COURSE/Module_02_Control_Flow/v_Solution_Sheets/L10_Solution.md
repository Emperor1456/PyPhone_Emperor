# L10 Solution – while Loops – Sentinel Repetition

## 🟢 Easy 1 – Sum Until Four
```python
total = 0
i = 1
while i <= 4:
    total += i
    i += 1
print(total)
```

## 🟢 Easy 2 – Countdown
```python
count = 3
while count > 0:
    print(count)
    count -= 1
print('Liftoff!')
```

## 🟡 Medium 1 – Factorial
```python
n = 4
prod = 1
while n > 0:
    prod *= n
    n -= 1
print(prod)
```

## 🟡 Medium 2 – Password Gate
```python
password = 'short'
while len(password) < 8:
    password = 'secure123'
print('Accepted')
```

## 🔴 Hard 1 – Doubling Investment
```python
x = 1
count = 0
while x <= 20:
    x *= 2
    count += 1
print(count)
```

## 🔴 Hard 2 – ATM Withdrawal
```python
balance = 500
amounts = [200, 250, 100, 0]
i = 0
while i < len(amounts):
    amt = amounts[i]
    if amt == 0:
        break
    if amt <= balance:
        balance -= amt
        print(balance)
    i += 1
```