import sys, csv; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'rows' in g and isinstance(g['rows'], list)
easy=Task("Read the file 'data.csv' (we'll create it with two rows) into a list of lists using csv.reader. Store in 'rows'.", verify_easy, Level.EASY, hints=["import csv","with open('data.csv','r') as f:\n    reader=csv.reader(f)\n    rows=list(reader)"])
def verify_medium(g): return 'dict_rows' in g and isinstance(g['dict_rows'], list) and 'name' in g['dict_rows'][0]
medium=Task("Read the same CSV using csv.DictReader and store in 'dict_rows'.", verify_medium, Level.MEDIUM, hints=["with open('data.csv','r') as f:\n    reader=csv.DictReader(f)\n    dict_rows=list(reader)"])
def verify_hard(g): return os.path.exists('out.csv') and open('out.csv').read()=='name,age\nEmperor,18\n'
hard=Task("Write a CSV file 'out.csv' with header 'name,age' and one row 'Emperor,18'.", verify_hard, Level.HARD, hints=["import csv","with open('out.csv','w',newline='') as f:\n    writer=csv.writer(f)\n    writer.writerow(['name','age'])\n    writer.writerow(['Emperor','18'])"])
def main():
    import os
    with open('data.csv','w') as f: f.write('name,age\nAlice,30\nBob,25')
    if os.path.exists('out.csv'): os.remove('out.csv')
    c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
