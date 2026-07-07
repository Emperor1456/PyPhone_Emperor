import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description=(
        "Define a class `Book` with:\n"
        "- `__init__(self,title,author)`\n"
        "- `__str__(self)` returning 'title by author'\n"
        "Create instance for '1984','Orwell' and print it."
    ),
    expected_output="1984 by Orwell",
    level=Level.EASY,
    hints=[
        "class Book:\n    def __init__(self,t,a):\n        self.t=t; self.a=a\n    def __str__(self):\n        return f'{self.t} by {self.a}'",
        "print(Book('1984','Orwell'))"
    ]
)

medium = Task(
    description=(
        "Define a class `Circle` with:\n"
        "- `__init__(self,radius)`\n"
        "- `@property` `diameter` returning 2*radius\n"
        "Create instance r=5, print diameter."
    ),
    expected_output="10",
    level=Level.MEDIUM,
    hints=[
        "class Circle:\n    def __init__(self,r):\n        self.r=r\n    @property\n    def diameter(self):\n        return 2*self.r",
        "print(Circle(5).diameter)"
    ]
)

hard = Task(
    description=(
        "Payroll System\n\n"
        "Define classes:\n"
        "- Employee: __init__(name, base_salary)\n"
        "  method `get_bonus()` returns 0\n"
        "  property `annual` returns base_salary*12\n"
        "- Manager(Employee): __init__(name, base_salary, team_size)\n"
        "  override `get_bonus()` returning team_size*100\n"
        "\n"
        "Process these employees:\n"
        "  Employee('Alice', 3000)\n"
        "  Manager('Bob', 5000, 4)\n"
        "  Employee('Charlie', 2500)\n"
        "\n"
        "Print a payroll report:\n"
        "Name, Base Salary, Bonus, Annual Salary\n"
        "one line per employee, sorted by name."
    ),
    expected_output=(
        "Alice 3000 0 36000\n"
        "Bob 5000 400 60000\n"
        "Charlie 2500 0 30000"
    ),
    level=Level.HARD,
    hints=[
        "class Employee:",
        "    def __init__(self,name,base):",
        "        self.name=name; self.base=base",
        "    def get_bonus(self):",
        "        return 0",
        "    @property",
        "    def annual(self):",
        "        return self.base*12",
        "class Manager(Employee):",
        "    def __init__(self,name,base,team):",
        "        super().__init__(name,base)",
        "        self.team=team",
        "    def get_bonus(self):",
        "        return self.team*100",
        "staff = [Employee('Alice',3000),Manager('Bob',5000,4),Employee('Charlie',2500)]",
        "for p in sorted(staff, key=lambda x: x.name):",
        "    print(f'{p.name} {p.base} {p.get_bonus()} {p.annual}')"
    ]
)

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__":
    main()
