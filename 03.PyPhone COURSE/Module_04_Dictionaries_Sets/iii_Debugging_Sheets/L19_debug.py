import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
user = dict()
user = {"name": "Emperor", "age": 18}
print(user["email"])"""

EXPECTED = "Emperor"
HINTS = [
    "The key 'email' does not exist in the dictionary.",
    "Printing user['email'] will raise a KeyError.",
    "Fix: print(user['name']) or use .get('email', 'default')."
]

if __name__ == "__main__":
    run_debug("L19: Dict Access", BROKEN, EXPECTED, HINTS)
