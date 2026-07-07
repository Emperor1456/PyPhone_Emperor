import sys, os; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Write 'Emperor' to a file named 'output.txt'.",
    expected_output="Emperor",
    level=Level.EASY,
    hints=["with open('output.txt','w') as f: f.write('Emperor')", "print(open('output.txt').read())"]
)

medium = Task(
    description="Overwrite 'output.txt' with 'PyPhone'.",
    expected_output="PyPhone",
    level=Level.MEDIUM,
    hints=["with open('output.txt','w') as f: f.write('PyPhone')", "print(open('output.txt').read())"]
)

hard = Task(
    description="Write list [1,2,3] to 'numbers.txt' as comma-separated values, then print the file content.",
    expected_output="1,2,3",
    level=Level.HARD,
    hints=["nums=[1,2,3]", "with open('numbers.txt','w') as f: f.write(','.join(map(str,nums)))", "print(open('numbers.txt').read())"]
)

def main():
    for f in ['output.txt','numbers.txt']:
        if os.path.exists(f): os.remove(f)
    c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
