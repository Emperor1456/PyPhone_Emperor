import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'result' in g and g['result']=='caught'
easy=Task("Try to open a non-existent file, catch FileNotFoundError, set result='caught'.", verify_easy, Level.EASY, hints=["try:\n    open('nofile.txt')\nexcept FileNotFoundError:\n    result='caught'"])
def verify_medium(g): return 'safe' in g and g['safe']=='ok'
medium=Task("Try to convert 'abc' to int, catch ValueError, set safe='ok'.", verify_medium, Level.MEDIUM, hints=["try:\n    int('abc')\nexcept ValueError:\n    safe='ok'"])
def verify_hard(g): return 'final' in g and g['final']=='clean'
hard=Task("Combine try/except/else/finally: set 'final' to 'try', if no error change to 'else', but finally always sets 'final'='clean'. Use a safe operation.", verify_hard, Level.HARD, hints=["try:\n    x=1\nexcept:\n    final='except'\nelse:\n    final='else'\nfinally:\n    final='clean'"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
