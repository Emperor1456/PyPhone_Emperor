import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks (2) ──────────────────────────

easy1 = Task(
    description=(
        "✅  Basic Comparison – Stock Availability\n\n"
        "Check if the quantity in stock is greater than 0.\n"
        "Print the boolean result.\n\n"
        "Given:\n"
        "  stock = 12\n\n"
        "Expected output: True"
    ),
    expected_output="True",
    level=Level.EASY,
    hints=["stock = 12", "print(stock > 0)"]
)

easy2 = Task(
    description=(
        "🔗  Logical AND – Qualified Customer\n\n"
        "A customer qualifies for a loan if they are over 18\n"
        "AND have a monthly income above 2000.\n\n"
        "Given:\n"
        "  age = 25\n"
        "  income = 2100\n\n"
        "Print whether the customer qualifies (True/False).\n"
        "Expected output: True"
    ),
    expected_output="True",
    level=Level.EASY,
    hints=["age = 25", "income = 2100", "print(age > 18 and income > 2000)"]
)

# ── Medium Tasks (2) ──────────────────────

medium1 = Task(
    description=(
        "🧪  Truthiness Check – Empty vs Non‑Empty\n\n"
        "Python treats empty collections as False.\n"
        "Create an empty list and a non‑empty string.\n"
        "Print their boolean values (True/False) separated\n"
        "by a space.\n\n"
        "Expected output: False True"
    ),
    expected_output="False True",
    level=Level.MEDIUM,
    hints=["empty_list = []", "non_empty = 'hello'", "print(bool(empty_list), bool(non_empty))"]
)

medium2 = Task(
    description=(
        "⚡  Short‑Circuit Evaluation – Safe Division\n\n"
        "A division should only be calculated if the divisor\n"
        "is not zero. Use short‑circuit logic to print\n"
        "'safe' if divisor != 0 and the result > 0.\n\n"
        "Given:\n"
        "  divisor = 5\n"
        "  dividend = 10\n\n"
        "Expected output: safe"
    ),
    expected_output="safe",
    level=Level.MEDIUM,
    hints=["divisor = 5", "dividend = 10", "if divisor != 0 and dividend / divisor > 0:", "    print('safe')", "else:", "    print('unsafe')"]
)

# ── Hard Tasks (2) ────────────────────────

hard1 = Task(
    description=(
        "🔍  Identity vs Equality – List Comparison\n\n"
        "Create two separate lists with the same content.\n"
        "Print the result of:\n"
        "  1. a == b\n"
        "  2. a is b\n"
        "Separated by a space.\n\n"
        "Expected output: True False"
    ),
    expected_output="True False",
    level=Level.HARD,
    hints=["a = [1, 2]", "b = [1, 2]", "print(a == b, a is b)"]
)

hard2 = Task(
    description=(
        "🚫  None Check – Flag Validation\n\n"
        "A sensor returns None when no reading is available.\n"
        "Check if a reading is None and print 'No data'\n"
        "if so; otherwise print 'Data present'.\n\n"
        "Given:\n"
        "  reading = None\n\n"
        "Expected output: No data"
    ),
    expected_output="No data",
    level=Level.HARD,
    hints=["reading = None", "if reading is None:", "    print('No data')", "else:", "    print('Data present')"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L06.json")
