import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🎁  Simple Decorator\n\n"
        "Define a decorator `bold` that wraps the return value of a function in `<b>..</b>`.\n"
        "Apply it to a function `say()` returning 'Hi'. Print the result of calling `say()`.\n\n"
        "Expected output: <b>Hi</b>"
    ),
    expected_output="<b>Hi</b>",
    level=Level.EASY,
    hints=["def bold(func):", "    def wrapper(): return f'<b>{func()}</b>'", "    return wrapper", "@bold", "def say(): return 'Hi'", "print(say())"]
)

easy2 = Task(
    description=(
        "🔠  Uppercase Decorator\n\n"
        "Define a decorator `uppercase` that converts the string return value to uppercase.\n"
        "Apply to a function `greet()` returning 'hello'. Print the result.\n\n"
        "Expected output: HELLO"
    ),
    expected_output="HELLO",
    level=Level.EASY,
    hints=["def uppercase(func):", "    def wrapper(): return func().upper()", "    return wrapper", "@uppercase", "def greet(): return 'hello'", "print(greet())"]
)

medium1 = Task(
    description=(
        "📊  Logging Decorator\n\n"
        "Define a decorator `log` that prints 'Calling (name)' before calling the function,\n"
        "and '(name) returned (result)' after. Apply to add(3,5). Print the final returned value.\n"
        "Output will have three lines; the engine expects only the final print: 8.\n\n"
        "Expected output: 8"
    ),
    expected_output="8",
    level=Level.MEDIUM,
    hints=["def log(func):", "    def wrapper(*args, **kwargs):", "        print(f'Calling {func.__name__}')", "        result = func(*args, **kwargs)", "        print(f'{func.__name__} returned {result}')", "        return result", "    return wrapper", "@log", "def add(a, b): return a+b", "print(add(3,5))"]
)

medium2 = Task(
    description=(
        "🔁  Stacking Decorators\n\n"
        "Stack both `bold` and `uppercase` decorators on a function `message()` returning 'hi'.\n"
        "The bold should be applied first (outermost). Print result.\n\n"
        "Expected output: <b>HI</b>"
    ),
    expected_output="<b>HI</b>",
    level=Level.MEDIUM,
    hints=["def bold(func):", "    def wrapper(): return f'<b>{func()}</b>'", "    return wrapper", "def uppercase(func):", "    def wrapper(): return func().upper()", "    return wrapper", "@bold", "@uppercase", "def message(): return 'hi'", "print(message())"]
)

hard1 = Task(
    description=(
        "⏱️  Timer Decorator\n\n"
        "Define a decorator `timer` that measures and prints the execution time of a function.\n"
        "Print 'Fast' after calling the decorated function (the timing line is ignored by engine).\n"
        "Apply to a function `compute()` that returns 42. Print the result, then print 'Fast'.\n\n"
        "Expected output:\n42\nFast"
    ),
    expected_output="42\nFast",
    level=Level.HARD,
    hints=["import time", "def timer(func):", "    def wrapper():", "        start = time.time()", "        result = func()", "        end = time.time()", "        print(f'Took {end-start:.4f}s')", "        return result", "    return wrapper", "@timer", "def compute(): return 42", "print(compute())", "print('Fast')"]
)

hard2 = Task(
    description=(
        "🛡️  Retry Decorator\n\n"
        "Define a decorator `retry(max_attempts=3)` that retries a function on exception.\n"
        "Create a function `unstable()` that raises ValueError the first two calls, then returns 'OK' on third.\n"
        "Apply @retry(3) and print the result.\n\n"
        "Expected output: OK"
    ),
    expected_output="OK",
    level=Level.HARD,
    hints=[
        "def retry(max_attempts):",
        "    def decorator(func):",
        "        def wrapper():",
        "            attempts = 0",
        "            while attempts < max_attempts:",
        "                try:",
        "                    return func()",
        "                except:",
        "                    attempts += 1",
        "            return func()",
        "        return wrapper",
        "    return decorator",
        "counter = [0]",
        "@retry(3)",
        "def unstable():",
        "    counter[0] += 1",
        "    if counter[0] < 3: raise ValueError('fail')",
        "    return 'OK'",
        "print(unstable())"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L55.json")
