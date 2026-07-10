import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
class Parent:
    def show(self):
        return "Parent"
class Child(Parent):
    def show(self):
        return super().show() + " Child"

c = Child()
print(c.show)"""

EXPECTED = "Parent Child"
HINTS = [
    "Again, missing parentheses in the method call.",
    "Change c.show to c.show()."
]

if __name__ == "__main__":
    run_debug("L45: Overriding", BROKEN, EXPECTED, HINTS)
