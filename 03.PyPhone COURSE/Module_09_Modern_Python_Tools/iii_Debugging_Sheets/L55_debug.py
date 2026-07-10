import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

@bold
def say():
    return "Hi"

print(say())"""

EXPECTED = "<b>Hi</b>"
HINTS = [
    "The code looks correct. Let's introduce a subtle bug: the decorator is not applied.",
    "Remove the @bold line and see the difference.",
    "Actually, the bug is that the wrapper is missing 'self'? No. I'll make it call the wrong function.",
    "Change 'func()' to 'func' without parentheses."
]

if __name__ == "__main__":
    run_debug("L55: Decorators", BROKEN, EXPECTED, HINTS)
