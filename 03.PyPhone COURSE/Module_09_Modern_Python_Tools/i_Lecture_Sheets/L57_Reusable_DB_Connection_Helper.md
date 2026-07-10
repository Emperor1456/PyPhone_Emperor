# 📘 PyPhone Emperor v3.0 · Module 9
# 📖 L‑57 – Reusable DB Connection Helper

---

## 🎯 OBJECTIVE — What You Will Master

> Write a utility function that connects to SQLite and abstracts away the boilerplate — your first bridge to SQLPhone.

- 🔗 **`sqlite3` module** – Python's built‑in SQLite support
- 🛠️ **Connection helper** – a function returning a cursor and connection
- 🧪 **Context manager** – create your own `with`‑compatible helper
- 🧱 **Why it matters** – every backend service needs a database helper

---

## 🧱 BASIC CONNECTION

```python
import sqlite3

conn = sqlite3.connect("empire.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
conn.commit()
conn.close()
```

---

## 🧱 HELPER FUNCTION

```python
def get_db(path="empire.db"):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row   # returns dict‑like rows
    return conn

conn = get_db()
cur = conn.cursor()
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
conn.close()
```

---

## 🧱 CONTEXT MANAGER VERSION

```python
from contextlib import contextmanager

@contextmanager
def connect(path="empire.db"):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

with connect() as conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    for row in cur.fetchall():
        print(row["name"])
```

---

## 💡 Real‑world Usage

**Banking – account database**
```python
with connect("bank.db") as conn:
    conn.execute("INSERT INTO accounts VALUES (?, ?)", (1, 5000))
    conn.commit()
```

**E‑commerce – product catalog**
```python
def get_products():
    with connect("shop.db") as conn:
        return conn.execute("SELECT * FROM products").fetchall()
```

**Logistics – shipment tracking**
```python
def update_status(tracking, status):
    with connect("logistics.db") as conn:
        conn.execute("UPDATE shipments SET status=? WHERE tracking=?", (status, tracking))
        conn.commit()
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Write a function that connects to an in‑memory SQLite DB and returns the connection. |
| Medium | Write a context manager that yields a connection and closes it automatically. |
| Hard | Create a table using the context manager and insert a row. |

Run the coach:
```bash
python ii_Practice_Sheets/L57_Reusable_DB_Connection_Helper.py
```

---

## 📌 Key Takeaway
- `sqlite3` is Python's built‑in lightweight database.
- Wrapping the connection in a helper or context manager eliminates boilerplate.
- This pattern is the foundation of every backend service you'll build.

*For Emperor.*