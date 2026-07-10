import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "⚡  Generator Expression Sum\n\n"
        "Sum the squares of numbers 1 through 5 using a generator expression inside sum(). Print the total.\n\n"
        "Expected output: 55"
    ),
    expected_output="55",
    level=Level.EASY,
    hints=["total = sum(x*x for x in range(1, 6))", "print(total)"]
)

easy2 = Task(
    description=(
        "🔁  List from Generator\n\n"
        "Create a generator expression (x*2 for x in range(3)), convert to list, and print it.\n\n"
        "Expected output: [0, 2, 4]"
    ),
    expected_output="[0, 2, 4]",
    level=Level.EASY,
    hints=["gen = (x*2 for x in range(3))", "print(list(gen))"]
)

medium1 = Task(
    description=(
        "🧵  Simple yield Function\n\n"
        "Define a generator function `gen()` that yields 1, then 2, then 3.\n"
        "Print list(gen()).\n\n"
        "Expected output: [1, 2, 3]"
    ),
    expected_output="[1, 2, 3]",
    level=Level.MEDIUM,
    hints=["def gen():", "    yield 1", "    yield 2", "    yield 3", "print(list(gen()))"]
)

medium2 = Task(
    description=(
        "🐇  Fibonacci Generator\n\n"
        "Define a generator `fib_gen(n)` that yields the first n Fibonacci numbers (starting 0,1).\n"
        "Call with n=5 and print as list.\n\n"
        "Expected output: [0, 1, 1, 2, 3]"
    ),
    expected_output="[0, 1, 1, 2, 3]",
    level=Level.MEDIUM,
    hints=["def fib_gen(n):", "    a, b = 0, 1", "    for _ in range(n):", "        yield a", "        a, b = b, a+b", "print(list(fib_gen(5)))"]
)

hard1 = Task(
    description=(
        "📉  Countdown Generator\n\n"
        "Define a generator `countdown(n)` that yields numbers from n down to 1.\n"
        "Call with n=5 and print as list.\n\n"
        "Expected output: [5, 4, 3, 2, 1]"
    ),
    expected_output="[5, 4, 3, 2, 1]",
    level=Level.HARD,
    hints=["def countdown(n):", "    while n > 0:", "        yield n", "        n -= 1", "print(list(countdown(5)))"]
)

hard2 = Task(
    description=(
        "📖  Read File Lines Generator\n\n"
        "Define a generator `read_lines(filepath)` that opens a file, yields each stripped line.\n"
        "For this task, simulate: iterate over a list ['Hello','World'] and yield each item.\n"
        "Call and print as list.\n\n"
        "Expected output: ['Hello', 'World']"
    ),
    expected_output="['Hello', 'World']",
    level=Level.HARD,
    hints=["def read_lines():", "    for line in ['Hello', 'World']:", "        yield line", "print(list(read_lines()))"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L54.json")
