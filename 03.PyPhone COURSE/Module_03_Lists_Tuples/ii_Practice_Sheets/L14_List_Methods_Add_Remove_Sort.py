import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "➕  Append to List\n\n"
        "Start with items = [1, 2, 3]. Append 4, then print the list.\n\n"
        "Expected output: [1, 2, 3, 4]"
    ),
    expected_output="[1, 2, 3, 4]",
    level=Level.EASY,
    hints=["items = [1, 2, 3]", "items.append(4)", "print(items)"]
)

easy2 = Task(
    description=(
        "📊  Sort a List\n\n"
        "Given lst = [3, 1, 5], sort it in ascending order and print.\n\n"
        "Expected output: [1, 3, 5]"
    ),
    expected_output="[1, 3, 5]",
    level=Level.EASY,
    hints=["lst = [3, 1, 5]", "lst.sort()", "print(lst)"]
)

medium1 = Task(
    description=(
        "✂️  Insert at Specific Position\n\n"
        "Insert 'review' at index 1 in ['write code', 'test', 'deploy'].\n"
        "Print the resulting list.\n\n"
        "Expected output: ['write code', 'review', 'test', 'deploy']"
    ),
    expected_output="['write code', 'review', 'test', 'deploy']",
    level=Level.MEDIUM,
    hints=["tasks = ['write code', 'test', 'deploy']", "tasks.insert(1, 'review')", "print(tasks)"]
)

medium2 = Task(
    description=(
        "🗑️  Remove by Value\n\n"
        "Given items = ['a', 'b', 'c', 'b'], remove the first 'b'.\n"
        "Print the list.\n\n"
        "Expected output: ['a', 'c', 'b']"
    ),
    expected_output="['a', 'c', 'b']",
    level=Level.MEDIUM,
    hints=["items = ['a', 'b', 'c', 'b']", "items.remove('b')", "print(items)"]
)

hard1 = Task(
    description=(
        "🔁  Pop and Print\n\n"
        "Given lst = [1, 2, 3], pop the last element, print it,\n"
        "then print the remaining list on the next line.\n\n"
        "Expected output:\n3\n[1, 2]"
    ),
    expected_output="3\n[1, 2]",
    level=Level.HARD,
    hints=["lst = [1, 2, 3]", "popped = lst.pop()", "print(popped)", "print(lst)"]
)

hard2 = Task(
    description=(
        "🔀  Reverse Order\n\n"
        "Given lst = [1, 2, 3], reverse its order in place and print.\n\n"
        "Expected output: [3, 2, 1]"
    ),
    expected_output="[3, 2, 1]",
    level=Level.HARD,
    hints=["lst = [1, 2, 3]", "lst.reverse()", "print(lst)"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L14.json")
