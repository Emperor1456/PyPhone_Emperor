import sys
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(g):
    return 'a' in g and g['a'] == 1  # 5 & 3 = 1

easy = Task("Compute 5 & 3 and store in 'a'.", verify_easy, Level.EASY,
            hints=["a = 5 & 3"])

def verify_medium(g):
    return 'b' in g and g['b'] == 7  # 5 | 3 = 7

medium = Task("Compute 5 | 3 and store in 'b'.", verify_medium, Level.MEDIUM,
              hints=["b = 5 | 3"])

def verify_hard(g):
    return 'c' in g and g['c'] == 6  # 12 & 6 = 4? Actually 12 & 6 = 4, but 12 | 6 = 14. We'll use 6 & 3 = 2? I need a correct example. Let's use 6 & 3 = 2, 6 | 3 = 7. We'll store both in c and d. But verify_hard checks only one variable. I'll adjust: create c = 6 & 3 (2) and d = 6 | 3 (7), then check both. But verify returns single bool. We'll return c == 2 and d == 7. We'll put both in one line? No, we need to check existence of both. We'll write verify for multiple vars.
    return 'c' in g and 'd' in g and g['c'] == 2 and g['d'] == 7

hard = Task("Compute 6 & 3 (result 2) in 'c', and 6 | 3 (result 7) in 'd'.", verify_hard, Level.HARD,
            hints=["c = 6 & 3", "d = 6 | 3"])

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__": main()
