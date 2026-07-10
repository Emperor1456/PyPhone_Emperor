import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks (2) ──────────────────────────

easy1 = Task(
    description=(
        "🔁  Sum Until Four – Accumulator Pattern\n\n"
        "Sum the numbers from 1 to 4 using a while loop.\n"
        "Print the total.\n\n"
        "Expected output: 10"
    ),
    expected_output="10",
    level=Level.EASY,
    hints=[
        "total = 0",
        "i = 1",
        "while i <= 4:",
        "    total += i",
        "    i += 1",
        "print(total)"
    ]
)

easy2 = Task(
    description=(
        "🚀  Countdown – Rocket Launch\n\n"
        "Print a countdown from 3 to 1, each on a new line,\n"
        "then print 'Liftoff!'.\n\n"
        "Expected output:\n3\n2\n1\nLiftoff!"
    ),
    expected_output="3\n2\n1\nLiftoff!",
    level=Level.EASY,
    hints=[
        "count = 3",
        "while count > 0:",
        "    print(count)",
        "    count -= 1",
        "print('Liftoff!')"
    ]
)

# ── Medium Tasks (2) ──────────────────────

medium1 = Task(
    description=(
        "🔢  Factorial – Product of Numbers\n\n"
        "Compute the factorial of 4 using a while loop.\n"
        "Print the result.\n\n"
        "Expected output: 24"
    ),
    expected_output="24",
    level=Level.MEDIUM,
    hints=[
        "n = 4",
        "prod = 1",
        "while n > 0:",
        "    prod *= n",
        "    n -= 1",
        "print(prod)"
    ]
)

medium2 = Task(
    description=(
        "🛡️  Password Gate – Input Validation\n\n"
        "Keep asking for a password until it's at least 8 characters.\n"
        "For this task, simulate: set password = 'short',\n"
        "then in a while loop, if len(password) < 8,\n"
        "set password = 'secure123' (to break the loop),\n"
        "then print 'Accepted'.\n\n"
        "Expected output: Accepted"
    ),
    expected_output="Accepted",
    level=Level.MEDIUM,
    hints=[
        "password = 'short'",
        "while len(password) < 8:",
        "    password = 'secure123'  # simulate correct input",
        "print('Accepted')"
    ]
)

# ── Hard Tasks (2) ────────────────────────

hard1 = Task(
    description=(
        "📈  Doubling Investment – Growth Tracking\n\n"
        "Start with x = 1. Count how many times you can double it\n"
        "before it exceeds 20. Print the count.\n\n"
        "Expected output: 5"
    ),
    expected_output="5",
    level=Level.HARD,
    hints=[
        "x = 1",
        "count = 0",
        "while x <= 20:",
        "    x *= 2",
        "    count += 1",
        "print(count)"
    ]
)

hard2 = Task(
    description=(
        "🏧  ATM Withdrawal – Sentinel‑Controlled\n\n"
        "A customer withdraws money until balance is insufficient.\n"
        "Given:\n"
        "  balance = 500\n\n"
        "Use a while loop with a sentinel: ask for amount,\n"
        "subtract if balance allows, stop if amount is 0.\n"
        "Simulate by processing these amounts in order:\n"
        "200, 250, 100, 0. Print the remaining balance after\n"
        "each successful withdrawal on a new line, and stop.\n\n"
        "Expected output:\n300\n50\n50"
    ),
    expected_output="300\n50\n50",
    level=Level.HARD,
    hints=[
        "balance = 500",
        "amounts = [200, 250, 100, 0]",
        "i = 0",
        "while i < len(amounts):",
        "    amt = amounts[i]",
        "    if amt == 0: break",
        "    if amt <= balance:",
        "        balance -= amt",
        "        print(balance)",
        "    i += 1"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L10.json")
