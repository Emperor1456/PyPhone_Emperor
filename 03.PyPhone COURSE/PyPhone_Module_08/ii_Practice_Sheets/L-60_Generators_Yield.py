import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'gen' in g and callable(g['gen']) and hasattr(g['gen'](), '__next__')
easy=Task("Define a generator function `gen` that yields 1, then 2, then 3. Create a generator object (don't need to store).", verify_easy, Level.EASY, hints=["def gen():\n    yield 1\n    yield 2\n    yield 3"])
def verify_medium(g): return 'result' in g and g['result']==[1,2,3]
medium=Task("Use the generator to collect all yielded values into list 'result'.", verify_medium, Level.MEDIUM, hints=["result=list(gen())"])
def verify_hard(g): return 'fib_gen' in g and callable(g['fib_gen']) and list(g['fib_gen'](5))==[0,1,1,2,3]
hard=Task("Write a generator `fib_gen(n)` that yields first n Fibonacci numbers (starting 0,1). Call with 5 and store list in 'fib_list' (we'll check).", verify_hard, Level.HARD, hints=["def fib_gen(n):\n    a,b=0,1\n    for _ in range(n):\n        yield a\n        a,b=b,a+b","fib_list=list(fib_gen(5))"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
