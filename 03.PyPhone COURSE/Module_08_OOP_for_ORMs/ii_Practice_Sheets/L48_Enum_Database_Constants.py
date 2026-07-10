import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🚦  Define an Enum\n\n"
        "Import Enum from enum. Define `Status` enum with PENDING=1, ACTIVE=2, INACTIVE=3.\n"
        "Print `Status.ACTIVE`.\n\n"
        "Expected output: Status.ACTIVE"
    ),
    expected_output="Status.ACTIVE",
    level=Level.EASY,
    hints=[
        "from enum import Enum",
        "class Status(Enum):",
        "    PENDING = 1",
        "    ACTIVE = 2",
        "    INACTIVE = 3",
        "print(Status.ACTIVE)"
    ]
)

easy2 = Task(
    description=(
        "🔢  Enum Value\n\n"
        "Print the value of `Status.ACTIVE` (should be 2).\n\n"
        "Expected output: 2"
    ),
    expected_output="2",
    level=Level.EASY,
    hints=[
        "from enum import Enum",
        "class Status(Enum): PENDING=1; ACTIVE=2; INACTIVE=3",
        "print(Status.ACTIVE.value)"
    ]
)

medium1 = Task(
    description=(
        "🔤  Enum with Strings\n\n"
        "Define `Role` enum with ADMIN='admin', USER='user', GUEST='guest'.\n"
        "Print `Role.USER.value`.\n\n"
        "Expected output: user"
    ),
    expected_output="user",
    level=Level.MEDIUM,
    hints=[
        "from enum import Enum",
        "class Role(Enum):",
        "    ADMIN = 'admin'",
        "    USER = 'user'",
        "    GUEST = 'guest'",
        "print(Role.USER.value)"
    ]
)

medium2 = Task(
    description=(
        "🔍  Enum Comparison\n\n"
        "Given an enum `Status`, check if Status.ACTIVE == Status.ACTIVE, print True.\n\n"
        "Expected output: True"
    ),
    expected_output="True",
    level=Level.MEDIUM,
    hints=[
        "from enum import Enum",
        "class Status(Enum): PENDING=1; ACTIVE=2; INACTIVE=3",
        "print(Status.ACTIVE == Status.ACTIVE)"
    ]
)

hard1 = Task(
    description=(
        "🔁  Enum in Function\n\n"
        "Define function `handle_status(status)` that prints 'Active' if status is Status.ACTIVE else 'Other'.\n"
        "Call with Status.ACTIVE.\n\n"
        "Expected output: Active"
    ),
    expected_output="Active",
    level=Level.HARD,
    hints=[
        "from enum import Enum",
        "class Status(Enum): PENDING=1; ACTIVE=2; INACTIVE=3",
        "def handle_status(status):",
        "    if status == Status.ACTIVE: print('Active')",
        "    else: print('Other')",
        "handle_status(Status.ACTIVE)"
    ]
)

hard2 = Task(
    description=(
        "📋  List All Enum Members\n\n"
        "Print a list of all enum member names from the Status enum.\n\n"
        "Expected output: ['PENDING', 'ACTIVE', 'INACTIVE']"
    ),
    expected_output="['PENDING', 'ACTIVE', 'INACTIVE']",
    level=Level.HARD,
    hints=[
        "from enum import Enum",
        "class Status(Enum): PENDING=1; ACTIVE=2; INACTIVE=3",
        "names = [s.name for s in Status]",
        "print(names)"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L48.json")
