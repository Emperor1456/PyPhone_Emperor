import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🏗️  Define a Simple Class\n\n"
        "Define a class `Dog` with a method `bark` that prints 'Woof!'.\n"
        "Create an instance `d = Dog()` and call `d.bark()`.\n\n"
        "Expected output: Woof!"
    ),
    expected_output="Woof!",
    level=Level.EASY,
    hints=[
        "class Dog:",
        "    def bark(self):",
        "        print('Woof!')",
        "d = Dog()",
        "d.bark()"
    ]
)

easy2 = Task(
    description=(
        "🐱  Class with __init__\n\n"
        "Define a class `Cat` with `__init__` that sets `self.name`.\n"
        "Create an instance `c = Cat('Whiskers')` and print `c.name`.\n\n"
        "Expected output: Whiskers"
    ),
    expected_output="Whiskers",
    level=Level.EASY,
    hints=[
        "class Cat:",
        "    def __init__(self, name):",
        "        self.name = name",
        "c = Cat('Whiskers')",
        "print(c.name)"
    ]
)

medium1 = Task(
    description=(
        "📚  Book Class with Two Attributes\n\n"
        "Define a class `Book` with `__init__(self, title, author)`.\n"
        "Create an instance `b = Book('1984', 'Orwell')` and print both attributes separated by a space.\n\n"
        "Expected output: 1984 Orwell"
    ),
    expected_output="1984 Orwell",
    level=Level.MEDIUM,
    hints=[
        "class Book:",
        "    def __init__(self, title, author):",
        "        self.title = title",
        "        self.author = author",
        "b = Book('1984', 'Orwell')",
        "print(b.title, b.author)"
    ]
)

medium2 = Task(
    description=(
        "🏦  Bank Account Class\n\n"
        "Define a class `BankAccount` with `__init__` that sets `self.balance` to 0.\n"
        "Create an instance `acc = BankAccount()` and print `acc.balance`.\n\n"
        "Expected output: 0"
    ),
    expected_output="0",
    level=Level.MEDIUM,
    hints=[
        "class BankAccount:",
        "    def __init__(self):",
        "        self.balance = 0",
        "acc = BankAccount()",
        "print(acc.balance)"
    ]
)

hard1 = Task(
    description=(
        "🧱  Product Class with Validation\n\n"
        "Define a class `Product` with `__init__(self, name, price)` that raises ValueError if price <= 0.\n"
        "Create an instance with `name='Widget', price=10` and print its name.\n\n"
        "Expected output: Widget"
    ),
    expected_output="Widget",
    level=Level.HARD,
    hints=[
        "class Product:",
        "    def __init__(self, name, price):",
        "        if price <= 0: raise ValueError('Price must be positive')",
        "        self.name = name",
        "        self.price = price",
        "p = Product('Widget', 10)",
        "print(p.name)"
    ]
)

hard2 = Task(
    description=(
        "👤  User with Default Values\n\n"
        "Define a class `User` with `__init__(self, name, active=True)`.\n"
        "Create a user `u = User('Emperor')` and print `u.active`.\n\n"
        "Expected output: True"
    ),
    expected_output="True",
    level=Level.HARD,
    hints=[
        "class User:",
        "    def __init__(self, name, active=True):",
        "        self.name = name",
        "        self.active = active",
        "u = User('Emperor')",
        "print(u.active)"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L41.json")
