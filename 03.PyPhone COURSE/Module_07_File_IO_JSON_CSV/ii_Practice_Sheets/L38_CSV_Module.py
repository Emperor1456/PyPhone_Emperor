import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "📊  Read CSV with csv.reader\n\n"
        "Read 'data.csv' (name,age) into a list of rows using csv.reader.\n"
        "Print the list. (The engine creates the file with header and two rows.)\n\n"
        "Expected output: [['name', 'age'], ['Alice', '30'], ['Bob', '25']]"
    ),
    expected_output="[['name', 'age'], ['Alice', '30'], ['Bob', '25']]",
    level=Level.EASY,
    hints=[
        "import csv",
        "with open('data.csv', 'r') as f:",
        "    reader = csv.reader(f)",
        "    rows = list(reader)",
        "print(rows)"
    ]
)

easy2 = Task(
    description=(
        "📇  Read CSV with DictReader\n\n"
        "Read the same 'data.csv' using csv.DictReader and print the list of dicts.\n\n"
        "Expected output: [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]"
    ),
    expected_output="[{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]",
    level=Level.EASY,
    hints=[
        "import csv",
        "with open('data.csv', 'r') as f:",
        "    reader = csv.DictReader(f)",
        "    dict_rows = list(reader)",
        "print(dict_rows)"
    ]
)

medium1 = Task(
    description=(
        "✍️  Write CSV with csv.writer\n\n"
        "Write a CSV file 'out.csv' with header 'name,age' and one row 'Emperor,18'.\n"
        "Then read and print its content.\n\n"
        "Expected output:\nname,age\nEmperor,18"
    ),
    expected_output="name,age\nEmperor,18",
    level=Level.MEDIUM,
    hints=[
        "import csv",
        "with open('out.csv', 'w', newline='') as f:",
        "    writer = csv.writer(f)",
        "    writer.writerow(['name', 'age'])",
        "    writer.writerow(['Emperor', '18'])",
        "print(open('out.csv').read().strip())"
    ]
)

medium2 = Task(
    description=(
        "📝  Write CSV with DictWriter\n\n"
        "Write a CSV 'dict_out.csv' with header 'name,age' and one row {'name':'Emperor','age':'18'}.\n"
        "Read and print content.\n\n"
        "Expected output:\nname,age\nEmperor,18"
    ),
    expected_output="name,age\nEmperor,18",
    level=Level.MEDIUM,
    hints=[
        "import csv",
        "with open('dict_out.csv', 'w', newline='') as f:",
        "    fieldnames = ['name', 'age']",
        "    writer = csv.DictWriter(f, fieldnames=fieldnames)",
        "    writer.writeheader()",
        "    writer.writerow({'name': 'Emperor', 'age': '18'})",
        "print(open('dict_out.csv').read().strip())"
    ]
)

hard1 = Task(
    description=(
        "🔢  Sum a CSV Column\n\n"
        "Read 'data.csv', sum the 'age' column, and print the total.\n"
        "(Alice=30, Bob=25 => 55).\n\n"
        "Expected output: 55"
    ),
    expected_output="55",
    level=Level.HARD,
    hints=[
        "import csv",
        "total = 0",
        "with open('data.csv', 'r') as f:",
        "    reader = csv.DictReader(f)",
        "    for row in reader:",
        "        total += int(row['age'])",
        "print(total)"
    ]
)

hard2 = Task(
    description=(
        "📊  Filter CSV Rows\n\n"
        "Read 'data.csv' and print only rows where age is greater than 28.\n"
        "Print each matching row as a dict.\n\n"
        "Expected output:\n{'name': 'Alice', 'age': '30'}"
    ),
    expected_output="{'name': 'Alice', 'age': '30'}",
    level=Level.HARD,
    hints=[
        "import csv",
        "with open('data.csv', 'r') as f:",
        "    reader = csv.DictReader(f)",
        "    for row in reader:",
        "        if int(row['age']) > 28:",
        "            print(row)"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L38.json")
