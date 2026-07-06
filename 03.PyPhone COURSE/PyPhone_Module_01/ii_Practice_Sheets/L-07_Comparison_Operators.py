import sys
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(g):
    return 'a' in g and 'b' in g and 'gt' in g and g['gt'] == (g['a'] > g['b'])

easy = Task("Create variables 'a'=10, 'b'=5, and store (a > b) in variable 'gt'.", verify_easy, Level.EASY,
            hints=["a = 10", "b = 5", "gt = a > b"])

def verify_medium(g):
    return 'eq' in g and g['eq'] == (5 == 5)

medium = Task("Store the result of 5 == 5 in variable 'eq'.", verify_medium, Level.MEDIUM,
              hints=["eq = 5 == 5"])

def verify_hard(g):
    return 'res' in g and g['res'] == (10 != 5 and 10 > 5 and 5 <= 10)

hard = Task("Store the result of (10 != 5 and 10 > 5 and 5 <= 10) in 'res'.", verify_hard, Level.HARD,
            hints=["res = 10 != 5 and 10 > 5 and 5 <= 10"])

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__": main()
