import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "📝  Write a Docstring\n\n"
        "Define a function `add_contact(name, phone)` that returns True.\n"
        "Add a docstring: 'Add a new contact to the database.'\n"
        "Print the docstring.\n\n"
        "Expected output: Add a new contact to the database."
    ),
    expected_output="Add a new contact to the database.",
    level=Level.EASY,
    hints=["def add_contact(name, phone):", "    'Add a new contact to the database.'", "    return True", "print(add_contact.__doc__)"]
)

easy2 = Task(
    description=(
        "🧪  Write a Simple Test with assert\n\n"
        "Define a function `double(x)` that returns 2*x. Use assert to verify double(3) == 6.\n"
        "If it passes, print 'pass'.\n\n"
        "Expected output: pass"
    ),
    expected_output="pass",
    level=Level.EASY,
    hints=["def double(x): return 2*x", "assert double(3) == 6", "print('pass')"]
)

medium1 = Task(
    description=(
        "🔬  Unittest Test Case\n\n"
        "Import unittest. Create a class `TestContactBook` that inherits `unittest.TestCase`.\n"
        "Add a method `test_add` that calls `self.assertTrue(True)`.\n"
        "Run with `unittest.main(argv=[''], exit=False)`. Then print 'done'.\n\n"
        "Expected output: done"
    ),
    expected_output="done",
    level=Level.MEDIUM,
    hints=["import unittest", "class TestContactBook(unittest.TestCase):", "    def test_add(self):", "        self.assertTrue(True)", "unittest.main(argv=[''], exit=False)", "print('done')"]
)

medium2 = Task(
    description=(
        "📄  Create a README.md Outline\n\n"
        "Print the main sections of a project README:\n"
        "['# Project Title', '## Features', '## Installation', '## Usage', '## Testing']\n\n"
        "Expected output: ['# Project Title', '## Features', '## Installation', '## Usage', '## Testing']"
    ),
    expected_output="['# Project Title', '## Features', '## Installation', '## Usage', '## Testing']",
    level=Level.MEDIUM,
    hints=["sections = ['# Project Title', '## Features', '## Installation', '## Usage', '## Testing']", "print(sections)"]
)

hard1 = Task(
    description=(
        "📦  Generate requirements.txt\n\n"
        "Print the command to generate requirements.txt.\n"
        "Then print a sample content: 'sqlite3 (built-in)\\n'.\n"
        "The expected output is two lines.\n\n"
        "Expected output:\npip freeze > requirements.txt\nsqlite3 (built-in)"
    ),
    expected_output="pip freeze > requirements.txt\nsqlite3 (built-in)",
    level=Level.HARD,
    hints=["print('pip freeze > requirements.txt')", "print('sqlite3 (built-in)')"]
)

hard2 = Task(
    description=(
        "🛠️  Test Setup and Teardown\n\n"
        "Write a unittest class `TestDB` with a `setUp` method that prints 'setup' and a `test_example` that prints 'test'.\n"
        "Run with unittest. The engine expects the final output to be 'setup' then 'test'.\n"
        "(Use unittest.main with exit=False and capture output? Print both in sequence).\n"
        "Print 'setup' then 'test' explicitly.\n\n"
        "Expected output:\nsetup\ntest"
    ),
    expected_output="setup\ntest",
    level=Level.HARD,
    hints=["import unittest", "class TestDB(unittest.TestCase):", "    def setUp(self): print('setup')", "    def test_example(self): print('test')", "# Manually trigger to see output:", "suite = unittest.TestLoader().loadTestsFromTestCase(TestDB)", "unittest.TextTestRunner(verbosity=0).run(suite)"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L60.json")
