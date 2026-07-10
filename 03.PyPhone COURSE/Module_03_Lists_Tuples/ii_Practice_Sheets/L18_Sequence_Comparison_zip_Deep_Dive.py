import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "⚖️  Compare Lists\n\n"
        "Check if [1,2,3] is equal to [1,2,3] and print the boolean result.\n\n"
        "Expected output: True"
    ),
    expected_output="True",
    level=Level.EASY,
    hints=["print([1,2,3] == [1,2,3])"]
)

easy2 = Task(
    description=(
        "🤝  Zip Two Lists\n\n"
        "Given names = ['Emperor', 'Rahim'] and scores = [95, 88],\n"
        "zip them together, convert to a list, and print the list of tuples.\n\n"
        "Expected output: [('Emperor', 95), ('Rahim', 88)]"
    ),
    expected_output="[('Emperor', 95), ('Rahim', 88)]",
    level=Level.EASY,
    hints=["names = ['Emperor', 'Rahim']", "scores = [95, 88]", "print(list(zip(names, scores)))"]
)

medium1 = Task(
    description=(
        "📊  Zip and Iterate\n\n"
        "Given products = ['Widget', 'Gadget'] and prices = [9.99, 19.99],\n"
        "iterate using zip and print each product with its price in format\n"
        "'Widget: $9.99'. Each on a new line.\n\n"
        "Expected output:\nWidget: $9.99\nGadget: $19.99"
    ),
    expected_output="Widget: $9.99\nGadget: $19.99",
    level=Level.MEDIUM,
    hints=["products = ['Widget', 'Gadget']", "prices = [9.99, 19.99]", "for p, pr in zip(products, prices):", "    print(f'{p}: ${pr:.2f}')"]
)

medium2 = Task(
    description=(
        "🔁  Unzip a List of Tuples\n\n"
        "Given pairs = [('A', 1), ('B', 2), ('C', 3)], use zip with unpacking (*)\n"
        "to separate into two lists and print them as a tuple of lists.\n"
        "Hints: letters, numbers = zip(*pairs) then print list(letters), list(numbers).\n\n"
        "Expected output: ['A', 'B', 'C'] [1, 2, 3]"
    ),
    expected_output="['A', 'B', 'C'] [1, 2, 3]",
    level=Level.MEDIUM,
    hints=["pairs = [('A', 1), ('B', 2), ('C', 3)]", "letters, numbers = zip(*pairs)", "print(list(letters), list(numbers))"]
)

hard1 = Task(
    description=(
        "🧱  Compare Sequences Lexicographically\n\n"
        "Check if [1,2,3] is less than [1,2,4] and print the boolean result.\n\n"
        "Expected output: True"
    ),
    expected_output="True",
    level=Level.HARD,
    hints=["print([1,2,3] < [1,2,4])"]
)

hard2 = Task(
    description=(
        "📇  Zip with Different Lengths\n\n"
        "Given a = [1,2,3], b = ['x','y'], use zip_longest from itertools\n"
        "with fillvalue='?' to create a list of tuples. Print the list.\n\n"
        "Expected output: [(1, 'x'), (2, 'y'), (3, '?')]"
    ),
    expected_output="[(1, 'x'), (2, 'y'), (3, '?')]",
    level=Level.HARD,
    hints=["from itertools import zip_longest", "a = [1,2,3]; b = ['x','y']", "result = list(zip_longest(a, b, fillvalue='?'))", "print(result)"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L18.json")
