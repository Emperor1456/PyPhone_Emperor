import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 's' in g and g['s']==15
easy=Task("Sum numbers in [1,2,3,4,5] using for loop into 's'", verify_easy,Level.EASY, hints=["s=0","for x in [1,2,3,4,5]: s+=x"])
def verify_medium(g): return 'res' in g and g['res']=='hello'
medium=Task("Concatenate characters ['h','e','l','l','o'] into 'res'", verify_medium,Level.MEDIUM, hints=["res=''","for ch in ['h','e','l','l','o']: res+=ch"])
def verify_hard(g): return 'evens' in g and g['evens']==[2,4,6,8,10]
hard=Task("Generate list of even numbers 2-10 using for and range", verify_hard,Level.HARD, hints=["evens=[]","for i in range(1,11): if i%2==0: evens.append(i)"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
