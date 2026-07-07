import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Print the current Python executable path using sys.executable.",
    expected_output=sys.executable,
    level=Level.EASY,
    hints=["import sys","print(sys.executable)"]
)

medium = Task(
    description="Print the command to create a virtual environment: 'python -m venv myenv'.",
    expected_output="python -m venv myenv",
    level=Level.MEDIUM,
    hints=["print('python -m venv myenv')"]
)

hard = Task(
    description="Print the activation command for a virtual environment: 'source myenv/bin/activate'.",
    expected_output="source myenv/bin/activate",
    level=Level.HARD,
    hints=["print('source myenv/bin/activate')"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
