import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy: Tax Bracket (if‑elif‑else) ──
easy = Task(
    description=(
        "💰  Imperial Tax Bracket\n\n"
        "Given:\n"
        "  income = 45000\n\n"
        "Print the correct tax bracket:\n"
        "  • 50000+ → 'High'\n"
        "  • 20000‑49999 → 'Medium'\n"
        "  • below 20000 → 'Low'\n\n"
        "Use if‑elif‑else.\n"
        "Expected output: Medium"
    ),
    expected_output="Medium",
    level=Level.EASY,
    hints=[
        "income = 45000",
        "if income >= 50000: print('High')",
        "elif income >= 20000: print('Medium')",
        "else: print('Low')"
    ]
)

# ── Medium: Queue Processor (while) ──
medium = Task(
    description=(
        "📋  Order Queue Processor\n\n"
        "Process orders until the queue is empty.\n"
        "Given:\n"
        "  orders = ['A', 'B', 'C']\n\n"
        "Print each order on a new line, then print 'Done'.\n\n"
        "Expected output:\nA\nB\nC\nDone"
    ),
    expected_output="A\nB\nC\nDone",
    level=Level.MEDIUM,
    hints=[
        "orders = ['A', 'B', 'C']",
        "while orders:",
        "    print(orders.pop(0))",
        "print('Done')"
    ]
)

# ── Hard: Filter & Format (for + continue) ──
hard = Task(
    description=(
        "🔢  Odd Number Filter\n\n"
        "Print only odd numbers from 1 to 10, each on a new line.\n"
        "Use a for loop and continue to skip evens.\n"
        "End with 'End'.\n\n"
        "Expected output:\n1\n3\n5\n7\n9\nEnd"
    ),
    expected_output="1\n3\n5\n7\n9\nEnd",
    level=Level.HARD,
    hints=[
        "for i in range(1, 11):",
        "    if i % 2 == 0: continue",
        "    print(i)",
        "print('End')"
    ]
)

if __name__ == "__main__":
    run_sequence([easy, medium, hard],
                 save_path=MODULE_DIR,
                 progress_name=".progress_review_M02.json")
