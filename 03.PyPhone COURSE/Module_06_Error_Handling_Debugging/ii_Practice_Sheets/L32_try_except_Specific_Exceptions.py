import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🚫  Catch ValueError\n\n"
        "Try to convert the string 'abc' to an integer.\n"
        "Catch ValueError and print 'error'.\n\n"
        "Expected output: error"
    ),
    expected_output="error",
    level=Level.EASY,
    hints=[
        "try:",
        "    int('abc')",
        "except ValueError:",
        "    print('error')"
    ]
)

easy2 = Task(
    description=(
        "🛡️  Catch ZeroDivisionError\n\n"
        "Divide 10 by 0 inside a try block.\n"
        "Catch ZeroDivisionError and print 'caught'.\n\n"
        "Expected output: caught"
    ),
    expected_output="caught",
    level=Level.EASY,
    hints=[
        "try:",
        "    10 / 0",
        "except ZeroDivisionError:",
        "    print('caught')"
    ]
)

medium1 = Task(
    description=(
        "📂  Catch FileNotFoundError\n\n"
        "Open a non-existent file 'nofile.txt' for reading.\n"
        "Catch FileNotFoundError and print 'missing'.\n\n"
        "Expected output: missing"
    ),
    expected_output="missing",
    level=Level.MEDIUM,
    hints=[
        "try:",
        "    open('nofile.txt')",
        "except FileNotFoundError:",
        "    print('missing')"
    ]
)

medium2 = Task(
    description=(
        "🔢  Multiple Exceptions\n\n"
        "Write a try block that first tries to convert 'abc' to int (ValueError)\n"
        "and then tries 10/0 (ZeroDivisionError). Catch both in separate except blocks.\n"
        "But execute only the first error: int('abc'). Print 'value error'.\n\n"
        "Expected output: value error"
    ),
    expected_output="value error",
    level=Level.MEDIUM,
    hints=[
        "try:",
        "    int('abc')",
        "except ValueError:",
        "    print('value error')",
        "except ZeroDivisionError:",
        "    print('zero error')"
    ]
)

hard1 = Task(
    description=(
        "🧪  Catch Exception and Print Type\n\n"
        "Try to access an undefined variable x inside a try block.\n"
        "Catch Exception as e, and print type(e).__name__.\n\n"
        "Expected output: NameError"
    ),
    expected_output="NameError",
    level=Level.HARD,
    hints=[
        "try:",
        "    print(x)",
        "except Exception as e:",
        "    print(type(e).__name__)"
    ]
)

hard2 = Task(
    description=(
        "📋  Validation with try/except\n\n"
        "Write a function safe_int(value) that tries to convert value to int.\n"
        "If it fails, return None. Call it with '42' and print the result.\n\n"
        "Expected output: 42"
    ),
    expected_output="42",
    level=Level.HARD,
    hints=[
        "def safe_int(value):",
        "    try:",
        "        return int(value)",
        "    except ValueError:",
        "        return None",
        "print(safe_int('42'))"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L32.json")
