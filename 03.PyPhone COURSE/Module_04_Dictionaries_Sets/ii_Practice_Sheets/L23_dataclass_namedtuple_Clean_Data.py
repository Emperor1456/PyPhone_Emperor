import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "📦  Namedtuple – Book Record\n\n"
        "From collections import namedtuple.\n"
        "Create a Book namedtuple with fields 'title' and 'author'.\n"
        "Create an instance for '1984' by 'Orwell' and print the title.\n\n"
        "Expected output: 1984"
    ),
    expected_output="1984",
    level=Level.EASY,
    hints=["from collections import namedtuple", "Book = namedtuple('Book', ['title', 'author'])", "b = Book('1984', 'Orwell')", "print(b.title)"]
)

easy2 = Task(
    description=(
        "🧪  Dataclass – Student Record\n\n"
        "From dataclasses import dataclass.\n"
        "Define a Student dataclass with fields name (str) and grade (float).\n"
        "Create an instance with name='Emperor', grade=95.0 and print it.\n\n"
        "Expected output: Student(name='Emperor', grade=95.0)"
    ),
    expected_output="Student(name='Emperor', grade=95.0)",
    level=Level.EASY,
    hints=["from dataclasses import dataclass", "@dataclass", "class Student:", "    name: str", "    grade: float", "s = Student('Emperor', 95.0)", "print(s)"]
)

medium1 = Task(
    description=(
        "⚖️  Compare Namedtuples\n\n"
        "Create two Book namedtuples with the same fields: b1 = Book('A', 'X'), b2 = Book('A', 'X').\n"
        "Print whether they are equal (==).\n\n"
        "Expected output: True"
    ),
    expected_output="True",
    level=Level.MEDIUM,
    hints=["from collections import namedtuple", "Book = namedtuple('Book', ['title', 'author'])", "b1 = Book('A', 'X')", "b2 = Book('A', 'X')", "print(b1 == b2)"]
)

medium2 = Task(
    description=(
        "🔧  Dataclass with Default\n\n"
        "Define a Product dataclass with fields: name (str), price (float), quantity (int) default 0.\n"
        "Create a Product with name='Widget', price=9.99, quantity omitted. Print it.\n\n"
        "Expected output: Product(name='Widget', price=9.99, quantity=0)"
    ),
    expected_output="Product(name='Widget', price=9.99, quantity=0)",
    level=Level.MEDIUM,
    hints=["from dataclasses import dataclass", "@dataclass", "class Product:", "    name: str", "    price: float", "    quantity: int = 0", "p = Product('Widget', 9.99)", "print(p)"]
)

hard1 = Task(
    description=(
        "🔒  Frozen Dataclass\n\n"
        "Define a frozen dataclass Point with x and y (both int).\n"
        "Create an instance p = Point(5, 10) and print p.x.\n"
        "Then try to change p.x (will raise error, but we just print the value).\n\n"
        "Expected output: 5"
    ),
    expected_output="5",
    level=Level.HARD,
    hints=["from dataclasses import dataclass", "@dataclass(frozen=True)", "class Point:", "    x: int", "    y: int", "p = Point(5, 10)", "print(p.x)"]
)

hard2 = Task(
    description=(
        "🔁  Namedtuple – Multiple Return\n\n"
        "Define a function get_min_max(lst) that returns a namedtuple 'MinMax' with\n"
        "fields 'min' and 'max'. Call it with [3,1,9,4] and print min and max separated by space.\n\n"
        "Expected output: 1 9"
    ),
    expected_output="1 9",
    level=Level.HARD,
    hints=["from collections import namedtuple", "MinMax = namedtuple('MinMax', ['min', 'max'])", "def get_min_max(lst):", "    return MinMax(min(lst), max(lst))", "result = get_min_max([3,1,9,4])", "print(result.min, result.max)"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L23.json")
