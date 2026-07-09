import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="x=10. If x>5 print 'OK', else print 'NO'.",
    expected_output="OK",
    level=Level.EASY,
    hints=["x=10","if x>5: print('OK')","else: print('NO')"]
)

medium = Task(
    description="num=4. If even print 'Even', else 'Odd'.",
    expected_output="Even",
    level=Level.MEDIUM,
    hints=["num=4","if num%2==0: print('Even')","else: print('Odd')"]
)

hard = Task(
    description="score=75. If score>=90 print 'A', elif >=80 print 'B', elif >=70 print 'C', else 'F'.",
    expected_output="C",
    level=Level.HARD,
    hints=["score=75","if score>=90: print('A')","elif score>=80: print('B')","elif score>=70: print('C')","else: print('F')"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
