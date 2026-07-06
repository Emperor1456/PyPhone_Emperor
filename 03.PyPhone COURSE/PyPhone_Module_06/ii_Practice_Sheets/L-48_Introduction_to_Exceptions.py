import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'result' in g and g['result'] == 'error'
easy=Task("Try to convert 'abc' to int, catch ValueError and set 'result' to 'error'.", verify_easy, Level.EASY, hints=["try:\n    int('abc')\nexcept ValueError:\n    result='error'"])
def verify_medium(g): return 'safe' in g and g['safe'] == 'ok'
medium=Task("Divide 10 by 0, catch ZeroDivisionError, set 'safe' to 'ok'.", verify_medium, Level.MEDIUM, hints=["try:\n    10/0\nexcept ZeroDivisionError:\n    safe='ok'"])
def verify_hard(g): return 'final' in g and g['final'] == 'done'
hard=Task("Open a non-existent file, catch FileNotFoundError, then set 'final'='done'.", verify_hard, Level.HARD, hints=["try:\n    open('missing.txt')\nexcept FileNotFoundError:\n    final='done'"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
