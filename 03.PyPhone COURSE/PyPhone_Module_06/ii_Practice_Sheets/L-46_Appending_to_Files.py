import sys, os; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Create 'log.txt' with 'line1', then append 'line2' on a new line. Print the final file content.",
    expected_output="line1\nline2",
    level=Level.EASY,
    hints=["with open('log.txt','w') as f: f.write('line1')", "with open('log.txt','a') as f: f.write('\\nline2')", "print(open('log.txt').read())"]
)

medium = Task(
    description="Append 'line3' to 'log.txt'. Print the file content (should show 3 lines).",
    expected_output="line1\nline2\nline3",
    level=Level.MEDIUM,
    hints=["with open('log.txt','a') as f: f.write('\\nline3')", "print(open('log.txt').read())"]
)

hard = Task(
    description="Append 'line4' to 'log.txt'. Print the file content (4 lines).",
    expected_output="line1\nline2\nline3\nline4",
    level=Level.HARD,
    hints=["with open('log.txt','a') as f: f.write('\\nline4')", "print(open('log.txt').read())"]
)

def main():
    if os.path.exists('log.txt'): os.remove('log.txt')
    with open('log.txt','w') as f: f.write('line1')
    c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
