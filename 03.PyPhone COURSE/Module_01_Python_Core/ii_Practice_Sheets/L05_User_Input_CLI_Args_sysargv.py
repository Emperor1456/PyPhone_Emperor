import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks (2) ──────────────────────────

easy1 = Task(
    description=(
        "📟  Command‑Line Arguments – Default Value\n\n"
        "Write a script that prints the first command‑line\n"
        "argument if it exists, otherwise prints 'none'.\n\n"
        "(The engine will run with no extra arguments,\n"
        "so your code should detect that and print 'none'.)\n\n"
        "Expected output: none"
    ),
    expected_output="none",
    level=Level.EASY,
    hints=[
        "import sys",
        "if len(sys.argv) > 1:",
        "    print(sys.argv[1])",
        "else:",
        "    print('none')"
    ]
)

easy2 = Task(
    description=(
        "🔢  Argument Count\n\n"
        "Print the total number of command‑line arguments,\n"
        "including the script name itself.\n\n"
        "When run without extra arguments, sys.argv contains\n"
        "exactly one element (the script path).\n\n"
        "Expected output: 1"
    ),
    expected_output="1",
    level=Level.EASY,
    hints=["import sys", "print(len(sys.argv))"]
)

# ── Medium Tasks (2) ──────────────────────

medium1 = Task(
    description=(
        "🔤  Argument Processor – Uppercase Converter\n\n"
        "If the user provides exactly one argument (so sys.argv\n"
        "has length 2), print that argument in uppercase.\n"
        "Otherwise, print 'usage'.\n\n"
        "Expected output: usage"
    ),
    expected_output="usage",
    level=Level.MEDIUM,
    hints=[
        "import sys",
        "if len(sys.argv) == 2:",
        "    print(sys.argv[1].upper())",
        "else:",
        "    print('usage')"
    ]
)

medium2 = Task(
    description=(
        "🏷️  Named Argument – Greeting\n\n"
        "If the first argument is provided, print 'Hello, '\n"
        "followed by that argument. Otherwise, print\n"
        "'Hello, Guest'.\n\n"
        "Expected output: Hello, Guest"
    ),
    expected_output="Hello, Guest",
    level=Level.MEDIUM,
    hints=[
        "import sys",
        "name = sys.argv[1] if len(sys.argv) > 1 else 'Guest'",
        "print(f'Hello, {name}')"
    ]
)

# ── Hard Tasks (2) ────────────────────────

hard1 = Task(
    description=(
        "🛡️  Access Control – Admin Check\n\n"
        "The script expects a role as the first argument.\n"
        "If the first argument is 'admin', print 'Access granted'.\n"
        "Otherwise, print 'Access denied'.\n\n"
        "Expected output: Access denied"
    ),
    expected_output="Access denied",
    level=Level.HARD,
    hints=[
        "import sys",
        "if len(sys.argv) > 1 and sys.argv[1] == 'admin':",
        "    print('Access granted')",
        "else:",
        "    print('Access denied')"
    ]
)

hard2 = Task(
    description=(
        "🔐  Multiple Arguments – Sum Checker\n\n"
        "The script should accept two numbers as arguments.\n"
        "If exactly two arguments are provided, print their sum\n"
        "(convert to float). Otherwise, print 'error'.\n\n"
        "Expected output: error"
    ),
    expected_output="error",
    level=Level.HARD,
    hints=[
        "import sys",
        "if len(sys.argv) == 3:",
        "    a = float(sys.argv[1])",
        "    b = float(sys.argv[2])",
        "    print(a + b)",
        "else:",
        "    print('error')"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L05.json")
