import sys, csv, os; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Read 'data.csv' (name,age) into a list of rows using csv.reader. Print the rows. (We'll create the file with two rows.)",
    expected_output="[['name', 'age'], ['Alice', '30'], ['Bob', '25']]",
    level=Level.EASY,
    hints=["import csv","with open('data.csv','r') as f:\n    reader=csv.reader(f)\n    rows=list(reader)","print(rows)"]
)

medium = Task(
    description="Read the same CSV using csv.DictReader and print the list of dicts.",
    expected_output="[{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]",
    level=Level.MEDIUM,
    hints=["with open('data.csv','r') as f:\n    reader=csv.DictReader(f)\n    dict_rows=list(reader)","print(dict_rows)"]
)

hard = Task(
    description="Write a CSV file 'out.csv' with header 'name,age' and one row 'Emperor,18'. Then read and print its content.",
    expected_output="name,age\nEmperor,18",
    level=Level.HARD,
    hints=["import csv","with open('out.csv','w',newline='') as f:\n    writer=csv.writer(f)\n    writer.writerow(['name','age'])\n    writer.writerow(['Emperor','18'])","print(open('out.csv').read().strip())"]
)

def main():
    with open('data.csv','w') as f: f.write('name,age\nAlice,30\nBob,25')
    if os.path.exists('out.csv'): os.remove('out.csv')
    c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
