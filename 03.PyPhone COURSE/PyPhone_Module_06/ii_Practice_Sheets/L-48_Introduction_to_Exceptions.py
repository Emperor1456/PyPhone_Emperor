import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Try to convert 'abc' to int, catch ValueError and print 'error'.",
    expected_output="error",
    level=Level.EASY,
    hints=["try:\n    int('abc')\nexcept ValueError:\n    print('error')"]
)

medium = Task(
    description="Divide 10 by 0, catch ZeroDivisionError and print 'caught'.",
    expected_output="caught",
    level=Level.MEDIUM,
    hints=["try:\n    10/0\nexcept ZeroDivisionError:\n    print('caught')"]
)

hard = Task(
    description="Open a non-existent file, catch FileNotFoundError and print 'missing'.",
    expected_output="missing",
    level=Level.HARD,
    hints=["try:\n    open('nofile.txt')\nexcept FileNotFoundError:\n    print('missing')"]
)

def main(): c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
