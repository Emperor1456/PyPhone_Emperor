import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'Employee' in g and callable(g['Employee']) and hasattr(g['Employee'], 'company') and g['Employee'].company=='PyPhone'
easy=Task("Define class `Employee` with class variable `company='PyPhone'`. Then create instance `e` and access `e.company`.", verify_easy, Level.EASY, hints=["class Employee:\n    company='PyPhone'","e=Employee()","print(e.company)"])
def verify_medium(g): return 'e1' in g and 'e2' in g and g['e1'].company==g['e2'].company and g['e1'].company=='PyPhone'
medium=Task("Create two instances of Employee and demonstrate that company is shared.", verify_medium, Level.MEDIUM, hints=["e1=Employee()","e2=Employee()","print(e1.company, e2.company)"])
def verify_hard(g): return 'Car' in g and callable(g['Car']) and hasattr(g['Car'], 'wheels') and g['Car'].wheels==4 and 'c' in g and isinstance(g['c'], g['Car']) and g['c'].wheels==4
hard=Task("Define class `Car` with class variable `wheels=4`. Create instance `c` and access `c.wheels`.", verify_hard, Level.HARD, hints=["class Car:\n    wheels=4","c=Car()","print(c.wheels)"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
