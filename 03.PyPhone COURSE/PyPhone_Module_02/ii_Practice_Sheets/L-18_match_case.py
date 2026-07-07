import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="x=1. Use match-case to print 'one' for 1, 'two' for 2, else 'other'.",
    expected_output="one",
    level=Level.EASY,
    hints=["x=1","match x:","    case 1: print('one')","    case 2: print('two')","    case _: print('other')"]
)

medium = Task(
    description="color='r'. Match: 'r'->'Red', 'g'->'Green', 'b'->'Blue'.",
    expected_output="Red",
    level=Level.MEDIUM,
    hints=["color='r'","match color:","    case 'r': print('Red')","    case 'g': print('Green')","    case 'b': print('Blue')"]
)

hard = Task(
    description="code=200. Match 200->'Success', 404->'Not Found', _->'Unknown'.",
    expected_output="Success",
    level=Level.HARD,
    hints=["code=200","match code:","    case 200: print('Success')","    case 404: print('Not Found')","    case _: print('Unknown')"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
