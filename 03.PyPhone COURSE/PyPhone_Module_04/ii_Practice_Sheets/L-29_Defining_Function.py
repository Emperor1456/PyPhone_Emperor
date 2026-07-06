import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'hello' in g and callable(g['hello'])
easy=Task("Define a function `hello` that prints 'Hello, Emperor'", verify_easy, Level.EASY, hints=["def hello(): print('Hello, Emperor')"])
def verify_medium(g): return 'greet' in g and callable(g['greet']) and 'output' in g and g['output']=='Hi'
medium=Task("Define `greet(name)` that returns 'Hi '+name, call it with 'Emperor' and store in 'output'", verify_medium, Level.MEDIUM, hints=["def greet(name): return 'Hi '+name","output=greet('Emperor')"])
def verify_hard(g): return 'square' in g and callable(g['square']) and 'result' in g and g['result']==25
hard=Task("Define `square(x)` returning x*x, call with 5 and store in 'result'", verify_hard, Level.HARD, hints=["def square(x): return x*x","result=square(5)"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
