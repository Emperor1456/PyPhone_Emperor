import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'total' in g and g['total']==10
easy=Task("Use while to sum 1 to 4 into 'total'", verify_easy,Level.EASY, hints=["total=0; i=1","while i<=4: total+=i; i+=1"])
def verify_medium(g): return 'prod' in g and g['prod']==24
medium=Task("Compute factorial of 4 using while", verify_medium,Level.MEDIUM, hints=["n=4; prod=1","while n>0: prod*=n; n-=1"])
def verify_hard(g): return 'count' in g and g['count']==5
hard=Task("Count how many times you can double 1 before exceeding 20", verify_hard,Level.HARD, hints=["x=1; count=0","while x<=20: x*=2; count+=1"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
