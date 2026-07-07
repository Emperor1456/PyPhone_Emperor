import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Define `Person` with `__init__` setting `self.name`. Create `p` with name 'Emperor' and print `p.name`.",
    expected_output="Emperor",
    level=Level.EASY,
    hints=["class Person:\n    def __init__(self,name):\n        self.name=name","p=Person('Emperor')","print(p.name)"]
)

medium = Task(
    description="Define `Car` with `__init__` taking make and model. Create `c` with make='Toyota', model='Corolla' and print both.",
    expected_output="Toyota Corolla",
    level=Level.MEDIUM,
    hints=["class Car:\n    def __init__(self,make,model):\n        self.make=make\n        self.model=model","c=Car('Toyota','Corolla')","print(c.make,c.model)"]
)

hard = Task(
    description="Define `BankAccount` with `__init__` setting `self.balance=0`. Create instance `acc`, then print `acc.balance`.",
    expected_output="0",
    level=Level.HARD,
    hints=["class BankAccount:\n    def __init__(self):\n        self.balance=0","acc=BankAccount()","print(acc.balance)"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
