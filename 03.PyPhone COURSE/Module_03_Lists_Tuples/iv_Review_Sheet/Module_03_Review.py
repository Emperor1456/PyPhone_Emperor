import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy: Stock Alert (list indexing, mutability) ──
easy = Task(
    description=(
        "📦  Inventory Stock Check\n\n"
        "Given:\n"
        "  stock = [150, 89, 320, 45]\n\n"
        "1. Print the first item's stock level.\n"
        "2. Update the second item to 95.\n"
        "3. Print the entire updated list.\n\n"
        "Expected output:\n150\n[150, 95, 320, 45]"
    ),
    expected_output="150\n[150, 95, 320, 45]",
    level=Level.EASY,
    hints=[
        "stock = [150, 89, 320, 45]",
        "print(stock[0])",
        "stock[1] = 95",
        "print(stock)"
    ]
)

# ── Medium: Remove & Sort (list methods) ──
medium = Task(
    description=(
        "🧹  Clean & Sort Product Codes\n\n"
        "Given:\n"
        "  codes = ['B', 'A', 'C', 'B']\n\n"
        "1. Remove the first occurrence of 'B'.\n"
        "2. Sort the remaining list.\n"
        "3. Print the final list.\n\n"
        "Expected output: ['A', 'B', 'C']"
    ),
    expected_output="['A', 'B', 'C']",
    level=Level.MEDIUM,
    hints=[
        "codes = ['B', 'A', 'C', 'B']",
        "codes.remove('B')",
        "codes.sort()",
        "print(codes)"
    ]
)

# ── Hard: Comprehension & zip (list comprehension + zip) ──
hard = Task(
    description=(
        "🧪  Sales Report Generator\n\n"
        "Given two lists:\n"
        "  months = ['Jan', 'Feb', 'Mar']\n"
        "  sales  = [1500, 2300, 1800]\n\n"
        "1. Use zip to pair them.\n"
        "2. Use a list comprehension to create a list of formatted strings:\n"
        "   'Jan: $1500', 'Feb: $2300', 'Mar: $1800'\n"
        "3. Print each string on a new line.\n\n"
        "Expected output:\nJan: $1500\nFeb: $2300\nMar: $1800"
    ),
    expected_output="Jan: $1500\nFeb: $2300\nMar: $1800",
    level=Level.HARD,
    hints=[
        "months = ['Jan', 'Feb', 'Mar']",
        "sales = [1500, 2300, 1800]",
        "report = [f'{m}: ${s}' for m, s in zip(months, sales)]",
        "for line in report: print(line)"
    ]
)

if __name__ == "__main__":
    run_sequence([easy, medium, hard],
                 save_path=MODULE_DIR,
                 progress_name=".progress_review_M03.json")
