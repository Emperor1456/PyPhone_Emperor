import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'keys' in g and g['keys']==['name','age']
easy=Task("d={'name':'Emperor','age':18}; get list of keys into 'keys'", verify_easy, Level.EASY, hints=["d={'name':'Emperor','age':18}","keys=list(d.keys())"])
def verify_medium(g): return 'vals' in g and g['vals']==['Emperor',18]
medium=Task("d={'name':'Emperor','age':18}; get list of values into 'vals'", verify_medium, Level.MEDIUM, hints=["d={'name':'Emperor','age':18}","vals=list(d.values())"])
def verify_hard(g): return 'popped' in g and g['popped']==18 and 'd' in g and g['d']=={'name':'Emperor'}
hard=Task("d={'name':'Emperor','age':18}; pop the 'age' key and store its value in 'popped', d should remain with only 'name'", verify_hard, Level.HARD, hints=["d={'name':'Emperor','age':18}","popped=d.pop('age')"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
