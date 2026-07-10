# L33 Solution – raise, Custom Exceptions & Chaining

## 🟢 Easy 1 – Raise ValueError
```python
def set_age(age):
    if age < 0:
        raise ValueError('Invalid age')
try:
    set_age(-5)
except ValueError:
    print('Invalid age')
```

## 🟢 Easy 2 – Custom Exception Class
```python
class NegativeBalanceError(Exception):
    pass
print(NegativeBalanceError.__name__)
```

## 🟡 Medium 1 – Raise Custom Exception
```python
class InsufficientFundsError(Exception):
    pass
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError('Not enough money')
try:
    withdraw(100, 200)
except InsufficientFundsError:
    print('Not enough money')
```

## 🟡 Medium 2 – Exception Chaining
```python
try:
    raise ValueError('original')
except ValueError as e:
    try:
        raise RuntimeError('wrapped') from e
    except RuntimeError:
        print('Chained')
```

## 🔴 Hard 1 – Validation with Custom Exception
```python
class InvalidEmailError(Exception):
    pass
def validate_email(email):
    if '@' not in email:
        raise InvalidEmailError('Bad email')
try:
    validate_email('invalid')
except InvalidEmailError:
    print('Bad email')
```

## 🔴 Hard 2 – Re-raise with Context
```python
try:
    try:
        raise ValueError('oops')
    except ValueError:
        print('Logged')
        raise
except ValueError:
    print('Handled')
```