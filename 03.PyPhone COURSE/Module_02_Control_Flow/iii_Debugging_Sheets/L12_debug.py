import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
for i in range(1, 7):
    if i % 2 == 0:
        print(i)
    else:
        continue
    print("done")"""

EXPECTED = "2\n4\n6\ndone\ndone\ndone"
HINTS = [
    "The continue statement skips the rest of the loop iteration.",
    "When i is odd, continue jumps to the next iteration, so 'done' is not printed.",
    "The expected output shows 'done' after every number, not just evens.",
    "Remove the else: continue block entirely."
]

if __name__ == "__main__":
    run_debug("L12: break, continue, pass", BROKEN, EXPECTED, HINTS)
