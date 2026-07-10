import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(fruit[i])"""

EXPECTED = "apple\nbanana\ncherry"
HINTS = [
    "The loop variable is 'i', but you're trying to use 'fruit' which is not defined.",
    "Either use 'for fruit in fruits:' or correct the indexing.",
    "Simplest fix: 'for fruit in fruits: print(fruit)'."
]

if __name__ == "__main__":
    run_debug("L11: for Loop", BROKEN, EXPECTED, HINTS)
