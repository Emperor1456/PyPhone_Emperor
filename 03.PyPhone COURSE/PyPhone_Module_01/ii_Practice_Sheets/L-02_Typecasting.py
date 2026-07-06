import sys
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(g):
    return 'age_str' in g and g['age_str'] == '25' and 'age_int' in g and g['age_int'] == 25

easy = Task("Create 'age_str' = '25' (str), then convert it to int and store in 'age_int'.", verify_easy, Level.EASY,
            hints=["age_str = '25'", "age_int = int(age_str)"])

def verify_medium(g):
    return 'pi' in g and isinstance(g['pi'], float) and abs(g['pi'] - 3.14) < 0.01 and 'pi_str' in g and g['pi_str'] == '3.14'

medium = Task("Create 'pi' = 3.14 (float), then convert to string '3.14' in 'pi_str'.", verify_medium, Level.MEDIUM,
              hints=["pi = 3.14", "pi_str = str(pi)"])

def verify_hard(g):
    return 'vals' in g and g['vals'] == ['1','2','3'] and 'nums' in g and g['nums'] == [1,2,3]

hard = Task("Given list 'vals' = ['1','2','3'], convert each element to int and store in 'nums'.", verify_hard, Level.HARD,
            hints=["vals = ['1','2','3']", "nums = [int(v) for v in vals]"])

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__": main()
