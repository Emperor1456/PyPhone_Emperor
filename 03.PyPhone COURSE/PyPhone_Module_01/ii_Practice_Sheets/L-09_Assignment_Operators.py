import sys
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(g):
    return 'x' in g and g['x'] == 15

easy = Task("Start with x=10, then use x += 5 to make it 15.", verify_easy, Level.EASY,
            hints=["x = 10", "x += 5"])

def verify_medium(g):
    return 'y' in g and g['y'] == 3 and 'z' in g and g['z'] == 9

medium = Task("Set y=9, then use y //= 3 to make it 3. Set z=3, then z **= 2 to make 9.", verify_medium, Level.MEDIUM,
              hints=["y = 9", "y //= 3", "z = 3", "z **= 2"])

def verify_hard(g):
    return 'a' in g and g['a'] == 1 and 'b' in g and g['b'] == 1

hard = Task("Given a=5, b=5. Use a %= 2 and b //= 2, both should become 1.", verify_hard, Level.HARD,
            hints=["a = 5", "a %= 2", "b = 5", "b //= 2"])

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__": main()
