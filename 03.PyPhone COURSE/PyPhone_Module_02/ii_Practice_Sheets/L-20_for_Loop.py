import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Sum numbers in list [1,2,3,4,5] using a for loop. Print the sum.",
    expected_output="15",
    level=Level.EASY,
    hints=["s=0","for x in [1,2,3,4,5]: s+=x","print(s)"]
)

medium = Task(
    description="Concatenate characters ['h','e','l','l','o'] into a string. Print it.",
    expected_output="hello",
    level=Level.MEDIUM,
    hints=["res=''","for ch in ['h','e','l','l','o']: res+=ch","print(res)"]
)

hard = Task(
    description="Generate list of even numbers from 1 to 10 using for and range. Print list.",
    expected_output="[2, 4, 6, 8, 10]",
    level=Level.HARD,
    hints=["evens=[]","for i in range(1,11):","    if i%2==0: evens.append(i)","print(evens)"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
