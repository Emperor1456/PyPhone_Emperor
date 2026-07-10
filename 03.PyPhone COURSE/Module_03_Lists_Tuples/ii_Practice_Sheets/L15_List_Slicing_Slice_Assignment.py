import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "✂️  Basic Slicing\n\n"
        "Given nums = [1, 2, 3, 4, 5], print the sublist [2, 3, 4] using slicing.\n\n"
        "Expected output: [2, 3, 4]"
    ),
    expected_output="[2, 3, 4]",
    level=Level.EASY,
    hints=["nums = [1, 2, 3, 4, 5]", "print(nums[1:4])"]
)

easy2 = Task(
    description=(
        "📋  Copy Entire List\n\n"
        "Given original = [10, 20, 30], create a full copy using slicing\n"
        "and print the copy.\n\n"
        "Expected output: [10, 20, 30]"
    ),
    expected_output="[10, 20, 30]",
    level=Level.EASY,
    hints=["original = [10, 20, 30]", "copy = original[:]", "print(copy)"]
)

medium1 = Task(
    description=(
        "🔄  Slice Assignment – Replace Middle\n\n"
        "Given data = [0, 1, 2, 3, 4], replace indices 1-3 (inclusive 1, exclusive 4)\n"
        "with [10, 20]. Print the updated list.\n\n"
        "Expected output: [0, 10, 20, 4]"
    ),
    expected_output="[0, 10, 20, 4]",
    level=Level.MEDIUM,
    hints=["data = [0, 1, 2, 3, 4]", "data[1:4] = [10, 20]", "print(data)"]
)

medium2 = Task(
    description=(
        "➕  Insert with Empty Slice\n\n"
        "Given data = [0, 10, 20, 4], insert 100 at index 2 without removing anything.\n"
        "Print the result.\n\n"
        "Expected output: [0, 10, 100, 20, 4]"
    ),
    expected_output="[0, 10, 100, 20, 4]",
    level=Level.MEDIUM,
    hints=["data = [0, 10, 20, 4]", "data[2:2] = [100]", "print(data)"]
)

hard1 = Task(
    description=(
        "🗑️  Delete with Slice Assignment\n\n"
        "Given data = [0, 10, 100, 20, 4], delete the elements at indices 1 and 2\n"
        "using slice assignment. Print the remaining list.\n\n"
        "Expected output: [0, 20, 4]"
    ),
    expected_output="[0, 20, 4]",
    level=Level.HARD,
    hints=["data = [0, 10, 100, 20, 4]", "data[1:3] = []", "print(data)"]
)

hard2 = Task(
    description=(
        "🔢  Every Second Element\n\n"
        "Given nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], print every second element\n"
        "starting from index 0 (i.e., indices 0,2,4,6,8).\n\n"
        "Expected output: [0, 2, 4, 6, 8]"
    ),
    expected_output="[0, 2, 4, 6, 8]",
    level=Level.HARD,
    hints=["nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]", "print(nums[::2])"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L15.json")
