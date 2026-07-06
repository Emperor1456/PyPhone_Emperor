import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'x' in g and g['x']==10
easy=Task("Use pass inside an empty if, then set x=10", verify_easy,Level.EASY, hints=["x=5","if x>0: pass","x=10"])
def verify_medium(g): return 'result' in g and g['result']=='done'
medium=Task("Define a function stub with pass, call it, then set result='done'", verify_medium,Level.MEDIUM, hints=["def stub(): pass","stub()","result='done'"])
def verify_hard(g): return 'res' in g and g['res']==42
hard=Task("Use pass in a loop to skip an iteration indirectly, then set res=42 after", verify_hard,Level.HARD, hints=["for i in range(3): if i==1: pass","res=42"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
