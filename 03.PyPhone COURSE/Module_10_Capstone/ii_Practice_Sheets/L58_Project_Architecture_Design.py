import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "📋  Requirements List\n\n"
        "List the core features of the Imperial Contact Book.\n"
        "Print a list of strings: ['Add contact', 'List contacts', 'Search', 'Update', 'Delete']\n\n"
        "Expected output: ['Add contact', 'List contacts', 'Search', 'Update', 'Delete']"
    ),
    expected_output="['Add contact', 'List contacts', 'Search', 'Update', 'Delete']",
    level=Level.EASY,
    hints=["features = ['Add contact', 'List contacts', 'Search', 'Update', 'Delete']", "print(features)"]
)

easy2 = Task(
    description=(
        "📁  Project Structure\n\n"
        "Print the names of the files that should be in the Imperial Contact Book project:\n"
        "['main.py', 'database.py', 'models.py', 'tests.py', 'requirements.txt']\n\n"
        "Expected output: ['main.py', 'database.py', 'models.py', 'tests.py', 'requirements.txt']"
    ),
    expected_output="['main.py', 'database.py', 'models.py', 'tests.py', 'requirements.txt']",
    level=Level.EASY,
    hints=["files = ['main.py', 'database.py', 'models.py', 'tests.py', 'requirements.txt']", "print(files)"]
)

medium1 = Task(
    description=(
        "🗃️  Database Schema Design\n\n"
        "Print the SQL CREATE TABLE statement for the contacts table.\n"
        "Columns: id (PK, autoincrement), name (TEXT NOT NULL), phone (TEXT NOT NULL UNIQUE),\n"
        "email (TEXT), group_name (TEXT DEFAULT 'General'), created_at (TEXT DEFAULT datetime('now')).\n\n"
        "Expected output:\nCREATE TABLE contacts (\n    id INTEGER PRIMARY KEY AUTOINCREMENT,\n    name TEXT NOT NULL,\n    phone TEXT NOT NULL UNIQUE,\n    email TEXT,\n    group_name TEXT DEFAULT 'General',\n    created_at TEXT DEFAULT (datetime('now'))\n);"
    ),
    expected_output=(
        "CREATE TABLE contacts (\n"
        "    id INTEGER PRIMARY KEY AUTOINCREMENT,\n"
        "    name TEXT NOT NULL,\n"
        "    phone TEXT NOT NULL UNIQUE,\n"
        "    email TEXT,\n"
        "    group_name TEXT DEFAULT 'General',\n"
        "    created_at TEXT DEFAULT (datetime('now'))\n"
        ");"
    ),
    level=Level.MEDIUM,
    hints=["print('CREATE TABLE contacts (')", "print('    id INTEGER PRIMARY KEY AUTOINCREMENT,')", "print('    name TEXT NOT NULL,')", "print('    phone TEXT NOT NULL UNIQUE,')", "print('    email TEXT,')", "print('    group_name TEXT DEFAULT \\'General\\',')", "print('    created_at TEXT DEFAULT (datetime(\\'now\\'))')", "print(');')"]
)

medium2 = Task(
    description=(
        "🏗️  CLI Interface Design\n\n"
        "Print the command-line usage for the Imperial Contact Book.\n"
        "Five commands: add, list, search, update, delete, each with required arguments.\n\n"
        "Expected output:\npython main.py add <name> <phone> [email] [group]\npython main.py list\npython main.py search <query>\npython main.py update <id> <new_phone>\npython main.py delete <id>"
    ),
    expected_output=(
        "python main.py add <name> <phone> [email] [group]\n"
        "python main.py list\n"
        "python main.py search <query>\n"
        "python main.py update <id> <new_phone>\n"
        "python main.py delete <id>"
    ),
    level=Level.MEDIUM,
    hints=[
        "print('python main.py add <name> <phone> [email] [group]')",
        "print('python main.py list')",
        "print('python main.py search <query>')",
        "print('python main.py update <id> <new_phone>')",
        "print('python main.py delete <id>')"
    ]
)

hard1 = Task(
    description=(
        "📊  Module Responsibility Map\n\n"
        "Print a dictionary mapping each module to its responsibility.\n"
        "Keys: 'main.py', 'database.py', 'models.py', 'tests.py'.\n"
        "Values: short description strings.\n\n"
        "Expected output: {'main.py': 'CLI entry point', 'database.py': 'DB connection and schema', 'models.py': 'CRUD operations', 'tests.py': 'Unit tests'}"
    ),
    expected_output="{'main.py': 'CLI entry point', 'database.py': 'DB connection and schema', 'models.py': 'CRUD operations', 'tests.py': 'Unit tests'}",
    level=Level.HARD,
    hints=["desc = {", "    'main.py': 'CLI entry point',", "    'database.py': 'DB connection and schema',", "    'models.py': 'CRUD operations',", "    'tests.py': 'Unit tests'", "}", "print(desc)"]
)

hard2 = Task(
    description=(
        "🧪  Design a Test Plan\n\n"
        "Print a list of test cases you would write for the contact book.\n"
        "Example: 'test_add_contact', 'test_list_contacts', 'test_search_found', 'test_search_not_found', 'test_update_phone', 'test_delete_contact'.\n\n"
        "Expected output: ['test_add_contact', 'test_list_contacts', 'test_search_found', 'test_search_not_found', 'test_update_phone', 'test_delete_contact']"
    ),
    expected_output="['test_add_contact', 'test_list_contacts', 'test_search_found', 'test_search_not_found', 'test_update_phone', 'test_delete_contact']",
    level=Level.HARD,
    hints=["tests = ['test_add_contact', 'test_list_contacts', 'test_search_found', 'test_search_not_found', 'test_update_phone', 'test_delete_contact']", "print(tests)"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L58.json")
