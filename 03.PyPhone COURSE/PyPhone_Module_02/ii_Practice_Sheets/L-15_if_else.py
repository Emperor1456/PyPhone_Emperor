import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="a=3. If a>0 print 'A', else 'B'.",
    expected_output="A",
    level=Level.EASY,
    hints=["a=3","if a>0: print('A')","else: print('B')"]
)

medium = Task(
    description="x=-5. If x>=0 print 'Positive', else 'Negative'.",
    expected_output="Negative",
    level=Level.MEDIUM,
    hints=["x=-5","if x>=0: print('Positive')","else: print('Negative')"]
)

hard = Task(
    description="n=8. Print 'Even' or 'Odd', and 'Positive' or 'Negative' on two lines.",
    expected_output="Even\nPositive",
    level=Level.HARD,
    hints=["n=8","print('Even' if n%2==0 else 'Odd')","print('Positive' if n>=0 else 'Negative')"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
