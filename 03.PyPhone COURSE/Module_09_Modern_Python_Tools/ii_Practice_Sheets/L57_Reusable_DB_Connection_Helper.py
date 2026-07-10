import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🔗  Connect to SQLite\n\n"
        "Import sqlite3. Connect to an in-memory database, create a cursor, and print 'connected'.\n\n"
        "Expected output: connected"
    ),
    expected_output="connected",
    level=Level.EASY,
    hints=["import sqlite3", "conn = sqlite3.connect(':memory:')", "cur = conn.cursor()", "print('connected')"]
)

easy2 = Task(
    description=(
        "📋  Create Table\n\n"
        "Create a table `users` with columns `id` INTEGER PRIMARY KEY and `name` TEXT.\n"
        "Print 'table created'.\n\n"
        "Expected output: table created"
    ),
    expected_output="table created",
    level=Level.EASY,
    hints=["import sqlite3", "conn = sqlite3.connect(':memory:')", "conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')", "print('table created')"]
)

medium1 = Task(
    description=(
        "✍️  Insert and Select\n\n"
        "Insert a row: id=1, name='Emperor'. Commit. Then SELECT all rows and print them as a list.\n\n"
        "Expected output: [(1, 'Emperor')]"
    ),
    expected_output="[(1, 'Emperor')]",
    level=Level.MEDIUM,
    hints=["import sqlite3", "conn = sqlite3.connect(':memory:')", "conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')", "conn.execute('INSERT INTO users VALUES (1, ?)', ('Emperor',))", "conn.commit()", "rows = conn.execute('SELECT * FROM users').fetchall()", "print(rows)"]
)

medium2 = Task(
    description=(
        "🛡️  Parameterised Query\n\n"
        "Using parameterised queries, insert a user with name='Rahim'. Then fetch and print only that user's name.\n\n"
        "Expected output: Rahim"
    ),
    expected_output="Rahim",
    level=Level.MEDIUM,
    hints=["import sqlite3", "conn = sqlite3.connect(':memory:')", "conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')", "conn.execute('INSERT INTO users (name) VALUES (?)', ('Rahim',))", "conn.commit()", "row = conn.execute('SELECT name FROM users WHERE name=?', ('Rahim',)).fetchone()", "print(row[0])"]
)

hard1 = Task(
    description=(
        "🧰  DB Connection Helper Function\n\n"
        "Write a function `get_db(path=':memory:')` that returns a connection with row_factory = sqlite3.Row.\n"
        "Call it, create users table, insert 'Emperor', fetch and print dict version of the row.\n\n"
        "Expected output: {'id': 1, 'name': 'Emperor'}"
    ),
    expected_output="{'id': 1, 'name': 'Emperor'}",
    level=Level.HARD,
    hints=["import sqlite3", "def get_db(path=':memory:'):", "    conn = sqlite3.connect(path)", "    conn.row_factory = sqlite3.Row", "    return conn", "conn = get_db()", "conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')", "conn.execute('INSERT INTO users VALUES (1, ?)', ('Emperor',))", "conn.commit()", "row = conn.execute('SELECT * FROM users WHERE id=1').fetchone()", "print(dict(row))"]
)

hard2 = Task(
    description=(
        "🔐  Context Manager for DB\n\n"
        "Write a context manager `connect_db` using @contextmanager that yields a connection and closes it.\n"
        "Use it to create a table, insert a row, and print the row count after insertion.\n\n"
        "Expected output: 1"
    ),
    expected_output="1",
    level=Level.HARD,
    hints=["import sqlite3", "from contextlib import contextmanager", "@contextmanager", "def connect_db(path=':memory:'):", "    conn = sqlite3.connect(path)", "    try:", "        yield conn", "    finally:", "        conn.close()", "with connect_db() as conn:", "    conn.execute('CREATE TABLE test (id INTEGER PRIMARY KEY, val TEXT)')", "    conn.execute('INSERT INTO test VALUES (1, ?)', ('x',))", "    conn.commit()", "    count = conn.execute('SELECT COUNT(*) FROM test').fetchone()[0]", "    print(count)"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L57.json")
