# 📘 PyPhone Emperor v3.0 · Module 10
# 📖 L‑60 – Testing, Documentation & Packaging

---

## 🎯 OBJECTIVE — What You Will Master

> Ship your project like a professional: tested, documented, and ready for the world.

- 🧪 **Testing with `unittest`** – write and run automated tests
- 📝 **Docstrings** – document every function and module
- 📄 **`README.md`** – create a project overview for GitHub
- 📦 **`requirements.txt`** – list dependencies
- 🧰 **Final review** – ensure all components work together

---

## 🧱 WRITING UNIT TESTS

```python
import unittest
from database import get_connection, create_table
from models import add_contact, list_contacts

class TestContactBook(unittest.TestCase):
    def setUp(self):
        self.conn = get_connection(":memory:")
        create_table(self.conn)

    def test_add_and_list(self):
        add_contact("Emperor", "+8801700000000", "emperor@pyphone.com")
        contacts = list_contacts()
        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0]["name"], "Emperor")

if __name__ == "__main__":
    unittest.main()
```

Run tests:
```bash
python tests.py
```

---

## 🧱 DOCUMENTING WITH DOCSTRINGS

Every function should have a docstring:

```python
def add_contact(name, phone, email=None, group_name="General"):
    """Add a new contact to the database.

    Args:
        name: Contact's full name.
        phone: Phone number (unique).
        email: Optional email address.
        group_name: Category (default 'General').

    Returns:
        bool: True if insertion succeeded.
    """
```

---

## 🧱 THE `README.md`

Your project's welcome mat:

```markdown
# Imperial Contact Book
A CLI contact manager built with Python and SQLite.

## Features
- Add, list, search, update, delete contacts
- Persistent SQLite storage
- Full test suite

## Usage
python main.py add "Name" "Phone" "Email" "Group"
python main.py list
python main.py search "query"
python main.py update ID "new_phone"
python main.py delete ID

## Requirements
- Python 3.8+
- No external dependencies (SQLite is built‑in)
```

---

## 🧱 `requirements.txt`

Even if your project has no dependencies, include the file to signal completeness:

```
# No external dependencies required.
# Python standard library + sqlite3.
```

---

## 💡 Real‑world Usage

**Banking – test transaction logic**
```python
class TestAccounts(unittest.TestCase):
    def test_deposit(self):
        create_account("A1", 100)
        deposit("A1", 50)
        self.assertEqual(get_balance("A1"), 150)
```

**E‑commerce – document API**
```python
def calculate_discount(price, pct):
    """Return discounted price.
    Args:
        price: original price in USD.
        pct: discount percentage (0‑100).
    Returns:
        float: price after discount.
    """
```

**Logistics – package app for deployment**
```bash
pip freeze > requirements.txt
git add . && git commit -m "Release v1.0" && git push
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Write a docstring for the `add_contact` function. |
| Medium | Write a unit test for `add_contact` and `list_contacts`. |
| Hard | Create a complete `README.md` for the Imperial Contact Book project. |

Run the coach:
```bash
python ii_Practice_Sheets/L60_Testing_Documentation_Packaging.py
```

---

## 📌 Key Takeaway
- Testing proves your code works; documentation explains how to use it.
- `unittest` is Python's built‑in testing framework.
- A good `README.md` is the first thing people see — make it count.
- With tests, docs, and requirements, your project is production‑ready.

*For Emperor.*