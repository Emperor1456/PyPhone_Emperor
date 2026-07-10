import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🔗  Create Database Connection\n\n"
        "Import sqlite3. Write a function `get_connection(db_path=':memory:')` that returns\n"
        "a connection with row_factory = sqlite3.Row. Call it and print 'Connected'.\n\n"
        "Expected output: Connected"
    ),
    expected_output="Connected",
    level=Level.EASY,
    hints=["import sqlite3", "def get_connection(db_path=':memory:'):", "    conn = sqlite3.connect(db_path)", "    conn.row_factory = sqlite3.Row", "    return conn", "conn = get_connection()", "print('Connected')"]
)

easy2 = Task(
    description=(
        "📋  Create Contacts Table\n\n"
        "Using the connection from Easy1, execute the CREATE TABLE statement for contacts\n"
        "(id PK autoincrement, name TEXT NOT NULL, phone TEXT NOT NULL UNIQUE). Print 'Table created'.\n\n"
        "Expected output: Table created"
    ),
    expected_output="Table created",
    level=Level.EASY,
    hints=["import sqlite3", "conn = sqlite3.connect(':memory:')", "conn.execute('CREATE TABLE contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone TEXT NOT NULL UNIQUE)')", "print('Table created')"]
)

medium1 = Task(
    description=(
        "➕  Add Contact (Create)\n\n"
        "Write a function `add_contact(conn, name, phone)` that inserts a new contact.\n"
        "Call it with ('Emperor', '+8801700000000'). Then SELECT all rows and print the list.\n\n"
        "Expected output: [('Emperor', '+8801700000000')]"
    ),
    expected_output="[('Emperor', '+8801700000000')]",
    level=Level.MEDIUM,
    hints=["import sqlite3", "conn = sqlite3.connect(':memory:')", "conn.execute('CREATE TABLE contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone TEXT NOT NULL UNIQUE)')", "def add_contact(conn, name, phone):", "    conn.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', (name, phone))", "    conn.commit()", "add_contact(conn, 'Emperor', '+8801700000000')", "rows = conn.execute('SELECT name, phone FROM contacts').fetchall()", "print([tuple(row) for row in rows])"]
)

medium2 = Task(
    description=(
        "🔍  Search Contacts (Read)\n\n"
        "Insert two contacts: 'Emperor' and 'Rahim'. Write a function `search_contacts(conn, query)`\n"
        "that returns rows where name LIKE '%query%'. Call with 'Em' and print the matching rows.\n\n"
        "Expected output: [('Emperor', '+8801700000000')]"
    ),
    expected_output="[('Emperor', '+8801700000000')]",
    level=Level.MEDIUM,
    hints=["import sqlite3", "conn = sqlite3.connect(':memory:')", "conn.execute('CREATE TABLE contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone TEXT NOT NULL UNIQUE)')", "conn.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', ('Emperor', '+8801700000000'))", "conn.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', ('Rahim', '+8801800000000'))", "conn.commit()", "def search_contacts(conn, query):", "    return conn.execute('SELECT name, phone FROM contacts WHERE name LIKE ?', ('%'+query+'%',)).fetchall()", "rows = search_contacts(conn, 'Em')", "print([tuple(row) for row in rows])"]
)

hard1 = Task(
    description=(
        "✏️  Update Contact Phone\n\n"
        "Insert 'Emperor' with phone '+8801700000000'. Write a function `update_phone(conn, contact_id, new_phone)`\n"
        "that updates the phone of the given id. Call with id=1, new_phone='+8801900000000'.\n"
        "Then SELECT the updated row and print it.\n\n"
        "Expected output: ('Emperor', '+8801900000000')"
    ),
    expected_output="('Emperor', '+8801900000000')",
    level=Level.HARD,
    hints=["import sqlite3", "conn = sqlite3.connect(':memory:')", "conn.execute('CREATE TABLE contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone TEXT NOT NULL UNIQUE)')", "conn.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', ('Emperor', '+8801700000000'))", "conn.commit()", "def update_phone(conn, cid, new_phone):", "    conn.execute('UPDATE contacts SET phone = ? WHERE id = ?', (new_phone, cid))", "    conn.commit()", "update_phone(conn, 1, '+8801900000000')", "row = conn.execute('SELECT name, phone FROM contacts WHERE id=1').fetchone()", "print(tuple(row))"]
)

hard2 = Task(
    description=(
        "🗑️  Delete Contact\n\n"
        "Insert two contacts: 'Emperor' and 'Rahim'. Write a function `delete_contact(conn, contact_id)`\n"
        "that deletes the row. Delete id=1. Then SELECT all remaining rows and print them.\n\n"
        "Expected output: [('Rahim', '+8801800000000')]"
    ),
    expected_output="[('Rahim', '+8801800000000')]",
    level=Level.HARD,
    hints=["import sqlite3", "conn = sqlite3.connect(':memory:')", "conn.execute('CREATE TABLE contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone TEXT NOT NULL UNIQUE)')", "conn.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', ('Emperor', '+8801700000000'))", "conn.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', ('Rahim', '+8801800000000'))", "conn.commit()", "def delete_contact(conn, cid):", "    conn.execute('DELETE FROM contacts WHERE id = ?', (cid,))", "    conn.commit()", "delete_contact(conn, 1)", "rows = conn.execute('SELECT name, phone FROM contacts').fetchall()", "print([tuple(row) for row in rows])"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L59.json")
