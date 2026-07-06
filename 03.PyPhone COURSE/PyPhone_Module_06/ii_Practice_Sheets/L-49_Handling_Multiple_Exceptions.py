import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'msg' in g and g['msg'] == 'ValueError'
easy=Task("Try int('abc'), except ValueError -> set msg='ValueError', except TypeError -> 'TypeError'.", verify_easy, Level.EASY, hints=["try:\n    int('abc')\nexcept ValueError:\n    msg='ValueError'"])
def verify_medium(g): return 'msg' in g and g['msg'] == 'TypeError'
medium=Task("Try len(5), catch TypeError, set msg='TypeError'.", verify_medium, Level.MEDIUM, hints=["try:\n    len(5)\nexcept TypeError:\n    msg='TypeError'"])
def verify_hard(g): return 'result' in g and g['result'] == 'ZeroDivisionError'
hard=Task("Try 5/0, catch both ZeroDivisionError and ValueError, but store the exception type name in 'result'.", verify_hard, Level.HARD, hints=["try:\n    5/0\nexcept ZeroDivisionError:\n    result='ZeroDivisionError'\nexcept ValueError:\n    result='ValueError'"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
