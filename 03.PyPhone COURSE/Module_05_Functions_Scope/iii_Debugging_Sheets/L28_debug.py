import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
def sum_all(*args):
    return sum(arg)

print(sum_all(1, 2, 3))"""

EXPECTED = "6"
HINTS = [
    "args is a tuple, not a single argument.",
    "sum(arg) should be sum(args).",
    "Change 'sum(arg)' to 'sum(args)'."
]

if __name__ == "__main__":
    run_debug("L28: *args", BROKEN, EXPECTED, HINTS)
