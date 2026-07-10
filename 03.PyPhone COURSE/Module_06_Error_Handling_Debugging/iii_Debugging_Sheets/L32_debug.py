import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
try:
    int("abc")
except:
    print("An error occurred")"""

EXPECTED = "invalid literal for int() with base 10: 'abc'"
HINTS = [
    "The bare except catches the error but doesn't print the specific message.",
    "You need to capture the exception and print its string representation.",
    "Use 'except ValueError as e: print(e)'."
]

if __name__ == "__main__":
    run_debug("L32: try/except", BROKEN, EXPECTED, HINTS)
