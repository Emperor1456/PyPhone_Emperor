import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "➕  Add Two Numbers\n\n"
        "Define a function add(a, b) that returns a + b.\n"
        "Call with 3 and 5, print the result.\n\n"
        "Expected output: 8"
    ),
    expected_output="8",
    level=Level.EASY,
    hints=["def add(a, b): return a + b", "print(add(3, 5))"]
)

easy2 = Task(
    description=(
        "📛  Full Name Formatter\n\n"
        "Define a function full_name(first, last) that returns 'first last'.\n"
        "Call with 'Emperor' and 'PyPhone', print the result.\n\n"
        "Expected output: Emperor PyPhone"
    ),
    expected_output="Emperor PyPhone",
    level=Level.EASY,
    hints=["def full_name(first, last): return first + ' ' + last", "print(full_name('Emperor', 'PyPhone'))"]
)

medium1 = Task(
    description=(
        "🔑  Keyword Arguments\n\n"
        "Define a function power(base, exp) that returns base ** exp.\n"
        "Call it using keyword arguments: base=2, exp=10. Print result.\n\n"
        "Expected output: 1024"
    ),
    expected_output="1024",
    level=Level.MEDIUM,
    hints=["def power(base, exp): return base ** exp", "print(power(base=2, exp=10))"]
)

medium2 = Task(
    description=(
        "🔄  Mixed Arguments\n\n"
        "Define a function describe_person(name, age, city) that prints\n"
        "'name is age years old and lives in city.'\n"
        "Call it with positional 'Emperor' and keyword age=18, city='Dhaka'.\n\n"
        "Expected output: Emperor is 18 years old and lives in Dhaka."
    ),
    expected_output="Emperor is 18 years old and lives in Dhaka.",
    level=Level.MEDIUM,
    hints=["def describe_person(name, age, city): print(f'{name} is {age} years old and lives in {city}.')", "describe_person('Emperor', age=18, city='Dhaka')"]
)

hard1 = Task(
    description=(
        "🛡️  __name__ == '__main__' Guard\n\n"
        "Write a function main() that prints 'Script executed directly'.\n"
        "Use if __name__ == '__main__': to call main().\n"
        "Ensure the script prints the message.\n\n"
        "Expected output: Script executed directly"
    ),
    expected_output="Script executed directly",
    level=Level.HARD,
    hints=["def main(): print('Script executed directly')", "if __name__ == '__main__': main()"]
)

hard2 = Task(
    description=(
        "🧪  Type Casting in Function\n\n"
        "Define a function safe_int(value) that attempts to convert value to int.\n"
        "If conversion fails, return None. Call with '42' and print the result.\n\n"
        "Expected output: 42"
    ),
    expected_output="42",
    level=Level.HARD,
    hints=["def safe_int(value):", "    try:", "        return int(value)", "    except ValueError:", "        return None", "print(safe_int('42'))"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L25.json")
