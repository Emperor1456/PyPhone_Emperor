# =============================================
#  PyPhone Emperor · Module 4
#  PRACTICE L‑31  –  Return Values
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

print("\n🎯 WELCOME TO L‑31 COACHING")
print("Return values make functions powerful.\n")

# TASK 1
task(
    "Define a function `add` that takes two numbers and returns their sum.",
    lambda: callable(globals().get('add')) and globals()['add'](10, 5) == 15,
    hint="def add(a, b):\n    return a + b"
)

# TASK 2
task(
    "Define a function `safe_divide` that takes a, b and returns a/b if b!=0, else returns None.",
    lambda: callable(globals().get('safe_divide')) and globals()['safe_divide'](10, 0) is None and globals()['safe_divide'](10, 2) == 5,
    hint="def safe_divide(a, b):\n    if b == 0:\n        return None\n    return a / b"
)

# TASK 3
task(
    "Define a function `min_max` that takes a list and returns both the minimum and maximum as a tuple (min, max).",
    lambda: callable(globals().get('min_max')) and globals()['min_max']([4,1,9,3]) == (1,9),
    hint="def min_max(lst):\n    return min(lst), max(lst)"
)

# TASK 4
task(
    "Call `min_max([5,2,8,1])` and unpack the result into variables `low` and `high`.",
    lambda: check_var('low', int, 1) and check_var('high', int, 8),
    hint="low, high = min_max([5,2,8,1])"
)

print("\n" + "="*44)
print("🏆 L‑31 complete – Return")
print("values now fuel your logic.")
print("="*44)