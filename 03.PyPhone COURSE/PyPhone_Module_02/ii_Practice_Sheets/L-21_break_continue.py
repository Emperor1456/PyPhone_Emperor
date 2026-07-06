import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'found' in g and g['found']==True
easy=Task("Search for 3 in [1,2,3,4]; break when found, set found=True", verify_easy,Level.EASY, hints=["found=False","for x in [1,2,3,4]: if x==3: found=True; break"])
def verify_medium(g): return 'odds' in g and g['odds']==[1,3,5]
medium=Task("Print odd numbers 1-6, skip evens with continue, store in 'odds'", verify_medium,Level.MEDIUM, hints=["odds=[]","for i in range(1,7): if i%2==0: continue; odds.append(i)"])
def verify_hard(g): return 'res' in g and g['res']==30
hard=Task("Sum numbers 1-10, but stop when sum exceeds 30", verify_hard,Level.HARD, hints=["res=0; i=1","while i<=10: res+=i; if res>30: break; i+=1"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
