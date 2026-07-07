import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Use try/except/else/finally with a deliberate error (1/0). Print 'except' and then 'finally' on separate lines.",
    expected_output="except\nfinally",
    level=Level.EASY,
    hints=["try:\n    1/0\nexcept:\n    print('except')\nfinally:\n    print('finally')"]
)

medium = Task(
    description="Use try/else without exception: print 'else'.",
    expected_output="else",
    level=Level.MEDIUM,
    hints=["try:\n    x=1\nexcept:\n    pass\nelse:\n    print('else')"]
)

hard = Task(
    description="Implement a safe division function that returns 'error' on ZeroDivisionError, else the result. Call with 10/2 and print the result.",
    expected_output="5.0",
    level=Level.HARD,
    hints=["def safe_div(a,b):\n    try:\n        return a/b\n    except ZeroDivisionError:\n        return 'error'","print(safe_div(10,2))"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
