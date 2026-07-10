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
    "The default list is shared across all calls.",
    "Use None as the default value and create a new list inside the function.",
    "Change def signature to items=None, and if items is None: items = []."
]

if __name__ == "__main__":
    run_debug("L07: None & Mutable Defaults", BROKEN, EXPECTED, HINTS)
