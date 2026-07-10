import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
f = open("test.txt", "r")
content = f.read()
print(content)"""

EXPECTED = "Hello"
HINTS = [
    "The file is opened but never closed.",
    "Use a with statement to ensure proper closing.",
    "Rewrite with 'with open(...) as f:'"
]

if __name__ == "__main__":
    run_debug("L36: Reading Files", BROKEN, EXPECTED, HINTS)
