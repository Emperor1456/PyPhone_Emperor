# 📘 PyPhone Emperor v3.0 · Module 10
# 📖 L‑59 – Full CRUD – Python + SQLite

---

## 🎯 OBJECTIVE — What You Will Master

> Build the complete Create, Read, Update, Delete operations for your contact book.

- ➕ **Create** – insert a new contact
- 📖 **Read** – list all or search contacts
- ✏️ **Update** – modify a contact’s details
- 🗑️ **Delete** – remove a contact
- 🧪 **SQLite integration** – using `sqlite3` from Python
- 🛡️ **Parameterised queries** – prevent SQL injection

---

## 🧱 DATABASE CONNECTION

```python
import sqlite3

def get_connection():
    conn = sqlite3.connect("contacts.db")
    conn.row_factory = sqlite3.Row
    return conn
```

---

## 🧱 CREATE A CONTACT

```python
def add_contact(name, phone, email=None, group_name="General"):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO contacts (name, phone, email, group_name) VALUES (?, ?, ?, ?)",
            (name, phone, email, group_name)
        )
        conn.commit()
    return True
```

---

## 🧱 LIST ALL CONTACTS

```python
def list_contacts():
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM contacts ORDER BY name").fetchall()
        return [dict(row) for row in rows]
```

---

## 🧱 SEARCH BY NAME OR GROUP

```python
def search_contacts(query):
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM contacts WHERE name LIKE ? OR group_name LIKE ?",
            (f"%{query}%", f"%{query}%")
        ).fetchall()
        return [dict(row) for row in rows]
```

---

## 🧱 UPDATE A CONTACT

```python
def update_phone(contact_id, new_phone):
    with get_connection() as conn:
        conn.execute(
            "UPDATE contacts SET phone = ? WHERE id = ?",
            (new_phone, contact_id)
        )
        conn.commit()
```

---

## 🧱 DELETE A CONTACT

```python
def delete_contact(contact_id):
    with get_connection() as conn:
        conn.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        conn.commit()
```

> ⚠️ **WARNING:** Always use parameterised queries (`?` placeholders). Never concatenate user input into SQL strings – that invites SQL injection.

---

## 💡 Real‑world Usage

**Banking – CRUD for accounts**
```python
def create_account(owner, balance=0):
    conn.execute("INSERT INTO accounts (owner, balance) VALUES (?, ?)", (owner, balance))
```

**E‑commerce – product management**
```python
def update_stock(product_id, new_qty):
    conn.execute("UPDATE products SET stock = ? WHERE id = ?", (new_qty, product_id))
```

**Logistics – delete delivered shipment**
```python
def archive_shipment(tracking_id):
    conn.execute("DELETE FROM shipments WHERE tracking_id = ?", (tracking_id,))
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Write the `add_contact` function and call it with test data. |
| Medium | Write `list_contacts` and print all rows. |
| Hard | Write the entire CRUD module (create, read, update, delete) and test each function. |

Run the coach:
```bash
python ii_Practice_Sheets/L59_Full_CRUD_Python_SQLite.py
```

---

## 📌 Key Takeaway
- CRUD operations are the backbone of every database‑driven application.
- Use context managers (`with`) for automatic connection cleanup.
- Parameterised queries prevent SQL injection and ensure data safety.

*For Emperor.*