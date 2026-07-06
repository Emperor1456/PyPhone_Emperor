import sys
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(g):
    return 'floor' in g and g['floor'] == 7 and 'remainder' in g and g['remainder'] == 3

easy = Task("Compute floor division 31 // 4 and store in 'floor', and modulus 31 % 4 in 'remainder'.", verify_easy, Level.EASY,
            hints=["floor = 31 // 4", "remainder = 31 % 4"])

def verify_medium(g):
    return 'power' in g and g['power'] == 1024

medium = Task("Compute 2 ** 10 and store in 'power'.", verify_medium, Level.MEDIUM,
              hints=["power = 2 ** 10"])

def verify_hard(g):
    return 'result' in g and abs(g['result'] - 2.0) < 0.001

hard = Task("Evaluate (3 + 5) // 4 + 2 ** 3 % 3 and store in 'result' (should be 2.0).", verify_hard, Level.HARD,
            hints=["result = (3 + 5) // 4 + 2 ** 3 % 3"])

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__": main()
