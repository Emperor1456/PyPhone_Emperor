# 📘 PyPhone Emperor v3.0 · Module 8
# 📖 L‑48 – `Enum` – Enumerations for Database Constants

---

## 🎯 OBJECTIVE — What You Will Master

> Replace magic strings and numbers with safe, self‑documenting constants.

- 🚦 **`Enum`** – a set of named values
- 🧪 **Why enums** – prevents typos, improves readability, safer comparisons
- 🔧 **Usage** – status codes, roles, categories, fixed options
- 🧱 **ORM integration** – enums map directly to database column constraints

---

## 🧱 DEFINING AN ENUM

```python
from enum import Enum

class Status(Enum):
    PENDING = 1
    ACTIVE = 2
    INACTIVE = 3
    DELETED = 4

print(Status.ACTIVE)        # Status.ACTIVE
print(Status.ACTIVE.value)  # 2
```

---

## 🧱 USING ENUMS IN BUSINESS LOGIC

```python
def handle_account(status):
    if status == Status.ACTIVE:
        print("Account is active")
    elif status == Status.PENDING:
        print("Awaiting activation")
    else:
        print("Account is inactive or deleted")

handle_account(Status.ACTIVE)
```

---

## 🧱 ENUMS WITH STRING VALUES

```python
class Role(Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

print(Role.ADMIN.value)   # "admin"
```

---

## 💡 Real‑world Usage

**Banking – transaction types**
```python
class TxnType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    TRANSFER = "transfer"
```

**E‑commerce – order status**
```python
class OrderStatus(Enum):
    PLACED = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELLED = 4
```

**Logistics – delivery priority**
```python
class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Define an `Enum` with three values and print one value. |
| Medium | Use an `Enum` in a conditional to print different messages. |
| Hard | Define an `Enum` with string values and use it as a function parameter. |

Run the coach:
```bash
python ii_Practice_Sheets/L48_Enum_Database_Constants.py
```

---

## 📌 Key Takeaway
- `Enum` creates a fixed set of symbolic names for values.
- Prevents invalid values at the code level.
- Essential for database column constraints and clean APIs.

*For Emperor.*