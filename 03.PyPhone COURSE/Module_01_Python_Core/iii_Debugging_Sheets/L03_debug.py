import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
word = "Python"
print(word[10])"""

EXPECTED = "n"

HINTS = [
    "The index 10 doesn't exist in a 6‑character string.",
    "Use a negative index to get the last character.",
    "Change 10 to -1."
]

if __name__ == "__main__":
    run_debug("L03: String Indexing", BROKEN, EXPECTED, HINTS)
