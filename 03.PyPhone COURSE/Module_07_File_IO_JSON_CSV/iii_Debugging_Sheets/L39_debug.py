import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
import json
data = {"name": "Emperor"}
json.dump(data, "data.json")
print(open("data.json").read())"""

EXPECTED = '{"name": "Emperor"}'
HINTS = [
    "json.dump writes to a file object, not a filename.",
    "Open the file and pass the file handle.",
    "Use with open('data.json', 'w') as f: json.dump(data, f)"
]

if __name__ == "__main__":
    run_debug("L39: JSON", BROKEN, EXPECTED, HINTS)
