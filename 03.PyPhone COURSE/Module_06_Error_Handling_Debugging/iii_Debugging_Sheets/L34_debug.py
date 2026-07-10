import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
try:
    1 / 0
except ZeroDivisionError:
    print("error")
else:
    print("success")
finally
    print("cleanup")
print("done")"""

EXPECTED = "error\ncleanup\ndone"
HINTS = [
    "Python requires a colon after 'finally'.",
    "Add a colon at the end of 'finally'.",
    "Correct syntax: 'finally:'"
]

if __name__ == "__main__":
    run_debug("L34: else/finally", BROKEN, EXPECTED, HINTS)
