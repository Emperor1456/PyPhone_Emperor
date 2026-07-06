import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'grade' in g and g['grade']=='C'
easy=Task("score=65; use if-elif-else to assign grade A(>=80),B(>=70),C(>=60),D else", verify_easy,Level.EASY, hints=["score=65","if score>=80: grade='A'\nelif score>=70: grade='B'\nelif score>=60: grade='C'\nelse: grade='D'"])
def verify_medium(g): return 'result' in g and g['result']=='B'
medium=Task("points=75; A>=90, B>=75, C>=60, else F", verify_medium,Level.MEDIUM, hints=["points=75","if points>=90: result='A'\nelif points>=75: result='B'\nelif points>=60: result='C'\nelse: result='F'"])
def verify_hard(g): return 'level' in g and g['level']=='Medium'
hard=Task("temp=55; >100 'Hot', >70 'Warm', >40 'Medium', else 'Cold'", verify_hard,Level.HARD, hints=["temp=55","if temp>100: level='Hot'\nelif temp>70: level='Warm'\nelif temp>40: level='Medium'\nelse: level='Cold'"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
