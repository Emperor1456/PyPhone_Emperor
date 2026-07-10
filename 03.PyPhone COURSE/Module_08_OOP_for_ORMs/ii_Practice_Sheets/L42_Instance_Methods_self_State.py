import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🐶  Dog with speak method\n\n"
        "Define a class `Dog` with `__init__` setting `self.name`, and method `speak` returning 'Woof! I am '+name.\n"
        "Create `d = Dog('Rex')`, call `d.speak()` and print.\n\n"
        "Expected output: Woof! I am Rex"
    ),
    expected_output="Woof! I am Rex",
    level=Level.EASY,
    hints=[
        "class Dog:",
        "    def __init__(self, name):",
        "        self.name = name",
        "    def speak(self):",
        "        return 'Woof! I am ' + self.name",
        "d = Dog('Rex')",
        "print(d.speak())"
    ]
)

easy2 = Task(
    description=(
        "🔢  Counter with increment\n\n"
        "Define a class `Counter` with `__init__` setting `self.count=0`, method `increment` that adds 1.\n"
        "Create `c = Counter()`, call `c.increment()`, then print `c.count`.\n\n"
        "Expected output: 1"
    ),
    expected_output="1",
    level=Level.EASY,
    hints=[
        "class Counter:",
        "    def __init__(self):",
        "        self.count = 0",
        "    def increment(self):",
        "        self.count += 1",
        "c = Counter()",
        "c.increment()",
        "print(c.count)"
    ]
)

medium1 = Task(
    description=(
        "🧮  Calculator with add method\n\n"
        "Define a class `Calculator` with method `add(self, a, b)` returning a+b.\n"
        "Create an instance, call `add(3,5)` and print result.\n\n"
        "Expected output: 8"
    ),
    expected_output="8",
    level=Level.MEDIUM,
    hints=[
        "class Calculator:",
        "    def add(self, a, b):",
        "        return a + b",
        "calc = Calculator()",
        "print(calc.add(3, 5))"
    ]
)

medium2 = Task(
    description=(
        "🏦  Bank Account with deposit\n\n"
        "Define a class `BankAccount` with `__init__` setting `self.balance=0`, method `deposit(self, amount)` that adds amount to balance if positive.\n"
        "Create `acc = BankAccount()`, deposit 100, print `acc.balance`.\n\n"
        "Expected output: 100"
    ),
    expected_output="100",
    level=Level.MEDIUM,
    hints=[
        "class BankAccount:",
        "    def __init__(self):",
        "        self.balance = 0",
        "    def deposit(self, amount):",
        "        if amount > 0:",
        "            self.balance += amount",
        "acc = BankAccount()",
        "acc.deposit(100)",
        "print(acc.balance)"
    ]
)

hard1 = Task(
    description=(
        "🔐  Safe Withdrawal\n\n"
        "Extend BankAccount: add method `withdraw(self, amount)` that subtracts if amount <= balance, else prints 'Insufficient'.\n"
        "Create account, deposit 100, withdraw 150 (should print 'Insufficient'), print balance.\n\n"
        "Expected output:\nInsufficient\n100"
    ),
    expected_output="Insufficient\n100",
    level=Level.HARD,
    hints=[
        "class BankAccount:",
        "    def __init__(self): self.balance = 0",
        "    def deposit(self, amount):",
        "        if amount > 0: self.balance += amount",
        "    def withdraw(self, amount):",
        "        if amount <= self.balance: self.balance -= amount",
        "        else: print('Insufficient')",
        "acc = BankAccount()",
        "acc.deposit(100)",
        "acc.withdraw(150)",
        "print(acc.balance)"
    ]
)

hard2 = Task(
    description=(
        "📊  Stats Tracker\n\n"
        "Define a class `Stats` with `__init__` that creates an empty list `self.numbers`, method `add(self, num)` that appends, method `average(self)` that returns mean of list or 0 if empty.\n"
        "Add 10, 20, 30 and print average.\n\n"
        "Expected output: 20.0"
    ),
    expected_output="20.0",
    level=Level.HARD,
    hints=[
        "class Stats:",
        "    def __init__(self): self.numbers = []",
        "    def add(self, num): self.numbers.append(num)",
        "    def average(self):",
        "        return sum(self.numbers)/len(self.numbers) if self.numbers else 0",
        "s = Stats()",
        "s.add(10); s.add(20); s.add(30)",
        "print(s.average())"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L42.json")
