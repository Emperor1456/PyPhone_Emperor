import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
with open("output.txt", "wb") as f:
    f.write("Emperor")
print(open("output.txt", "r").read())"""

EXPECTED = "Emperor"
HINTS = [
    "Mode 'wb' is for writing bytes, not strings.",
    "Use 'w' for text mode.",
    "Change 'wb' to 'w'."
]

if __name__ == "__main__":
    run_debug("L37: Writing Files", BROKEN, EXPECTED, HINTS)
