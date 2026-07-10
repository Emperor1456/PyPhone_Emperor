import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
import csv
with open("data.csv", "r") as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        print(row)"""

EXPECTED = "['name', 'age']\n['Alice', '30']\n['Bob', '25']"
HINTS = [
    "The file 'data.csv' is actually comma-separated, but the reader expects semicolons.",
    "Remove the delimiter argument or set it to ','.",
    "Delete 'delimiter=';''."
]

if __name__ == "__main__":
    run_debug("L38: CSV", BROKEN, EXPECTED, HINTS)
