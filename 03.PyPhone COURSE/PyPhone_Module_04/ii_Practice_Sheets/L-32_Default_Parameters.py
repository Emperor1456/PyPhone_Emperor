import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'greet' in g and callable(g['greet']) and 'm1' in g and g['m1']=='Hello Guest'
easy=Task("Define `greet(name='Guest')` returning 'Hello '+name, call with no args into 'm1'", verify_easy, Level.EASY, hints=["def greet(name='Guest'): return 'Hello '+name","m1=greet()"])
def verify_medium(g): return 'm2' in g and g['m2']=='Hello Emperor'
medium=Task("Using same `greet`, call with 'Emperor' into 'm2'", verify_medium, Level.MEDIUM, hints=["m2=greet('Emperor')"])
def verify_hard(g): return 'power' in g and callable(g['power']) and 'p1' in g and g['p1']==8 and 'p2' in g and g['p2']==9
hard=Task("Define `power(x,exp=2)` returning x**exp, call with 2 into 'p1', and with 3,2 into 'p2'", verify_hard, Level.HARD, hints=["def power(x,exp=2): return x**exp","p1=power(2)","p2=power(3,2)"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
