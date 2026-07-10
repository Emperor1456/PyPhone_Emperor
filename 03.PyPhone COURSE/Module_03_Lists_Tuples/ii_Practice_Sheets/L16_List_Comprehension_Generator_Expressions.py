import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🔢  Squares with Comprehension\n\n"
        "Create a list of squares for numbers [1, 2, 3] using a list comprehension.\n"
        "Print the list.\n\n"
        "Expected output: [1, 4, 9]"
    ),
    expected_output="[1, 4, 9]",
    level=Level.EASY,
    hints=["squares = [x*x for x in [1, 2, 3]]", "print(squares)"]
)

easy2 = Task(
    description=(
        "📊  Even Numbers Filter\n\n"
        "Given range(1, 11), create a list of only even numbers using comprehension.\n"
        "Print the list.\n\n"
        "Expected output: [2, 4, 6, 8, 10]"
    ),
    expected_output="[2, 4, 6, 8, 10]",
    level=Level.EASY,
    hints=["evens = [x for x in range(1, 11) if x % 2 == 0]", "print(evens)"]
)

medium1 = Task(
    description=(
        "🔄  Map with Comprehension\n\n"
        "Given prices = [100, 200, 300], apply 10% tax using a list comprehension.\n"
        "Print the new list with tax-inclusive prices.\n\n"
        "Expected output: [110.0, 220.0, 330.0]"
    ),
    expected_output="[110.0, 220.0, 330.0]",
    level=Level.MEDIUM,
    hints=["prices = [100, 200, 300]", "with_tax = [p * 1.1 for p in prices]", "print(with_tax)"]
)

medium2 = Task(
    description=(
        "🧹  Generator Expression Sum\n\n"
        "Sum the squares of numbers 1 through 5 using a generator expression\n"
        "(inside sum()). Print the total.\n\n"
        "Expected output: 55"
    ),
    expected_output="55",
    level=Level.MEDIUM,
    hints=["total = sum(x*x for x in range(1, 6))", "print(total)"]
)

hard1 = Task(
    description=(
        "🔁  Nested Comprehension – Flatten Matrix\n\n"
        "Given a matrix = [[1,2],[3,4],[5,6]], flatten it into a single list\n"
        "using list comprehension with two 'for' clauses. Print the result.\n\n"
        "Expected output: [1, 2, 3, 4, 5, 6]"
    ),
    expected_output="[1, 2, 3, 4, 5, 6]",
    level=Level.HARD,
    hints=["matrix = [[1,2],[3,4],[5,6]]", "flat = [num for row in matrix for num in row]", "print(flat)"]
)

hard2 = Task(
    description=(
        "🎲  Conditional Expression in Comprehension\n\n"
        "Given numbers 1 to 6, create a list where even numbers are squared\n"
        "and odd numbers are kept as is (use an if-else inside the comprehension).\n"
        "Print the list.\n\n"
        "Expected output: [1, 4, 3, 16, 5, 36]"
    ),
    expected_output="[1, 4, 3, 16, 5, 36]",
    level=Level.HARD,
    hints=["result = [x**2 if x%2==0 else x for x in range(1, 7)]", "print(result)"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L16.json")
