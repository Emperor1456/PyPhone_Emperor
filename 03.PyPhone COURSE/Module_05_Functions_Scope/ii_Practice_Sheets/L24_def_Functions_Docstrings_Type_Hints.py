import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🔧  Define a Simple Function\n\n"
        "Define a function hello() that prints 'Hello, Emperor'.\n"
        "Call the function.\n\n"
        "Expected output: Hello, Emperor"
    ),
    expected_output="Hello, Emperor",
    level=Level.EASY,
    hints=["def hello(): print('Hello, Emperor')", "hello()"]
)

easy2 = Task(
    description=(
        "📝  Function with Docstring\n\n"
        "Define a function add(a, b) that returns the sum of a and b.\n"
        "Include a docstring: 'Return the sum of two numbers.'\n"
        "Call it with 3 and 5, and print the result.\n\n"
        "Expected output: 8"
    ),
    expected_output="8",
    level=Level.EASY,
    hints=["def add(a, b):", "    'Return the sum of two numbers.'", "    return a + b", "print(add(3, 5))"]
)

medium1 = Task(
    description=(
        "🏷️  Function with Type Hints\n\n"
        "Define a function multiply(x: float, y: float) -> float that returns x * y.\n"
        "Include a docstring: 'Multiply two floats.'\n"
        "Call it with 2.5 and 4.0, and print the result.\n\n"
        "Expected output: 10.0"
    ),
    expected_output="10.0",
    level=Level.MEDIUM,
    hints=["def multiply(x: float, y: float) -> float:", "    'Multiply two floats.'", "    return x * y", "print(multiply(2.5, 4.0))"]
)

medium2 = Task(
    description=(
        "📋  Function with Multiple Returns\n\n"
        "Define a function min_max(numbers) that returns both min and max of a list.\n"
        "Call with [4, 1, 9, 3] and print both values separated by a space.\n\n"
        "Expected output: 1 9"
    ),
    expected_output="1 9",
    level=Level.MEDIUM,
    hints=["def min_max(numbers): return min(numbers), max(numbers)", "low, high = min_max([4, 1, 9, 3])", "print(low, high)"]
)

hard1 = Task(
    description=(
        "🧪  Function with Validation\n\n"
        "Define a function safe_divide(a, b) that returns a / b if b != 0,\n"
        "otherwise returns None. Call with 10 and 2, print the result.\n\n"
        "Expected output: 5.0"
    ),
    expected_output="5.0",
    level=Level.HARD,
    hints=["def safe_divide(a, b):", "    if b == 0: return None", "    return a / b", "print(safe_divide(10, 2))"]
)

hard2 = Task(
    description=(
        "🔁  Recursive Function – Sum of List\n\n"
        "Define a recursive function sum_list(lst) that returns sum of all elements.\n"
        "Base case: empty list returns 0. Recursive: first + sum_list(rest).\n"
        "Call with [1, 2, 3, 4] and print result.\n\n"
        "Expected output: 10"
    ),
    expected_output="10",
    level=Level.HARD,
    hints=["def sum_list(lst):", "    if not lst: return 0", "    return lst[0] + sum_list(lst[1:])", "print(sum_list([1, 2, 3, 4]))"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L24.json")
