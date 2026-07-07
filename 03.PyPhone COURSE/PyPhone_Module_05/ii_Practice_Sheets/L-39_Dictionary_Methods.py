import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="d={'name':'Emperor','age':18}. Print list of keys.",
    expected_output="['name', 'age']",
    level=Level.EASY,
    hints=["d={'name':'Emperor','age':18}", "print(list(d.keys()))"]
)

medium = Task(
    description="Same d. Print list of values.",
    expected_output="['Emperor', 18]",
    level=Level.MEDIUM,
    hints=["print(list(d.values()))"]
)

hard = Task(
    description="d={'name':'Emperor','age':18}. Pop the 'age' key, print the popped value and the remaining dict on two lines.",
    expected_output="18\n{'name': 'Emperor'}",
    level=Level.HARD,
    hints=["d={'name':'Emperor','age':18}", "popped=d.pop('age')", "print(popped)", "print(d)"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
