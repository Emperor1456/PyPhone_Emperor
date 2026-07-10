import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
print(c.diameter())"""

EXPECTED = "10"
HINTS = [
    "A @property method should be accessed without parentheses.",
    "Change c.diameter() to c.diameter."
]

if __name__ == "__main__":
    run_debug("L47: Properties", BROKEN, EXPECTED, HINTS)
