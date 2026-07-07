import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="s='emperor'. Print it in uppercase.",
    expected_output="EMPEROR",
    level=Level.EASY,
    hints=["s='emperor'","print(s.upper())"]
)

medium = Task(
    description="t='  data  '. Print it without surrounding spaces.",
    expected_output="data",
    level=Level.MEDIUM,
    hints=["t='  data  '","print(t.strip())"]
)

hard = Task(
    description="msg='Hello World'. Replace 'World' with 'Emperor' and print.",
    expected_output="Hello Emperor",
    level=Level.HARD,
    hints=["msg='Hello World'","print(msg.replace('World','Emperor'))"]
)

def main(): c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
