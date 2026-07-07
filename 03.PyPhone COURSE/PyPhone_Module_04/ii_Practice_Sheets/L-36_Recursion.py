import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Define recursive `factorial(n)`. Call with 4 and print.",
    expected_output="24",
    level=Level.EASY,
    hints=["def factorial(n):\n    if n<=1: return 1\n    return n*factorial(n-1)","print(factorial(4))"]
)

medium = Task(
    description="Define recursive `fib(n)` returning nth Fibonacci (0-indexed: fib(0)=0, fib(1)=1). Call with 5 and print.",
    expected_output="5",
    level=Level.MEDIUM,
    hints=["def fib(n):\n    if n<=1: return n\n    return fib(n-1)+fib(n-2)","print(fib(5))"]
)

hard = Task(
    description="Define recursive `countdown(n)` returning a list from n down to 1. Call with 5 and print.",
    expected_output="[5, 4, 3, 2, 1]",
    level=Level.HARD,
    hints=["def countdown(n):\n    if n<=0: return []\n    return [n]+countdown(n-1)","print(countdown(5))"]
)

def main(): c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
