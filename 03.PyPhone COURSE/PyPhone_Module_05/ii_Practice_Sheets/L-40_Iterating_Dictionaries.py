import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="d={'name':'Emperor','age':18}. Print all key-value pairs as tuples using items().",
    expected_output="[('name', 'Emperor'), ('age', 18)]",
    level=Level.EASY,
    hints=["d={'name':'Emperor','age':18}", "print(list(d.items()))"]
)

medium = Task(
    description="Same d. Build a string 'name:Emperor, age:18' and print it.",
    expected_output="name:Emperor, age:18",
    level=Level.MEDIUM,
    hints=["result=', '.join(f'{k}:{v}' for k,v in d.items())", "print(result)"]
)

hard = Task(
    description="d={'a':1,'b':2,'c':3}. Count how many values are even, print count.",
    expected_output="1",
    level=Level.HARD,
    hints=["d={'a':1,'b':2,'c':3}", "count=sum(1 for v in d.values() if v%2==0)", "print(count)"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
