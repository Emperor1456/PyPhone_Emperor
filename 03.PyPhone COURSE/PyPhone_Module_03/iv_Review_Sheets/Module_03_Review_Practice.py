import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description=(
        "Name Formatter\n"
        "Full name string: 'emperor pyphone'\n"
        "Print it in title case, then print initials only."
    ),
    expected_output="Emperor Pyphone\nEP",
    level=Level.EASY,
    hints=[
        "full = 'emperor pyphone'",
        "print(full.title())",
        "initials = ''.join(word[0].upper() for word in full.split())",
        "print(initials)"
    ]
)

medium = Task(
    description=(
        "CSV Parser\n"
        "Raw data: 'Laptop, 999.99, 5'\n"
        "Extract product, price, quantity.\n"
        "Print them with labels, each on a new line."
    ),
    expected_output="Product: Laptop\nPrice: 999.99\nQuantity: 5",
    level=Level.MEDIUM,
    hints=[
        "data = 'Laptop, 999.99, 5'",
        "parts = data.split(',')",
        "product = parts[0].strip()",
        "price = float(parts[1].strip())",
        "qty = int(parts[2].strip())",
        "print(f'Product: {product}')",
        "print(f'Price: {price}')",
        "print(f'Quantity: {qty}')"
    ]
)

hard = Task(
    description=(
        "Sales Log Report\n"
        "Given a log string:\n"
        "'Mouse 2 24.99,Keyboard 1 49.95,Monitor 3 199.99,Mouse 5 24.99'\n"
        "Compute:\n"
        "- Total revenue per product\n"
        "- Overall revenue\n"
        "Print results sorted by product name.\n\n"
        "Output format:\n"
        "Keyboard: $49.95\n"
        "Monitor: $599.97\n"
        "Mouse: $174.93\n"
        "Total: $824.85"
    ),
    expected_output="Keyboard: $49.95\nMonitor: $599.97\nMouse: $174.93\nTotal: $824.85",
    level=Level.HARD,
    hints=[
        "log = 'Mouse 2 24.99,Keyboard 1 49.95,Monitor 3 199.99,Mouse 5 24.99'",
        "revenue = {}",
        "for entry in log.split(','):",
        "    product, qty, price = entry.split()",
        "    qty = int(qty); price = float(price)",
        "    revenue[product] = revenue.get(product, 0) + qty * price",
        "for product in sorted(revenue):",
        "    print(f'{product}: ${revenue[product]:.2f}')",
        "total = sum(revenue.values())",
        "print(f'Total: ${total:.2f}')"
    ]
)

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__":
    main()
