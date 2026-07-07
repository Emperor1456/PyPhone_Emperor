import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description=(
        "File Reader\n"
        "A file 'message.txt' contains the text 'Hello World'.\n"
        "Read the file and print its content exactly."
    ),
    expected_output="Hello World",
    level=Level.EASY,
    hints=[
        "with open('message.txt','r') as f:\n    content=f.read()",
        "print(content)"
    ]
)

medium = Task(
    description=(
        "Safe File Open\n"
        "Try to open a non‑existent file 'ghost.txt'.\n"
        "Catch FileNotFoundError and print 'File missing'."
    ),
    expected_output="File missing",
    level=Level.MEDIUM,
    hints=[
        "try:\n    open('ghost.txt')\nexcept FileNotFoundError:\n    print('File missing')"
    ]
)

hard = Task(
    description=(
        "Log Analyzer & Report Generator\n\n"
        "A file 'server.log' contains lines like:\n"
        "  ERROR: disk full\n"
        "  WARNING: high memory\n"
        "  INFO: server started\n"
        "  ERROR: connection lost\n\n"
        "Your script must:\n"
        "1. Read 'server.log'.\n"
        "2. Count how many lines start with ERROR and WARNING.\n"
        "3. Write a report to 'report.txt' with the counts.\n"
        "4. Print the report exactly as shown.\n"
        "If 'server.log' does not exist, print 'Log file not found'.\n\n"
        "Report format:\n"
        "Errors: 2\n"
        "Warnings: 1"
    ),
    expected_output="Errors: 2\nWarnings: 1",
    level=Level.HARD,
    hints=[
        "import os",
        "if not os.path.exists('server.log'):\n    print('Log file not found')",
        "else:",
        "    with open('server.log','r') as f:\n        lines=f.readlines()",
        "    errors = sum(1 for line in lines if line.startswith('ERROR'))",
        "    warnings = sum(1 for line in lines if line.startswith('WARNING'))",
        "    with open('report.txt','w') as f:\n        f.write(f'Errors: {errors}\\nWarnings: {warnings}')",
        "    print(f'Errors: {errors}')",
        "    print(f'Warnings: {warnings}')"
    ]
)

def main():
    import os
    # Prepare test files
    with open('message.txt','w') as f: f.write('Hello World')
    with open('server.log','w') as f:
        f.write("ERROR: disk full\n")
        f.write("WARNING: high memory\n")
        f.write("INFO: server started\n")
        f.write("ERROR: connection lost\n")
    if os.path.exists('ghost.txt'): os.remove('ghost.txt')
    for f in ['report.txt','ghost.txt']:
        if os.path.exists(f): os.remove(f)

    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__":
    main()
