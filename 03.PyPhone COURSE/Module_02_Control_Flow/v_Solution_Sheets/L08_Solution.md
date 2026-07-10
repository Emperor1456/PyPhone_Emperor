# L08 Solution – if, elif, else – Business Rules

## 🟢 Easy 1 – Stock Availability
```python
stock = 12
if stock > 0:
    print('Available')
else:
    print('Out of stock')
```

## 🟢 Easy 2 – Temperature Alert
```python
temp = 28
if temp > 30:
    print('Hot day')
else:
    print('Not too hot')
```

## 🟡 Medium 1 – Tax Bracket
```python
income = 25000
if income >= 50000:
    print('High tax')
elif income >= 20000:
    print('Medium tax')
else:
    print('Low tax')
```

## 🟡 Medium 2 – Shipping Cost
```python
weight_kg = 12
if weight_kg > 20:
    print('Heavy shipment')
elif weight_kg > 10:
    print('Standard shipment')
elif weight_kg > 5:
    print('Light shipment')
else:
    print('Envelope')
```

## 🔴 Hard 1 – Loan Qualification
```python
age = 25
income = 32000
existing_loans = 0
if age >= 21 and income >= 30000 and existing_loans == 0:
    print('Approved')
else:
    print('Denied')
```

## 🔴 Hard 2 – Cold Storage Check
```python
temp = 5
humidity = 55
if 2 <= temp <= 8 and humidity < 60:
    print('Safe')
else:
    print('Unsafe')
```