import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🖨️  __str__ Method\n\n"
        "Define a class `Book` with `__init__(title, author)` and `__str__` returning 'title by author'.\n"
        "Create `b = Book('1984', 'Orwell')` and print `str(b)`.\n\n"
        "Expected output: 1984 by Orwell"
    ),
    expected_output="1984 by Orwell",
    level=Level.EASY,
    hints=[
        "class Book:",
        "    def __init__(self, title, author):",
        "        self.title = title",
        "        self.author = author",
        "    def __str__(self):",
        "        return f'{self.title} by {self.author}'",
        "b = Book('1984', 'Orwell')",
        "print(str(b))"
    ]
)

easy2 = Task(
    description=(
        "📏  __len__ Method\n\n"
        "Add `__len__` to the Book class that returns 0. Print `len(b)`.\n\n"
        "Expected output: 0"
    ),
    expected_output="0",
    level=Level.EASY,
    hints=[
        "class Book:",
        "    def __init__(self, title, author): self.title=title; self.author=author",
        "    def __str__(self): return f'{self.title} by {self.author}'",
        "    def __len__(self): return 0",
        "b = Book('1984','Orwell')",
        "print(len(b))"
    ]
)

medium1 = Task(
    description=(
        "🔬  __repr__ Method\n\n"
        "Define a class `Point` with `__init__(x,y)` and `__repr__` returning 'Point(x, y)'.\n"
        "Create `p = Point(3, 4)` and print `repr(p)`.\n\n"
        "Expected output: Point(3, 4)"
    ),
    expected_output="Point(3, 4)",
    level=Level.MEDIUM,
    hints=[
        "class Point:",
        "    def __init__(self, x, y): self.x=x; self.y=y",
        "    def __repr__(self): return f'Point({self.x}, {self.y})'",
        "p = Point(3, 4)",
        "print(repr(p))"
    ]
)

medium2 = Task(
    description=(
        "⚖️  __eq__ Method\n\n"
        "Add `__eq__` to Point that returns True if both x and y are equal. Create two points p1(1,2) and p2(1,2), print p1 == p2.\n\n"
        "Expected output: True"
    ),
    expected_output="True",
    level=Level.MEDIUM,
    hints=[
        "class Point:",
        "    def __init__(self,x,y): self.x=x; self.y=y",
        "    def __eq__(self, other): return self.x==other.x and self.y==other.y",
        "p1=Point(1,2); p2=Point(1,2)",
        "print(p1==p2)"
    ]
)

hard1 = Task(
    description=(
        "➕  __add__ Operator Overloading\n\n"
        "Define `Vector` with x,y and `__add__` to add two vectors. Create v1=(2,3), v2=(4,5), print (v1+v2).x and (v1+v2).y on separate lines.\n\n"
        "Expected output:\n6\n8"
    ),
    expected_output="6\n8",
    level=Level.HARD,
    hints=[
        "class Vector:",
        "    def __init__(self, x, y): self.x=x; self.y=y",
        "    def __add__(self, other): return Vector(self.x+other.x, self.y+other.y)",
        "v1=Vector(2,3); v2=Vector(4,5)",
        "v3=v1+v2",
        "print(v3.x)",
        "print(v3.y)"
    ]
)

hard2 = Task(
    description=(
        "📋  __str__ for Product\n\n"
        "Define `Product` with name and price. `__str__` returns f'{name} (${price:.2f})'.\n"
        "Create product 'Laptop' at 999.99, print it.\n\n"
        "Expected output: Laptop ($999.99)"
    ),
    expected_output="Laptop ($999.99)",
    level=Level.HARD,
    hints=[
        "class Product:",
        "    def __init__(self, name, price): self.name=name; self.price=price",
        "    def __str__(self): return f'{self.name} (${self.price:.2f})'",
        "p = Product('Laptop', 999.99)",
        "print(p)"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L46.json")
