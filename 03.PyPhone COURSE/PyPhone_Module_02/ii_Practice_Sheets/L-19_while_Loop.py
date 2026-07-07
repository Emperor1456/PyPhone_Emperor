import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Sum numbers from 1 to 4 using a while loop. Print the total.",
    expected_output="10",
    level=Level.EASY,
    hints=["total=0; i=1","while i<=4:","    total+=i","    i+=1","print(total)"]
)

medium = Task(
    description="Compute factorial of 4 using while. Print the result.",
    expected_output="24",
    level=Level.MEDIUM,
    hints=["n=4; prod=1","while n>0:","    prod*=n","    n-=1","print(prod)"]
)

hard = Task(
    description="Count how many times you can double 1 before exceeding 20. Print count.",
    expected_output="5",
    level=Level.HARD,
    hints=["x=1; count=0","while x<=20:","    x*=2","    count+=1","print(count)"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
