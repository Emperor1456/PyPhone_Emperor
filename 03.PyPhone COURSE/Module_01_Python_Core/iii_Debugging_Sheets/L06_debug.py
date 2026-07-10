import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
is_logged_in = True
is_admin = False
if is_logged_in = True and is_admin:
    print("Access granted")
else:
    print("Access denied")"""

EXPECTED = "Access denied"

HINTS = [
    "There is a syntax error in the condition.",
    "= is assignment, == is comparison. Which one should be used?",
    "Change '= True' to '== True' (or better, just 'is_logged_in')."
]

if __name__ == "__main__":
    run_debug("L06: Boolean Logic & Conditionals", BROKEN, EXPECTED, HINTS)
