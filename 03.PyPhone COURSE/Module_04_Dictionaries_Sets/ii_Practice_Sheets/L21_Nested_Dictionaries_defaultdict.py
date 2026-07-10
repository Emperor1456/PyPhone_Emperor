import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🧱  Create Nested Dictionary\n\n"
        "Create a dictionary 'company' with key 'employees', containing another dict\n"
        "with employee 'emp1': {'name': 'Emperor', 'dept': 'Engineering'}.\n"
        "Print the entire nested dict.\n\n"
        "Expected output: {'employees': {'emp1': {'name': 'Emperor', 'dept': 'Engineering'}}}"
    ),
    expected_output="{'employees': {'emp1': {'name': 'Emperor', 'dept': 'Engineering'}}}",
    level=Level.EASY,
    hints=["company = {'employees': {'emp1': {'name': 'Emperor', 'dept': 'Engineering'}}}", "print(company)"]
)

easy2 = Task(
    description=(
        "🔍  Access Nested Value\n\n"
        "Using the same dictionary, print the department of emp1.\n\n"
        "Expected output: Engineering"
    ),
    expected_output="Engineering",
    level=Level.EASY,
    hints=["company = {'employees': {'emp1': {'name': 'Emperor', 'dept': 'Engineering'}}}", "print(company['employees']['emp1']['dept'])"]
)

medium1 = Task(
    description=(
        "✏️  Modify Nested Dict\n\n"
        "Add a new employee 'emp2' with name 'Rahim' and dept 'Sales' to the\n"
        "employees dict. Then print the whole company dict.\n\n"
        "Expected output: {'employees': {'emp1': {'name': 'Emperor', 'dept': 'Engineering'}, 'emp2': {'name': 'Rahim', 'dept': 'Sales'}}}"
    ),
    expected_output="{'employees': {'emp1': {'name': 'Emperor', 'dept': 'Engineering'}, 'emp2': {'name': 'Rahim', 'dept': 'Sales'}}}",
    level=Level.MEDIUM,
    hints=["company = {'employees': {'emp1': {'name': 'Emperor', 'dept': 'Engineering'}}}", "company['employees']['emp2'] = {'name': 'Rahim', 'dept': 'Sales'}", "print(company)"]
)

medium2 = Task(
    description=(
        "📦  defaultdict – Group by First Letter\n\n"
        "Given a list of words: ['apple', 'banana', 'avocado', 'cherry'],\n"
        "use defaultdict(list) from collections to group words by their first letter.\n"
        "Print the resulting dict (convert to regular dict for display).\n\n"
        "Expected output: {'a': ['apple', 'avocado'], 'b': ['banana'], 'c': ['cherry']}"
    ),
    expected_output="{'a': ['apple', 'avocado'], 'b': ['banana'], 'c': ['cherry']}",
    level=Level.MEDIUM,
    hints=["from collections import defaultdict", "by_letter = defaultdict(list)", "for w in ['apple','banana','avocado','cherry']:", "    by_letter[w[0]].append(w)", "print(dict(by_letter))"]
)

hard1 = Task(
    description=(
        "🧮  Nested Dict Counting\n\n"
        "You have transaction data: [('A', 100), ('B', 200), ('A', 50)].\n"
        "Build a nested dict where the first key is the category and the inner dict\n"
        "tracks 'total' and 'count'. Print the final nested dict.\n\n"
        "Expected output: {'A': {'total': 150, 'count': 2}, 'B': {'total': 200, 'count': 1}}"
    ),
    expected_output="{'A': {'total': 150, 'count': 2}, 'B': {'total': 200, 'count': 1}}",
    level=Level.HARD,
    hints=["data = [('A',100),('B',200),('A',50)]", "summary = {}", "for cat, amt in data:", "    if cat not in summary:", "        summary[cat] = {'total':0, 'count':0}", "    summary[cat]['total'] += amt", "    summary[cat]['count'] += 1", "print(summary)"]
)

hard2 = Task(
    description=(
        "🔢  defaultdict(int) – Character Frequency\n\n"
        "Count how many times each character appears in the string 'mississippi'.\n"
        "Use defaultdict(int) and print the dict.\n\n"
        "Expected output: {'m': 1, 'i': 4, 's': 4, 'p': 2}"
    ),
    expected_output="{'m': 1, 'i': 4, 's': 4, 'p': 2}",
    level=Level.HARD,
    hints=["from collections import defaultdict", "counts = defaultdict(int)", "for ch in 'mississippi':", "    counts[ch] += 1", "print(dict(counts))"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L21.json")
