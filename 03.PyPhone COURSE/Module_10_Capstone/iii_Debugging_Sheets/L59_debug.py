import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone TEXT NOT NULL UNIQUE)")
conn.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", ("Emperor", "123"))
# Missing commit
print(conn.execute("SELECT * FROM contacts").fetchall())"""

EXPECTED = "[(1, 'Emperor', '123')]"
HINTS = [
    "The insert is not visible because no commit was issued.",
    "Add 'conn.commit()' after the INSERT.",
    "Transactions must be committed to persist data."
]

if __name__ == "__main__":
    run_debug("L59: Full CRUD", BROKEN, EXPECTED, HINTS)
