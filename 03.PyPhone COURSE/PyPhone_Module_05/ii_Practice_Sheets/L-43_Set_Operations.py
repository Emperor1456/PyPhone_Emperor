import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="a={1,2}, b={3,4}. Print their union.",
    expected_output="{1, 2, 3, 4}",
    level=Level.EASY,
    hints=["a={1,2}; b={3,4}", "print(a|b)"]
)

medium = Task(
    description="a={1,2,3}, b={3,4,5}. Print their intersection.",
    expected_output="{3}",
    level=Level.MEDIUM,
    hints=["a={1,2,3}; b={3,4,5}", "print(a&b)"]
)

hard = Task(
    description="a={1,2,3}, b={3,4,5}. Print the difference a-b.",
    expected_output="{1, 2}",
    level=Level.HARD,
    hints=["a={1,2,3}; b={3,4,5}", "print(a-b)"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
