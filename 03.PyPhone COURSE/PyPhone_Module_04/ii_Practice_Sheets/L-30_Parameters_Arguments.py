import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Define `add(a,b)` returning a+b. Call with 3,5 and print.",
    expected_output="8",
    level=Level.EASY,
    hints=["def add(a,b): return a+b", "print(add(3,5))"]
)

medium = Task(
    description="Define `full_name(first,last)` returning 'first last'. Call with 'Emperor','PyPhone' and print.",
    expected_output="Emperor PyPhone",
    level=Level.MEDIUM,
    hints=["def full_name(first,last): return first+' '+last", "print(full_name('Emperor','PyPhone'))"]
)

hard = Task(
    description="Define `power(base,exp)` returning base**exp. Call with 2,10 and print.",
    expected_output="1024",
    level=Level.HARD,
    hints=["def power(base,exp): return base**exp", "print(power(2,10))"]
)

def main(): c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
