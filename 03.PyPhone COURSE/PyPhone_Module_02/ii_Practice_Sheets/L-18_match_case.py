import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'res' in g and g['res']=='one'
easy=Task("x=1; match-case map 1->'one',2->'two',_ ->'other'", verify_easy,Level.EASY, hints=["x=1","match x:\n    case 1: res='one'\n    case 2: res='two'\n    case _: res='other'"])
def verify_medium(g): return 'msg' in g and g['msg']=='Red'
medium=Task("color='r'; match 'r'->'Red','g'->'Green','b'->'Blue'", verify_medium,Level.MEDIUM, hints=["color='r'","match color:\n    case 'r': msg='Red'\n    case 'g': msg='Green'\n    case 'b': msg='Blue'"])
def verify_hard(g): return 'status' in g and g['status']=='Success'
hard=Task("code=200; match 200->'Success', 404->'Not Found', _ ->'Unknown'", verify_hard,Level.HARD, hints=["code=200","match code:\n    case 200: status='Success'\n    case 404: status='Not Found'\n    case _: status='Unknown'"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
