import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
def double(x):
    return 2 * x

assert double(3) == 5
print("OK")"""

EXPECTED = "OK"
HINTS = [
    "The assertion fails because 2*3 != 5.",
    "Fix the expected value in the assert to 6.",
    "Change '5' to '6'."
]

if __name__ == "__main__":
    run_debug("L60: Testing", BROKEN, EXPECTED, HINTS)
