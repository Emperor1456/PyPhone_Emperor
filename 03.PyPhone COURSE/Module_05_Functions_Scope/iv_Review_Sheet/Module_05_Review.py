import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy: Function with default parameter ──
easy = Task(
    description=(
        "👤  Custom Greeting\n\n"
        "Define a function `greet(name='Guest')` that returns `'Hello, ' + name`.\n"
        "Call it with no argument and print the result.\n\n"
        "Expected output: Hello, Guest"
    ),
    expected_output="Hello, Guest",
    level=Level.EASY,
    hints=[
        "def greet(name='Guest'):",
        "    return 'Hello, ' + name",
        "print(greet())"
    ]
)

# ── Medium: Early return & validation ──
medium = Task(
    description=(
        "🛡️  Safe Division Function\n\n"
        "Define a function `safe_divide(a, b)` that returns `None` if `b` is zero,\n"
        "otherwise returns `a / b`.\n"
        "Call it with `10, 2` and print the result.\n\n"
        "Expected output: 5.0"
    ),
    expected_output="5.0",
    level=Level.MEDIUM,
    hints=[
        "def safe_divide(a, b):",
        "    if b == 0: return None",
        "    return a / b",
        "print(safe_divide(10, 2))"
    ]
)

# ── Hard: Recursive sum of list ──
hard = Task(
    description=(
        "🔁  Recursive List Sum\n\n"
        "Define a recursive function `sum_list(lst)` that returns the sum of all elements.\n"
        "Call it with `[1, 2, 3, 4]` and print the result.\n\n"
        "Expected output: 10"
    ),
    expected_output="10",
    level=Level.HARD,
    hints=[
        "def sum_list(lst):",
        "    if not lst: return 0",
        "    return lst[0] + sum_list(lst[1:])",
        "print(sum_list([1, 2, 3, 4]))"
    ]
)

if __name__ == "__main__":
    run_sequence([easy, medium, hard],
                 save_path=MODULE_DIR,
                 progress_name=".progress_review_M05.json")
