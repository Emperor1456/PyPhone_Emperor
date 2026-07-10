import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy = Task(
    description=(
        "🗃️  Create Contacts Table\n\n"
        "Import sqlite3, connect to ':memory:', and execute a CREATE TABLE statement\n"
        "for a `contacts` table with columns: id (INTEGER PRIMARY KEY AUTOINCREMENT),\n"
        "name (TEXT NOT NULL), phone (TEXT NOT NULL UNIQUE).\n"
        "Print 'table created' after successful execution.\n\n"
        "Expected output: table created"
    ),
    expected_output="table created",
    level=Level.EASY,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('CREATE TABLE contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone TEXT NOT NULL UNIQUE)')",
        "print('table created')"
    ]
)

medium = Task(
    description=(
        "➕  Insert and Search Contact\n\n"
        "Using the contacts table created in Easy, insert two rows:\n"
        "  ('Emperor', '+8801700000000') and ('Rahim', '+8801800000000').\n"
        "Then write a query that searches for contacts whose name contains 'Em'\n"
        "and print the list of matching names.\n\n"
        "Expected output: [('Emperor', '+8801700000000')]"
    ),
    expected_output="[('Emperor', '+8801700000000')]",
    level=Level.MEDIUM,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('CREATE TABLE contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone TEXT NOT NULL UNIQUE)')",
        "conn.execute(\"INSERT INTO contacts (name, phone) VALUES ('Emperor', '+8801700000000')\")",
        "conn.execute(\"INSERT INTO contacts (name, phone) VALUES ('Rahim', '+8801800000000')\")",
        "conn.commit()",
        "rows = conn.execute(\"SELECT name, phone FROM contacts WHERE name LIKE '%Em%'\").fetchall()",
        "print(rows)"
    ]
)

hard = Task(
    description=(
        "📦  Full CRUD & Test\n\n"
        "Perform a complete CRUD cycle on the contacts table:\n"
        "1. Insert 'Emperor' with phone '123'.\n"
        "2. Update the phone to '456'.\n"
        "3. Delete the contact.\n"
        "4. Assert that the table is empty (use `assert` that count of rows is 0).\n"
        "If the assertion passes, print 'All tests passed'.\n\n"
        "Expected output: All tests passed"
    ),
    expected_output="All tests passed",
    level=Level.HARD,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('CREATE TABLE contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone TEXT NOT NULL UNIQUE)')",
        "conn.execute(\"INSERT INTO contacts (name, phone) VALUES ('Emperor', '123')\")",
        "conn.commit()",
        "conn.execute(\"UPDATE contacts SET phone = '456' WHERE name = 'Emperor'\")",
        "conn.commit()",
        "conn.execute(\"DELETE FROM contacts WHERE name = 'Emperor'\")",
        "conn.commit()",
        "count = conn.execute('SELECT COUNT(*) FROM contacts').fetchone()[0]",
        "assert count == 0",
        "print('All tests passed')"
    ]
)

if __name__ == "__main__":
    run_sequence([easy, medium, hard],
                 save_path=MODULE_DIR,
                 progress_name=".progress_review_M10.json")
