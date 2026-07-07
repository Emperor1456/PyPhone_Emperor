import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="items=[1,2,3]. Append 4, then print the list.",
    expected_output="[1, 2, 3, 4]",
    level=Level.EASY,
    hints=["items=[1,2,3]","items.append(4)","print(items)"]
)

medium = Task(
    description="lst=[3,1,5]. Sort it and print the sorted list.",
    expected_output="[1, 3, 5]",
    level=Level.MEDIUM,
    hints=["lst=[3,1,5]","lst.sort()","print(lst)"]
)

hard = Task(
    description="lst=[1,2,3]. Pop the last element, print it, then print the remaining list.",
    expected_output="3\n[1, 2]",
    level=Level.HARD,
    hints=["lst=[1,2,3]","popped=lst.pop()","print(popped)","print(lst)"]
)

def main(): c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
