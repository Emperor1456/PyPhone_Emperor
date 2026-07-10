import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
class MyError(Exception):
    pass

raise MyError"""

EXPECTED = "__main__.MyError"
HINTS = [
    "The code is correct but expects to print the error class name.",
    "We need to catch the exception and print its class name.",
    "Wrap the raise in try/except and print type(e).__name__."
]

if __name__ == "__main__":
    run_debug("L33: Custom Exceptions", BROKEN, EXPECTED, HINTS)
