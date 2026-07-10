import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🐑  Lambda – Double a Number\n\n"
        "Create a lambda that doubles a number, assign to double, call with 5, print.\n\n"
        "Expected output: 10"
    ),
    expected_output="10",
    level=Level.EASY,
    hints=["double = lambda x: x * 2", "print(double(5))"]
)

easy2 = Task(
    description=(
        "➕  Lambda – Add Two Numbers\n\n"
        "Create lambda add that adds a and b, call with 3,5 and print.\n\n"
        "Expected output: 8"
    ),
    expected_output="8",
    level=Level.EASY,
    hints=["add = lambda a, b: a + b", "print(add(3, 5))"]
)

medium1 = Task(
    description=(
        "🗺️  map() – Square a List\n\n"
        "Given nums = [1,2,3], use map with a lambda to square each element.\n"
        "Convert to list and print.\n\n"
        "Expected output: [1, 4, 9]"
    ),
    expected_output="[1, 4, 9]",
    level=Level.MEDIUM,
    hints=["nums = [1,2,3]", "squared = list(map(lambda x: x**2, nums))", "print(squared)"]
)

medium2 = Task(
    description=(
        "🔍  filter() – Even Numbers\n\n"
        "Given nums = [1,2,3,4,5,6], use filter with lambda to keep evens.\n"
        "Convert to list and print.\n\n"
        "Expected output: [2, 4, 6]"
    ),
    expected_output="[2, 4, 6]",
    level=Level.MEDIUM,
    hints=["nums = [1,2,3,4,5,6]", "evens = list(filter(lambda x: x%2==0, nums))", "print(evens)"]
)

hard1 = Task(
    description=(
        "📊  sorted() with Key\n\n"
        "Sort ['banana','cherry','apple'] by the second character using lambda key.\n"
        "Print the sorted list.\n\n"
        "Expected output: ['banana', 'cherry', 'apple']"
    ),
    expected_output="['banana', 'cherry', 'apple']",
    level=Level.HARD,
    hints=["words = ['banana','cherry','apple']", "sorted_words = sorted(words, key=lambda w: w[1])", "print(sorted_words)"]
)

hard2 = Task(
    description=(
        "🔁  Lambda in Function\n\n"
        "Define a function make_multiplier(factor) that returns a lambda multiplying by factor.\n"
        "Call with 3 to get a function, then call that function with 5, print result.\n\n"
        "Expected output: 15"
    ),
    expected_output="15",
    level=Level.HARD,
    hints=["def make_multiplier(factor): return lambda x: x * factor", "triple = make_multiplier(3)", "print(triple(5))"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L30.json")
