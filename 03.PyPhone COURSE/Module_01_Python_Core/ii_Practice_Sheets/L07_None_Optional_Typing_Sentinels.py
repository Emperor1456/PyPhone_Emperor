import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks (2) ──────────────────────────

easy1 = Task(
    description=(
        "🕳️  None Check – Missing Sensor Data\n\n"
        "A warehouse sensor returns None when no reading\n"
        "is available. Check if a variable is None and print\n"
        "'No data' if so, else 'Data found'.\n\n"
        "Given:\n"
        "  reading = None\n\n"
        "Expected output: No data"
    ),
    expected_output="No data",
    level=Level.EASY,
    hints=["reading = None", "if reading is None: print('No data')", "else: print('Data found')"]
)

easy2 = Task(
    description=(
        "🧪  Function Returning None – Missing Record\n\n"
        "Define a function `find_item()` that simply returns None.\n"
        "Call it, store the result, and print 'Missing'\n"
        "if the result is None, else 'Found'.\n\n"
        "Expected output: Missing"
    ),
    expected_output="Missing",
    level=Level.EASY,
    hints=["def find_item(): return None", "result = find_item()", "if result is None: print('Missing')", "else: print('Found')"]
)

# ── Medium Tasks (2) ──────────────────────

medium1 = Task(
    description=(
        "🛡️  Sentinel Value – Mutable Default Fix\n\n"
        "Write a function `add_item(item, items=None)` that:\n"
        "  • If items is None, creates a new empty list.\n"
        "  • Appends item to the list.\n"
        "  • Returns the list.\n\n"
        "Call it with 'A' and print the returned list.\n\n"
        "Expected output: ['A']"
    ),
    expected_output="['A']",
    level=Level.MEDIUM,
    hints=[
        "def add_item(item, items=None):",
        "    if items is None: items = []",
        "    items.append(item)",
        "    return items",
        "print(add_item('A'))"
    ]
)

medium2 = Task(
    description=(
        "🔧  Default Config with None Sentinel\n\n"
        "Write a function `connect(host, port=None)` that:\n"
        "  • If port is None, sets port to 5432 (default).\n"
        "  • Prints host:port.\n\n"
        "Call it with 'localhost' and no port.\n\n"
        "Expected output: localhost:5432"
    ),
    expected_output="localhost:5432",
    level=Level.MEDIUM,
    hints=[
        "def connect(host, port=None):",
        "    if port is None: port = 5432",
        "    print(f'{host}:{port}')",
        "connect('localhost')"
    ]
)

# ── Hard Tasks (2) ────────────────────────

hard1 = Task(
    description=(
        "⚠️  Safe Division – Return None on Error\n\n"
        "Write a function `safe_divide(a, b)` that returns\n"
        "None if b is zero, otherwise returns a / b.\n\n"
        "Call it with 10 and 2, and print the result.\n\n"
        "Expected output: 5.0"
    ),
    expected_output="5.0",
    level=Level.HARD,
    hints=[
        "def safe_divide(a, b):",
        "    if b == 0: return None",
        "    return a / b",
        "print(safe_divide(10, 2))"
    ]
)

hard2 = Task(
    description=(
        "🔍  User Lookup – None for Not Found\n\n"
        "Write a function `find_user(user_id)` that looks up\n"
        "a user in a dictionary:\n"
        "  {1: 'Emperor', 2: 'Rahim'}\n"
        "Return the name if found, else None.\n\n"
        "Call it with id=1 and print the result.\n\n"
        "Expected output: Emperor"
    ),
    expected_output="Emperor",
    level=Level.HARD,
    hints=[
        "def find_user(user_id):",
        "    users = {1: 'Emperor', 2: 'Rahim'}",
        "    return users.get(user_id)",
        "print(find_user(1))"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L07.json")
