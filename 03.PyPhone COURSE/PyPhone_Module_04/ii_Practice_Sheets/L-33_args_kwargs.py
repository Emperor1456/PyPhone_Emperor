import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Define `sum_all(*args)` returning sum(args). Call with 1,2,3,4 and print.",
    expected_output="10",
    level=Level.EASY,
    hints=["def sum_all(*args): return sum(args)", "print(sum_all(1,2,3,4))"]
)

medium = Task(
    description="Define `print_info(**kwargs)` returning a string like 'name: Emperor, age: 18'. Call with name='Emperor', age=18 and print.",
    expected_output="name: Emperor, age: 18",
    level=Level.MEDIUM,
    hints=["def print_info(**kwargs):\n    parts=[]\n    for k,v in kwargs.items():\n        parts.append(f'{k}: {v}')\n    return ', '.join(parts)", "print(print_info(name='Emperor', age=18))"]
)

hard = Task(
    description="Define `mixed(*args, **kwargs)` returning sum(args) if no kwargs, else str(kwargs). Call with 1,2,3 (should print 6) and with name='Emperor' (should print {'name':'Emperor'}).",
    expected_output="6\n{'name': 'Emperor'}",
    level=Level.HARD,
    hints=["def mixed(*args, **kwargs):\n    if not kwargs:\n        return sum(args)\n    else:\n        return str(kwargs)", "print(mixed(1,2,3))", "print(mixed(name='Emperor'))"]
)

def main(): c=input("1 Easy 2 Medium 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
