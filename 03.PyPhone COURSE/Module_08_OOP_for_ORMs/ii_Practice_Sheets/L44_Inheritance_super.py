import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🧬  Simple Inheritance\n\n"
        "Define `Animal` with method `speak` returning '?'. Define `Dog(Animal)` overriding `speak` to return 'Woof'.\n"
        "Create `d = Dog()` and print `d.speak()`.\n\n"
        "Expected output: Woof"
    ),
    expected_output="Woof",
    level=Level.EASY,
    hints=[
        "class Animal:",
        "    def speak(self): return '?'",
        "class Dog(Animal):",
        "    def speak(self): return 'Woof'",
        "d = Dog()",
        "print(d.speak())"
    ]
)

easy2 = Task(
    description=(
        "🐱  Another Child\n\n"
        "Add another subclass `Cat` overriding `speak` to return 'Meow'. Create instance and print.\n\n"
        "Expected output: Meow"
    ),
    expected_output="Meow",
    level=Level.EASY,
    hints=[
        "class Animal: def speak(self): return '?'",
        "class Cat(Animal):",
        "    def speak(self): return 'Meow'",
        "c = Cat()",
        "print(c.speak())"
    ]
)

medium1 = Task(
    description=(
        "🐦  Child Without Override\n\n"
        "Define `Bird(Animal)` that does NOT override speak. Create instance, print `speak()`.\n\n"
        "Expected output: ?"
    ),
    expected_output="?",
    level=Level.MEDIUM,
    hints=[
        "class Animal: def speak(self): return '?'",
        "class Bird(Animal): pass",
        "b = Bird()",
        "print(b.speak())"
    ]
)

medium2 = Task(
    description=(
        "⚙️  Using super().__init__\n\n"
        "Define `Animal` with `__init__(self, name)`. `Dog` inherits, calls `super().__init__(name)`.\n"
        "Create `d = Dog('Rex')`, print `d.name`.\n\n"
        "Expected output: Rex"
    ),
    expected_output="Rex",
    level=Level.MEDIUM,
    hints=[
        "class Animal:",
        "    def __init__(self, name): self.name = name",
        "class Dog(Animal):",
        "    def __init__(self, name):",
        "        super().__init__(name)",
        "d = Dog('Rex')",
        "print(d.name)"
    ]
)

hard1 = Task(
    description=(
        "🏦  Account Hierarchy\n\n"
        "Define `Account` with `__init__(self, id, balance)`. `SavingsAccount(Account)` with `interest_rate` in __init__.\n"
        "Create `sa = SavingsAccount('A1', 1000, 0.05)`. Print balance.\n\n"
        "Expected output: 1000"
    ),
    expected_output="1000",
    level=Level.HARD,
    hints=[
        "class Account:",
        "    def __init__(self, id, balance):",
        "        self.id = id",
        "        self.balance = balance",
        "class SavingsAccount(Account):",
        "    def __init__(self, id, balance, rate):",
        "        super().__init__(id, balance)",
        "        self.rate = rate",
        "sa = SavingsAccount('A1', 1000, 0.05)",
        "print(sa.balance)"
    ]
)

hard2 = Task(
    description=(
        "🔁  Method Override with super()\n\n"
        "Define `Employee` with `info()` returning 'Employee'. `Manager(Employee)` overrides `info()` to return super().info() + ' Manager'.\n"
        "Create `m = Manager()`, print `m.info()`.\n\n"
        "Expected output: Employee Manager"
    ),
    expected_output="Employee Manager",
    level=Level.HARD,
    hints=[
        "class Employee:",
        "    def info(self): return 'Employee'",
        "class Manager(Employee):",
        "    def info(self): return super().info() + ' Manager'",
        "m = Manager()",
        "print(m.info())"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L44.json")
