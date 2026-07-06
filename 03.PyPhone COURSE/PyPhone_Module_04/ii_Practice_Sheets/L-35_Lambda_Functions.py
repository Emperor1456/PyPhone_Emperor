import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'double' in g and callable(g['double']) and 'res' in g and g['res']==10
easy=Task("Create a lambda that doubles a number, assign to 'double', then call with 5 into 'res'", verify_easy, Level.EASY, hints=["double=lambda x: x*2","res=double(5)"])
def verify_medium(g): return 'add' in g and callable(g['add']) and 'sum' in g and g['sum']==8
medium=Task("Create lambda `add` that adds two numbers, call with 3,5 into 'sum'", verify_medium, Level.MEDIUM, hints=["add=lambda a,b: a+b","sum=add(3,5)"])
def verify_hard(g): return 'sorted_words' in g and g['sorted_words']==['apple','banana','cherry']
hard=Task("Sort the list ['banana','cherry','apple'] by the second character using a lambda as key, store in 'sorted_words'", verify_hard, Level.HARD, hints=["words=['banana','cherry','apple']","sorted_words=sorted(words, key=lambda w: w[1])"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
