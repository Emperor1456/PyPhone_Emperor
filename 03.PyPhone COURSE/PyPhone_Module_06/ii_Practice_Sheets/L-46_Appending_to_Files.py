import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g):
    with open('log.txt','r') as f: return 'line1\nline2' in f.read()
easy=Task("Create 'log.txt' with 'line1', then append 'line2' on a new line.", verify_easy, Level.EASY, hints=["with open('log.txt','w') as f: f.write('line1')","with open('log.txt','a') as f: f.write('\\nline2')"])
def verify_medium(g): return open('log.txt').read().count('line') == 3
medium=Task("Append another line 'line3' to 'log.txt'.", verify_medium, Level.MEDIUM, hints=["with open('log.txt','a') as f: f.write('\\nline3')"])
def verify_hard(g): return len(open('log.txt').readlines()) == 4
hard=Task("Append 'line4' using 'a' mode to make total 4 lines.", verify_hard, Level.HARD, hints=["with open('log.txt','a') as f: f.write('\\nline4')"])
def main():
    import os
    if os.path.exists('log.txt'): os.remove('log.txt')
    c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
