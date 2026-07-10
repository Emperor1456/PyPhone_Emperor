import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🔄  Recursive Factorial\n\n"
        "Define factorial(n) recursively. Base: n<=1 returns 1. Recursive: n * factorial(n-1).\n"
        "Call with 4 and print.\n\n"
        "Expected output: 24"
    ),
    expected_output="24",
    level=Level.EASY,
    hints=["def factorial(n):", "    if n <= 1: return 1", "    return n * factorial(n - 1)", "print(factorial(4))"]
)

easy2 = Task(
    description=(
        "🔢  Recursive Sum of List\n\n"
        "Define sum_list(lst) returning 0 if empty, else lst[0] + sum_list(lst[1:]).\n"
        "Call with [1,2,3] and print.\n\n"
        "Expected output: 6"
    ),
    expected_output="6",
    level=Level.EASY,
    hints=["def sum_list(lst):", "    if not lst: return 0", "    return lst[0] + sum_list(lst[1:])", "print(sum_list([1,2,3]))"]
)

medium1 = Task(
    description=(
        "🐇  Fibonacci Recursive\n\n"
        "Define fib(n) returning n if n<=1 else fib(n-1)+fib(n-2).\n"
        "Call with 5 and print.\n\n"
        "Expected output: 5"
    ),
    expected_output="5",
    level=Level.MEDIUM,
    hints=["def fib(n):", "    if n <= 1: return n", "    return fib(n-1) + fib(n-2)", "print(fib(5))"]
)

medium2 = Task(
    description=(
        "📉  Countdown Recursive\n\n"
        "Define countdown(n) returning [] if n<=0 else [n] + countdown(n-1).\n"
        "Call with 5 and print.\n\n"
        "Expected output: [5, 4, 3, 2, 1]"
    ),
    expected_output="[5, 4, 3, 2, 1]",
    level=Level.MEDIUM,
    hints=["def countdown(n):", "    if n <= 0: return []", "    return [n] + countdown(n-1)", "print(countdown(5))"]
)

hard1 = Task(
    description=(
        "🧠  Memoized Fibonacci\n\n"
        "Import lru_cache from functools. Decorate a recursive fib function with @lru_cache(maxsize=None).\n"
        "Call fib(10) and print.\n\n"
        "Expected output: 55"
    ),
    expected_output="55",
    level=Level.HARD,
    hints=["from functools import lru_cache", "@lru_cache(maxsize=None)", "def fib(n):", "    if n <= 1: return n", "    return fib(n-1) + fib(n-2)", "print(fib(10))"]
)

hard2 = Task(
    description=(
        "🏗️  Recursive Power\n\n"
        "Define power(base, exp) returning 1 if exp==0 else base * power(base, exp-1).\n"
        "Call with 2,5 and print.\n\n"
        "Expected output: 32"
    ),
    expected_output="32",
    level=Level.HARD,
    hints=["def power(base, exp):", "    if exp == 0: return 1", "    return base * power(base, exp-1)", "print(power(2, 5))"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L31.json")
