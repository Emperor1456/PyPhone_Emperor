import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'x' in g and g['x']==10 and 'msg' in g and g['msg']=='OK'
easy=Task("x=10; if x>5: msg='OK' else msg='NO'", verify_easy,Level.EASY, hints=["x=10","if x>5: msg='OK' else: msg='NO'"])
def verify_medium(g): return 'result' in g and g['result']=='Even'
medium=Task("num=4; if num%2==0: result='Even' else result='Odd'", verify_medium,Level.MEDIUM, hints=["num=4","if num%2==0: result='Even' else: result='Odd'"])
def verify_hard(g): return 'grade' in g and g['grade']=='B'
hard=Task("score=75; if >=90 'A', >=80 'B', >=70 'C', else 'F'", verify_hard,Level.HARD, hints=["score=75","if score>=90: grade='A'\nelif score>=80: grade='B'\nelif score>=70: grade='C'\nelse: grade='F'"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
