import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'Person' in g and callable(g['Person']) and 'p' in g and isinstance(g['p'], g['Person']) and g['p'].name=='Emperor'
easy=Task("Define class `Person` with `__init__` that sets `self.name`. Create `p` with name 'Emperor'.", verify_easy, Level.EASY, hints=["class Person:\n    def __init__(self,name):\n        self.name=name","p=Person('Emperor')"])
def verify_medium(g): return 'Car' in g and callable(g['Car']) and 'c' in g and isinstance(g['c'], g['Car']) and g['c'].make=='Toyota' and g['c'].model=='Corolla'
medium=Task("Define class `Car` with `__init__` taking make and model. Create instance `c` with make='Toyota', model='Corolla'.", verify_medium, Level.MEDIUM, hints=["class Car:\n    def __init__(self,make,model):\n        self.make=make\n        self.model=model","c=Car('Toyota','Corolla')"])
def verify_hard(g): return 'BankAccount' in g and callable(g['BankAccount']) and 'acc' in g and isinstance(g['acc'], g['BankAccount']) and g['acc'].balance==0
hard=Task("Define class `BankAccount` with `__init__` that sets `self.balance=0`. Create instance `acc`.", verify_hard, Level.HARD, hints=["class BankAccount:\n    def __init__(self):\n        self.balance=0","acc=BankAccount()"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
