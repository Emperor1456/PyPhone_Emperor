import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Define a function `hello()` that prints 'Hello, Emperor'. Call it.",
    expected_output="Hello, Emperor",
    level=Level.EASY,
    hints=["def hello(): print('Hello, Emperor')", "hello()"]
)

medium = Task(
    description="Define `greet(name)` returning 'Hi, '+name. Call with 'Emperor' and print the result.",
    expected_output="Hi, Emperor",
    level=Level.MEDIUM,
    hints=["def greet(name): return 'Hi, '+name", "print(greet('Emperor'))"]
)

hard = Task(
    description="Define `square(x)` returning x*x. Call with 5 and print the result.",
    expected_output="25",
    level=Level.HARD,
    hints=["def square(x): return x*x", "print(square(5))"]
)

def main(): c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
