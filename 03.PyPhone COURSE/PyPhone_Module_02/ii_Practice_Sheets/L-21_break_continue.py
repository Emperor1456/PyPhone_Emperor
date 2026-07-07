import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Search for 3 in [1,2,3,4]. Break when found. Print 'Found'.",
    expected_output="Found",
    level=Level.EASY,
    hints=["for x in [1,2,3,4]:","    if x==3: print('Found'); break"]
)

medium = Task(
    description="Print odd numbers from 1 to 6, skip evens with continue.",
    expected_output="1\n3\n5",
    level=Level.MEDIUM,
    hints=["for i in range(1,7):","    if i%2==0: continue","    print(i)"]
)

hard = Task(
    description="Sum numbers 1 to 10, stop when sum exceeds 30. Print sum.",
    expected_output="36",
    level=Level.HARD,
    hints=["res=0; i=1","while i<=10:","    res+=i","    if res>30: break","    i+=1","print(res)"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
