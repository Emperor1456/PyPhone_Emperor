import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description=(
        "Grade Calculator:\n"
        "Given a fixed score = 82, use if-elif-else\n"
        "to assign and print the letter grade:\n"
        "A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60"
    ),
    expected_output="Grade: B",
    level=Level.EASY,
    hints=[
        "score = 82",
        "if score >= 90: grade = 'A'",
        "elif score >= 80: grade = 'B'",
        "elif score >= 70: grade = 'C'",
        "elif score >= 60: grade = 'D'",
        "else: grade = 'F'",
        "print(f'Grade: {grade}')"
    ]
)

medium = Task(
    description=(
        "Menu-Driven Calculator:\n"
        "Use match-case with a fixed operation='multiply'\n"
        "and a=15, b=3. Print the result.\n"
        "Support: add, subtract, multiply, divide."
    ),
    expected_output="Result: 45",
    level=Level.MEDIUM,
    hints=[
        "operation = 'multiply'",
        "a, b = 15, 3",
        "match operation:",
        "    case 'add': result = a + b",
        "    case 'subtract': result = a - b",
        "    case 'multiply': result = a * b",
        "    case 'divide': result = a / b",
        "print(f'Result: {result}')"
    ]
)

hard = Task(
    description=(
        "ATM Simulator with Audit Trail\n"
        "Starting balance: 2000.\n"
        "Process these transactions in order:\n"
        "  ('deposit', 500)\n"
        "  ('withdraw', 3000)  ← exceeds balance\n"
        "  ('withdraw', 200)\n"
        "  ('withdraw', 800)\n"
        "  ('deposit', 100)\n\n"
        "Rules:\n"
        "- Skip any withdrawal that exceeds balance.\n"
        "- Print 'Insufficient funds' for skipped ones.\n"
        "- Print balance after every valid transaction.\n"
        "- After all 5, print final balance and\n"
        "  count of rejected transactions."
    ),
    expected_output=(
        "Deposit: 500 | Balance: 2500\n"
        "Insufficient funds for withdrawal 3000\n"
        "Withdrawal: 200 | Balance: 2300\n"
        "Withdrawal: 800 | Balance: 1500\n"
        "Deposit: 100 | Balance: 1600\n"
        "Final balance: 1600\n"
        "Rejected transactions: 1"
    ),
    level=Level.HARD,
    hints=[
        "balance = 2000; rejected = 0",
        "transactions = [('deposit',500),('withdraw',3000),('withdraw',200),('withdraw',800),('deposit',100)]",
        "for t, amt in transactions:",
        "    if t == 'deposit':",
        "        balance += amt",
        "        print(f'Deposit: {amt} | Balance: {balance}')",
        "    elif amt > balance:",
        "        print(f'Insufficient funds for withdrawal {amt}')",
        "        rejected += 1",
        "    else:",
        "        balance -= amt",
        "        print(f'Withdrawal: {amt} | Balance: {balance}')",
        "print(f'Final balance: {balance}')",
        "print(f'Rejected transactions: {rejected}')"
    ]
)

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__":
    main()
