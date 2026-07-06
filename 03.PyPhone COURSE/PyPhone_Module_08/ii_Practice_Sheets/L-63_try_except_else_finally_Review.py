import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'flow' in g and g['flow']=='finally'
easy=Task("Use full try/except/else/finally with deliberate error. Ensure 'flow' ends up 'finally' because finally always runs. Use 1/0.", verify_easy, Level.EASY, hints=["try:\n    1/0\nexcept ZeroDivisionError:\n    flow='except'\nelse:\n    flow='else'\nfinally:\n    flow='finally'"])
def verify_medium(g): return 'path' in g and g['path']=='else'
medium=Task("Use try/else without exception: set 'path'='else'.", verify_medium, Level.MEDIUM, hints=["try:\n    x=1\nexcept:\n    path='except'\nelse:\n    path='else'"])
def verify_hard(g): return 'status' in g and g['status']=='ok'
hard=Task("Implement a safe division function that returns 'error' if division by zero, else the result. Call with 10/2 and store in 'status' only if no error. Use else and finally for cleanup.", verify_hard, Level.HARD, hints=["def safe_div(a,b):\n    try:\n        return a/b\n    except ZeroDivisionError:\n        return 'error'\n    finally:\n        pass","status=safe_div(10,2) if safe_div(10,2)!='error' else 'error'"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
