import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="x=10. Define a function that uses `global x` to change x to 20. Call it, then print x.",
    expected_output="20",
    level=Level.EASY,
    hints=["x=10","def change():\n    global x\n    x=20","change()","print(x)"]
)

medium = Task(
    description="counter=5. Define `increment()` that increments global counter by 1. Call it, then print counter.",
    expected_output="6",
    level=Level.MEDIUM,
    hints=["counter=5","def increment():\n    global counter\n    counter+=1","increment()","print(counter)"]
)

hard = Task(
    description="Define `outer()` with local x=10, inner function that uses `nonlocal x` to set x=20, calls inner, and returns x. Print the returned value.",
    expected_output="20",
    level=Level.HARD,
    hints=["def outer():\n    x=10\n    def inner():\n        nonlocal x\n        x=20\n    inner()\n    return x","print(outer())"]
)

def main(): c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
