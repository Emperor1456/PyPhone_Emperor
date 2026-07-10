import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
nums = [3, 1, 5]
sorted_nums = nums.sort()
print(sorted_nums)"""

EXPECTED = "[1, 3, 5]"
HINTS = [
    "The .sort() method sorts in place and returns None.",
    "Assigning its result to a variable gives None.",
    "Either sort in place then print the original list, or use sorted()."
]

if __name__ == "__main__":
    run_debug("L14: List Methods", BROKEN, EXPECTED, HINTS)
