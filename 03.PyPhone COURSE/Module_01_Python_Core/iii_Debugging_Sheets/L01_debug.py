import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
a = [1, 2, 3]
b = a
b.append(4)
print("Same object" if a is b else "Different objects")
print("Equal values" if a == b else "Not equal")"""

EXPECTED = "Different objects\nEqual values"

HINTS = [
    "Check if 'b' is really a copy of 'a'.",
    "Modify the assignment of 'b' so it gets a separate copy of the list.",
    "Use b = a.copy() instead of b = a."
]

if __name__ == "__main__":
    run_debug("L01: Variables & Identity", BROKEN, EXPECTED, HINTS)
