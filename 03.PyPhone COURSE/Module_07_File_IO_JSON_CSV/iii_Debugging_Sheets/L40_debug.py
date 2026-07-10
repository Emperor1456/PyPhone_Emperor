import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
p = Path("test.txt")
print(p.read_text())"""

EXPECTED = "Hello"
HINTS = [
    "The name 'Path' is not defined; you need to import it from pathlib.",
    "Add 'from pathlib import Path' at the top.",
    "After importing, the code will run."
]

if __name__ == "__main__":
    run_debug("L40: pathlib", BROKEN, EXPECTED, HINTS)
