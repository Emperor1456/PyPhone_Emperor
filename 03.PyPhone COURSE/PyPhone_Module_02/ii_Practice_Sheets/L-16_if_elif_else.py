import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="score=65. Print grade: A>=80, B>=70, C>=60, else D.",
    expected_output="C",
    level=Level.EASY,
    hints=["score=65","if score>=80: print('A')","elif score>=70: print('B')","elif score>=60: print('C')","else: print('D')"]
)

medium = Task(
    description="points=75. A>=90, B>=75, C>=60, else F.",
    expected_output="B",
    level=Level.MEDIUM,
    hints=["points=75","if points>=90: print('A')","elif points>=75: print('B')","elif points>=60: print('C')","else: print('F')"]
)

hard = Task(
    description="temp=55. Hot>100, Warm>70, Medium>40, else Cold.",
    expected_output="Medium",
    level=Level.HARD,
    hints=["temp=55","if temp>100: print('Hot')","elif temp>70: print('Warm')","elif temp>40: print('Medium')","else: print('Cold')"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
