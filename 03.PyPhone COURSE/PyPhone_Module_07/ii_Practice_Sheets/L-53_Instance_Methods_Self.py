import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Define `Dog` with `__init__` setting `self.name`, and method `speak` returning 'Woof! I am '+name. Create `d` with name 'Rex', call `d.speak()` and print.",
    expected_output="Woof! I am Rex",
    level=Level.EASY,
    hints=["class Dog:\n    def __init__(self,name):\n        self.name=name\n    def speak(self):\n        return 'Woof! I am '+self.name","d=Dog('Rex')","print(d.speak())"]
)

medium = Task(
    description="Define `Counter` with `__init__` setting `self.count=0`, method `increment` that adds 1. Create `c`, call `c.increment()`, then print `c.count`.",
    expected_output="1",
    level=Level.MEDIUM,
    hints=["class Counter:\n    def __init__(self):\n        self.count=0\n    def increment(self):\n        self.count+=1","c=Counter()","c.increment()","print(c.count)"]
)

hard = Task(
    description="Define `Calculator` with method `add(self,a,b)` returning a+b. Create instance, call `add(3,5)` and print result.",
    expected_output="8",
    level=Level.HARD,
    hints=["class Calculator:\n    def add(self,a,b):\n        return a+b","calc=Calculator()","print(calc.add(3,5))"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
