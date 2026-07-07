import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="s='PyPhone'. Print the first character.",
    expected_output="P",
    level=Level.EASY,
    hints=["s='PyPhone'","print(s[0])"]
)

medium = Task(
    description="s='PyPhone'. Print substring from index 1 to 3 (exclusive 4).",
    expected_output="yPh",
    level=Level.MEDIUM,
    hints=["s='PyPhone'","print(s[1:4])"]
)

hard = Task(
    description="s='PyPhone'. Print the string reversed using slicing.",
    expected_output="enohPyP",
    level=Level.HARD,
    hints=["s='PyPhone'","print(s[::-1])"]
)

def main(): c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
