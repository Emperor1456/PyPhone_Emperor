import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
import asyncio

async def greet():
    print("Hello, Emperor")

greet()"""

EXPECTED = "Hello, Emperor"
HINTS = [
    "Calling an async function returns a coroutine object, not the result.",
    "You need to use asyncio.run() to execute it.",
    "Change 'greet()' to 'asyncio.run(greet())'."
]

if __name__ == "__main__":
    run_debug("L56: Async", BROKEN, EXPECTED, HINTS)
