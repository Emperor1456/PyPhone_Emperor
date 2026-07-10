import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
total = 0
i = 1
while i <= 4
    total += i
print(total)"""

EXPECTED = "10"
HINTS = [
    "Python expects a colon after the while condition.",
    "Add a colon at the end of 'while i <= 4'.",
    "Also you need to increment i inside the loop to avoid infinite loop.",
    "Add 'i += 1' inside the loop."
]

if __name__ == "__main__":
    run_debug("L10: while Loop", BROKEN, EXPECTED, HINTS)
