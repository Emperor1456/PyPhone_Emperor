# =============================================
#  PyPhone Emperor · Module 5
#  PRACTICE L‑42  –  Sets
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
        try:
            if verify_func():
                print("  ✅ Correct!")
                break
            else:
                print("  ❌ Not yet. Try again.")
                print(f"  💡 Hint: {hint}")
        except Exception as e:
            print(f"  ❌ Check failed: {e}")
            print(f"  💡 Hint: {hint}")

print("\n🎯 WELCOME TO L‑42 COACHING")
print("Create sets and manipulate unique elements.\n")

# TASK 1
task(
    "Create a set `fruits` containing 'apple', 'banana', 'cherry'.",
    lambda: check_var('fruits', set, {'apple','banana','cherry'}),
    hint="fruits = {'apple', 'banana', 'cherry'}"
)

# TASK 2
task(
    "Create a list `nums = [1,2,2,3,3,3]`. Convert it to a set `unique_nums` to remove duplicates.",
    lambda: check_var('unique_nums', set, {1,2,3}),
    hint="unique_nums = set(nums)"
)

# TASK 3
task(
    "Add 'date' to the `fruits` set, then add 'elderberry' and 'fig' with one call.",
    lambda: check_var('fruits', set, {'apple','banana','cherry','date','elderberry','fig'}),
    hint="fruits.add('date')\nfruits.update(['elderberry', 'fig'])"
)

# TASK 4
task(
    "Remove 'banana' using `.remove()`. Then safely discard 'kiwi' (which doesn't exist).",
    lambda: 'banana' not in globals().get('fruits', set()) and 'kiwi' not in globals().get('fruits', set()),
    hint="fruits.remove('banana')\nfruits.discard('kiwi')"
)

# TASK 5
task(
    "Check if 'apple' is in `fruits` and store the boolean result in `has_apple`.",
    lambda: check_var('has_apple', bool, True),
    hint="has_apple = 'apple' in fruits"
)

print("\n" + "="*44)
print("🏆 L‑42 complete – Sets")
print("keep your data unique.")
print("="*44)