import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
stock = 10
if stock > 0
    print("In stock")
else:
    print("Out of stock")"""

EXPECTED = "In stock"
HINTS = [
    "Check the if statement syntax carefully.",
    "A colon is missing after the condition.",
    "if stock > 0:"
]

if __name__ == "__main__":
    run_debug("L08: if-elif-else", BROKEN, EXPECTED, HINTS)
