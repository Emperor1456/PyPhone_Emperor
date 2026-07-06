import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'items' in g and g['items']==[1,2,3,4]
easy=Task("items=[1,2,3]; append 4 so items becomes [1,2,3,4]", verify_easy, Level.EASY, hints=["items=[1,2,3]","items.append(4)"])
def verify_medium(g): return 'sorted_lst' in g and g['sorted_lst']==[1,3,5]
medium=Task("lst=[3,1,5]; sort and store in 'sorted_lst'", verify_medium, Level.MEDIUM, hints=["lst=[3,1,5]","sorted_lst=sorted(lst)"])
def verify_hard(g): return 'popped' in g and g['popped']==3 and 'remaining' in g and g['remaining']==[1,2]
hard=Task("lst=[1,2,3]; pop the last element into 'popped', and let 'remaining' be the list after pop", verify_hard, Level.HARD, hints=["lst=[1,2,3]","popped=lst.pop()","remaining=lst"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
