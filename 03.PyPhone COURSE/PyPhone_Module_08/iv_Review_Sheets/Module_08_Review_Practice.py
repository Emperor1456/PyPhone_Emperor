import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description=(
        "Use a list comprehension to generate squares\n"
        "of numbers 1 through 5, and print the list."
    ),
    expected_output="[1, 4, 9, 16, 25]",
    level=Level.EASY,
    hints=[
        "print([x**2 for x in range(1,6)])"
    ]
)

medium = Task(
    description=(
        "Define a decorator `title` that takes a string\n"
        "and returns it wrapped as '=== STR ==='.\n"
        "Apply it to a function `message()` that\n"
        "returns 'Hello'. Call and print the result."
    ),
    expected_output="=== Hello ===",
    level=Level.MEDIUM,
    hints=[
        "def title(func):\n    def wrapper():\n        return f'=== {func()} ==='\n    return wrapper",
        "@title\ndef message():\n    return 'Hello'",
        "print(message())"
    ]
)

hard = Task(
    description=(
        "Data Pipeline with Generator & Decorator\n\n"
        "You have a list of sales figures:\n"
        "  sales = [120, 85, 210, 45, 330]\n\n"
        "Build the following pipeline:\n"
        "1. Define a generator `filter_high` that yields\n"
        "   values >= 100 from an iterable.\n"
        "2. Define a decorator `add_header` that wraps a\n"
        "   function's output with '--- REPORT ---' on the\n"
        "   first line and '--- END ---' on the last line.\n"
        "3. Define a function `build_report` that creates\n"
        "   a report string by iterating over the generator\n"
        "   and appending each value to a list, then\n"
        "   joining with newlines.\n"
        "4. Decorate `build_report` with `add_header`.\n"
        "5. Call `build_report(sales)` and print the result.\n\n"
        "Output must be exactly:\n"
        "--- REPORT ---\n"
        "120\n"
        "210\n"
        "330\n"
        "--- END ---"
    ),
    expected_output="--- REPORT ---\n120\n210\n330\n--- END ---",
    level=Level.HARD,
    hints=[
        "def filter_high(iterable):\n    for val in iterable:\n        if val >= 100:\n            yield val",
        "def add_header(func):\n    def wrapper(*args):\n        result = func(*args)\n        return f'--- REPORT ---\\n{result}\\n--- END ---'\n    return wrapper",
        "@add_header\ndef build_report(data):\n    return '\\n'.join(str(v) for v in filter_high(data))",
        "sales = [120, 85, 210, 45, 330]",
        "print(build_report(sales))"
    ]
)

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__":
    main()
