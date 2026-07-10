import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
d = {"a": 1, "b": 2}
for key, value in d:
    print(key, value)"""

EXPECTED = "a 1\nb 2"
HINTS = [
    "Iterating over a dictionary directly yields only keys.",
    "To get key-value pairs, use d.items().",
    "Change 'for key, value in d:' to 'for key, value in d.items():'."
]

if __name__ == "__main__":
    run_debug("L20: Dict Iteration", BROKEN, EXPECTED, HINTS)
