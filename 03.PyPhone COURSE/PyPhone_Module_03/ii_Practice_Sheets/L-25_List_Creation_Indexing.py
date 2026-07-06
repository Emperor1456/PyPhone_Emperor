import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'lst' in g and g['lst']==[1,2,3]
easy=Task("Create list [1,2,3] in variable 'lst'", verify_easy, Level.EASY, hints=["lst=[1,2,3]"])
def verify_medium(g): return 'third' in g and g['third']==3
medium=Task("lst=[10,20,30,40]; get the third element into 'third'", verify_medium, Level.MEDIUM, hints=["lst=[10,20,30,40]","third=lst[2]"])
def verify_hard(g): return 'last' in g and g['last']==40
hard=Task("lst=[10,20,30,40]; get the last element into 'last' using negative indexing", verify_hard, Level.HARD, hints=["lst=[10,20,30,40]","last=lst[-1]"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
