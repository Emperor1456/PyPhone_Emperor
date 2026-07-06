import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'res' in g and g['res']=='Valid Adult'
easy=Task("age=25; citizen=True; nested if to get 'Valid Adult'", verify_easy,Level.EASY, hints=["age=25; citizen=True","if age>=18:\n    if citizen:\n        res='Valid Adult'\n    else:\n        res='Non-citizen'\nelse:\n    res='Minor'"])
def verify_medium(g): return 'msg' in g and g['msg']=='Discount Applied'
medium=Task("price=100, member=True; nested to 'Discount Applied'", verify_medium,Level.MEDIUM, hints=["price=100; member=True","if member:\n    if price>50: msg='Discount Applied'\n    else: msg='No discount'\nelse: msg='Not a member'"])
def verify_hard(g): return 'result' in g and g['result']=='Prime Even'
hard=Task("num=2; nested to identify even, and if 2 then 'Prime Even'", verify_hard,Level.HARD, hints=["num=2","if num>1:\n    if num%2==0:\n        if num==2: result='Prime Even'\n        else: result='Even'\n    else: result='Odd'\nelse: result='Not >1'"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
