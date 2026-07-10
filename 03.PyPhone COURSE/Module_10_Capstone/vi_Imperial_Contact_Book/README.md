# 📇 Imperial Contact Book
*A CLI contact manager built with Python and SQLite*

---

## 📂 Project Structure
```
vi_Imperial_Contact_Book/
├── database.py   → Connection & schema
├── models.py     → CRUD operations
├── main.py       → CLI entry point
├── tests.py      → Unit tests
└── README.md     → This file
```

---

## ⚙️ Features
- **Add** a contact (name, phone, email, group)
- **List** all contacts in alphabetical order
- **Search** by name or group
- **Update** phone number of a contact
- **Delete** a contact by ID
- Persistent storage in `contacts.db`
- Full unit test suite

---

## 🚀 Usage
```bash
# Add a new contact
python main.py add "Emperor" "+8801700000000" "emperor@pyphone.com" "Family"

# List all contacts
python main.py list

# Search contacts
python main.py search "Emperor"

# Update phone number
python main.py update 1 "+8801800000000"

# Delete a contact
python main.py delete 1
```

---

## 🧪 Running Tests
```bash
cd vi_Imperial_Contact_Book
python tests.py
```

All tests should pass with `OK`.

---

## 📋 Requirements
- Python 3.8 or later
- No external libraries (SQLite3 is built into Python)

---

## 🧠 Design Decisions
- SQLite is used for zero‑configuration persistent storage.
- The `row_factory` is set to `sqlite3.Row` so that query results behave like dictionaries.
- A context manager (`with get_connection()`) ensures the database connection is always closed, even on error.
- All user input is passed via parameterized queries to prevent SQL injection.

---

*Built entirely on a phone by Emperor.*