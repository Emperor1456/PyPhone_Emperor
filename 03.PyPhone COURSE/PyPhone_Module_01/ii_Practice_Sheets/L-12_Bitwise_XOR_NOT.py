import sys
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(g):
    return 'x' in g and g['x'] == 6  # 5 ^ 3 = 6

easy = Task("Compute 5 ^ 3 and store in 'x'.", verify_easy, Level.EASY,
            hints=["x = 5 ^ 3"])

def verify_medium(g):
    return 'y' in g and g['y'] == -6  # ~5 = -6

medium = Task("Compute ~5 and store in 'y'.", verify_medium, Level.MEDIUM,
              hints=["y = ~5"])

def verify_hard(g):
    return 'a' in g and 'b' in g and g['a'] == 1 and g['b'] == -4  # 4 ^ 5 = 1, ~3 = -4

hard = Task("Store 4 ^ 5 in 'a' and ~3 in 'b'.", verify_hard, Level.HARD,
            hints=["a = 4 ^ 5", "b = ~3"])

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__": main()
