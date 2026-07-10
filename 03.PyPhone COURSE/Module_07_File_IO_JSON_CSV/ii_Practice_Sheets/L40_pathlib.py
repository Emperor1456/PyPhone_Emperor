import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "📂  Create Path Object\n\n"
        "From pathlib import Path. Create a Path object for 'test.txt'.\n"
        "Print its name (use .name).\n\n"
        "Expected output: test.txt"
    ),
    expected_output="test.txt",
    level=Level.EASY,
    hints=[
        "from pathlib import Path",
        "p = Path('test.txt')",
        "print(p.name)"
    ]
)

easy2 = Task(
    description=(
        "🔍  Check File Existence\n\n"
        "Check if 'test.txt' exists (it does, the engine creates it). Print True.\n\n"
        "Expected output: True"
    ),
    expected_output="True",
    level=Level.EASY,
    hints=[
        "from pathlib import Path",
        "print(Path('test.txt').exists())"
    ]
)

medium1 = Task(
    description=(
        "📖  Read Text with Path\n\n"
        "Read the content of 'test.txt' using Path.read_text() and print it.\n"
        "(Content is 'Hello'.)\n\n"
        "Expected output: Hello"
    ),
    expected_output="Hello",
    level=Level.MEDIUM,
    hints=[
        "from pathlib import Path",
        "content = Path('test.txt').read_text()",
        "print(content.strip())"
    ]
)

medium2 = Task(
    description=(
        "✍️  Write Text with Path\n\n"
        "Write 'PyPhone' to 'output.txt' using Path.write_text().\n"
        "Then read and print.\n\n"
        "Expected output: PyPhone"
    ),
    expected_output="PyPhone",
    level=Level.MEDIUM,
    hints=[
        "from pathlib import Path",
        "Path('output.txt').write_text('PyPhone')",
        "print(Path('output.txt').read_text().strip())"
    ]
)

hard1 = Task(
    description=(
        "📁  Create Directory\n\n"
        "Create a directory 'temp_dir' using Path.mkdir(exist_ok=True).\n"
        "Then print 'created'.\n\n"
        "Expected output: created"
    ),
    expected_output="created",
    level=Level.HARD,
    hints=[
        "from pathlib import Path",
        "Path('temp_dir').mkdir(exist_ok=True)",
        "print('created')"
    ]
)

hard2 = Task(
    description=(
        "🔎  Glob for Python Files\n\n"
        "Use Path('.').glob('*.py') to list Python files in current directory.\n"
        "Print how many .py files are found (just print the count).\n"
        "Simulate by printing 1 if 'practice_engine.py' exists, else 0.\n"
        "Print 0 as a safe fallback that won't break.\n\n"
        "Expected output: 0"
    ),
    expected_output="0",
    level=Level.HARD,
    hints=[
        "from pathlib import Path",
        "count = len(list(Path('.').glob('*.py')))",
        "print(count)"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L40.json")
