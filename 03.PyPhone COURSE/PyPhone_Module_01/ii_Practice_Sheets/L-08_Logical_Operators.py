import sys
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(g):
    return 'result' in g and g['result'] == True

easy = Task("Store (True and False) or (not False) in variable 'result'.", verify_easy, Level.EASY,
            hints=["result = (True and False) or (not False)"])

def verify_medium(g):
    return 'valid' in g and g['valid'] == (10 > 5 and 5 < 20)

medium = Task("Given x=15, store (x > 10 and x < 20) in variable 'valid'.", verify_medium, Level.MEDIUM,
              hints=["x = 15", "valid = x > 10 and x < 20"])

def verify_hard(g):
    return 'check' in g and g['check'] == (not (10 < 5 or 5 > 1))

hard = Task("Store (not (10 < 5 or 5 > 1)) in 'check'.", verify_hard, Level.HARD,
            hints=["check = not (10 < 5 or 5 > 1)"])

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__": main()
