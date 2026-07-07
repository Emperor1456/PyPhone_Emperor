import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Use try/finally to print 'cleanup' no matter what (safe operation).",
    expected_output="cleanup",
    level=Level.EASY,
    hints=["try:\n    x=1\nfinally:\n    print('cleanup')"]
)

medium = Task(
    description="Use try/except/else: set a variable and print 'else' when no exception occurs.",
    expected_output="else",
    level=Level.MEDIUM,
    hints=["try:\n    y=2\nexcept:\n    pass\nelse:\n    print('else')"]
)

hard = Task(
    description="Combine try/except/else/finally with a deliberate error (1/0). Ensure 'finally' prints last. Print the final value.",
    expected_output="finally",
    level=Level.HARD,
    hints=["try:\n    1/0\nexcept:\n    flow='except'\nelse:\n    flow='else'\nfinally:\n    flow='finally'","print(flow)"]
)

def main(): c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
