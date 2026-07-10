import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{title} by {author}"

b = Book("1984", "Orwell")
print(b)"""

EXPECTED = "1984 by Orwell"
HINTS = [
    "Inside __str__, 'title' and 'author' are not defined; they must be accessed via self.",
    "Use self.title and self.author.",
    "Correct the return statement."
]

if __name__ == "__main__":
    run_debug("L46: Special Methods", BROKEN, EXPECTED, HINTS)
