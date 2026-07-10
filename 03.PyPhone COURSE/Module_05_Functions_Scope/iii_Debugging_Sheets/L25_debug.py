import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
def add(a, b):
    return a + b

result = add(3, 5
print(result)"""

EXPECTED = "8"
HINTS = [
    "Look at the function call.",
    "Missing closing parenthesis after add(3, 5.",
    "Add )"
]

if __name__ == "__main__":
    run_debug("L25: Parameters", BROKEN, EXPECTED, HINTS)
