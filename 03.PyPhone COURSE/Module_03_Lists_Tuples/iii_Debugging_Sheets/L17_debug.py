import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
point = (10, 20)
point[0] = 15
print(point)"""

EXPECTED = "(15, 20)"
HINTS = [
    "Tuples are immutable; you cannot change them after creation.",
    "To 'modify', convert to list, change, convert back.",
    "Create a new tuple from the modified list."
]

if __name__ == "__main__":
    run_debug("L17: Tuples Immutability", BROKEN, EXPECTED, HINTS)
