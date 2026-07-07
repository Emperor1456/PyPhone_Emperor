import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Define generator `gen()` that yields 1, then 2, then 3. Print list(gen()).",
    expected_output="[1, 2, 3]",
    level=Level.EASY,
    hints=["def gen():\n    yield 1\n    yield 2\n    yield 3","print(list(gen()))"]
)

medium = Task(
    description="Use the generator to print values one by one using a for loop.",
    expected_output="1\n2\n3",
    level=Level.MEDIUM,
    hints=["for val in gen(): print(val)"]
)

hard = Task(
    description="Define generator `fib_gen(n)` yielding first n Fibonacci numbers (0,1,1,2,3,...). Call with n=5 and print as list.",
    expected_output="[0, 1, 1, 2, 3]",
    level=Level.HARD,
    hints=["def fib_gen(n):\n    a,b=0,1\n    for _ in range(n):\n        yield a\n        a,b=b,a+b","print(list(fib_gen(5)))"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
