import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
def factorial(n):
    return n * factorial(n-1)

print(factorial(4))"""

EXPECTED = "24"
HINTS = [
    "The recursion has no base case, leading to infinite recursion.",
    "Add a base case: if n <= 1: return 1.",
    "Ensure the recursive call moves toward the base case."
]

if __name__ == "__main__":
    run_debug("L31: Recursion", BROKEN, EXPECTED, HINTS)
