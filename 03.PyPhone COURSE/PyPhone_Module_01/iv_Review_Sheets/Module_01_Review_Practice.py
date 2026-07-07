import sys
sys.path.append("../..")
from practice_engine import Task, Level, run_task

# ─── Easy ─────────────────────────────────────
easy = Task(
    description=(
        "Create three variables:\n"
        "name = 'Mouse'\n"
        "price = 24.99\n"
        "stock = 150\n"
        "Print each on a separate line."
    ),
    expected_output="Mouse\n24.99\n150",
    level=Level.EASY,
    hints=[
        "name = 'Mouse'",
        "price = 24.99",
        "stock = 150",
        "print(name)",
        "print(price)",
        "print(stock)"
    ]
)

# ─── Medium ──────────────────────────────────
medium = Task(
    description=(
        "A customer orders 4 monitors at $249.95 each.\n"
        "qty = 4\n"
        "unit = 249.95\n"
        "total = qty * unit\n"
        "Apply 5% discount if total > 200.\n"
        "Print final amount exactly:\n"
        "Final total: $949.81"
    ),
    expected_output="Final total: $949.81",
    level=Level.MEDIUM,
    hints=[
        "qty = 4",
        "unit = 249.95",
        "total = qty * unit",
        "if total > 200: total *= 0.95",
        "print(f'Final total: ${total:.2f}')"
    ]
)

# ─── Hard (Full Receipt) ─────────────────────
hard = Task(
    description=(
        "Given these exact variables:\n"
        "product = 'Mouse'\n"
        "qty = 4\n"
        "unit = 24.99\n"
        "stock = 150\n"
        "tid = 1001\n\n"
        "Write a script that prints a receipt.\n"
        "Check if qty <= stock, else print\n"
        "'Not enough stock' and stop.\n"
        "Compute total, apply 5% discount\n"
        "if total > 200.\n"
        "Print the receipt exactly like:\n\n"
        "---- RECEIPT ----\n"
        "Product: Mouse\n"
        "Quantity: 4\n"
        "Price per unit: $24.99\n"
        "Total before discount: $99.96\n"
        "Discount: $0.00\n"
        "Final total: $99.96\n"
        "Remaining stock: 146\n"
        "Transaction ID: 1001\n"
        "Transaction ID (string): 1001"
    ),
    expected_output=(
        "---- RECEIPT ----\n"
        "Product: Mouse\n"
        "Quantity: 4\n"
        "Price per unit: $24.99\n"
        "Total before discount: $99.96\n"
        "Discount: $0.00\n"
        "Final total: $99.96\n"
        "Remaining stock: 146\n"
        "Transaction ID: 1001\n"
        "Transaction ID (string): 1001"
    ),
    level=Level.HARD,
    hints=[
        "product = 'Mouse'; qty = 4; unit = 24.99; stock = 150; tid = 1001",
        "if qty > stock: print('Not enough stock')",
        "total = qty * unit",
        "if total > 200: total *= 0.95; discount = '49.99' else discount = '0.00'",
        "print('---- RECEIPT ----')",
        "print(f'Product: {product}')",
        "print(f'Quantity: {qty}')",
        "print(f'Price per unit: ${unit:.2f}')",
        "print(f'Total before discount: ${qty*unit:.2f}')",
        "print(f'Discount: ${discount}')",
        "print(f'Final total: ${total:.2f}')",
        "print(f'Remaining stock: {stock - qty}')",
        "print(f'Transaction ID: {tid}')",
        "print(f'Transaction ID (string): {str(tid)}')"
    ]
)

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__":
    main()