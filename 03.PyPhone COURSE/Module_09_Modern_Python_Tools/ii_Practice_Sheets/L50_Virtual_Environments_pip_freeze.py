import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🔧  Create venv Command\n\n"
        "Print the exact command to create a virtual environment named 'myenv'.\n\n"
        "Expected output: python -m venv myenv"
    ),
    expected_output="python -m venv myenv",
    level=Level.EASY,
    hints=["print('python -m venv myenv')"]
)

easy2 = Task(
    description=(
        "⚡  Activate venv Command\n\n"
        "Print the command to activate a virtual environment (Linux/Termux).\n\n"
        "Expected output: source myenv/bin/activate"
    ),
    expected_output="source myenv/bin/activate",
    level=Level.EASY,
    hints=["print('source myenv/bin/activate')"]
)

medium1 = Task(
    description=(
        "📋  Freeze Requirements\n\n"
        "Print the command to freeze installed packages to requirements.txt.\n\n"
        "Expected output: pip freeze > requirements.txt"
    ),
    expected_output="pip freeze > requirements.txt",
    level=Level.MEDIUM,
    hints=["print('pip freeze > requirements.txt')"]
)

medium2 = Task(
    description=(
        "📦  Install from Requirements\n\n"
        "Print the command to install packages from requirements.txt.\n\n"
        "Expected output: pip install -r requirements.txt"
    ),
    expected_output="pip install -r requirements.txt",
    level=Level.MEDIUM,
    hints=["print('pip install -r requirements.txt')"]
)

hard1 = Task(
    description=(
        "🧪  Deactivate Command\n\n"
        "Print the command to deactivate a virtual environment.\n\n"
        "Expected output: deactivate"
    ),
    expected_output="deactivate",
    level=Level.HARD,
    hints=["print('deactivate')"]
)

hard2 = Task(
    description=(
        "🛠️  Full Workflow\n\n"
        "Print all three commands (create, activate, freeze) on separate lines.\n\n"
        "Expected output:\npython -m venv myenv\nsource myenv/bin/activate\npip freeze > requirements.txt"
    ),
    expected_output="python -m venv myenv\nsource myenv/bin/activate\npip freeze > requirements.txt",
    level=Level.HARD,
    hints=[
        "print('python -m venv myenv')",
        "print('source myenv/bin/activate')",
        "print('pip freeze > requirements.txt')"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L50.json")
