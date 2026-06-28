# =============================================
#  PyPhone Emperor · Module 6
#  PRACTICE L‑48  –  Introduction to Exceptions
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

print("\n🎯 WELCOME TO L‑48 COACHING")
print("Catch errors before they crash")
print("your program.\n")

# TASK 1
task(
    "Write a try/except that attempts `int('abc')` and catches ValueError. Store the string 'conversion failed' in a variable `msg` inside the except block.",
    lambda: check_var('msg', str, 'conversion failed'),
    hint="try:\n    int('abc')\nexcept ValueError:\n    msg = 'conversion failed'"
)

# TASK 2
task(
    "Write a try/except that divides 10 by 0 and catches ZeroDivisionError. Inside except, store 'division error' in `err_msg`.",
    lambda: check_var('err_msg', str, 'division error'),
    hint="try:\n    10/0\nexcept ZeroDivisionError:\n    err_msg = 'division error'"
)

# TASK 3
task(
    "Write a try/except that attempts to open a nonexistent file. Catch FileNotFoundError and set `status = 'missing'`.",
    lambda: check_var('status', str, 'missing'),
    hint="try:\n    open('nonexistent_file.txt')\nexcept FileNotFoundError:\n    status = 'missing'"
)

# TASK 4
task(
    "Write a try/except that catches any Exception. Inside try, evaluate `undefined_variable`. Set `result = 'caught'` in the except block using `except Exception as e:`.",
    lambda: check_var('result', str, 'caught'),
    hint="try:\n    undefined_variable\nexcept Exception as e:\n    result = 'caught'"
)

print("\n" + "="*44)
print("🏆 L‑48 complete – Exceptions")
print("are now handled, not feared.")
print("="*44)