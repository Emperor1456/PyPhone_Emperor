import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
squares = [x^2 for x in range(5)]
print(squares)"""

EXPECTED = "[0, 1, 4, 9, 16]"
HINTS = [
    "The exponentiation operator in Python is **, not ^.",
    "^ is bitwise XOR.",
    "Change x^2 to x**2."
]

if __name__ == "__main__":
    run_debug("L16: List Comprehensions", BROKEN, EXPECTED, HINTS)
