import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
items = [1, 2, 3, 4, 5]
print(items[5])"""

EXPECTED = "5"
HINTS = [
    "List indices start at 0, so the last element is at len(items)-1.",
    "items[5] is out of range; use negative index.",
    "Change to items[-1]."
]

if __name__ == "__main__":
    run_debug("L13: List Indexing", BROKEN, EXPECTED, HINTS)
