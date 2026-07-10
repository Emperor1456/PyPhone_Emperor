import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy = Task(
    description=(
        "🚫  Catch ValueError\n\n"
        "Try to convert the string 'abc' to an integer.\n"
        "Catch ValueError and print 'error'.\n\n"
        "Expected output: error"
    ),
    expected_output="error",
    level=Level.EASY,
    hints=[
        "try:",
        "    int('abc')",
        "except ValueError:",
        "    print('error')"
    ]
)

medium = Task(
    description=(
        "📂  File Not Found Handler\n\n"
        "Try to open a non‑existent file 'nofile.txt' for reading.\n"
        "Catch FileNotFoundError and print 'missing'.\n\n"
        "Expected output: missing"
    ),
    expected_output="missing",
    level=Level.MEDIUM,
    hints=[
        "try:",
        "    open('nofile.txt')",
        "except FileNotFoundError:",
        "    print('missing')"
    ]
)

hard = Task(
    description=(
        "🧪  Complete Error Handling Pattern\n\n"
        "Use try/except/else/finally with a safe operation:\n"
        "  • Set x = 1 in try.\n"
        "  • Print 'try' in try.\n"
        "  • Print 'else' in else.\n"
        "  • Print 'finally' in finally.\n\n"
        "Expected output:\ntry\nelse\nfinally"
    ),
    expected_output="try\nelse\nfinally",
    level=Level.HARD,
    hints=[
        "try:",
        "    x = 1",
        "    print('try')",
        "except:",
        "    pass",
        "else:",
        "    print('else')",
        "finally:",
        "    print('finally')"
    ]
)

if __name__ == "__main__":
    run_sequence([easy, medium, hard],
                 save_path=MODULE_DIR,
                 progress_name=".progress_review_M06.json")
