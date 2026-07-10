import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks (2) ──────────────────────────

easy1 = Task(
    description=(
        "🧮  Sum a List – Fixed Sales Totals\n\n"
        "Given the list [1, 2, 3, 4, 5] representing daily sales.\n"
        "Use a for loop to sum them and print the total.\n\n"
        "Expected output: 15"
    ),
    expected_output="15",
    level=Level.EASY,
    hints=[
        "sales = [1, 2, 3, 4, 5]",
        "total = 0",
        "for sale in sales:",
        "    total += sale",
        "print(total)"
    ]
)

easy2 = Task(
    description=(
        "🔤  Print Characters – Product Code\n\n"
        "Given the string 'Emperor', print each character\n"
        "on a new line using a for loop.\n\n"
        "Expected output:\nE\nm\np\ne\nr\no\nr"
    ),
    expected_output="E\nm\np\ne\nr\no\nr",
    level=Level.EASY,
    hints=[
        "code = 'Emperor'",
        "for ch in code:",
        "    print(ch)"
    ]
)

# ── Medium Tasks (2) ──────────────────────

medium1 = Task(
    description=(
        "📇  Enumerate – Invoice Line Numbers\n\n"
        "Given a list of items: ['Laptop', 'Mouse', 'Keyboard'].\n"
        "Use enumerate() to print each item with its line number\n"
        "(starting from 1) in the format:\n"
        "1. Laptop\n2. Mouse\n3. Keyboard\n\n"
        "Expected output:\n1. Laptop\n2. Mouse\n3. Keyboard"
    ),
    expected_output="1. Laptop\n2. Mouse\n3. Keyboard",
    level=Level.MEDIUM,
    hints=[
        "items = ['Laptop', 'Mouse', 'Keyboard']",
        "for i, item in enumerate(items, start=1):",
        "    print(f'{i}. {item}')"
    ]
)

medium2 = Task(
    description=(
        "🤝  Zip – Match Products with Prices\n\n"
        "You have two lists:\n"
        "  products = ['Widget', 'Gadget']\n"
        "  prices   = [9.99, 19.99]\n\n"
        "Use zip() and a for loop to print each product with its price\n"
        "in the format: 'Widget: $9.99' on each line.\n\n"
        "Expected output:\nWidget: $9.99\nGadget: $19.99"
    ),
    expected_output="Widget: $9.99\nGadget: $19.99",
    level=Level.MEDIUM,
    hints=[
        "products = ['Widget', 'Gadget']",
        "prices = [9.99, 19.99]",
        "for product, price in zip(products, prices):",
        "    print(f'{product}: ${price:.2f}')"
    ]
)

# ── Hard Tasks (2) ────────────────────────

hard1 = Task(
    description=(
        "🧱  Build a List – Even Numbers from 1 to 10\n\n"
        "Use a for loop and range() to create a list of even numbers\n"
        "from 1 to 10 (inclusive). Print the resulting list.\n\n"
        "Expected output: [2, 4, 6, 8, 10]"
    ),
    expected_output="[2, 4, 6, 8, 10]",
    level=Level.HARD,
    hints=[
        "evens = []",
        "for i in range(1, 11):",
        "    if i % 2 == 0:",
        "        evens.append(i)",
        "print(evens)"
    ]
)

hard2 = Task(
    description=(
        "📊  Combine Enumerate & Zip – Monthly Report\n\n"
        "Given:\n"
        "  months = ['Jan', 'Feb', 'Mar']\n"
        "  sales  = [1500, 2300, 1800]\n\n"
        "Print a report showing the month, its index (starting 1),\n"
        "and the sales figure, like:\n"
        "1: Jan sales $1500\n"
        "2: Feb sales $2300\n"
        "3: Mar sales $1800\n\n"
        "Expected output:\n1: Jan sales $1500\n2: Feb sales $2300\n3: Mar sales $1800"
    ),
    expected_output="1: Jan sales $1500\n2: Feb sales $2300\n3: Mar sales $1800",
    level=Level.HARD,
    hints=[
        "months = ['Jan', 'Feb', 'Mar']",
        "sales = [1500, 2300, 1800]",
        "for i, (month, sale) in enumerate(zip(months, sales), start=1):",
        "    print(f'{i}: {month} sales ${sale}')"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L11.json")
