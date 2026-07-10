import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
def countdown(n):
    while n > 0:
        yield n
    n -= 1

for num in countdown(3):
    print(num)"""

EXPECTED = "3\n2\n1"
HINTS = [
    "The decrement of n is outside the loop.",
    "Move 'n -= 1' inside the while loop.",
    "Indent the line correctly."
]

if __name__ == "__main__":
    run_debug("L54: Generators", BROKEN, EXPECTED, HINTS)
