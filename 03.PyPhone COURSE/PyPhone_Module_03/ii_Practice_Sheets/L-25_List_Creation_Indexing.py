import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Create list [1,2,3] and print it.",
    expected_output="[1, 2, 3]",
    level=Level.EASY,
    hints=["lst=[1,2,3]","print(lst)"]
)

medium = Task(
    description="lst=[10,20,30,40]. Print the third element (index 2).",
    expected_output="30",
    level=Level.MEDIUM,
    hints=["lst=[10,20,30,40]","print(lst[2])"]
)

hard = Task(
    description="lst=[10,20,30,40]. Print the last element using negative indexing.",
    expected_output="40",
    level=Level.HARD,
    hints=["lst=[10,20,30,40]","print(lst[-1])"]
)

def main(): c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
