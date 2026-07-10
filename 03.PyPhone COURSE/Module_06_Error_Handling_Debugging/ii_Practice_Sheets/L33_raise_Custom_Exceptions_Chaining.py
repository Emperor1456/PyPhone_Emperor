import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "📢  Raise ValueError\n\n"
        "Write a function set_age(age) that raises ValueError if age < 0.\n"
        "Call it with -5 inside try/except and print 'Invalid age'.\n\n"
        "Expected output: Invalid age"
    ),
    expected_output="Invalid age",
    level=Level.EASY,
    hints=[
        "def set_age(age):",
        "    if age < 0: raise ValueError('Invalid age')",
        "try:",
        "    set_age(-5)",
        "except ValueError:",
        "    print('Invalid age')"
    ]
)

easy2 = Task(
    description=(
        "🏷️  Custom Exception Class\n\n"
        "Define a custom exception class named 'NegativeBalanceError(Exception)'.\n"
        "Do not raise it, just print the class name via print(NegativeBalanceError.__name__).\n\n"
        "Expected output: NegativeBalanceError"
    ),
    expected_output="NegativeBalanceError",
    level=Level.EASY,
    hints=[
        "class NegativeBalanceError(Exception): pass",
        "print(NegativeBalanceError.__name__)"
    ]
)

medium1 = Task(
    description=(
        "⚡  Raise Custom Exception\n\n"
        "Define InsufficientFundsError(Exception). Write a function withdraw(balance, amount)\n"
        "that raises InsufficientFundsError if amount > balance. Call with (100, 200) inside\n"
        "try/except and print 'Not enough money'.\n\n"
        "Expected output: Not enough money"
    ),
    expected_output="Not enough money",
    level=Level.MEDIUM,
    hints=[
        "class InsufficientFundsError(Exception): pass",
        "def withdraw(balance, amount):",
        "    if amount > balance: raise InsufficientFundsError('Not enough money')",
        "try:",
        "    withdraw(100, 200)",
        "except InsufficientFundsError:",
        "    print('Not enough money')"
    ]
)

medium2 = Task(
    description=(
        "⛓️  Exception Chaining\n\n"
        "Write a function that raises ValueError, catch it and raise RuntimeError from it.\n"
        "Print 'Chained' after catching RuntimeError.\n"
        "Simplified: just demonstrate the pattern and print 'Chained'.\n\n"
        "Expected output: Chained"
    ),
    expected_output="Chained",
    level=Level.MEDIUM,
    hints=[
        "try:",
        "    raise ValueError('original')",
        "except ValueError as e:",
        "    try:",
        "        raise RuntimeError('wrapped') from e",
        "    except RuntimeError:",
        "        print('Chained')"
    ]
)

hard1 = Task(
    description=(
        "🧼  Validation with Custom Exception\n\n"
        "Define InvalidEmailError(Exception). Write a function validate_email(email) that raises\n"
        "InvalidEmailError if '@' not in email. Call with 'invalid' and print 'Bad email' on catch.\n\n"
        "Expected output: Bad email"
    ),
    expected_output="Bad email",
    level=Level.HARD,
    hints=[
        "class InvalidEmailError(Exception): pass",
        "def validate_email(email):",
        "    if '@' not in email: raise InvalidEmailError('Bad email')",
        "try:",
        "    validate_email('invalid')",
        "except InvalidEmailError:",
        "    print('Bad email')"
    ]
)

hard2 = Task(
    description=(
        "🔁  Re-raise with Context\n\n"
        "Catch a ValueError, log it (print 'Logged'), then re-raise the same exception.\n"
        "Catch it again and print 'Handled'.\n\n"
        "Expected output:\nLogged\nHandled"
    ),
    expected_output="Logged\nHandled",
    level=Level.HARD,
    hints=[
        "try:",
        "    try:",
        "        raise ValueError('oops')",
        "    except ValueError:",
        "        print('Logged')",
        "        raise",
        "except ValueError:",
        "    print('Handled')"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L33.json")
