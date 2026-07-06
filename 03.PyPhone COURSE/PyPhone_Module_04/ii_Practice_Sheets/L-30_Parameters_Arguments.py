import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'add' in g and callable(g['add']) and 'sum' in g and g['sum']==8
easy=Task("Define `add(a,b)` returning a+b, call with 3,5 and store in 'sum'", verify_easy, Level.EASY, hints=["def add(a,b): return a+b","sum=add(3,5)"])
def verify_medium(g): return 'full_name' in g and callable(g['full_name']) and 'name' in g and g['name']=='Emperor PyPhone'
medium=Task("Define `full_name(first,last)` returning first+' '+last, call with 'Emperor','PyPhone' into 'name'", verify_medium, Level.MEDIUM, hints=["def full_name(first,last): return first+' '+last","name=full_name('Emperor','PyPhone')"])
def verify_hard(g): return 'power' in g and callable(g['power']) and 'res' in g and g['res']==1024
hard=Task("Define `power(base,exp)` returning base**exp, call with 2,10 into 'res'", verify_hard, Level.HARD, hints=["def power(base,exp): return base**exp","res=power(2,10)"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
