import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "📦  Create Inventory List\n\n"
        "Create a list of three product names: 'Laptop', 'Mouse', 'Keyboard'.\n"
        "Print the entire list.\n\n"
        "Expected output: ['Laptop', 'Mouse', 'Keyboard']"
    ),
    expected_output="['Laptop', 'Mouse', 'Keyboard']",
    level=Level.EASY,
    hints=["products = ['Laptop', 'Mouse', 'Keyboard']", "print(products)"]
)

easy2 = Task(
    description=(
        "🔢  Access by Index – Second Product\n\n"
        "Given the list [10, 20, 30, 40], print the third element.\n\n"
        "Expected output: 30"
    ),
    expected_output="30",
    level=Level.EASY,
    hints=["nums = [10, 20, 30, 40]", "print(nums[2])"]
)

medium1 = Task(
    description=(
        "✏️  Mutability – Update Stock\n\n"
        "Given stock = [150, 89, 320, 45].\n"
        "The second item (index 1) had a recount and is now 95.\n"
        "Update the list and print it.\n\n"
        "Expected output: [150, 95, 320, 45]"
    ),
    expected_output="[150, 95, 320, 45]",
    level=Level.MEDIUM,
    hints=["stock = [150, 89, 320, 45]", "stock[1] = 95", "print(stock)"]
)

medium2 = Task(
    description=(
        "📏  Length of a List\n\n"
        "Given a list of shipment weights: [12, 8, 15, 10, 7].\n"
        "Print the number of shipments.\n\n"
        "Expected output: 5"
    ),
    expected_output="5",
    level=Level.MEDIUM,
    hints=["weights = [12, 8, 15, 10, 7]", "print(len(weights))"]
)

hard1 = Task(
    description=(
        "🔄  Swap Two Products\n\n"
        "A product list ['A', 'B', 'C', 'D'] needs the first two items swapped.\n"
        "Swap items at index 0 and 1 without using a temporary variable,\n"
        "then print the list.\n\n"
        "Expected output: ['B', 'A', 'C', 'D']"
    ),
    expected_output="['B', 'A', 'C', 'D']",
    level=Level.HARD,
    hints=["items = ['A', 'B', 'C', 'D']", "items[0], items[1] = items[1], items[0]", "print(items)"]
)

hard2 = Task(
    description=(
        "🧱  Nested List Access\n\n"
        "Given matrix = [[1,2],[3,4],[5,6]], print the element\n"
        "from the second row, first column (value 3).\n\n"
        "Expected output: 3"
    ),
    expected_output="3",
    level=Level.HARD,
    hints=["matrix = [[1,2],[3,4],[5,6]]", "print(matrix[1][0])"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L13.json")
