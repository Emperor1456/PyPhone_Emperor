import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🔒  Read-Only Property\n\n"
        "Define a class `Circle` with `__init__(radius)` and `@property` `diameter` returning 2*radius.\n"
        "Create `c = Circle(5)` and print `c.diameter`.\n\n"
        "Expected output: 10"
    ),
    expected_output="10",
    level=Level.EASY,
    hints=[
        "class Circle:",
        "    def __init__(self, radius): self.radius = radius",
        "    @property",
        "    def diameter(self): return 2 * self.radius",
        "c = Circle(5)",
        "print(c.diameter)"
    ]
)

easy2 = Task(
    description=(
        "🌡️  Fahrenheit Property\n\n"
        "Define `Temperature` with `__init__(celsius)` and `@property` `fahrenheit` returning celsius*9/5+32.\n"
        "Create `t = Temperature(0)`, print `t.fahrenheit`.\n\n"
        "Expected output: 32.0"
    ),
    expected_output="32.0",
    level=Level.EASY,
    hints=[
        "class Temperature:",
        "    def __init__(self, celsius): self.celsius = celsius",
        "    @property",
        "    def fahrenheit(self): return self.celsius * 9/5 + 32",
        "t = Temperature(0)",
        "print(t.fahrenheit)"
    ]
)

medium1 = Task(
    description=(
        "✏️  Setter for Radius\n\n"
        "Add a setter to Circle for radius that validates radius > 0.\n"
        "Create circle, set radius to 10 via setter, print `c.diameter`.\n\n"
        "Expected output: 20"
    ),
    expected_output="20",
    level=Level.MEDIUM,
    hints=[
        "class Circle:",
        "    def __init__(self, radius): self._radius = radius",
        "    @property",
        "    def radius(self): return self._radius",
        "    @radius.setter",
        "    def radius(self, value):",
        "        if value <= 0: raise ValueError('Positive only')",
        "        self._radius = value",
        "    @property",
        "    def diameter(self): return 2 * self._radius",
        "c = Circle(5)",
        "c.radius = 10",
        "print(c.diameter)"
    ]
)

medium2 = Task(
    description=(
        "🌡️  Setter for Celsius\n\n"
        "Add a setter to Temperature for celsius that updates `_celsius`.\n"
        "Create `t = Temperature(0)`, set `t.celsius = 100`, print `t.fahrenheit`.\n\n"
        "Expected output: 212.0"
    ),
    expected_output="212.0",
    level=Level.MEDIUM,
    hints=[
        "class Temperature:",
        "    def __init__(self, celsius): self._celsius = celsius",
        "    @property",
        "    def celsius(self): return self._celsius",
        "    @celsius.setter",
        "    def celsius(self, value): self._celsius = value",
        "    @property",
        "    def fahrenheit(self): return self._celsius * 9/5 + 32",
        "t = Temperature(0)",
        "t.celsius = 100",
        "print(t.fahrenheit)"
    ]
)

hard1 = Task(
    description=(
        "🏦  Bank Account Property\n\n"
        "Define `Account` with private `_balance`. Provide property `balance` with getter, and setter that rejects negative.\n"
        "Create account with 100, set to 200, print balance.\n\n"
        "Expected output: 200"
    ),
    expected_output="200",
    level=Level.HARD,
    hints=[
        "class Account:",
        "    def __init__(self, balance): self._balance = balance",
        "    @property",
        "    def balance(self): return self._balance",
        "    @balance.setter",
        "    def balance(self, amount):",
        "        if amount < 0: raise ValueError('Negative not allowed')",
        "        self._balance = amount",
        "acc = Account(100)",
        "acc.balance = 200",
        "print(acc.balance)"
    ]
)

hard2 = Task(
    description=(
        "🔐  Password Validation with Property\n\n"
        "Define `User` with `_password`. Use property `password` with setter that enforces min length 8.\n"
        "Create user, set password to 'secure123', print 'Set'.\n\n"
        "Expected output: Set"
    ),
    expected_output="Set",
    level=Level.HARD,
    hints=[
        "class User:",
        "    def __init__(self): self._password = ''",
        "    @property",
        "    def password(self): return '****'",
        "    @password.setter",
        "    def password(self, value):",
        "        if len(value) < 8: raise ValueError('Too short')",
        "        self._password = value",
        "u = User()",
        "u.password = 'secure123'",
        "print('Set')"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L47.json")
