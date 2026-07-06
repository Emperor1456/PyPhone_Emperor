import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'first' in g and g['first']=='P'
easy=Task("s='PyPhone'; get first character into 'first'", verify_easy, Level.EASY, hints=["s='PyPhone'","first=s[0]"])
def verify_medium(g): return 'sub' in g and g['sub']=='yPh'
medium=Task("s='PyPhone'; extract substring from index 1 to 3 into 'sub'", verify_medium, Level.MEDIUM, hints=["s='PyPhone'","sub=s[1:4]"])
def verify_hard(g): return 'rev' in g and g['rev']=='enohPyP'
hard=Task("s='PyPhone'; store reversed string in 'rev' using slicing", verify_hard, Level.HARD, hints=["s='PyPhone'","rev=s[::-1]"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
