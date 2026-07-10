import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🏢  Class Variable\n\n"
        "Define a class `Employee` with class variable `company = 'PyPhone'`.\n"
        "Print `Employee.company`.\n\n"
        "Expected output: PyPhone"
    ),
    expected_output="PyPhone",
    level=Level.EASY,
    hints=[
        "class Employee:",
        "    company = 'PyPhone'",
        "print(Employee.company)"
    ]
)

easy2 = Task(
    description=(
        "👥  Two Instances Share Class Var\n\n"
        "Create two Employee instances `e1`, `e2`. Print both `e1.company` and `e2.company`\n"
        "separated by a space.\n\n"
        "Expected output: PyPhone PyPhone"
    ),
    expected_output="PyPhone PyPhone",
    level=Level.EASY,
    hints=[
        "class Employee: company = 'PyPhone'",
        "e1 = Employee(); e2 = Employee()",
        "print(e1.company, e2.company)"
    ]
)

medium1 = Task(
    description=(
        "🚗  Class Variable with Instance\n\n"
        "Define a class `Car` with class variable `wheels = 4`.\n"
        "Create an instance `c = Car()` and print `c.wheels`.\n\n"
        "Expected output: 4"
    ),
    expected_output="4",
    level=Level.MEDIUM,
    hints=[
        "class Car:",
        "    wheels = 4",
        "c = Car()",
        "print(c.wheels)"
    ]
)

medium2 = Task(
    description=(
        "✏️  Shadow Class Variable\n\n"
        "Using the Employee class, set `e1.company = 'Freelance'`.\n"
        "Print `e1.company` and `Employee.company` on separate lines.\n\n"
        "Expected output:\nFreelance\nPyPhone"
    ),
    expected_output="Freelance\nPyPhone",
    level=Level.MEDIUM,
    hints=[
        "class Employee: company = 'PyPhone'",
        "e1 = Employee()",
        "e1.company = 'Freelance'",
        "print(e1.company)",
        "print(Employee.company)"
    ]
)

hard1 = Task(
    description=(
        "🔢  Shared Counter\n\n"
        "Define a class `User` with class variable `count = 0`. In `__init__`, increment `User.count`.\n"
        "Create two users, then print `User.count`.\n\n"
        "Expected output: 2"
    ),
    expected_output="2",
    level=Level.HARD,
    hints=[
        "class User:",
        "    count = 0",
        "    def __init__(self):",
        "        User.count += 1",
        "u1 = User(); u2 = User()",
        "print(User.count)"
    ]
)

hard2 = Task(
    description=(
        "📊  Default Config via Class Var\n\n"
        "Define class `AppConfig` with class variable `theme = 'dark'`.\n"
        "Create an instance, change theme to 'light' via instance, then print instance.theme and AppConfig.theme.\n\n"
        "Expected output:\nlight\ndark"
    ),
    expected_output="light\ndark",
    level=Level.HARD,
    hints=[
        "class AppConfig:",
        "    theme = 'dark'",
        "config = AppConfig()",
        "config.theme = 'light'",
        "print(config.theme)",
        "print(AppConfig.theme)"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L43.json")
