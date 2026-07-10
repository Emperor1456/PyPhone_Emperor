import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "✍️  Write to a File\n\n"
        "Open 'output.txt' in write mode, write 'Emperor', then read and print its content.\n\n"
        "Expected output: Emperor"
    ),
    expected_output="Emperor",
    level=Level.EASY,
    hints=[
        "with open('output.txt', 'w') as f:",
        "    f.write('Emperor')",
        "print(open('output.txt').read())"
    ]
)

easy2 = Task(
    description=(
        "🔄  Overwrite a File\n\n"
        "Overwrite 'output.txt' with 'PyPhone', then read and print.\n\n"
        "Expected output: PyPhone"
    ),
    expected_output="PyPhone",
    level=Level.EASY,
    hints=[
        "with open('output.txt', 'w') as f:",
        "    f.write('PyPhone')",
        "print(open('output.txt').read())"
    ]
)

medium1 = Task(
    description=(
        "📋  Write Multiple Lines\n\n"
        "Write a list of lines ['First\\n', 'Second\\n'] to 'lines.txt' using writelines.\n"
        "Then read and print the content.\n\n"
        "Expected output:\nFirst\nSecond"
    ),
    expected_output="First\nSecond",
    level=Level.MEDIUM,
    hints=[
        "lines = ['First\\n', 'Second\\n']",
        "with open('lines.txt', 'w') as f:",
        "    f.writelines(lines)",
        "print(open('lines.txt').read().strip())"
    ]
)

medium2 = Task(
    description=(
        "➕  Append to File\n\n"
        "Create 'log.txt' with 'line1', then append 'line2' on a new line.\n"
        "Print the final content.\n\n"
        "Expected output:\nline1\nline2"
    ),
    expected_output="line1\nline2",
    level=Level.MEDIUM,
    hints=[
        "with open('log.txt', 'w') as f: f.write('line1')",
        "with open('log.txt', 'a') as f: f.write('\\nline2')",
        "print(open('log.txt').read().strip())"
    ]
)

hard1 = Task(
    description=(
        "🧪  Write Numbers as CSV\n\n"
        "Write a list [1,2,3] to 'numbers.txt' as comma-separated values.\n"
        "Then read and print the content.\n\n"
        "Expected output: 1,2,3"
    ),
    expected_output="1,2,3",
    level=Level.HARD,
    hints=[
        "nums = [1,2,3]",
        "with open('numbers.txt', 'w') as f:",
        "    f.write(','.join(map(str, nums)))",
        "print(open('numbers.txt').read())"
    ]
)

hard2 = Task(
    description=(
        "📝  Write Dictionary as Key-Value Pairs\n\n"
        "Write a dict {'name':'Emperor','age':'18'} to 'config.txt', each key=value on new line.\n"
        "Then read and print the content.\n\n"
        "Expected output:\nname=Emperor\nage=18"
    ),
    expected_output="name=Emperor\nage=18",
    level=Level.HARD,
    hints=[
        "d = {'name':'Emperor', 'age':'18'}",
        "with open('config.txt', 'w') as f:",
        "    for k,v in d.items():",
        "        f.write(f'{k}={v}\\n')",
        "print(open('config.txt').read().strip())"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L37.json")
