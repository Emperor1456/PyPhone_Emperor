import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy = Task(
    description=(
        "🧮  Math Module\n\n"
        "Import math and print the value of pi.\n\n"
        "Expected output: 3.141592653589793"
    ),
    expected_output="3.141592653589793",
    level=Level.EASY,
    hints=["import math", "print(math.pi)"]
)

medium = Task(
    description=(
        "⚡  Generator Expression Sum\n\n"
        "Sum the squares of numbers 1 through 5 using a generator expression inside sum().\n"
        "Print the result.\n\n"
        "Expected output: 55"
    ),
    expected_output="55",
    level=Level.MEDIUM,
    hints=["total = sum(x*x for x in range(1, 6))", "print(total)"]
)

hard = Task(
    description=(
        "🔗  SQLite Connection Helper\n\n"
        "Write a function `get_db(path=':memory:')` that returns a connection with\n"
        "`row_factory = sqlite3.Row`. Call it, create a table `test` with one column\n"
        "`value TEXT`, insert 'OK', and print the inserted value by fetching it.\n\n"
        "Expected output: OK"
    ),
    expected_output="OK",
    level=Level.HARD,
    hints=[
        "import sqlite3",
        "def get_db(path=':memory:'):",
        "    conn = sqlite3.connect(path)",
        "    conn.row_factory = sqlite3.Row",
        "    return conn",
        "conn = get_db()",
        "conn.execute('CREATE TABLE test (value TEXT)')",
        "conn.execute('INSERT INTO test VALUES (?)', ('OK',))",
        "conn.commit()",
        "row = conn.execute('SELECT value FROM test').fetchone()",
        "print(row[0])"
    ]
)

if __name__ == "__main__":
    run_sequence([easy, medium, hard],
                 save_path=MODULE_DIR,
                 progress_name=".progress_review_M09.json")
