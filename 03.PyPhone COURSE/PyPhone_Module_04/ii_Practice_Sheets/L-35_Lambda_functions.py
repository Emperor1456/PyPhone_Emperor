# =============================================
#  PyPhone Emperor · Module 4
#  PRACTICE L‑35  –  Lambda Functions
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

print("\n🎯 WELCOME TO L‑35 COACHING")
print("Anonymous functions in one line.\n")

# TASK 1
task(
    "Assign a lambda to `square` that squares a number. Test: square(5) should be 25.",
    lambda: callable(globals().get('square')) and globals()['square'](5) == 25,
    hint="square = lambda x: x ** 2"
)

# TASK 2
task(
    "Use a lambda inside `map()` to square every number in `nums = [1,2,3,4]`. Store the result in `squared` (convert to list).",
    lambda: check_var('squared', list, [1,4,9,16]),
    hint="nums = [1,2,3,4]\nsquared = list(map(lambda x: x**2, nums))"
)

# TASK 3
task(
    "Use a lambda inside `filter()` to keep only even numbers from `nums = [1,2,3,4,5,6]`. Store in `evens`.",
    lambda: check_var('evens', list, [2,4,6]),
    hint="nums = [1,2,3,4,5,6]\nevens = list(filter(lambda x: x%2==0, nums))"
)

# TASK 4
task(
    "Sort `pairs = [(1,'one'),(3,'three'),(2,'two')]` by the first element using `sorted()` and a lambda key. Store in `sorted_pairs`.",
    lambda: check_var('sorted_pairs', list, [(1,'one'),(2,'two'),(3,'three')]),
    hint="pairs = [(1,'one'),(3,'three'),(2,'two')]\nsorted_pairs = sorted(pairs, key=lambda p: p[0])"
)

print("\n" + "="*44)
print("🏆 L‑35 complete – Lambdas")
print("are your one‑line assistants.")
print("="*44)