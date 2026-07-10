import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
conn.execute("INSERT INTO users VALUES (1, 'Emperor')")

rows = conn.execute("SELECT * FROM users").fetchall()
print(rows)"""

EXPECTED = "[(1, 'Emperor')]"
HINTS = [
    "The insert needs a commit to be visible.",
    "Add 'conn.commit()' after the insert.",
    "Transactions must be committed."
]

if __name__ == "__main__":
    run_debug("L57: DB Helper", BROKEN, EXPECTED, HINTS)
