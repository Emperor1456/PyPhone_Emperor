import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "👤  Greeting with Default\n\n"
        "Define greet(name='Guest') returning 'Hello ' + name.\n"
        "Call with no arguments and print.\n\n"
        "Expected output: Hello Guest"
    ),
    expected_output="Hello Guest",
    level=Level.EASY,
    hints=["def greet(name='Guest'): return 'Hello ' + name", "print(greet())"]
)

easy2 = Task(
    description=(
        "🔢  Power with Default Exponent\n\n"
        "Define power(x, exp=2) returning x**exp.\n"
        "Call with 2 only and print.\n\n"
        "Expected output: 4"
    ),
    expected_output="4",
    level=Level.EASY,
    hints=["def power(x, exp=2): return x ** exp", "print(power(2))"]
)

medium1 = Task(
    description=(
        "📝  Override Default\n\n"
        "Using the same greet function, call with 'Emperor' and print.\n\n"
        "Expected output: Hello Emperor"
    ),
    expected_output="Hello Emperor",
    level=Level.MEDIUM,
    hints=["print(greet('Emperor'))"]
)

medium2 = Task(
    description=(
        "🔧  Default with Type Casting\n\n"
        "Define increment(n, step=1) returning n + step.\n"
        "Call with 10 and print. Then call with 10, 5 and print.\n\n"
        "Expected output:\n11\n15"
    ),
    expected_output="11\n15",
    level=Level.MEDIUM,
    hints=["def increment(n, step=1): return n + step", "print(increment(10))", "print(increment(10, 5))"]
)

hard1 = Task(
    description=(
        "⚠️  Avoid Mutable Default\n\n"
        "Define add_item(item, items=None) that creates new list if None,\n"
        "appends item, returns list. Call twice with 'A' and 'B' separately,\n"
        "printing each result.\n\n"
        "Expected output:\n['A']\n['B']"
    ),
    expected_output="['A']\n['B']",
    level=Level.HARD,
    hints=["def add_item(item, items=None):", "    if items is None: items = []", "    items.append(item)", "    return items", "print(add_item('A'))", "print(add_item('B'))"]
)

hard2 = Task(
    description=(
        "🧪  Default with Validation\n\n"
        "Define connect(host, port=None) where if port is None, set to 5432.\n"
        "Print f'{host}:{port}'. Call with 'localhost'.\n\n"
        "Expected output: localhost:5432"
    ),
    expected_output="localhost:5432",
    level=Level.HARD,
    hints=["def connect(host, port=None):", "    if port is None: port = 5432", "    print(f'{host}:{port}')", "connect('localhost')"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L27.json")
