# =============================================
#  PyPhone Emperor · Module 3
#  PRACTICE L‑27  –  List Slicing & Comprehensions
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

print("\n🎯 WELCOME TO L‑27 COACHING")
print("Advanced slicing and list")
print("comprehensions.\n")

# TASK 1
task(
    "Create `nums = [0,1,2,3,4]`. Replace indices 1 to 3 (exclusive of 4) with [10,20] using slice assignment. Then store the modified list in `modified`.",
    lambda: check_var('modified', list, [0,10,20,4]),
    hint="nums[1:4] = [10,20]\nmodified = nums"
)

# TASK 2
task(
    "Insert 100 at index 2 using an empty slice. Start with `nums = [0,10,20,4]` (from previous). Then set `inserted` to the resulting list.",
    lambda: check_var('inserted', list, [0,10,100,20,4]),
    hint="nums[2:2] = [100]\ninserted = nums"
)

# TASK 3
task(
    "Delete elements at indices 1 and 2 using slice assignment to empty list. Start with `nums = [0,10,100,20,4]`. Store result in `deleted`.",
    lambda: check_var('deleted', list, [0,20,4]),
    hint="nums[1:3] = []\ndeleted = nums"
)

# TASK 4
task(
    "Create a list comprehension that produces squares of numbers 0-9 (0,1,4,...,81) and store in `squares`.",
    lambda: check_var('squares', list, [x**2 for x in range(10)]),
    hint="squares = [x**2 for x in range(10)]"
)

# TASK 5
task(
    "Create a list comprehension that extracts even numbers from 0-19, storing in `evens`.",
    lambda: check_var('evens', list, [x for x in range(20) if x % 2 == 0]),
    hint="evens = [x for x in range(20) if x % 2 == 0]"
)

# TASK 6
task(
    "Given `words = ['hello', 'world']`, use a list comprehension to make a list of their uppercase versions, store in `upper_words`.",
    lambda: check_var('upper_words', list, ['HELLO', 'WORLD']),
    hint="upper_words = [w.upper() for w in words]"
)

print("\n" + "="*44)
print("🏆 L‑27 complete – Slicing and")
print("comprehensions mastered.")
print("="*44)