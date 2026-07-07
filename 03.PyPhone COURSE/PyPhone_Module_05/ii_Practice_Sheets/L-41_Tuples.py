import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Create a tuple (1,2,3) and print it.",
    expected_output="(1, 2, 3)",
    level=Level.EASY,
    hints=["t=(1,2,3)", "print(t)"]
)

medium = Task(
    description="t=(1,2,3). Print the first and last element on separate lines.",
    expected_output="1\n3",
    level=Level.MEDIUM,
    hints=["t=(1,2,3)", "print(t[0])", "print(t[-1])"]
)

hard = Task(
    description="t1=(1,2,3), t2=(4,5). Concatenate and print the result.",
    expected_output="(1, 2, 3, 4, 5)",
    level=Level.HARD,
    hints=["t1=(1,2,3); t2=(4,5)", "print(t1+t2)"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
