import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return os.path.exists('output.txt')
easy=Task("Write 'Emperor' to a file named 'output.txt'.", verify_easy, Level.EASY, hints=["with open('output.txt','w') as f: f.write('Emperor')"])
def verify_medium(g): return open('output.txt').read() == 'PyPhone'
medium=Task("Overwrite 'output.txt' with the text 'PyPhone'.", verify_medium, Level.MEDIUM, hints=["with open('output.txt','w') as f: f.write('PyPhone')"])
def verify_hard(g): return open('numbers.txt').read().strip() == '1,2,3'
hard=Task("Write a list [1,2,3] to 'numbers.txt' as comma-separated values.", verify_hard, Level.HARD, hints=["nums=[1,2,3]","with open('numbers.txt','w') as f: f.write(','.join(map(str,nums)))"])
def main():
    import os
    for f in ['output.txt','numbers.txt']:
        if os.path.exists(f): os.remove(f)
    c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
