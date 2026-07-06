import sys
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(g):
    return 'left' in g and g['left'] == 32  # 8 << 2 = 32

easy = Task("Compute 8 << 2 and store in 'left'.", verify_easy, Level.EASY,
            hints=["left = 8 << 2"])

def verify_medium(g):
    return 'right' in g and g['right'] == 2  # 8 >> 2 = 2

medium = Task("Compute 8 >> 2 and store in 'right'.", verify_medium, Level.MEDIUM,
              hints=["right = 8 >> 2"])

def verify_hard(g):
    return 'a' in g and 'b' in g and g['a'] == 40 and g['b'] == 5  # 10 << 2 = 40, 20 >> 2 = 5

hard = Task("Store 10 << 2 in 'a' and 20 >> 2 in 'b'.", verify_hard, Level.HARD,
            hints=["a = 10 << 2", "b = 20 >> 2"])

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__": main()
