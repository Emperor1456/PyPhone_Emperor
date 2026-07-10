# L48 Solution – Enum – Database Constants

## 🟢 Easy 1 – Define an Enum
```python
from enum import Enum
class Status(Enum):
    PENDING = 1
    ACTIVE = 2
    INACTIVE = 3
print(Status.ACTIVE)
```

## 🟢 Easy 2 – Enum Value
```python
from enum import Enum
class Status(Enum):
    PENDING = 1
    ACTIVE = 2
    INACTIVE = 3
print(Status.ACTIVE.value)
```

## 🟡 Medium 1 – Enum with Strings
```python
from enum import Enum
class Role(Enum):
    ADMIN = 'admin'
    USER = 'user'
    GUEST = 'guest'
print(Role.USER.value)
```

## 🟡 Medium 2 – Enum Comparison
```python
from enum import Enum
class Status(Enum):
    PENDING = 1
    ACTIVE = 2
    INACTIVE = 3
print(Status.ACTIVE == Status.ACTIVE)
```

## 🔴 Hard 1 – Enum in Function
```python
from enum import Enum
class Status(Enum):
    PENDING = 1
    ACTIVE = 2
    INACTIVE = 3
def handle_status(status):
    if status == Status.ACTIVE:
        print('Active')
    else:
        print('Other')
handle_status(Status.ACTIVE)
```

## 🔴 Hard 2 – List All Enum Members
```python
from enum import Enum
class Status(Enum):
    PENDING = 1
    ACTIVE = 2
    INACTIVE = 3
names = [s.name for s in Status]
print(names)
```