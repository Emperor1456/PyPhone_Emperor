import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'res' in g and g['res']=='A'
easy=Task("a=3; if a>0: res='A' else res='B'", verify_easy,Level.EASY, hints=["a=3","if a>0: res='A' else: res='B'"])
def verify_medium(g): return 'msg' in g and g['msg']=='Positive'
medium=Task("x=-5; if x>=0: msg='Positive' else msg='Negative'", verify_medium,Level.MEDIUM, hints=["x=-5","if x>=0: msg='Positive' else: msg='Negative'"])
def verify_hard(g): return 'parity' in g and g['parity']=='Even' and 'sign' in g and g['sign']=='Positive'
hard=Task("n=8; set 'parity' even/odd, 'sign' positive/negative", verify_hard,Level.HARD, hints=["n=8","parity='Even' if n%2==0 else 'Odd'","sign='Positive' if n>=0 else 'Negative'"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
