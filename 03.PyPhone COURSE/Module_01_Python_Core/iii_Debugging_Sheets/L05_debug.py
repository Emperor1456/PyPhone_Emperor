import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
import sys
name = sys.argv[1]
print(f"Hello, {name}!")"""

EXPECTED = "Hello, Guest"

HINTS = [
    "What if no argument is provided? sys.argv may have only one element.",
    "Check if len(sys.argv) > 1 before accessing sys.argv[1].",
    "Use name = sys.argv[1] if len(sys.argv) > 1 else 'Guest'."
]

if __name__ == "__main__":
    run_debug("L05: Command‑Line Arguments", BROKEN, EXPECTED, HINTS)
