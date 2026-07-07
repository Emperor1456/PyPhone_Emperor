import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="d={'name':'Emperor','age':18}. Print the value of 'name'.",
    expected_output="Emperor",
    level=Level.EASY,
    hints=["d={'name':'Emperor','age':18}", "print(d['name'])"]
)

medium = Task(
    description="d={'name':'Emperor','age':18}. Add key 'city'='Dhaka', then print d.",
    expected_output="{'name': 'Emperor', 'age': 18, 'city': 'Dhaka'}",
    level=Level.MEDIUM,
    hints=["d={'name':'Emperor','age':18}", "d['city']='Dhaka'", "print(d)"]
)

hard = Task(
    description="d={'name':'Emperor','age':18}. Increment age by 1, print the updated dict.",
    expected_output="{'name': 'Emperor', 'age': 19}",
    level=Level.HARD,
    hints=["d={'name':'Emperor','age':18}", "d['age']+=1", "print(d)"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
