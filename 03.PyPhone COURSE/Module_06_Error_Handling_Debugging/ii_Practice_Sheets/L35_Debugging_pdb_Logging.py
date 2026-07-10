import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🐞  Use assert\n\n"
        "Write an assert statement that checks 1+1 == 2.\n"
        "If it passes, print 'pass'.\n\n"
        "Expected output: pass"
    ),
    expected_output="pass",
    level=Level.EASY,
    hints=[
        "assert 1+1 == 2",
        "print('pass')"
    ]
)

easy2 = Task(
    description=(
        "📋  Basic Logging\n\n"
        "Import logging, set level to INFO, and log an info message 'Test message'.\n"
        "Catch the output? For simplicity, just print 'logging ready'.\n\n"
        "Expected output: logging ready"
    ),
    expected_output="logging ready",
    level=Level.EASY,
    hints=[
        "import logging",
        "print('logging ready')"
    ]
)

medium1 = Task(
    description=(
        "🧪  Test with assert function\n\n"
        "Define a function test_sum() that asserts sum([1,2,3]) == 6.\n"
        "Call the function and print 'ok' after.\n\n"
        "Expected output: ok"
    ),
    expected_output="ok",
    level=Level.MEDIUM,
    hints=[
        "def test_sum():",
        "    assert sum([1,2,3]) == 6",
        "test_sum()",
        "print('ok')"
    ]
)

medium2 = Task(
    description=(
        "🛠️  Using pdb.set_trace (simulation)\n\n"
        "Print 'breakpoint set' to simulate placing a breakpoint.\n\n"
        "Expected output: breakpoint set"
    ),
    expected_output="breakpoint set",
    level=Level.MEDIUM,
    hints=[
        "print('breakpoint set')"
    ]
)

hard1 = Task(
    description=(
        "🔬  Unittest Simulation\n\n"
        "Create a minimal unittest.TestCase subclass with a test method that checks assertEqual(2+2,4).\n"
        "Run with unittest.main(argv=[''], exit=False). After that, print 'done'.\n\n"
        "Expected output: done"
    ),
    expected_output="done",
    level=Level.HARD,
    hints=[
        "import unittest",
        "class TestMath(unittest.TestCase):",
        "    def test_addition(self):",
        "        self.assertEqual(2+2, 4)",
        "unittest.main(argv=[''], exit=False)",
        "print('done')"
    ]
)

hard2 = Task(
    description=(
        "📊  Logging Levels\n\n"
        "Use logging to print a warning 'Low disk space'.\n"
        "Simulate by printing 'WARNING:root:Low disk space'.\n\n"
        "Expected output: WARNING:root:Low disk space"
    ),
    expected_output="WARNING:root:Low disk space",
    level=Level.HARD,
    hints=[
        "import logging",
        "logging.basicConfig(level=logging.WARNING)",
        "logging.warning('Low disk space')"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L35.json")
