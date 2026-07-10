import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "⭐  Sum All – *args\n\n"
        "Define sum_all(*args) returning sum(args). Call with 1,2,3,4 and print.\n\n"
        "Expected output: 10"
    ),
    expected_output="10",
    level=Level.EASY,
    hints=["def sum_all(*args): return sum(args)", "print(sum_all(1,2,3,4))"]
)

easy2 = Task(
    description=(
        "📋  Print Info – **kwargs\n\n"
        "Define print_info(**kwargs) that returns a string of 'key: value' pairs\n"
        "joined by comma and space. Call with name='Emperor', age=18, print result.\n\n"
        "Expected output: name: Emperor, age: 18"
    ),
    expected_output="name: Emperor, age: 18",
    level=Level.EASY,
    hints=["def print_info(**kwargs):", "    return ', '.join(f'{k}: {v}' for k,v in kwargs.items())", "print(print_info(name='Emperor', age=18))"]
)

medium1 = Task(
    description=(
        "🔀  Mixed *args and **kwargs\n\n"
        "Define mixed(*args, **kwargs) returning sum(args) if not kwargs,\n"
        "else str(kwargs). Call with 1,2,3 and print.\n\n"
        "Expected output: 6"
    ),
    expected_output="6",
    level=Level.MEDIUM,
    hints=["def mixed(*args, **kwargs):", "    if not kwargs: return sum(args)", "    return str(kwargs)", "print(mixed(1,2,3))"]
)

medium2 = Task(
    description=(
        "📦  Unpacking List into Function\n\n"
        "Define add(a,b,c) returning a+b+c. Call with unpacked [1,2,3].\n\n"
        "Expected output: 6"
    ),
    expected_output="6",
    level=Level.MEDIUM,
    hints=["def add(a,b,c): return a+b+c", "nums = [1,2,3]", "print(add(*nums))"]
)

hard1 = Task(
    description=(
        "🧱  Kwargs as Dict\n\n"
        "Using the mixed function from Medium1, call with name='Emperor' and print.\n\n"
        "Expected output: {'name': 'Emperor'}"
    ),
    expected_output="{'name': 'Emperor'}",
    level=Level.HARD,
    hints=["print(mixed(name='Emperor'))"]
)

hard2 = Task(
    description=(
        "🔁  Combine Unpacking\n\n"
        "Define a function that prints three values. Accept a list and a dict, then\n"
        "call function with unpacked list and dict values. Print them.\n"
        "Use def show(a, b, c): print(a, b, c).\n"
        "nums=[1,2]; kwargs={'c':3}. Use *nums, **kwargs.\n\n"
        "Expected output: 1 2 3"
    ),
    expected_output="1 2 3",
    level=Level.HARD,
    hints=["def show(a,b,c): print(a, b, c)", "nums = [1,2]", "kwargs = {'c': 3}", "show(*nums, **kwargs)"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L28.json")
