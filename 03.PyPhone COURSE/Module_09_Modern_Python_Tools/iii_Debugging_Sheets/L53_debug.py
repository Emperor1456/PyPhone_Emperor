import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
from datetime import datetime
date_str = "2026-01-15"
parsed = datetime.strptime(date_str, "%Y-%m-%d")
print(parsed.year(), parsed.month())"""

EXPECTED = "2026 1"
HINTS = [
    "year and month are attributes, not methods.",
    "Remove the parentheses after 'year' and 'month'.",
    "Also print them with a space."
]

if __name__ == "__main__":
    run_debug("L53: datetime", BROKEN, EXPECTED, HINTS)
