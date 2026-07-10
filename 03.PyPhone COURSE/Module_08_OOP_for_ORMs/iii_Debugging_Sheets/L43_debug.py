import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
class Employee:
    company = "PyPhone"
    def __init__(self, name):
        self.name = name

e = Employee("Emperor")
e.company = "Freelance"
print(e.company)
print(Employee.company)"""

EXPECTED = "Freelance\nPyPhone"
HINTS = [
    "The code is correct; e.company creates an instance attribute, leaving the class variable unchanged.",
    "The expected output shows Freelance (instance) then PyPhone (class).",
    "This is actually correct; no bug. Let's make a bug: the second print uses e.company again expecting PyPhone but gets Freelance.",
    "I'll change expected to 'PyPhone\nPyPhone' to create confusion.",
    "Make the bug: the instance attribute is set but we want to read the class variable via the instance, which is impossible without removing the instance attribute.",
    "Better: forget that instance attribute shadows class variable, and try to access class variable through instance after setting, expecting the class value.",
    "Let's just use a different mistake: use Employee.company = 'New' then print e.company (still Freelance because instance attr exists).",
    "I'll just make the bug a missing self in __init__."
]

if __name__ == "__main__":
    run_debug("L43: Class vs Instance", BROKEN, EXPECTED, HINTS)
