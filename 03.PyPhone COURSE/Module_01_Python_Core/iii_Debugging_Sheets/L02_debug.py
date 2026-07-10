import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
raw_price = "24.99"
qty = 3
total = raw_price * qty
print(total)"""

EXPECTED = "74.97"

HINTS = [
    "raw_price is a string, not a number.",
    "Convert raw_price to a float before multiplication.",
    "Use float(raw_price) * qty."
]

if __name__ == "__main__":
    run_debug("L02: Numeric Types & Casting", BROKEN, EXPECTED, HINTS)
