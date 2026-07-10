import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
x = 10

def increment():
    x += 1

increment()
print(x)"""

EXPECTED = "11"
HINTS = [
    "Modifying a global variable inside a function requires 'global' declaration.",
    "Without global, x += 1 creates a local variable that is referenced before assignment.",
    "Add 'global x' inside increment() before x += 1."
]

if __name__ == "__main__":
    run_debug("L29: Global vs Local", BROKEN, EXPECTED, HINTS)
