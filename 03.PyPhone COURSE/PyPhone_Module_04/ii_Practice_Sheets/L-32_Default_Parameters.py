import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Define `greet(name='Guest')` returning 'Hello '+name. Call with no arguments and print.",
    expected_output="Hello Guest",
    level=Level.EASY,
    hints=["def greet(name='Guest'): return 'Hello '+name", "print(greet())"]
)

medium = Task(
    description="Using same `greet`, call with 'Emperor' and print.",
    expected_output="Hello Emperor",
    level=Level.MEDIUM,
    hints=["print(greet('Emperor'))"]
)

hard = Task(
    description="Define `power(x,exp=2)` returning x**exp. Call with 2 (default exp) and print; then with 3,2 and print.",
    expected_output="4\n9",
    level=Level.HARD,
    hints=["def power(x,exp=2): return x**exp", "print(power(2))", "print(power(3,2))"]
)

def main(): c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
