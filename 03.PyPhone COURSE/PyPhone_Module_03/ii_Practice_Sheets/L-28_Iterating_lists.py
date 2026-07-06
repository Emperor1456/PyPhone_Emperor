# =============================================
#  PyPhone Emperor · Module 3
#  PRACTICE L‑28  –  Iterating Through Lists
#  Enterprise Coaching Engine
# =============================================
import sys

def safe_exec(code):
    try:
        exec(code, globals())
        return None
    except Exception as e:
        return str(e)

def check_var(name, expected_type, expected_value=None):
    if name not in globals():
        return False
    val = globals()[name]
    if not isinstance(val, expected_type):
        return False
    if expected_value is not None and val != expected_value:
        return False
    return True

def task(instruction, verify_func, hint):
    print("\n" + "-"*44)
    words = instruction.split()
    line = "  📋 "
    for w in words:
        if len(line) + len(w) + 1 > 42:
            print(line)
            line = "      " + w
        else:
            if line == "  📋 ":
                line += w
            else:
                line += " " + w
    print(line)
    print("-"*44)
    while True:
        code = input("  >>> ").strip()
        if code.lower() in ("exit", "quit"):
            print("\n👋 Practice ended.")
            sys.exit(0)
        err = safe_exec(code)
        if err:
            print(f"  ❌ Python error: {err}")
            print(f"  💡 Hint: {hint}")
            continue
        if verify_func():
            print("  ✅ Correct!")
            break
        else:
            print("  ❌ Not yet. Try again.")
            print(f"  💡 Hint: {hint}")

print("\n🎯 WELCOME TO L‑28 COACHING")
print("Loop through lists like a pro.\n")

# TASK 1
task(
    "Create a list `fruits = ['apple','banana','cherry']`. Write a `for` loop that prints each fruit. Then set a variable `done1 = True` after the loop.",
    lambda: check_var('done1', bool, True),
    hint="for fruit in fruits:\n    print(fruit)\ndone1 = True"
)

# TASK 2
task(
    "Given `sales = [150, 89, 320, 45]`, write a `for` loop to sum all values and store the total in `total_sales`.",
    lambda: abs(globals().get('total_sales', 0) - 604) < 0.001,
    hint="total_sales = 0\nfor amount in sales:\n    total_sales += amount"
)

# TASK 3
task(
    "Given `scores = [55, 72, 40, 91, 33]`, write a `for` loop that collects scores >= 50 into a new list `passing`.",
    lambda: check_var('passing', list, [55, 72, 91]),
    hint="passing = []\nfor s in scores:\n    if s >= 50:\n        passing.append(s)"
)

# TASK 4
task(
    "Given `prices = [10, 20, 30]`, increase each price by 10% using a loop with indexes. Store the modified list back in `prices`.",
    lambda: check_var('prices', list, [11.0, 22.0, 33.0]),
    hint="for i in range(len(prices)):\n    prices[i] *= 1.1"
)

# TASK 5
task(
    "Given `tasks = ['design','code','test']`, use `enumerate()` in a loop to create a string `log` where each line is 'idx: task' separated by newline. E.g., '0: design\\n1: code\\n2: test'.",
    lambda: check_var('log', str, '0: design\n1: code\n2: test'),
    hint="log = ''\nfor idx, t in enumerate(tasks):\n    log += f'{idx}: {t}\\n'\nlog = log.rstrip('\\n')"
)

print("\n" + "="*44)
print("🏆 L‑28 complete – List iteration")
print("is now your daily bread.")
print("="*44)