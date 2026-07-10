# L59 Solution – Full CRUD – Python + SQLite

## 🟢 Easy 1 – Create Database Connection
```python
import sqlite3

def get_connection(db_path=':memory:'):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

conn = get_connection()
print('Connected')
```

## 🟢 Easy 2 – Create Contacts Table
```python
import sqlite3
conn = sqlite3.connect(':memory:')
conn.execute('CREATE TABLE contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone TEXT NOT NULL UNIQUE)')
print('Table created')
```

## 🟡 Medium 1 – Add Contact (Create)
```python
import sqlite3
conn = sqlite3.connect(':memory:')
conn.execute('CREATE TABLE contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone TEXT NOT NULL UNIQUE)')

def add_contact(conn, name, phone):
    conn.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', (name, phone))
    conn.commit()

add_contact(conn, 'Emperor', '+8801700000000')
rows = conn.execute('SELECT name, phone FROM contacts').fetchall()
print([tuple(row) for row in rows])
```

## 🟡 Medium 2 – Search Contacts (Read)
```python
import sqlite3
conn = sqlite3.connect(':memory:')
conn.execute('CREATE TABLE contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone TEXT NOT NULL UNIQUE)')
conn.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', ('Emperor', '+8801700000000'))
conn.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', ('Rahim', '+8801800000000'))
conn.commit()

def search_contacts(conn, query):
    return conn.execute("SELECT name, phone FROM contacts WHERE name LIKE ?", ('%'+query+'%',)).fetchall()

rows = search_contacts(conn, 'Em')
print([tuple(row) for row in rows])
```

## 🔴 Hard 1 – Update Contact Phone
```python
import sqlite3
conn = sqlite3.connect(':memory:')
conn.execute('CREATE TABLE contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone TEXT NOT NULL UNIQUE)')
conn.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', ('Emperor', '+8801700000000'))
conn.commit()

def update_phone(conn, cid, new_phone):
    conn.execute('UPDATE contacts SET phone = ? WHERE id = ?', (new_phone, cid))
    conn.commit()

update_phone(conn, 1, '+8801900000000')
row = conn.execute('SELECT name, phone FROM contacts WHERE id=1').fetchone()
print(tuple(row))
```

## 🔴 Hard 2 – Delete Contact
```python
import sqlite3
conn = sqlite3.connect(':memory:')
conn.execute('CREATE TABLE contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone TEXT NOT NULL UNIQUE)')
conn.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', ('Emperor', '+8801700000000'))
conn.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', ('Rahim', '+8801800000000'))
conn.commit()

def delete_contact(conn, cid):
    conn.execute('DELETE FROM contacts WHERE id = ?', (cid,))
    conn.commit()

delete_contact(conn, 1)
rows = conn.execute('SELECT name, phone FROM contacts').fetchall()
print([tuple(row) for row in rows])
```