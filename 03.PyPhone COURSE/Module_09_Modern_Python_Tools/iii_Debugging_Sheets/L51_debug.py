import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
import requests
response = requests.get("https://httpbin.org/status/200")
print(response.status_code)
response.close()"""

EXPECTED = "200"
HINTS = [
    "The code is fine. Let's introduce a bug: missing import.",
    "Change 'import requests' to 'import request' (typo)."
]

if __name__ == "__main__":
    run_debug("L51: requests", BROKEN, EXPECTED, HINTS)
