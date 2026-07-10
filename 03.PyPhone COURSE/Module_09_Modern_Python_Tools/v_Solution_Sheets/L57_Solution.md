# L57 Solution – Reusable DB Connection Helper

## 🟢 Easy 1 – Connect to SQLite
```python
import sqlite3
conn = sqlite3.connect(':memory:')
cur = conn.cursor()
print('connected')
```

## 🟢 Easy 2 – Create Table
```python
import sqlite3
conn = sqlite3.connect(':memory:')
conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')
print('table created')
```

## 🟡 Medium 1 – Insert and Select
```python
import sqlite3
conn = sqlite3.connect(':memory:')
conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')
conn.execute('INSERT INTO users VALUES (1, ?)', ('Emperor',))
conn.commit()
rows = conn.execute('SELECT * FROM users').fetchall()
print(rows)
```

## 🟡 Medium 2 – Parameterised Query
```python
import sqlite3
conn = sqlite3.connect(':memory:')
conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')
conn.execute('INSERT INTO users (name) VALUES (?)', ('Rahim',))
conn.commit()
row = conn.execute('SELECT name FROM users WHERE name=?', ('Rahim',)).fetchone()
print(row[0])
```

## 🔴 Hard 1 – DB Connection Helper Function
```python
import sqlite3
def get_db(path=':memory:'):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db()
conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')
conn.execute('INSERT INTO users VALUES (1, ?)', ('Emperor',))
conn.commit()
row = conn.execute('SELECT * FROM users WHERE id=1').fetchone()
print(dict(row))
```

## 🔴 Hard 2 – Context Manager for DB
```python
import sqlite3
from contextlib import contextmanager

@contextmanager
def connect_db(path=':memory:'):
    conn = sqlite3.connect(path)
    try:
        yield conn
    finally:
        conn.close()

with connect_db() as conn:
    conn.execute('CREATE TABLE test (id INTEGER PRIMARY KEY, val TEXT)')
    conn.execute('INSERT INTO test VALUES (1, ?)', ('x',))
    conn.commit()
    count = conn.execute('SELECT COUNT(*) FROM test').fetchone()[0]
    print(count)
```