import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="age=25, citizen=True. If age>=18 and citizen, print 'Valid Adult'.",
    expected_output="Valid Adult",
    level=Level.EASY,
    hints=["age=25; citizen=True","if age>=18:","    if citizen: print('Valid Adult')"]
)

medium = Task(
    description="price=100, member=True. If member and price>50, print 'Discount Applied'.",
    expected_output="Discount Applied",
    level=Level.MEDIUM,
    hints=["price=100; member=True","if member:","    if price>50: print('Discount Applied')"]
)

hard = Task(
    description="num=2. If num>1: if even, if 2 print 'Prime Even' else 'Even', else 'Odd'.",
    expected_output="Prime Even",
    level=Level.HARD,
    hints=["num=2","if num>1:","    if num%2==0:","        if num==2: print('Prime Even')","        else: print('Even')","    else: print('Odd')"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
