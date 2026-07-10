import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
print("python -m venv myenv")
print("source myenv/bin/activate")
print("pip freeze > requirements.txt")"""

EXPECTED = "python -m venv myenv\nsource myenv/bin/activate\npip freeze > requirements.txt"
HINTS = [
    "The code is correct. I need to introduce a bug: missing parentheses.",
    "Let's just make a typo in one of the strings.",
    "Change 'source myenv/bin/activate' to 'source myenv/bin/active'."
]

if __name__ == "__main__":
    run_debug("L50: venv", BROKEN, EXPECTED, HINTS)
