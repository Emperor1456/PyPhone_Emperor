import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy = Task(
    description=(
        "🏗️  Product Class\n\n"
        "Define a class `Product` with `__init__(self, name, price)`.\n"
        "Create an instance `p = Product('Widget', 9.99)` and print its name.\n\n"
        "Expected output: Widget"
    ),
    expected_output="Widget",
    level=Level.EASY,
    hints=[
        "class Product:",
        "    def __init__(self, name, price): self.name=name; self.price=price",
        "p = Product('Widget', 9.99)",
        "print(p.name)"
    ]
)

medium = Task(
    description=(
        "🧬  Inheritance & Override\n\n"
        "Define `Animal` with method `speak` returning '?'. Define `Cat(Animal)`\n"
        "overriding `speak` to return 'Meow'. Create a Cat and print its speak.\n\n"
        "Expected output: Meow"
    ),
    expected_output="Meow",
    level=Level.MEDIUM,
    hints=[
        "class Animal:",
        "    def speak(self): return '?'",
        "class Cat(Animal):",
        "    def speak(self): return 'Meow'",
        "c = Cat()",
        "print(c.speak())"
    ]
)

hard = Task(
    description=(
        "🔒  Property with Setter\n\n"
        "Define a class `Circle` with a private `_radius`. Add a property `radius`\n"
        "with a getter and a setter that validates radius > 0. Create a circle,\n"
        "set radius to 10 via the setter, and print the diameter (2*radius) via a\n"
        "property `diameter`.\n\n"
        "Expected output: 20"
    ),
    expected_output="20",
    level=Level.HARD,
    hints=[
        "class Circle:",
        "    def __init__(self, radius): self._radius = radius",
        "    @property",
        "    def radius(self): return self._radius",
        "    @radius.setter",
        "    def radius(self, val):",
        "        if val <= 0: raise ValueError",
        "        self._radius = val",
        "    @property",
        "    def diameter(self): return 2 * self._radius",
        "c = Circle(5)",
        "c.radius = 10",
        "print(c.diameter)"
    ]
)

if __name__ == "__main__":
    run_sequence([easy, medium, hard],
                 save_path=MODULE_DIR,
                 progress_name=".progress_review_M08.json")
