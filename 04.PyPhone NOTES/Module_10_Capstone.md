# 📘 Module 10 – Capstone · Revision Note

---

## L58 – Project Architecture & Design
- Plan before coding: requirements → architecture → schema → interface.
- Separate concerns: database, models, CLI controller, tests.
- Imperial Contact Book uses SQLite with a `contacts` table.

```sql
CREATE TABLE contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL UNIQUE,
    email TEXT,
    group_name TEXT DEFAULT 'General',
    created_at TEXT DEFAULT (datetime('now'))
);
```

---

## L59 – Full CRUD – Python + SQLite
- **C**reate: `INSERT INTO contacts (...) VALUES (?, ...)`.
- **R**ead: `SELECT * FROM contacts WHERE ...`.
- **U**pdate: `UPDATE contacts SET ... WHERE id = ?`.
- **D**elete: `DELETE FROM contacts WHERE id = ?`.
- Always use parameterised queries to prevent SQL injection.

```python
import sqlite3
conn = sqlite3.connect("contacts.db")
conn.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", ("Emperor", "123"))
conn.commit()
```

---

## L60 – Testing, Documentation & Packaging
- Use `unittest` for automated tests.
- Write docstrings for every function and module.
- Create `README.md` with title, features, installation, usage, testing.
- `pip freeze > requirements.txt` locks dependencies.

```python
import unittest
class TestContacts(unittest.TestCase):
    def test_add_contact(self):
        self.assertTrue(True)
if __name__ == "__main__":
    unittest.main()
```

---

*Quick Test:*  
- What are the four CRUD operations?  
- Why use parameterised queries?  
- What sections should every project README include?  
- Command to lock current dependencies?