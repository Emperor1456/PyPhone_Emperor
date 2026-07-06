import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'd' in g and g['d']=={'name':'Emperor','age':18}
easy=Task("Create a dictionary 'd' with keys 'name':'Emperor' and 'age':18", verify_easy, Level.EASY, hints=["d={'name':'Emperor','age':18}"])
def verify_medium(g): return 'info' in g and g['info']=={'brand':'Samsung','model':'Galaxy'}
medium=Task("Create dict 'info' with 'brand':'Samsung', 'model':'Galaxy' using dict() constructor", verify_medium, Level.MEDIUM, hints=["info=dict(brand='Samsung',model='Galaxy')"])
def verify_hard(g): return 'nested' in g and g['nested']=={'person':{'name':'Emperor','age':18},'city':'Dhaka'}
hard=Task("Create nested dict 'nested' with 'person': {'name':'Emperor','age':18} and 'city':'Dhaka'", verify_hard, Level.HARD, hints=["nested={'person':{'name':'Emperor','age':18},'city':'Dhaka'}"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
