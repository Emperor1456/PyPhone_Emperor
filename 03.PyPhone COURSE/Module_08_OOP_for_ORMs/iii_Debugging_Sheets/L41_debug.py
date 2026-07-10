import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
class Dog:
    def __init__(name):
        self.name = name
    def bark(self):
        print("Woof!")

d = Dog("Rex")
d.bark()"""

EXPECTED = "Woof!"
HINTS = [
    "The __init__ method is missing the 'self' parameter.",
    "Add 'self' as the first parameter: def __init__(self, name).",
    "Also adjust the instance creation: Dog('Rex')."
]

if __name__ == "__main__":
    run_debug("L41: Classes & __init__", BROKEN, EXPECTED, HINTS)
