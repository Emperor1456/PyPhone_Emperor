import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🧹  Create a Set from List\n\n"
        "Given a list with duplicates [1, 2, 2, 3, 3, 3], convert it to a set\n"
        "and print the set.\n\n"
        "Expected output: {1, 2, 3}"
    ),
    expected_output="{1, 2, 3}",
    level=Level.EASY,
    hints=["nums = [1, 2, 2, 3, 3, 3]", "unique = set(nums)", "print(unique)"]
)

easy2 = Task(
    description=(
        "🔍  Membership Test\n\n"
        "Given s = {'apple', 'banana', 'cherry'}, check if 'apple' is in the set.\n"
        "Print True if it is, else False.\n\n"
        "Expected output: True"
    ),
    expected_output="True",
    level=Level.EASY,
    hints=["s = {'apple', 'banana', 'cherry'}", "print('apple' in s)"]
)

medium1 = Task(
    description=(
        "➕  Add and Remove Elements\n\n"
        "Start with s = {1, 2, 3}. Add 4, then remove 2 using discard() (safe).\n"
        "Print the resulting set.\n\n"
        "Expected output: {1, 3, 4}"
    ),
    expected_output="{1, 3, 4}",
    level=Level.MEDIUM,
    hints=["s = {1, 2, 3}", "s.add(4)", "s.discard(2)", "print(s)"]
)

medium2 = Task(
    description=(
        "📊  Unique Characters\n\n"
        "Given the string 'hello', create a set of its unique characters\n"
        "and print it.\n\n"
        "Expected output: {'h', 'e', 'l', 'o'}"
    ),
    expected_output="{'h', 'e', 'l', 'o'}",
    level=Level.MEDIUM,
    hints=["word = 'hello'", "unique = set(word)", "print(unique)"]
)

hard1 = Task(
    description=(
        "🔀  Set Update – Merge Multiple Iterables\n\n"
        "Start with s = {1, 2}. Update it with [3, 4] and {5, 6}.\n"
        "Print the final set.\n\n"
        "Expected output: {1, 2, 3, 4, 5, 6}"
    ),
    expected_output="{1, 2, 3, 4, 5, 6}",
    level=Level.HARD,
    hints=["s = {1, 2}", "s.update([3, 4], {5, 6})", "print(s)"]
)

hard2 = Task(
    description=(
        "🧹  Deduplicate and Sort\n\n"
        "Given a list with duplicates [5, 3, 5, 1, 3, 2], convert to a set\n"
        "to remove duplicates, then convert to a sorted list and print it.\n\n"
        "Expected output: [1, 2, 3, 5]"
    ),
    expected_output="[1, 2, 3, 5]",
    level=Level.HARD,
    hints=["nums = [5, 3, 5, 1, 3, 2]", "unique_sorted = sorted(set(nums))", "print(unique_sorted)"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L22.json")
