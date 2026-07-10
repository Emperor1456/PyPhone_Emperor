import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
s = {1, 2, 3}
s.add({4, 5})
print(s)"""

EXPECTED = "{1, 2, 3, 4, 5}"
HINTS = [
    "You cannot add a mutable set as an element of another set.",
    "Use s.update({4, 5}) to add multiple elements.",
    "Change s.add({4,5}) to s.update({4,5})."
]

if __name__ == "__main__":
    run_debug("L22: Sets", BROKEN, EXPECTED, HINTS)
