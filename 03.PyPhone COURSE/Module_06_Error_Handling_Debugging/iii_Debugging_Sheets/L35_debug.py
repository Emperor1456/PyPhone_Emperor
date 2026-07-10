import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
logging.basicConfig(level=logging.INFO)
logging.info("Information")
logging.warning("Warning")"""

EXPECTED = "INFO:root:Information\nWARNING:root:Warning"
HINTS = [
    "The module 'logging' is used but not imported.",
    "Add 'import logging' at the top.",
    "After importing, both messages will appear."
]

if __name__ == "__main__":
    run_debug("L35: Logging", BROKEN, EXPECTED, HINTS)
