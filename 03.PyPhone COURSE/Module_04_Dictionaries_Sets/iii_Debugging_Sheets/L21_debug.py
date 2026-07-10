import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
counts = {}
counts["apple"] = 1
print(counts["banana"])"""

EXPECTED = "0"
HINTS = [
    "The regular dict raises KeyError for missing keys.",
    "Use dict.get('banana', 0) to provide a default.",
    "Change print(counts['banana']) to print(counts.get('banana', 0))."
]

if __name__ == "__main__":
    run_debug("L21: defaultdict", BROKEN, EXPECTED, HINTS)
