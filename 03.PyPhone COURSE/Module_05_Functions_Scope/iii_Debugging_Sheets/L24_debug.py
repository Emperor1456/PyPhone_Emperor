import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
def greet():
    print("Hello, Emperor!"

greet()"""

EXPECTED = "Hello, Emperor!"
HINTS = [
    "Check parentheses and syntax.",
    "Missing closing parenthesis in print statement.",
    "Add ) after 'Emperor!'"
]

if __name__ == "__main__":
    run_debug("L24: Defining Functions", BROKEN, EXPECTED, HINTS)
