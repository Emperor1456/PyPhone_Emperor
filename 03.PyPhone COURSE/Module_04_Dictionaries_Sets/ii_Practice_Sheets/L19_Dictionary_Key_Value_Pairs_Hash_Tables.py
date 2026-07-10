import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "📖  Create a Dictionary\n\n"
        "Create a dictionary with keys 'name' and 'age', values 'Emperor' and 18.\n"
        "Print the dictionary.\n\n"
        "Expected output: {'name': 'Emperor', 'age': 18}"
    ),
    expected_output="{'name': 'Emperor', 'age': 18}",
    level=Level.EASY,
    hints=["user = {'name': 'Emperor', 'age': 18}", "print(user)"]
)

easy2 = Task(
    description=(
        "🔑  Access a Value by Key\n\n"
        "Given d = {'name': 'Emperor', 'age': 18}, print the value for key 'name'.\n\n"
        "Expected output: Emperor"
    ),
    expected_output="Emperor",
    level=Level.EASY,
    hints=["d = {'name': 'Emperor', 'age': 18}", "print(d['name'])"]
)

medium1 = Task(
    description=(
        "🛡️  Safe Access with .get()\n\n"
        "Given d = {'name': 'Emperor'}, safely retrieve the key 'phone'.\n"
        "If the key is missing, print 'Not found'.\n\n"
        "Expected output: Not found"
    ),
    expected_output="Not found",
    level=Level.MEDIUM,
    hints=["d = {'name': 'Emperor'}", "print(d.get('phone', 'Not found'))"]
)

medium2 = Task(
    description=(
        "✏️  Add and Update\n\n"
        "Start with d = {'name': 'Emperor', 'age': 18}.\n"
        "Add a new key 'city' with value 'Dhaka'.\n"
        "Then update 'age' to 19. Print the final dictionary.\n\n"
        "Expected output: {'name': 'Emperor', 'age': 19, 'city': 'Dhaka'}"
    ),
    expected_output="{'name': 'Emperor', 'age': 19, 'city': 'Dhaka'}",
    level=Level.MEDIUM,
    hints=["d = {'name': 'Emperor', 'age': 18}", "d['city'] = 'Dhaka'", "d['age'] = 19", "print(d)"]
)

hard1 = Task(
    description=(
        "🧹  Remove with pop()\n\n"
        "Given d = {'name': 'Emperor', 'age': 18, 'city': 'Dhaka'},\n"
        "remove the key 'age' using pop(), capture its value,\n"
        "print the popped value, then print the remaining dict.\n\n"
        "Expected output:\n18\n{'name': 'Emperor', 'city': 'Dhaka'}"
    ),
    expected_output="18\n{'name': 'Emperor', 'city': 'Dhaka'}",
    level=Level.HARD,
    hints=["d = {'name': 'Emperor', 'age': 18, 'city': 'Dhaka'}", "popped = d.pop('age')", "print(popped)", "print(d)"]
)

hard2 = Task(
    description=(
        "🔍  Check Key Existence\n\n"
        "Given d = {'name': 'Emperor'}, check if 'email' exists in d.\n"
        "Print 'Exists' if it does, else 'Missing'.\n\n"
        "Expected output: Missing"
    ),
    expected_output="Missing",
    level=Level.HARD,
    hints=["d = {'name': 'Emperor'}", "if 'email' in d:", "    print('Exists')", "else:", "    print('Missing')"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L19.json")
