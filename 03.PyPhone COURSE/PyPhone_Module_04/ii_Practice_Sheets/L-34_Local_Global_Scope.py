import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'x' in g and g['x']==10 and 'result' in g and g['result']==20
easy=Task("x=10; define a function that modifies a global variable x (using `global x`) to 20, then call it and store x in 'result' after call", verify_easy, Level.EASY, hints=["x=10","def change():\n    global x\n    x=20","change()","result=x"])
def verify_medium(g): return 'counter' in g and g['counter']==5 and 'increment' in g and callable(g['increment']) and 'val' in g and g['val']==6
medium=Task("Define a function `increment()` that increments a global `counter` by 1. Set counter=5, call increment, then store counter into 'val'.", verify_medium, Level.MEDIUM, hints=["counter=5","def increment():\n    global counter\n    counter+=1","increment()","val=counter"])
def verify_hard(g): return 'outer' in g and g['outer']==10 and 'inner_val' in g and g['inner_val']==20
hard=Task("Define a function `outer()` that has a local variable x=10, and inside it define `inner()` that modifies x using `nonlocal` to 20. Call outer() and after execution, we can't test directly. Instead, write the code so that outer returns the inner function and we call it, capturing x? Better: have outer return the value of x after calling inner. So define outer that sets x=10, defines inner that does nonlocal x; x=20, calls inner, and returns x. Then call outer() and store in 'outer_res'. That's more testable. We'll do that.", verify_hard, Level.HARD, hints=["def outer():\n    x=10\n    def inner():\n        nonlocal x\n        x=20\n    inner()\n    return x","outer_res=outer()"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
