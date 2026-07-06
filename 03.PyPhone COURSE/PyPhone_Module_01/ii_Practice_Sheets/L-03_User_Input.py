import sys
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(g):
    return 'name' in g and isinstance(g['name'], str) and len(g['name']) > 0

easy = Task("Use input() to get a user's name and store it in 'name'. Then print 'Hello, ' + name.", verify_easy, Level.EASY,
            hints=["name = input('Enter name: ')", "print('Hello, ' + name)"])

def verify_medium(g):
    return 'age' in g and isinstance(g['age'], int) and 'year_of_birth' in g and g['year_of_birth'] == 2026 - g['age']

medium = Task("Ask for age (input), convert to int, then calculate year_of_birth = 2026 - age.", verify_medium, Level.MEDIUM,
              hints=["age = int(input('Age: '))", "year_of_birth = 2026 - age"])

def verify_hard(g):
    return 'nums' in g and isinstance(g['nums'], list) and g['nums'] == [int(x) for x in ['5','10','15']]

hard = Task("Take input '5,10,15' (a comma‑separated string), split it, and convert each to int in list 'nums'.", verify_hard, Level.HARD,
            hints=["data = input('Enter numbers: ')","nums = [int(x) for x in data.split(',')]"])

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__": main()
