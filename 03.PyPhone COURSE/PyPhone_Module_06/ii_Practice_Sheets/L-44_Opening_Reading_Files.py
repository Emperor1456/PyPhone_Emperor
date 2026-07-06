import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'content' in g and isinstance(g['content'], str)
easy=Task("Open and read the file 'test.txt' (we'll create it). Write Python code to read its content into variable 'content'. Assume the file contains 'Hello'. We'll create it before.", verify_easy, Level.EASY, hints=["with open('test.txt','r') as f: content=f.read()"])
def verify_medium(g): return 'lines' in g and isinstance(g['lines'], list) and len(g['lines']) > 0
medium=Task("Read all lines from 'test.txt' into list 'lines'.", verify_medium, Level.MEDIUM, hints=["with open('test.txt') as f: lines=f.readlines()"])
def verify_hard(g): return 'first_line' in g and g['first_line'] == 'Hello'
hard=Task("Read the first line of 'test.txt' into 'first_line'.", verify_hard, Level.HARD, hints=["with open('test.txt') as f: first_line=f.readline().strip()"])
def main():
    # Create test file
    with open('test.txt','w') as f: f.write('Hello\nWorld')
    c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
