import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Sum all numbers in [1,2,3,4,5] using a for loop. Print the sum.",
    expected_output="15",
    level=Level.EASY,
    hints=["total=0","for x in [1,2,3,4,5]: total+=x","print(total)"]
)

medium = Task(
    description="Join the words ['apple','banana'] with a space using a loop. Print the result.",
    expected_output="apple banana",
    level=Level.MEDIUM,
    hints=["words=['apple','banana']","result=''","for w in words: result+=w+' '","print(result.strip())"]
)

hard = Task(
    description="Convert ['a','b','c'] to uppercase using a loop/comprehension. Print the list.",
    expected_output="['A', 'B', 'C']",
    level=Level.HARD,
    hints=["upper=[ch.upper() for ch in ['a','b','c']]","print(upper)"]
)

def main(): c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
