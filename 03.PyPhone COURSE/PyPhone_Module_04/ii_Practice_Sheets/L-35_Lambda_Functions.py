import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Create a lambda that doubles a number, assign to `double`, call with 5 and print.",
    expected_output="10",
    level=Level.EASY,
    hints=["double=lambda x: x*2","print(double(5))"]
)

medium = Task(
    description="Create lambda `add` that adds two numbers, call with 3,5 and print.",
    expected_output="8",
    level=Level.MEDIUM,
    hints=["add=lambda a,b: a+b","print(add(3,5))"]
)

hard = Task(
    description="Sort ['banana','cherry','apple'] by the second character using a lambda as key. Print the sorted list.",
    expected_output="['banana', 'cherry', 'apple']",
    level=Level.HARD,
    hints=["words=['banana','cherry','apple']","sorted_words=sorted(words, key=lambda w: w[1])","print(sorted_words)"]
)

def main(): c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
