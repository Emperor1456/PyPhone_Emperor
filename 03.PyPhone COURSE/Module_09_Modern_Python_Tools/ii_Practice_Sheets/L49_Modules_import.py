import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🧮  Import Math and Print Pi\n\n"
        "Import the math module and print the value of pi.\n\n"
        "Expected output: 3.141592653589793"
    ),
    expected_output="3.141592653589793",
    level=Level.EASY,
    hints=["import math", "print(math.pi)"]
)

easy2 = Task(
    description=(
        "🎲  Random Integer\n\n"
        "Import random and print a random integer between 1 and 10 (inclusive).\n"
        "For reproducibility, set random.seed(42) before generating.\n\n"
        "Expected output: 2 (with seed 42)"
    ),
    expected_output="2",
    level=Level.EASY,
    hints=["import random", "random.seed(42)", "print(random.randint(1, 10))"]
)

medium1 = Task(
    description=(
        "📅  Current Date and Time\n\n"
        "From datetime import datetime. Print the current year using datetime.now().year.\n\n"
        "Expected output: (current year, e.g., 2026)"
    ),
    expected_output=str(__import__('datetime').datetime.now().year),
    level=Level.MEDIUM,
    hints=["from datetime import datetime", "print(datetime.now().year)"]
)

medium2 = Task(
    description=(
        "📂  List Files in Current Directory\n\n"
        "Import os. Print a sorted list of files/folders in the current directory.\n"
        "(The list will contain at least the module folders.)\n\n"
        "Expected output: (a list of directory contents)"
    ),
    expected_output=str(sorted(os.listdir('.'))),
    level=Level.MEDIUM,
    hints=["import os", "print(sorted(os.listdir('.')))"]
)

hard1 = Task(
    description=(
        "🧰  Custom Module Import\n\n"
        "Create a small module: write a file 'mycalc.py' with function add(a,b) returning a+b.\n"
        "Then in your practice script, import mycalc and call mycalc.add(3,4). Print the result.\n"
        "(The engine will handle file creation; just write the import and call.)\n\n"
        "Expected output: 7"
    ),
    expected_output="7",
    level=Level.HARD,
    hints=[
        "# First, the engine creates mycalc.py with:",
        "# def add(a,b): return a+b",
        "import mycalc",
        "print(mycalc.add(3, 4))"
    ]
)

hard2 = Task(
    description=(
        "⚡  Import Specific Function\n\n"
        "From the math module, import sqrt and ceil. Print sqrt(16) and ceil(3.2) on two lines.\n\n"
        "Expected output:\n4.0\n4"
    ),
    expected_output="4.0\n4",
    level=Level.HARD,
    hints=[
        "from math import sqrt, ceil",
        "print(sqrt(16))",
        "print(ceil(3.2))"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L49.json")
