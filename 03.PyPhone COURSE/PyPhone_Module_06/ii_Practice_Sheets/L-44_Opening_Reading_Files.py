import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Open 'test.txt' in read mode, read its content into a variable, and print it. (We'll create 'test.txt' with 'Hello' beforehand.)",
    expected_output="Hello",
    level=Level.EASY,
    hints=["with open('test.txt','r') as f: content=f.read()", "print(content)"]
)

medium = Task(
    description="Read all lines from 'test.txt' into a list and print the list.",
    expected_output="['Hello', 'World']",
    level=Level.MEDIUM,
    hints=["with open('test.txt','r') as f: lines=f.readlines()", "print(lines)"]
)

hard = Task(
    description="Read the first line of 'test.txt' and print it stripped.",
    expected_output="Hello",
    level=Level.HARD,
    hints=["with open('test.txt','r') as f: first=f.readline().strip()", "print(first)"]
)

def main():
    with open('test.txt','w') as f: f.write('Hello\nWorld')
    c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
