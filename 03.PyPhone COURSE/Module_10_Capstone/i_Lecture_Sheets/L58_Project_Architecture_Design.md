# 📘 PyPhone Emperor v3.0 · Module 10
# 📖 L‑58 – Project Architecture & Design

---

## 🎯 OBJECTIVE — What You Will Master

> Plan a complete CLI application before writing a single line of code.

- 🧠 **Requirements analysis** – what must the Imperial Contact Book do?
- 🏗️ **Architecture** – separating concerns into modules (database, models, CLI)
- 📐 **Schema design** – tables, columns, constraints
- 🧪 **Interface design** – command‑line arguments vs interactive menu
- 🛠️ **Project structure** – file and folder layout

---

## 🧱 THE IMPERIAL CONTACT BOOK – REQUIREMENTS

The Emperor needs a contact management system that runs offline on a phone.
It must:
- Add a new contact (name, phone, email, group)
- List all contacts
- Search contacts by name or group
- Update a contact’s phone number
- Delete a contact
- Save data persistently (SQLite database)

---

## 🧱 PROJECT STRUCTURE

```
Imperial_Contact_Book/
├── main.py          # CLI entry point
├── database.py      # connection and table creation
├── models.py        # Contact class and CRUD functions
├── tests.py         # unit tests for all functions
└── requirements.txt # dependencies (if any)
```

Each file has a single responsibility – the foundation of maintainable software.

---

## 🧱 DATABASE SCHEMA

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

Constraints enforce business rules at the database level.

---

## 🧱 CLI DESIGN

The app will be command‑driven via `sys.argv`:

```bash
python main.py add "Emperor" "+8801700000000" "emperor@pyphone.com" "Family"
python main.py list
python main.py search "Emperor"
python main.py update 1 "+8801800000000"
python main.py delete 1
```

The `main.py` script parses the command and dispatches to the appropriate function.

---

## 💡 Real‑world Usage

This architecture mirrors production backend services:
- A **database layer** for all SQL operations.
- A **model layer** with business logic and validation.
- A **controller/CLI layer** handling user input and output.
- A **test layer** ensuring everything works.

You will reuse this pattern when building APIs, web apps, and Companion’s memory module.

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Write the requirements list for the contact book in your own words. |
| Medium | Draw the project folder structure and list what each file does. |
| Hard | Write the `CREATE TABLE` SQL statement with all constraints. |

Run the coach:
```bash
python ii_Practice_Sheets/L58_Project_Architecture_Design.py
```

---

## 📌 Key Takeaway
- Plan before coding: requirements → architecture → schema → interface.
- Separate concerns into modules: database, models, CLI.
- Constraints in the database prevent bad data.

*For Emperor.*