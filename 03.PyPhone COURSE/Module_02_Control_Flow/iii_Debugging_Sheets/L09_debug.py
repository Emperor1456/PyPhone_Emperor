import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
is_logged_in = True
is_admin = False
if is_logged_in:
    if is_admin = True:
        print("Admin panel")
    else:
        print("User dashboard")
else:
    print("Please log in")"""

EXPECTED = "User dashboard"
HINTS = [
    "There's a common mistake in the inner if condition.",
    "= is assignment; == is comparison.",
    "Change 'is_admin = True' to 'is_admin == True' or simply 'is_admin'."
]

if __name__ == "__main__":
    run_debug("L09: Nested Conditionals", BROKEN, EXPECTED, HINTS)
