import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description=(
        "Define a function `greet(name, greeting='Hello')` that\n"
        "returns 'greeting, name!'. Call it with 'Emperor' and\n"
        "print the result."
    ),
    expected_output="Hello, Emperor!",
    level=Level.EASY,
    hints=[
        "def greet(name, greeting='Hello'):\n    return f'{greeting}, {name}!'",
        "print(greet('Emperor'))"
    ]
)

medium = Task(
    description=(
        "Define a function `apply_discount(prices, discount=0.1)`\n"
        "that takes a list of prices and returns a new list with\n"
        "the discount applied (price * (1 - discount)). Use a\n"
        "lambda to map the discount. Test with [100,200,50] and\n"
        "print the result list."
    ),
    expected_output="[90.0, 180.0, 45.0]",
    level=Level.MEDIUM,
    hints=[
        "def apply_discount(prices, discount=0.1):\n    return list(map(lambda p: p * (1 - discount), prices))",
        "print(apply_discount([100,200,50]))"
    ]
)

hard = Task(
    description=(
        "Mini Investment Tracker\n\n"
        "Use functions to simulate investment growth:\n"
        "- `compound(balance, rate, years)` returns final\n"
        "  amount after compound interest (recursive).\n"
        "- `contribute(balance, amount)` adds to balance.\n"
        "- `statement(name, balance, **extras)` returns a\n"
        "  formatted string.\n\n"
        "Start with balance=1000, rate=0.1, years=3.\n"
        "After compounding, contribute 500.\n"
        "Print a statement with account='Emperor' and\n"
        "a bonus comment='Top performer'.\n\n"
        "Expected output exactly:\n"
        "Emperor: $1831.00\n"
        "Comment: Top performer"
    ),
    expected_output="Emperor: $1831.00\nComment: Top performer",
    level=Level.HARD,
    hints=[
        "def compound(balance, rate, years):\n    return balance if years == 0 else compound(balance * (1+rate), rate, years-1)",
        "def contribute(balance, amount):\n    return balance + amount",
        "def statement(name, balance, **extras):\n    return f\"{name}: ${balance:.2f}\" + (f\"\\nComment: {extras['comment']}\" if 'comment' in extras else '')",
        "balance = 1000",
        "balance = compound(balance, 0.1, 3)",
        "balance = contribute(balance, 500)",
        "print(statement('Emperor', balance, comment='Top performer'))"
    ]
)

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__":
    main()
