import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Create a set with elements 1,2,3 and print it.",
    expected_output="{1, 2, 3}",
    level=Level.EASY,
    hints=["s={1,2,3}", "print(s)"]
)

medium = Task(
    description="Start with s={1,2,3}. Add 4 to the set, then print the set.",
    expected_output="{1, 2, 3, 4}",
    level=Level.MEDIUM,
    hints=["s={1,2,3}", "s.add(4)", "print(s)"]
)

hard = Task(
    description="Given list [1,2,2,3,3,3], convert to a set and back to a sorted list. Print the list.",
    expected_output="[1, 2, 3]",
    level=Level.HARD,
    hints=["lst=[1,2,2,3,3,3]", "unique=sorted(set(lst))", "print(unique)"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
