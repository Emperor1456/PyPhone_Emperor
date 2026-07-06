import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'squares' in g and g['squares']==[1,4,9]
easy=Task("Use list comprehension to create 'squares' of [1,2,3] -> [1,4,9]", verify_easy, Level.EASY, hints=["squares=[x*x for x in [1,2,3]]"])
def verify_medium(g): return 'dict_comp' in g and g['dict_comp']=={1:1,2:4,3:9}
medium=Task("Create dict comprehension {x: x*x for x in [1,2,3]} into 'dict_comp'", verify_medium, Level.MEDIUM, hints=["dict_comp={x:x*x for x in [1,2,3]}"])
def verify_hard(g): return 'even_squares' in g and g['even_squares']==[4,16]
hard=Task("Create list of squares of numbers from 1 to 5 but only if the square is even, store in 'even_squares'", verify_hard, Level.HARD, hints=["even_squares=[x*x for x in range(1,6) if (x*x)%2==0]"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
