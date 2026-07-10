import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🌍  Global Variable Access\n\n"
        "Define a global variable x = 10. Write a function print_x() that prints x.\n"
        "Call the function.\n\n"
        "Expected output: 10"
    ),
    expected_output="10",
    level=Level.EASY,
    hints=["x = 10", "def print_x(): print(x)", "print_x()"]
)

easy2 = Task(
    description=(
        "🏠  Local Variable\n\n"
        "Define a function set_local() that sets y = 5 and prints y.\n"
        "Call it.\n\n"
        "Expected output: 5"
    ),
    expected_output="5",
    level=Level.EASY,
    hints=["def set_local(): y = 5; print(y)", "set_local()"]
)

medium1 = Task(
    description=(
        "🔧  Modify Global with `global`\n\n"
        "Given global counter = 0, define increment() that increments counter by 1\n"
        "using global keyword. Call it, then print counter.\n\n"
        "Expected output: 1"
    ),
    expected_output="1",
    level=Level.MEDIUM,
    hints=["counter = 0", "def increment():", "    global counter", "    counter += 1", "increment()", "print(counter)"]
)

medium2 = Task(
    description=(
        "🔐  Enclosing Scope with `nonlocal`\n\n"
        "Define outer() with local x=10, then inner() that uses nonlocal x\n"
        "to set x=20. Return x after calling inner(). Print outer().\n\n"
        "Expected output: 20"
    ),
    expected_output="20",
    level=Level.MEDIUM,
    hints=["def outer():", "    x = 10", "    def inner():", "        nonlocal x", "        x = 20", "    inner()", "    return x", "print(outer())"]
)

hard1 = Task(
    description=(
        "🧪  LEGB Order Demonstration\n\n"
        "Define x='global'. Inside outer() define x='enclosing', inside inner() print x.\n"
        "Call outer(). What prints? It should be 'enclosing' because LEGB order.\n\n"
        "Expected output: enclosing"
    ),
    expected_output="enclosing",
    level=Level.HARD,
    hints=["x = 'global'", "def outer():", "    x = 'enclosing'", "    def inner(): print(x)", "    inner()", "outer()"]
)

hard2 = Task(
    description=(
        "🔍  Shadowing Global\n\n"
        "Set x=100 globally. Define a function shadow() that sets x=200 locally\n"
        "and prints x. Call shadow(), then print global x. Show both.\n\n"
        "Expected output:\n200\n100"
    ),
    expected_output="200\n100",
    level=Level.HARD,
    hints=["x = 100", "def shadow():", "    x = 200", "    print(x)", "shadow()", "print(x)"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L29.json")
