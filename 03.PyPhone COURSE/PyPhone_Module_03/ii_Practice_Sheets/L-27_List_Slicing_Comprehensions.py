import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'sub' in g and g['sub']==[2,3,4]
easy=Task("nums=[1,2,3,4,5]; extract sublist [2,3,4] using slicing into 'sub'", verify_easy, Level.EASY, hints=["nums=[1,2,3,4,5]","sub=nums[1:4]"])
def verify_medium(g): return 'squares' in g and g['squares']==[1,4,9,16]
medium=Task("nums=[1,2,3,4]; create list of squares using comprehension into 'squares'", verify_medium, Level.MEDIUM, hints=["nums=[1,2,3,4]","squares=[x*x for x in nums]"])
def verify_hard(g): return 'evens' in g and g['evens']==[2,4,6]
hard=Task("Use list comprehension to filter only even numbers from [1,2,3,4,5,6] into 'evens'", verify_hard, Level.HARD, hints=["evens=[x for x in [1,2,3,4,5,6] if x%2==0]"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
