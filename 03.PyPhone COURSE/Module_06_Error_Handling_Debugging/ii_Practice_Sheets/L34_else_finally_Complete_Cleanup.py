import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "✅  else Block on Success\n\n"
        "Write a try block that sets x=1, no except, and an else block that prints 'success'.\n\n"
        "Expected output: success"
    ),
    expected_output="success",
    level=Level.EASY,
    hints=[
        "try:",
        "    x = 1",
        "except:",
        "    pass",
        "else:",
        "    print('success')"
    ]
)

easy2 = Task(
    description=(
        "🧹  finally Always Runs\n\n"
        "Write a try block with a deliberate error (1/0). Catch ZeroDivisionError and print 'error'.\n"
        "Add a finally block that prints 'cleanup'. Ensure 'cleanup' appears after 'error'.\n\n"
        "Expected output:\nerror\ncleanup"
    ),
    expected_output="error\ncleanup",
    level=Level.EASY,
    hints=[
        "try:",
        "    1/0",
        "except ZeroDivisionError:",
        "    print('error')",
        "finally:",
        "    print('cleanup')"
    ]
)

medium1 = Task(
    description=(
        "🔄  Full Pattern (success case)\n\n"
        "Use try/except/else/finally with a safe operation (x=1).\n"
        "Print 'try' inside try, 'else' inside else, 'finally' inside finally.\n\n"
        "Expected output:\ntry\nelse\nfinally"
    ),
    expected_output="try\nelse\nfinally",
    level=Level.MEDIUM,
    hints=[
        "try:",
        "    print('try')",
        "except:",
        "    pass",
        "else:",
        "    print('else')",
        "finally:",
        "    print('finally')"
    ]
)

medium2 = Task(
    description=(
        "📂  File Handling with finally\n\n"
        "Simulate file handling: open a file for writing, try to write, finally close.\n"
        "Print 'opened', 'closed' (ignore actual file operations). Use a flag.\n"
        "Print both strings.\n\n"
        "Expected output:\nopened\nclosed"
    ),
    expected_output="opened\nclosed",
    level=Level.MEDIUM,
    hints=[
        "f = None",
        "try:",
        "    print('opened')",
        "finally:",
        "    print('closed')"
    ]
)

hard1 = Task(
    description=(
        "⚠️  finally Overrides Return\n\n"
        "Write a function demo() that returns 'try' inside try, but has a finally block that\n"
        "prints 'finally' and returns 'finally'. Call and print the result.\n\n"
        "Expected output: finally"
    ),
    expected_output="finally",
    level=Level.HARD,
    hints=[
        "def demo():",
        "    try:",
        "        return 'try'",
        "    finally:",
        "        return 'finally'",
        "print(demo())"
    ]
)

hard2 = Task(
    description=(
        "🛡️  Complete Error Handling with Logging\n\n"
        "Write a function process(data) that tries to convert data to int, else logs 'Invalid',\n"
        "finally prints 'Done'. Call with 'abc' and print outputs.\n"
        "Output should be 'Invalid' then 'Done'.\n\n"
        "Expected output:\nInvalid\nDone"
    ),
    expected_output="Invalid\nDone",
    level=Level.HARD,
    hints=[
        "def process(data):",
        "    try:",
        "        int(data)",
        "    except ValueError:",
        "        print('Invalid')",
        "    finally:",
        "        print('Done')",
        "process('abc')"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L34.json")
