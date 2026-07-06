import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'up' in g and g['up']=='EMPEROR'
easy=Task("s='emperor'; convert to uppercase into 'up'", verify_easy, Level.EASY, hints=["s='emperor'","up=s.upper()"])
def verify_medium(g): return 'stripped' in g and g['stripped']=='data'
medium=Task("t='  data  '; strip whitespace into 'stripped'", verify_medium, Level.MEDIUM, hints=["t='  data  '","stripped=t.strip()"])
def verify_hard(g): return 'replaced' in g and g['replaced']=='Hello Emperor'
hard=Task("msg='Hello World'; replace 'World' with 'Emperor' into 'replaced'", verify_hard, Level.HARD, hints=["msg='Hello World'","replaced=msg.replace('World','Emperor')"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
