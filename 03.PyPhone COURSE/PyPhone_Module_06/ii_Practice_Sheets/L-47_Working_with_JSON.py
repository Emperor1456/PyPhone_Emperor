import sys, json, os; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Parse the JSON string '{\"key\":\"value\"}' into a dict and print it.",
    expected_output="{'key': 'value'}",
    level=Level.EASY,
    hints=["import json", "data=json.loads('{\"key\":\"value\"}')", "print(data)"]
)

medium = Task(
    description="Convert the dict {'name':'Emperor'} to a JSON string and print it.",
    expected_output='{"name": "Emperor"}',
    level=Level.MEDIUM,
    hints=["import json", "json_str=json.dumps({'name':'Emperor'})", "print(json_str)"]
)

hard = Task(
    description="Write dict {'age':18} to a file 'data.json', then read it back and print the dict.",
    expected_output="{'age': 18}",
    level=Level.HARD,
    hints=["import json", "with open('data.json','w') as f: json.dump({'age':18},f)", "with open('data.json','r') as f: data=json.load(f)", "print(data)"]
)

def main():
    if os.path.exists('data.json'): os.remove('data.json')
    c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
