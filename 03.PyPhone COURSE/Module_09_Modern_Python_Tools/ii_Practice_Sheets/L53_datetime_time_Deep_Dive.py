import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "📅  Today's Date\n\n"
        "From datetime import date. Print today's date in YYYY-MM-DD format.\n"
        "(The engine will accept the actual current date.)\n\n"
        "Expected output: (current date in YYYY-MM-DD)"
    ),
    expected_output=__import__('datetime').date.today().strftime("%Y-%m-%d"),
    level=Level.EASY,
    hints=["from datetime import date", "print(date.today().strftime('%Y-%m-%d'))"]
)

easy2 = Task(
    description=(
        "⏰  Current Time\n\n"
        "From datetime import datetime. Print the current time in HH:MM format.\n\n"
        "Expected output: (current time as HH:MM)"
    ),
    expected_output=__import__('datetime').datetime.now().strftime("%H:%M"),
    level=Level.EASY,
    hints=["from datetime import datetime", "print(datetime.now().strftime('%H:%M'))"]
)

medium1 = Task(
    description=(
        "📊  Days Until New Year\n\n"
        "Calculate the number of days from today until the next January 1st.\n"
        "If today is Jan 1, return 0. Print the number.\n"
        "(Accept any reasonable positive integer.)\n\n"
        "Expected output: (a positive number of days)"
    ),
    expected_output=str((__import__('datetime').date(__import__('datetime').date.today().year+1, 1, 1) - __import__('datetime').date.today()).days),
    level=Level.MEDIUM,
    hints=["from datetime import date", "today = date.today()", "next_year = date(today.year+1, 1, 1)", "print((next_year - today).days)"]
)

medium2 = Task(
    description=(
        "⏱️  Parse a Date String\n\n"
        "Given date_str = '2026-01-15', parse it using strptime with format '%Y-%m-%d'.\n"
        "Print the month (as integer, e.g., 1).\n\n"
        "Expected output: 1"
    ),
    expected_output="1",
    level=Level.MEDIUM,
    hints=["from datetime import datetime", "date_str = '2026-01-15'", "parsed = datetime.strptime(date_str, '%Y-%m-%d')", "print(parsed.month)"]
)

hard1 = Task(
    description=(
        "🔁  Add 30 Days\n\n"
        "From datetime import datetime, timedelta. Get the current date, add 30 days,\n"
        "and print the resulting date in YYYY-MM-DD format.\n\n"
        "Expected output: (30 days from today)"
    ),
    expected_output=(__import__('datetime').date.today() + __import__('datetime').timedelta(days=30)).strftime("%Y-%m-%d"),
    level=Level.HARD,
    hints=["from datetime import date, timedelta", "future = date.today() + timedelta(days=30)", "print(future.strftime('%Y-%m-%d'))"]
)

hard2 = Task(
    description=(
        "🛠️  Age Calculator\n\n"
        "Given birth_date = date(2008, 7, 10), calculate age in years.\n"
        "Subtract birth year from current year, adjust if birthday hasn't occurred yet this year.\n"
        "Print the integer age.\n\n"
        "Expected output: (current age based on 2008-07-10)"
    ),
    expected_output=str(
        __import__('datetime').date.today().year - 2008 -
        (1 if __import__('datetime').date.today().strftime("%m-%d") < "07-10" else 0)
    ),
    level=Level.HARD,
    hints=["from datetime import date", "birth = date(2008, 7, 10)", "today = date.today()", "age = today.year - birth.year", "if today.strftime('%m-%d') < birth.strftime('%m-%d'): age -= 1", "print(age)"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L53.json")
