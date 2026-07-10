import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks (2) ──────────────────────────

easy1 = Task(
    description=(
        "🛑  Break – Find the Treasure\n\n"
        "Search the list [1, 2, 3, 4] for the number 3.\n"
        "Loop through the list, and when you find 3,\n"
        "print 'Found' and break.\n\n"
        "Expected output: Found"
    ),
    expected_output="Found",
    level=Level.EASY,
    hints=[
        "for x in [1, 2, 3, 4]:",
        "    if x == 3:",
        "        print('Found')",
        "        break"
    ]
)

easy2 = Task(
    description=(
        "⏩  Continue – Skip Even Numbers\n\n"
        "Print only odd numbers from 1 to 6 (inclusive),\n"
        "each on a new line. Use continue to skip evens.\n\n"
        "Expected output:\n1\n3\n5"
    ),
    expected_output="1\n3\n5",
    level=Level.EASY,
    hints=[
        "for i in range(1, 7):",
        "    if i % 2 == 0:",
        "        continue",
        "    print(i)"
    ]
)

# ── Medium Tasks (2) ──────────────────────

medium1 = Task(
    description=(
        "🚫  Filter Out Noise – Process Only Active\n\n"
        "Given a list of account statuses:\n"
        "['active', 'inactive', 'active', 'suspended']\n"
        "Print 'Sending statement' only for 'active' accounts.\n"
        "Use continue to skip others.\n\n"
        "Expected output:\nSending statement\nSending statement"
    ),
    expected_output="Sending statement\nSending statement",
    level=Level.MEDIUM,
    hints=[
        "statuses = ['active', 'inactive', 'active', 'suspended']",
        "for status in statuses:",
        "    if status != 'active':",
        "        continue",
        "    print('Sending statement')"
    ]
)

medium2 = Task(
    description=(
        "🛑  Early Stop – Exceed Limit\n\n"
        "Sum numbers from 1 to 10 using a while loop,\n"
        "but stop if the sum exceeds 30.\n"
        "Print the sum after the loop ends.\n\n"
        "Expected output: 36"
    ),
    expected_output="36",
    level=Level.MEDIUM,
    hints=[
        "res = 0",
        "i = 1",
        "while i <= 10:",
        "    res += i",
        "    if res > 30:",
        "        break",
        "    i += 1",
        "print(res)"
    ]
)

# ── Hard Tasks (2) ────────────────────────

hard1 = Task(
    description=(
        "🧹  Pass – Placeholder for Future Logic\n\n"
        "Create a for loop that iterates over range(5).\n"
        "Inside, if i == 2, use pass (placeholder),\n"
        "otherwise print i.\n"
        "After the loop, print 'Done'.\n\n"
        "Expected output:\n0\n1\n3\n4\nDone"
    ),
    expected_output="0\n1\n3\n4\nDone",
    level=Level.HARD,
    hints=[
        "for i in range(5):",
        "    if i == 2:",
        "        pass",
        "    else:",
        "        print(i)",
        "print('Done')"
    ]
)

hard2 = Task(
    description=(
        "🔁  Validate & Retry – Interactive Input\n\n"
        "Simulate an input loop that asks for a positive number.\n"
        "Start with an 'input' value of -5 (as a variable).\n"
        "Use a while loop: if the number <= 0, print 'Invalid'\n"
        "and set the number to 10 (simulating a corrected input).\n"
        "When the number > 0, print 'Valid' and break.\n\n"
        "Expected output:\nInvalid\nValid"
    ),
    expected_output="Invalid\nValid",
    level=Level.HARD,
    hints=[
        "num = -5",
        "while True:",
        "    if num <= 0:",
        "        print('Invalid')",
        "        num = 10  # simulate correction",
        "    else:",
        "        print('Valid')",
        "        break"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L12.json")
