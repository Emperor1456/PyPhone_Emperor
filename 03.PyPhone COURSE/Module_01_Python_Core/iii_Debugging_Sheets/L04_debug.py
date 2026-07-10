import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
item = "Laptop"
price = 999.99
qty = 2
print(f"{qty} x {item} = ${total:.2f}")"""

EXPECTED = "2 x Laptop = $1999.98"

HINTS = [
    "The variable 'total' is never defined.",
    "Calculate total = price * qty before printing.",
    "Add 'total = price * qty' before the print statement."
]

if __name__ == "__main__":
    run_debug("L04: f‑strings", BROKEN, EXPECTED, HINTS)
