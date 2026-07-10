# L53 Solution – datetime & time Deep Dive

## 🟢 Easy 1 – Today's Date
```python
from datetime import date
print(date.today().strftime('%Y-%m-%d'))
```

## 🟢 Easy 2 – Current Time
```python
from datetime import datetime
print(datetime.now().strftime('%H:%M'))
```

## 🟡 Medium 1 – Days Until New Year
```python
from datetime import date
today = date.today()
next_year = date(today.year + 1, 1, 1)
print((next_year - today).days)
```

## 🟡 Medium 2 – Parse a Date String
```python
from datetime import datetime
date_str = '2026-01-15'
parsed = datetime.strptime(date_str, '%Y-%m-%d')
print(parsed.month)
```

## 🔴 Hard 1 – Add 30 Days
```python
from datetime import date, timedelta
future = date.today() + timedelta(days=30)
print(future.strftime('%Y-%m-%d'))
```

## 🔴 Hard 2 – Age Calculator
```python
from datetime import date
birth = date(2008, 7, 10)
today = date.today()
age = today.year - birth.year
if today.strftime('%m-%d') < birth.strftime('%m-%d'):
    age -= 1
print(age)
```