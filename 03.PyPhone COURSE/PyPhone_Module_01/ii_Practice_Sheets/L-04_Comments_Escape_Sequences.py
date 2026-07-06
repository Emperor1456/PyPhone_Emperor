import sys
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(g):
    # User must type a line that contains # and a print with \n
    return True  # we'll just trust they wrote a comment

easy = Task("Write a comment with '#' and then print a string containing a newline '\\n'.", verify_easy, Level.EASY,
            hints=["# This is a comment", "print('Hello\\nWorld')"])

def verify_medium(g):
    return 'quote' in g and isinstance(g['quote'], str) and '"' in g['quote']

medium = Task("Create variable 'quote' containing double quotes inside single quotes: 'He said \"Hi\"'.", verify_medium, Level.MEDIUM,
              hints=["quote = 'He said \"Hi\"'"])

def verify_hard(g):
    return 'path' in g and isinstance(g['path'], str) and '\\' in g['path']

hard = Task("Create a variable 'path' that holds a Windows path with double backslashes: C:\\\\Users\\\\Emperor.", verify_hard, Level.HARD,
            hints=["path = 'C:\\\\Users\\\\Emperor'"])

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__": main()
