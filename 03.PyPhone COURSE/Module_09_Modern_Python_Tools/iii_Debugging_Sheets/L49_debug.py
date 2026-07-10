import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
import math
print(pi)"""

EXPECTED = "3.141592653589793"
HINTS = [
    "The name 'pi' is not defined; it's a constant in the math module.",
    "Use math.pi.",
    "Change print(pi) to print(math.pi)."
]

if __name__ == "__main__":
    run_debug("L49: Modules", BROKEN, EXPECTED, HINTS)
