import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy: Inventory Count (dict counting) ──
easy = Task(
    description=(
        "📦  Warehouse Stock Counter\n\n"
        "Given a list of products:\n"
        "  items = ['mouse', 'keyboard', 'mouse', 'monitor', 'keyboard']\n\n"
        "Count how many times each product appears using a dictionary.\n"
        "Print the resulting dict.\n\n"
        "Expected output: {'mouse': 2, 'keyboard': 2, 'monitor': 1}"
    ),
    expected_output="{'mouse': 2, 'keyboard': 2, 'monitor': 1}",
    level=Level.EASY,
    hints=[
        "items = ['mouse', 'keyboard', 'mouse', 'monitor', 'keyboard']",
        "counts = {}",
        "for item in items:",
        "    counts[item] = counts.get(item, 0) + 1",
        "print(counts)"
    ]
)

# ── Medium: Group by Category (defaultdict) ──
medium = Task(
    description=(
        "🗂️  Product Grouper\n\n"
        "Given a list of (category, product) tuples:\n"
        "  data = [('Electronics', 'Laptop'), ('Office', 'Desk'), ('Electronics', 'Mouse')]\n\n"
        "Use defaultdict(list) to group products by category.\n"
        "Print the dict.\n\n"
        "Expected output: {'Electronics': ['Laptop', 'Mouse'], 'Office': ['Desk']}"
    ),
    expected_output="{'Electronics': ['Laptop', 'Mouse'], 'Office': ['Desk']}",
    level=Level.MEDIUM,
    hints=[
        "from collections import defaultdict",
        "data = [('Electronics','Laptop'), ('Office','Desk'), ('Electronics','Mouse')]",
        "groups = defaultdict(list)",
        "for cat, prod in data:",
        "    groups[cat].append(prod)",
        "print(dict(groups))"
    ]
)

# ── Hard: Dedup & Sort (set + sorted) ──
hard = Task(
    description=(
        "🧹  Unique Product Finder\n\n"
        "Given a list with duplicate product codes:\n"
        "  codes = ['B', 'A', 'C', 'B', 'D', 'A']\n\n"
        "1. Convert to a set to get unique codes.\n"
        "2. Sort the unique codes alphabetically.\n"
        "3. Print the sorted list of unique codes.\n\n"
        "Expected output: ['A', 'B', 'C', 'D']"
    ),
    expected_output="['A', 'B', 'C', 'D']",
    level=Level.HARD,
    hints=[
        "codes = ['B', 'A', 'C', 'B', 'D', 'A']",
        "unique = set(codes)",
        "sorted_unique = sorted(unique)",
        "print(sorted_unique)"
    ]
)

if __name__ == "__main__":
    run_sequence([easy, medium, hard],
                 save_path=MODULE_DIR,
                 progress_name=".progress_review_M04.json")
