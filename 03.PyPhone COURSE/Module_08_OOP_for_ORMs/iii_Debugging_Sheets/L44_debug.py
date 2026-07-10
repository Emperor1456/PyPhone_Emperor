import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
class Animal:
    def speak(self):
        return "?"
class Dog(Animal):
    def speak(self):
        return "Woof"

d = Dog()
print(d.speak)"""

EXPECTED = "Woof"
HINTS = [
    "The method is called without parentheses.",
    "Change d.speak to d.speak()."
]

if __name__ == "__main__":
    run_debug("L44: Inheritance", BROKEN, EXPECTED, HINTS)
