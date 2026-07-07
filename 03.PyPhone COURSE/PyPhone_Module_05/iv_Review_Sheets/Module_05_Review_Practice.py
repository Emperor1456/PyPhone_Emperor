import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description=(
        "Product Lookup\n"
        "Given a dictionary:\n"
        "  products = {'mouse':24.99, 'keyboard':49.95, 'monitor':199.99}\n"
        "Print the price of 'keyboard'."
    ),
    expected_output="49.95",
    level=Level.EASY,
    hints=[
        "products = {'mouse':24.99, 'keyboard':49.95, 'monitor':199.99}",
        "print(products['keyboard'])"
    ]
)

medium = Task(
    description=(
        "Set Operations\n"
        "Given two sets of user IDs:\n"
        "  active = {101,102,103,104}\n"
        "  premium = {103,104,105,106}\n"
        "Print the intersection (common users) as a set."
    ),
    expected_output="{103, 104}",
    level=Level.MEDIUM,
    hints=[
        "active = {101,102,103,104}",
        "premium = {103,104,105,106}",
        "print(active & premium)"
    ]
)

hard = Task(
    description=(
        "Inventory Sales Summary\n\n"
        "Given a list of sales tuples:\n"
        "  sales = [('Mouse',2,24.99),('Keyboard',1,49.95),\n"
        "           ('Monitor',3,199.99),('Mouse',1,24.99),\n"
        "           ('Keyboard',2,49.95)]\n\n"
        "Compute:\n"
        "- Total revenue per product (store in dict)\n"
        "- Overall revenue\n"
        "- Unique products sold (as a set)\n"
        "- Top‑selling product by revenue\n\n"
        "Print results exactly:\n"
        "Mouse: $74.97\n"
        "Keyboard: $149.85\n"
        "Monitor: $599.97\n"
        "Total: $824.79\n"
        "Unique products: {'Monitor', 'Keyboard', 'Mouse'}\n"
        "Top product: Monitor ($599.97)"
    ),
    expected_output=(
        "Mouse: $74.97\n"
        "Keyboard: $149.85\n"
        "Monitor: $599.97\n"
        "Total: $824.79\n"
        "Unique products: {'Monitor', 'Keyboard', 'Mouse'}\n"
        "Top product: Monitor ($599.97)"
    ),
    level=Level.HARD,
    hints=[
        "sales = [('Mouse',2,24.99),('Keyboard',1,49.95),('Monitor',3,199.99),('Mouse',1,24.99),('Keyboard',2,49.95)]",
        "revenue = {}",
        "for product, qty, price in sales:",
        "    revenue[product] = revenue.get(product, 0) + qty * price",
        "for prod in sorted(revenue):",
        "    print(f'{prod}: ${revenue[prod]:.2f}')",
        "total = sum(revenue.values())",
        "print(f'Total: ${total:.2f}')",
        "unique = set(revenue.keys())",
        "print(f'Unique products: {unique}')",
        "top_prod = max(revenue, key=revenue.get)",
        "print(f'Top product: {top_prod} (${revenue[top_prod]:.2f}')"
    ]
)

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__":
    main()
