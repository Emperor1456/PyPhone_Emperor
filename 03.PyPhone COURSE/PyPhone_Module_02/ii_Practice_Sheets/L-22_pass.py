import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Use pass in an empty if statement. Then print 'done'.",
    expected_output="done",
    level=Level.EASY,
    hints=["x=5","if x>0: pass","print('done')"]
)

medium = Task(
    description="Define a function stub with pass, call it, then print 'called'.",
    expected_output="called",
    level=Level.MEDIUM,
    hints=["def stub(): pass","stub()","print('called')"]
)

hard = Task(
    description="Use pass inside a loop to skip an iteration indirectly, then print '42' after loop.",
    expected_output="42",
    level=Level.HARD,
    hints=["for i in range(3):","    if i==1: pass","print(42)"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
