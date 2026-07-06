import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 't' in g and g['t']==(1,2,3)
easy=Task("Create a tuple 't' with values 1,2,3", verify_easy, Level.EASY, hints=["t=(1,2,3)"])
def verify_medium(g): return 'first' in g and g['first']==1 and 'last' in g and g['last']==3
medium=Task("Given t=(1,2,3), extract the first element into 'first' and last into 'last'", verify_medium, Level.MEDIUM, hints=["t=(1,2,3)","first=t[0]","last=t[-1]"])
def verify_hard(g): return 'concatenated' in g and g['concatenated']==(1,2,3,4,5)
hard=Task("Given t1=(1,2,3), t2=(4,5), concatenate them into 'concatenated'", verify_hard, Level.HARD, hints=["t1=(1,2,3)","t2=(4,5)","concatenated=t1+t2"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
