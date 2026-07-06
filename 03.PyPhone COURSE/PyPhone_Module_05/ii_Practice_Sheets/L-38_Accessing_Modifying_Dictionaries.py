import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'name' in g and g['name']=='Emperor'
easy=Task("Given d={'name':'Emperor','age':18}, extract the value of 'name' into variable 'name'", verify_easy, Level.EASY, hints=["d={'name':'Emperor','age':18}","name=d['name']"])
def verify_medium(g): return 'd' in g and g['d']=={'name':'Emperor','age':18,'city':'Dhaka'}
medium=Task("Given d={'name':'Emperor','age':18}, add key 'city' with value 'Dhaka'", verify_medium, Level.MEDIUM, hints=["d={'name':'Emperor','age':18}","d['city']='Dhaka'"])
def verify_hard(g): return 'updated' in g and g['updated']=={'name':'Emperor','age':19}
hard=Task("Given d={'name':'Emperor','age':18}, increment 'age' by 1 and store the modified dict in 'updated'", verify_hard, Level.HARD, hints=["d={'name':'Emperor','age':18}","d['age']+=1","updated=d"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
