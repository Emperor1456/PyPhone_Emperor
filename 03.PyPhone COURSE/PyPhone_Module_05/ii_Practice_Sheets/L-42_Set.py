import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 's' in g and g['s']=={1,2,3}
easy=Task("Create a set 's' containing 1,2,3", verify_easy, Level.EASY, hints=["s={1,2,3}"])
def verify_medium(g): return 's' in g and 4 in g['s']
medium=Task("Start with s={1,2,3}; add 4 to the set", verify_medium, Level.MEDIUM, hints=["s={1,2,3}","s.add(4)"])
def verify_hard(g): return 'unique' in g and set(g['unique'])=={1,2,3}
hard=Task("Given list [1,2,2,3,3,3], convert to set and back to list (order doesn't matter) into 'unique'", verify_hard, Level.HARD, hints=["lst=[1,2,2,3,3,3]","unique=list(set(lst))"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
