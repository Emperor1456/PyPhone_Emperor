import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
data = [0, 1, 2, 3, 4]
data[1:4] = [10, 20, 30, 40]
print(data)"""

EXPECTED = "[0, 10, 20, 30, 40, 4]"
HINTS = [
    "Slice assignment can change the length of the list.",
    "Replacing indices 1-3 with four items inserts extra elements.",
    "Ensure the number of replacement elements matches the slice length if you want to keep the same size."
]

if __name__ == "__main__":
    run_debug("L15: Slice Assignment", BROKEN, EXPECTED, HINTS)
