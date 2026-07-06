import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'factorial' in g and callable(g['factorial']) and 'f' in g and g['f']==24
easy=Task("Define recursive `factorial(n)` returning n! (n>=0). Call with 4 into 'f'.", verify_easy, Level.EASY, hints=["def factorial(n):\n    if n<=1: return 1\n    return n*factorial(n-1)","f=factorial(4)"])
def verify_medium(g): return 'fib' in g and callable(g['fib']) and 'fib5' in g and g['fib5']==5
medium=Task("Define recursive `fib(n)` returning the nth Fibonacci number (0-indexed: fib(0)=0, fib(1)=1). Call with 5 into 'fib5'", verify_medium, Level.MEDIUM, hints=["def fib(n):\n    if n<=1: return n\n    return fib(n-1)+fib(n-2)","fib5=fib(5)"])
def verify_hard(g): return 'countdown' in g and callable(g['countdown']) and 'output' in g and isinstance(g['output'],list) and g['output']==[5,4,3,2,1]
hard=Task("Define recursive `countdown(n)` that returns a list of numbers from n down to 1. Call with 5 into 'output'.", verify_hard, Level.HARD, hints=["def countdown(n):\n    if n<=0: return []\n    return [n]+countdown(n-1)","output=countdown(5)"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
