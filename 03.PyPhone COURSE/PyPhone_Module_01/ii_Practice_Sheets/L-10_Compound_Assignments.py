import sys
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(g):
    return 'x' in g and g['x'] == 50

easy = Task("Set x=10, then use x *= 5 to get 50.", verify_easy, Level.EASY,
            hints=["x = 10", "x *= 5"])

def verify_medium(g):
    return 'y' in g and g['y'] == 3.0

medium = Task("Set y=10, then y /= 3 should be approximately 3.333, but we'll check as float.", verify_medium, Level.MEDIUM,
              hints=["y = 10", "y /= 3"])

def verify_hard(g):
    return 'a' in g and 'b' in g and g['a'] == 2 and g['b'] == 2

hard = Task("Given a=5, b=5. Do a //= 2 and b %= 3, both should end as 2.", verify_hard, Level.HARD,
            hints=["a = 5", "a //= 2", "b = 5", "b %= 3"])

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__": main()
