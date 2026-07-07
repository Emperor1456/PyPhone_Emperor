import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Try int('abc'), catch ValueError and print 'ValueError'.",
    expected_output="ValueError",
    level=Level.EASY,
    hints=["try:\n    int('abc')\nexcept ValueError:\n    print('ValueError')"]
)

medium = Task(
    description="Try len(5), catch TypeError and print 'TypeError'.",
    expected_output="TypeError",
    level=Level.MEDIUM,
    hints=["try:\n    len(5)\nexcept TypeError:\n    print('TypeError')"]
)

hard = Task(
    description="Try 5/0, catch both ZeroDivisionError and ValueError; print the exception type name that was caught.",
    expected_output="ZeroDivisionError",
    level=Level.HARD,
    hints=["try:\n    5/0\nexcept ZeroDivisionError:\n    print('ZeroDivisionError')\nexcept ValueError:\n    print('ValueError')"]
)

def main(): c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
