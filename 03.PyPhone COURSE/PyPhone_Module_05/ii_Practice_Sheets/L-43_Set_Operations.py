import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'union' in g and g['union']=={1,2,3,4}
easy=Task("Given a={1,2}, b={3,4}, compute union into 'union'", verify_easy, Level.EASY, hints=["a={1,2}","b={3,4}","union=a|b"])
def verify_medium(g): return 'intersection' in g and g['intersection']=={3}
medium=Task("Given a={1,2,3}, b={3,4,5}, compute intersection into 'intersection'", verify_medium, Level.MEDIUM, hints=["a={1,2,3}","b={3,4,5}","intersection=a&b"])
def verify_hard(g): return 'diff' in g and g['diff']=={1,2}
hard=Task("Given a={1,2,3}, b={3,4,5}, compute a-b (difference) into 'diff'", verify_hard, Level.HARD, hints=["a={1,2,3}","b={3,4,5}","diff=a-b"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
