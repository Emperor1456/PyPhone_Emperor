import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🔙  Return a Value\n\n"
        "Define double(x) returning 2*x. Call with 5 and print.\n\n"
        "Expected output: 10"
    ),
    expected_output="10",
    level=Level.EASY,
    hints=["def double(x): return 2 * x", "print(double(5))"]
)

easy2 = Task(
    description=(
        "➕  Return Sum\n\n"
        "Define add(a, b) returning a+b. Call with 3 and 5, print.\n\n"
        "Expected output: 8"
    ),
    expected_output="8",
    level=Level.EASY,
    hints=["def add(a, b): return a + b", "print(add(3, 5))"]
)

medium1 = Task(
    description=(
        "⏪  Early Return – Absolute Value\n\n"
        "Define absolute(x) returning x if x>=0 else -x.\n"
        "Call with -7 and print.\n\n"
        "Expected output: 7"
    ),
    expected_output="7",
    level=Level.MEDIUM,
    hints=["def absolute(x):", "    if x >= 0: return x", "    return -x", "print(absolute(-7))"]
)

medium2 = Task(
    description=(
        "🚫  Early Return – Safe Division\n\n"
        "Define safe_divide(a, b) returning None if b==0 else a/b.\n"
        "Call with 10,2 and print.\n\n"
        "Expected output: 5.0"
    ),
    expected_output="5.0",
    level=Level.MEDIUM,
    hints=["def safe_divide(a, b):", "    if b == 0: return None", "    return a / b", "print(safe_divide(10, 2))"]
)

hard1 = Task(
    description=(
        "📦  Return Multiple Values\n\n"
        "Define min_max(lst) returning (min, max). Call with [4,1,9,3].\n"
        "Print min and max on separate lines.\n\n"
        "Expected output:\n1\n9"
    ),
    expected_output="1\n9",
    level=Level.HARD,
    hints=["def min_max(lst): return min(lst), max(lst)", "low, high = min_max([4,1,9,3])", "print(low)", "print(high)"]
)

hard2 = Task(
    description=(
        "🔍  Return Boolean – Even Check\n\n"
        "Define is_even(n) returning True if n%2==0 else False.\n"
        "Call with 8 and print.\n\n"
        "Expected output: True"
    ),
    expected_output="True",
    level=Level.HARD,
    hints=["def is_even(n): return n % 2 == 0", "print(is_even(8))"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L26.json")
