import sys
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(g):
    return 'tabbed' in g and isinstance(g['tabbed'], str) and '\t' in g['tabbed']

easy = Task("Create a string 'tabbed' that contains a tab character between two words.", verify_easy, Level.EASY,
            hints=["tabbed = 'Hello\\tWorld'"])

def verify_medium(g):
    return 'bell' in g and isinstance(g['bell'], str) and '\a' in g['bell']

medium = Task("Create a string 'bell' that contains the bell character \\a.", verify_medium, Level.MEDIUM,
              hints=["bell = '\\a'"])

def verify_hard(g):
    return 'raw' in g and isinstance(g['raw'], str) and '\\n' in g['raw']

hard = Task("Create a raw string 'raw' that literally shows backslash-n instead of a newline.", verify_hard, Level.HARD,
            hints=["raw = r'\\n'"])

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__": main()
