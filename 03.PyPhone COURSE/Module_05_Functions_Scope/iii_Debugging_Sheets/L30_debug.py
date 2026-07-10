import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
double = lambda x: x*2
print(double(5, 3))"""

EXPECTED = "10"
HINTS = [
    "The lambda was defined with one parameter, but called with two.",
    "Remove the extra argument.",
    "Change double(5, 3) to double(5)."
]

if __name__ == "__main__":
    run_debug("L30: Lambda", BROKEN, EXPECTED, HINTS)
