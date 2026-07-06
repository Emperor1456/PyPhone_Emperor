import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'cleanup' in g and g['cleanup'] == True
easy=Task("Use try/finally to set 'cleanup'=True after any operation (even if exception). Use a safe operation.", verify_easy, Level.EASY, hints=["try:\n    x=1\nexcept:\n    pass\nfinally:\n    cleanup=True"])
def verify_medium(g): return 'else_run' in g and g['else_run'] == True
medium=Task("Use try/except/else: set 'else_run'=True inside else block when no exception occurs.", verify_medium, Level.MEDIUM, hints=["try:\n    y=2\nexcept:\n    pass\nelse:\n    else_run=True"])
def verify_hard(g): return 'flow' in g and g['flow'] == 'finally'
hard=Task("Combine try/except/else/finally. If exception occurs, set 'flow'='except', else 'flow'='else', but 'finally' always runs and should overwrite 'flow' to 'finally'. Simulate with a deliberate error to test.", verify_hard, Level.HARD, hints=["try:\n    1/0\nexcept:\n    flow='except'\nelse:\n    flow='else'\nfinally:\n    flow='finally'"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
