import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

# ─── Easy: simple product label ─────────────────
easy = Task(
    description=(
        "Create a product label:\n"
        "name = 'Wireless Mouse'\n"
        "price = 24.99\n"
        "stock = 150\n"
        "Print each on a separate line."
    ),
    expected_output="Wireless Mouse\n24.99\n150",
    level=Level.EASY,
    hints=[
        "name = 'Wireless Mouse'",
        "price = 24.99",
        "stock = 150",
        "print(name)",
        "print(price)",
        "print(stock)"
    ]
)

# ─── Medium: order receipt ─────────────────────
medium = Task(
    description=(
        "A customer buys 4 monitors at $249.95 each.\n"
        "qty = 4\n"
        "unit = 249.95\n"
        "total = qty * unit\n"
        "Print exactly:\n"
        "Total: $999.80"
    ),
    expected_output="Total: $999.80",
    level=Level.MEDIUM,
    hints=[
        "qty = 4",
        "unit = 249.95",
        "total = qty * unit",
        "print(f'Total: ${total:.2f}')"
    ]
)

# ─── Hard: dynamic typing demo ─────────────────
hard = Task(
    description=(
        "Store an integer 1234 in a variable.\n"
        "Print its type.\n"
        "Reassign the same variable to '1234'.\n"
        "Print its type again.\n"
        "Output must be:\n"
        "<class 'int'>\n"
        "<class 'str'>"
    ),
    expected_output="<class 'int'>\n<class 'str'>",
    level=Level.HARD,
    hints=[
        "x = 1234",
        "print(type(x))",
        "x = '1234'",
        "print(type(x))"
    ]
)

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__":
    main()
