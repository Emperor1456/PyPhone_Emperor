import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'total' in g and g['total']==15
easy=Task("Sum all numbers in [1,2,3,4,5] into 'total' using a loop", verify_easy, Level.EASY, hints=["total=0","for x in [1,2,3,4,5]: total+=x"])
def verify_medium(g): return 'result' in g and g['result']=='apple banana'
medium=Task("Join words ['apple','banana'] with space into 'result' using a loop", verify_medium, Level.MEDIUM, hints=["words=['apple','banana']","result=''","for w in words: result+=w+' '","result=result.strip()"])
def verify_hard(g): return 'uppercase' in g and g['uppercase']==['A','B','C']
hard=Task("Convert ['a','b','c'] to uppercase using a loop or list comprehension into 'uppercase'", verify_hard, Level.HARD, hints=["uppercase=[ch.upper() for ch in ['a','b','c']]"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
