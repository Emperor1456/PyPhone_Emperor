import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
names = ["Emperor", "Rahim"]
scores = [95, 88]
pairs = zip(name, scores)
print(list(pairs))"""

EXPECTED = "[('Emperor', 95), ('Rahim', 88)]"
HINTS = [
    "Look at the variable name passed to zip.",
    "It says 'name' but the list is 'names'.",
    "Change 'zip(name, scores)' to 'zip(names, scores)'."
]

if __name__ == "__main__":
    run_debug("L18: zip", BROKEN, EXPECTED, HINTS)
