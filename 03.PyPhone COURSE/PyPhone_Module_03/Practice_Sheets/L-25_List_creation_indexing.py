# =============================================
#  PyPhone Emperor · Module 3
#  PRACTICE L‑25  –  List Creation & Indexing
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

print("\n🎯 WELCOME TO L‑25 COACHING")
print("Create lists, access elements,")
print("and modify them by index.\n")

# TASK 1
task(
    "Create a list `colors` with three items: 'red', 'green', 'blue'. Then store the second item in `second`.",
    lambda: check_var('second', str, 'green'),
    hint="colors = ['red', 'green', 'blue']\nsecond = colors[1]"
)

# TASK 2
task(
    "Using the same `colors` list, change the last element to 'yellow' using indexing. Then store the last element in `last`.",
    lambda: check_var('last', str, 'yellow'),
    hint="colors[-1] = 'yellow'\nlast = colors[-1]"
)

# TASK 3
task(
    "Create a nested list `matrix = [[1,2],[3,4],[5,6]]`. Extract the number 4 using indexing and store in `num`.",
    lambda: check_var('num', int, 4),
    hint="num = matrix[1][1]"
)

# TASK 4
task(
    "Create `nums = [0,1,2,3,4,5]`. Slice to get [2,3,4] and store in `sub`.",
    lambda: check_var('sub', list, [2,3,4]),
    hint="sub = nums[2:5]"
)

# TASK 5
task(
    "Using slicing with a step, get every other element from `nums` (0,2,4) and store in `every_other`.",
    lambda: check_var('every_other', list, [0,2,4]),
    hint="every_other = nums[::2]"
)

print("\n" + "="*44)
print("🏆 L‑25 complete – List creation")
print("and indexing are yours.")
print("="*44)