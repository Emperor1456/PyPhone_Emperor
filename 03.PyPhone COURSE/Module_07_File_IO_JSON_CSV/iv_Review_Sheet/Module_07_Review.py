import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy: Read a file ──
easy = Task(
    description=(
        "📖  Read Log File\n\n"
        "Read the contents of 'test.txt' (which contains 'Hello') and print it.\n\n"
        "Expected output: Hello"
    ),
    expected_output="Hello",
    level=Level.EASY,
    hints=[
        "with open('test.txt', 'r') as f:",
        "    content = f.read()",
        "print(content)"
    ]
)

# ── Medium: Write and read JSON ──
medium = Task(
    description=(
        "📝  Write & Read JSON\n\n"
        "Write the dict {'age': 18} to a file 'data.json'. Then read it back and print the dict.\n\n"
        "Expected output: {'age': 18}"
    ),
    expected_output="{'age': 18}",
    level=Level.MEDIUM,
    hints=[
        "import json",
        "with open('data.json', 'w') as f:",
        "    json.dump({'age': 18}, f)",
        "with open('data.json', 'r') as f:",
        "    data = json.load(f)",
        "print(data)"
    ]
)

# ── Hard: Write CSV and read back ──
hard = Task(
    description=(
        "📊  CSV Round Trip\n\n"
        "Write a CSV file 'out.csv' with header 'name,age' and one row 'Emperor,18'.\n"
        "Then read and print its content exactly as:\n"
        "name,age\nEmperor,18\n\n"
        "Expected output:\nname,age\nEmperor,18"
    ),
    expected_output="name,age\nEmperor,18",
    level=Level.HARD,
    hints=[
        "import csv",
        "with open('out.csv', 'w', newline='') as f:",
        "    writer = csv.writer(f)",
        "    writer.writerow(['name', 'age'])",
        "    writer.writerow(['Emperor', '18'])",
        "print(open('out.csv').read().strip())"
    ]
)

if __name__ == "__main__":
    run_sequence([easy, medium, hard],
                 save_path=MODULE_DIR,
                 progress_name=".progress_review_M07.json")
