import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="nums=[1,2,3,4,5]. Print sublist [2,3,4] using slicing.",
    expected_output="[2, 3, 4]",
    level=Level.EASY,
    hints=["nums=[1,2,3,4,5]","print(nums[1:4])"]
)

medium = Task(
    description="nums=[1,2,3,4]. Create list of squares using comprehension. Print it.",
    expected_output="[1, 4, 9, 16]",
    level=Level.MEDIUM,
    hints=["nums=[1,2,3,4]","squares=[x*x for x in nums]","print(squares)"]
)

hard = Task(
    description="From [1,2,3,4,5,6], use comprehension to keep only evens. Print the list.",
    expected_output="[2, 4, 6]",
    level=Level.HARD,
    hints=["evens=[x for x in [1,2,3,4,5,6] if x%2==0]","print(evens)"]
)

def main(): c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
