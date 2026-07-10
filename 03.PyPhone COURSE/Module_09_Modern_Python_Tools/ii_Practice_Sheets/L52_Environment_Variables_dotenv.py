import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🔐  Read Environment Variable\n\n"
        "Import os. Print the value of the HOME environment variable.\n"
        "If it doesn't exist, print 'not set'.\n\n"
        "Expected output: (your home directory path)"
    ),
    expected_output=os.getenv("HOME", "not set"),
    level=Level.EASY,
    hints=["import os", "print(os.getenv('HOME', 'not set'))"]
)

easy2 = Task(
    description=(
        "🛡️  Default Value for Missing Variable\n\n"
        "Read an environment variable 'NONEXISTENT' with default 'default_value'.\n"
        "Print the result.\n\n"
        "Expected output: default_value"
    ),
    expected_output="default_value",
    level=Level.EASY,
    hints=["import os", "print(os.getenv('NONEXISTENT', 'default_value'))"]
)

medium1 = Task(
    description=(
        "📄  Load .env File\n\n"
        "Print the code to load a .env file using dotenv.\n"
        "Print 'from dotenv import load_dotenv' then 'load_dotenv()' on two lines.\n\n"
        "Expected output:\nfrom dotenv import load_dotenv\nload_dotenv()"
    ),
    expected_output="from dotenv import load_dotenv\nload_dotenv()",
    level=Level.MEDIUM,
    hints=["print('from dotenv import load_dotenv')", "print('load_dotenv()')"]
)

medium2 = Task(
    description=(
        "🔧  Set Environment Variable\n\n"
        "Using os.environ, set a variable 'MY_VAR' to 'emperor'. Then print its value.\n\n"
        "Expected output: emperor"
    ),
    expected_output="emperor",
    level=Level.MEDIUM,
    hints=["import os", "os.environ['MY_VAR'] = 'emperor'", "print(os.getenv('MY_VAR'))"]
)

hard1 = Task(
    description=(
        "🧪  Check Multiple Variables\n\n"
        "Define a function get_config() that reads 'DB_HOST' and 'DB_PORT' from environment\n"
        "with defaults 'localhost' and '5432'. Return them as a tuple and print the tuple.\n\n"
        "Expected output: ('localhost', '5432')"
    ),
    expected_output="('localhost', '5432')",
    level=Level.HARD,
    hints=["import os", "def get_config():", "    host = os.getenv('DB_HOST', 'localhost')", "    port = os.getenv('DB_PORT', '5432')", "    return host, port", "print(get_config())"]
)

hard2 = Task(
    description=(
        "🔐  Secret Key Pattern\n\n"
        "Read an env var 'SECRET_KEY'. If missing, generate a random 16-character hex string\n"
        "using os.urandom(8).hex() and print it.\n\n"
        "Expected output: (a random 16-char hex string)"
    ),
    expected_output=os.getenv("SECRET_KEY", os.urandom(8).hex()),
    level=Level.HARD,
    hints=["import os", "secret = os.getenv('SECRET_KEY')", "if secret is None:", "    secret = os.urandom(8).hex()", "print(secret)"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L52.json")
