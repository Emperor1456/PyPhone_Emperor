import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "📖  Read Entire File\n\n"
        "Read the content of 'test.txt' into a variable using open and read.\n"
        "Print the content. (The engine will create 'test.txt' with 'Hello' beforehand.)\n\n"
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

easy2 = Task(
    description=(
        "📄  Read All Lines\n\n"
        "Read all lines from 'test.txt' into a list and print that list.\n"
        "(The file contains two lines: 'Hello' and 'World'.)\n\n"
        "Expected output: ['Hello\\n', 'World\\n']"
    ),
    expected_output="['Hello\\n', 'World\\n']",
    level=Level.EASY,
    hints=[
        "with open('test.txt', 'r') as f:",
        "    lines = f.readlines()",
        "print(lines)"
    ]
)

medium1 = Task(
    description=(
        "🔍  Read First Line and Strip\n\n"
        "Read the first line of 'test.txt', strip the newline, and print it.\n\n"
        "Expected output: Hello"
    ),
    expected_output="Hello",
    level=Level.MEDIUM,
    hints=[
        "with open('test.txt', 'r') as f:",
        "    first = f.readline().strip()",
        "print(first)"
    ]
)

medium2 = Task(
    description=(
        "🔁  Iterate Over Lines\n\n"
        "Open 'test.txt', iterate over each line, print each stripped line.\n"
        "The file has lines: 'Hello' and 'World'.\n\n"
        "Expected output:\nHello\nWorld"
    ),
    expected_output="Hello\nWorld",
    level=Level.MEDIUM,
    hints=[
        "with open('test.txt', 'r') as f:",
        "    for line in f:",
        "        print(line.strip())"
    ]
)

hard1 = Task(
    description=(
        "🧪  Read File into a List Comprehension\n\n"
        "Use a list comprehension with open file iterator to create a list of stripped lines.\n"
        "Print the list.\n\n"
        "Expected output: ['Hello', 'World']"
    ),
    expected_output="['Hello', 'World']",
    level=Level.HARD,
    hints=[
        "with open('test.txt', 'r') as f:",
        "    lines = [line.strip() for line in f]",
        "print(lines)"
    ]
)

hard2 = Task(
    description=(
        "📊  Count Lines\n\n"
        "Open 'test.txt' and count the number of lines. Print the count.\n"
        "(The file has 2 lines.)\n\n"
        "Expected output: 2"
    ),
    expected_output="2",
    level=Level.HARD,
    hints=[
        "with open('test.txt', 'r') as f:",
        "    count = sum(1 for _ in f)",
        "print(count)"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L36.json")
