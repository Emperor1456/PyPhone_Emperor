import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
import os
api_key = os.getenv("API_KEY", "default_value")
print(api_key)
# The variable is spelled incorrectly"""

EXPECTED = "default_value"
HINTS = [
    "Check the variable name on the print line.",
    "It says 'api_key' but the variable is 'api_key'.",
    "Make sure the variable name matches exactly."
]

if __name__ == "__main__":
    run_debug("L52: Environment Variables", BROKEN, EXPECTED, HINTS)
