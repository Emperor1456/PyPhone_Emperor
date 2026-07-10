import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "📦  Create a Tuple\n\n"
        "Create a tuple with values (1, 2, 3) and print it.\n\n"
        "Expected output: (1, 2, 3)"
    ),
    expected_output="(1, 2, 3)",
    level=Level.EASY,
    hints=["t = (1, 2, 3)", "print(t)"]
)

easy2 = Task(
    description=(
        "🔢  Access Tuple Elements\n\n"
        "Given t = (10, 20, 30), print the first element.\n\n"
        "Expected output: 10"
    ),
    expected_output="10",
    level=Level.EASY,
    hints=["t = (10, 20, 30)", "print(t[0])"]
)

medium1 = Task(
    description=(
        "🔄  Unpack a Tuple\n\n"
        "Unpack the tuple (5, 8) into variables x and y, then print x and y\n"
        "separated by a space.\n\n"
        "Expected output: 5 8"
    ),
    expected_output="5 8",
    level=Level.MEDIUM,
    hints=["point = (5, 8)", "x, y = point", "print(x, y)"]
)

medium2 = Task(
    description=(
        "🔁  Swap Variables with Tuple\n\n"
        "Set a = 10, b = 20. Swap their values in one line using tuple unpacking.\n"
        "Then print a and b separated by a space.\n\n"
        "Expected output: 20 10"
    ),
    expected_output="20 10",
    level=Level.MEDIUM,
    hints=["a, b = 10, 20", "a, b = b, a", "print(a, b)"]
)

hard1 = Task(
    description=(
        "📇  Tuple as Dictionary Key\n\n"
        "Create a dictionary with a tuple (1, 2) as a key mapping to 'point A'.\n"
        "Then print the value for that key.\n\n"
        "Expected output: point A"
    ),
    expected_output="point A",
    level=Level.HARD,
    hints=["d = {(1, 2): 'point A'}", "print(d[(1, 2)])"]
)

hard2 = Task(
    description=(
        "🧱  Multiple Return Values\n\n"
        "Define a function min_max(lst) that returns the minimum and maximum\n"
        "of a list as a tuple. Call it with [4,1,9,3] and print both values\n"
        "on separate lines.\n\n"
        "Expected output:\n1\n9"
    ),
    expected_output="1\n9",
    level=Level.HARD,
    hints=["def min_max(lst): return min(lst), max(lst)", "low, high = min_max([4,1,9,3])", "print(low)", "print(high)"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L17.json")
