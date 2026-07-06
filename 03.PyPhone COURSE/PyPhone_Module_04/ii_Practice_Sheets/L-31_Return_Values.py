import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'double' in g and callable(g['double']) and 'val' in g and g['val']==10
easy=Task("Define `double(x)` returning 2*x, call with 5 into 'val'", verify_easy, Level.EASY, hints=["def double(x): return 2*x","val=double(5)"])
def verify_medium(g): return 'absolute' in g and callable(g['absolute']) and 'r' in g and g['r']==7
medium=Task("Define `absolute(x)` that returns x if x>=0 else -x, call with -7 into 'r'", verify_medium, Level.MEDIUM, hints=["def absolute(x):\n    if x>=0: return x\n    else: return -x","r=absolute(-7)"])
def verify_hard(g): return 'is_even' in g and callable(g['is_even']) and 'check' in g and g['check']==True
hard=Task("Define `is_even(n)` returning True if n%2==0 else False, call with 8 into 'check'", verify_hard, Level.HARD, hints=["def is_even(n): return n%2==0","check=is_even(8)"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
