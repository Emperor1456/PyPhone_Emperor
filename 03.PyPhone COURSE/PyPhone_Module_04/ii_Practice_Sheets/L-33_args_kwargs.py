import sys
sys.path.append("../..")
from practice_engine import Task, Level, run_task

# ─── Easy ─────────────────────────────────────
easy = Task(
    description="Define a function `sum_all(*args)` that returns the sum of all arguments. "
                "Call it with 1,2,3,4 and print the result.",
    expected_output="10",
    level=Level.EASY,
    hints=[
        "def sum_all(*args): return sum(args)",
        "print(sum_all(1,2,3,4))"
    ]
)

# ─── Medium ──────────────────────────────────
medium = Task(
    description="Define a function `print_info(**kwargs)` that returns a string like "
                "'name: Emperor, age: 18' (format: key: value, separated by comma+space). "
                "Call it with name='Emperor', age=18 and print the result.",
    expected_output="name: Emperor, age: 18",
    level=Level.MEDIUM,
    hints=[
        "def print_info(**kwargs):\n    parts = []\n    for k,v in kwargs.items():\n        parts.append(f'{k}: {v}')\n    return ', '.join(parts)",
        "print(print_info(name='Emperor', age=18))"
    ]
)

# ─── Hard ────────────────────────────────────
hard = Task(
    description="Define a function `mixed(*args, **kwargs)` that returns the sum of args if no kwargs are given, "
                "otherwise returns a string representation of kwargs. "
                "Call it with 1,2,3 and print the result on the first line, "
                "then call it with name='Emperor' and print the result on the second line.",
    expected_output="6\n{'name': 'Emperor'}",
    level=Level.HARD,
    hints=[
        "def mixed(*args, **kwargs):\n    if not kwargs:\n        return sum(args)\n    else:\n        return str(kwargs)",
        "print(mixed(1,2,3))",
        "print(mixed(name='Emperor'))"
    ]
)

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__":
    main()