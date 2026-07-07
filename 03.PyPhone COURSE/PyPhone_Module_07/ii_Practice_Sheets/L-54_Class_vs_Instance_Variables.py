import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Define `Employee` with class variable `company='PyPhone'`. Print `Employee.company`.",
    expected_output="PyPhone",
    level=Level.EASY,
    hints=["class Employee:\n    company='PyPhone'","print(Employee.company)"]
)

medium = Task(
    description="Create two Employee instances and print both share the same `company` value.",
    expected_output="PyPhone PyPhone",
    level=Level.MEDIUM,
    hints=["e1=Employee(); e2=Employee()","print(e1.company, e2.company)"]
)

hard = Task(
    description="Define `Car` with class variable `wheels=4`. Create instance `c` and print `c.wheels`.",
    expected_output="4",
    level=Level.HARD,
    hints=["class Car:\n    wheels=4","c=Car()","print(c.wheels)"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
