import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'items_list' in g and g['items_list']==[('name','Emperor'),('age',18)]
easy=Task("d={'name':'Emperor','age':18}; collect key-value pairs into list 'items_list' using items()", verify_easy, Level.EASY, hints=["d={'name':'Emperor','age':18}","items_list=list(d.items())"])
def verify_medium(g): return 'result' in g and g['result']=='name:Emperor, age:18'
medium=Task("d={'name':'Emperor','age':18}; build a string 'name:Emperor, age:18' into 'result' using a loop", verify_medium, Level.MEDIUM, hints=["d={'name':'Emperor','age':18}","result=', '.join(f'{k}:{v}' for k,v in d.items())"])
def verify_hard(g): return 'count' in g and g['count']==2
hard=Task("d={'a':1,'b':2,'c':3}; count how many values are even and store in 'count'", verify_hard, Level.HARD, hints=["d={'a':1,'b':2,'c':3}","count=sum(1 for v in d.values() if v%2==0)"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
