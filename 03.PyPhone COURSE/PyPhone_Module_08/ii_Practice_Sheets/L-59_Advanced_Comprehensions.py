import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Use list comprehension to create squares of [1,2,3] -> [1,4,9]. Print the list.",
    expected_output="[1, 4, 9]",
    level=Level.EASY,
    hints=["squares=[x*x for x in [1,2,3]]","print(squares)"]
)

medium = Task(
    description="Create dict comprehension {x: x*x for x in [1,2,3]}. Print the dict.",
    expected_output="{1: 1, 2: 4, 3: 9}",
    level=Level.MEDIUM,
    hints=["d={x:x*x for x in [1,2,3]}","print(d)"]
)

hard = Task(
    description="From range(1,6), create list of squares only if the square is even. Print the list.",
    expected_output="[4, 16]",
    level=Level.HARD,
    hints=["even_squares=[x*x for x in range(1,6) if (x*x)%2==0]","print(even_squares)"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
