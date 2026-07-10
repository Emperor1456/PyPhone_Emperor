import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

print(absolute(-7)
"""

EXPECTED = "7"
HINTS = [
    "Missing closing parenthesis in the print call.",
    "Add ) after absolute(-7."
]

if __name__ == "__main__":
    run_debug("L26: Return Values", BROKEN, EXPECTED, HINTS)
