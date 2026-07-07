import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Open a non-existent file, catch FileNotFoundError and print 'file missing'.",
    expected_output="file missing",
    level=Level.EASY,
    hints=["try:\n    open('nofile.txt')\nexcept FileNotFoundError:\n    print('file missing')"]
)

medium = Task(
    description="Try to convert 'abc' to int, catch ValueError and print 'value error'.",
    expected_output="value error",
    level=Level.MEDIUM,
    hints=["try:\n    int('abc')\nexcept ValueError:\n    print('value error')"]
)

hard = Task(
    description="Combine try/except/else/finally with a safe operation. Print 'try', then 'else', then 'finally' on separate lines by executing appropriate blocks.",
    expected_output="try\nelse\nfinally",
    level=Level.HARD,
    hints=["try:\n    print('try')\nexcept:\n    pass\nelse:\n    print('else')\nfinally:\n    print('finally')"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
