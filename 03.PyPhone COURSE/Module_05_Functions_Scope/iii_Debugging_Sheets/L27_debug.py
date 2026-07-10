import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("A"))
print(add_item("B"))"""

EXPECTED = "['A']\n['B']"
HINTS = [
    "Mutable default arguments retain state across calls.",
    "The list is shared, causing 'B' to be added to the same list.",
    "Use None as default and create a new list inside the function."
]

if __name__ == "__main__":
    run_debug("L27: Mutable Default", BROKEN, EXPECTED, HINTS)
