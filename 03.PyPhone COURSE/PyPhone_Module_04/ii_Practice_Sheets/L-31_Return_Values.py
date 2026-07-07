import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Define `double(x)` returning 2*x. Call with 5 and print.",
    expected_output="10",
    level=Level.EASY,
    hints=["def double(x): return 2*x", "print(double(5))"]
)

medium = Task(
    description="Define `absolute(x)` returning x if x>=0 else -x. Call with -7 and print.",
    expected_output="7",
    level=Level.MEDIUM,
    hints=["def absolute(x):\n    if x>=0: return x\n    else: return -x", "print(absolute(-7))"]
)

hard = Task(
    description="Define `is_even(n)` returning True if n%2==0 else False. Call with 8 and print.",
    expected_output="True",
    level=Level.HARD,
    hints=["def is_even(n): return n%2==0", "print(is_even(8))"]
)

def main(): c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
