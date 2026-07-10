import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

p = Product("Widget", 9.99)
print(p.description)"""

EXPECTED = "0"
HINTS = [
    "The Product class doesn't have a 'description' field.",
    "The code tries to print p.description, which raises AttributeError.",
    "Fix: print(p.quantity) instead."
]

if __name__ == "__main__":
    run_debug("L23: dataclass", BROKEN, EXPECTED, HINTS)
