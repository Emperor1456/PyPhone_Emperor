import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        count += 1

c = Counter()
c.increment()
print(c.count)"""

EXPECTED = "1"
HINTS = [
    "Inside increment, 'count' is a local variable, not the instance attribute.",
    "Use 'self.count += 1' instead.",
    "Always refer to instance attributes with self."
]

if __name__ == "__main__":
    run_debug("L42: Instance Methods", BROKEN, EXPECTED, HINTS)
