import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
from enum import Enum

class Status(Enum):
    PENDING = 1
    ACTIVE = 2

print(Status.ACTIVE == 2)"""

EXPECTED = "True"
HINTS = [
    "Enum members are not equal to their values directly; you must compare with .value.",
    "Change to 'Status.ACTIVE.value == 2' or compare enum with enum.",
    "Simpler: compare Status.ACTIVE == Status.ACTIVE."
]

if __name__ == "__main__":
    run_debug("L48: Enum", BROKEN, EXPECTED, HINTS)
