import sys, json; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'data' in g and g['data'] == {'key':'value'}
easy=Task("Parse the JSON string '{\"key\":\"value\"}' into a Python dict stored in 'data'.", verify_easy, Level.EASY, hints=["import json","data=json.loads('{\"key\":\"value\"}')"])
def verify_medium(g): return 'json_str' in g and g['json_str'] == '{"name": "Emperor"}'
medium=Task("Convert the dict {'name':'Emperor'} to a JSON string stored in 'json_str'.", verify_medium, Level.MEDIUM, hints=["import json","json_str=json.dumps({'name':'Emperor'})"])
def verify_hard(g): return os.path.exists('data.json') and json.load(open('data.json')) == {'age':18}
hard=Task("Write dict {'age':18} to a file 'data.json' using json.dump.", verify_hard, Level.HARD, hints=["import json","with open('data.json','w') as f: json.dump({'age':18}, f)"])
def main():
    import os
    if os.path.exists('data.json'): os.remove('data.json')
    c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
