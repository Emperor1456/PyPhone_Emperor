import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "📋  List All Keys\n\n"
        "Given d = {'name': 'Emperor', 'age': 18}, print a list of all keys.\n\n"
        "Expected output: ['name', 'age']"
    ),
    expected_output="['name', 'age']",
    level=Level.EASY,
    hints=["d = {'name': 'Emperor', 'age': 18}", "print(list(d.keys()))"]
)

easy2 = Task(
    description=(
        "📊  List All Values\n\n"
        "Using the same dict, print a list of all values.\n\n"
        "Expected output: ['Emperor', 18]"
    ),
    expected_output="['Emperor', 18]",
    level=Level.EASY,
    hints=["print(list(d.values()))"]
)

medium1 = Task(
    description=(
        "🔁  Iterate Over Items\n\n"
        "Given d = {'name': 'Emperor', 'age': 18}, iterate over its items\n"
        "and print each key-value pair in the format 'key: value' on separate lines.\n\n"
        "Expected output:\nname: Emperor\nage: 18"
    ),
    expected_output="name: Emperor\nage: 18",
    level=Level.MEDIUM,
    hints=["d = {'name': 'Emperor', 'age': 18}", "for k, v in d.items():", "    print(f'{k}: {v}')"]
)

medium2 = Task(
    description=(
        "🧮  Counting Pattern\n\n"
        "Given a list of words: ['apple', 'banana', 'apple', 'cherry'],\n"
        "count the frequency of each word using a dictionary.\n"
        "Print the resulting dict.\n\n"
        "Expected output: {'apple': 2, 'banana': 1, 'cherry': 1}"
    ),
    expected_output="{'apple': 2, 'banana': 1, 'cherry': 1}",
    level=Level.MEDIUM,
    hints=["words = ['apple', 'banana', 'apple', 'cherry']", "counts = {}", "for w in words:", "    counts[w] = counts.get(w, 0) + 1", "print(counts)"]
)

hard1 = Task(
    description=(
        "🔀  Merge Two Dictionaries\n\n"
        "Given d1 = {'a': 1, 'b': 2} and d2 = {'b': 3, 'c': 4},\n"
        "merge d2 into d1 using update(). Then print d1.\n\n"
        "Expected output: {'a': 1, 'b': 3, 'c': 4}"
    ),
    expected_output="{'a': 1, 'b': 3, 'c': 4}",
    level=Level.HARD,
    hints=["d1 = {'a': 1, 'b': 2}", "d2 = {'b': 3, 'c': 4}", "d1.update(d2)", "print(d1)"]
)

hard2 = Task(
    description=(
        "🧹  Pop and Clear\n\n"
        "Start with d = {'x': 10, 'y': 20, 'z': 30}.\n"
        "Remove the last inserted item using popitem() and print its key-value pair\n"
        "as a tuple. Then clear the dictionary and print the empty dict.\n\n"
        "Expected output:\n('z', 30)\n{}"
    ),
    expected_output="('z', 30)\n{}",
    level=Level.HARD,
    hints=["d = {'x': 10, 'y': 20, 'z': 30}", "last = d.popitem()", "print(last)", "d.clear()", "print(d)"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L20.json")
