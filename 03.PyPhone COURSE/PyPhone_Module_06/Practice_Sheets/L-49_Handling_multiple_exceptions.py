# =============================================
#  PyPhone Emperor · Module 6
#  PRACTICE L‑49  –  Handling Multiple Exceptions
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

print("\n🎯 WELCOME TO L‑49 COACHING")
print("Handle different errors with")
print("multiple except blocks.\n")

# TASK 1
task(
    "Write a try/except that converts input to int and divides 100 by it. Catch ValueError (set `out='bad input'`) and ZeroDivisionError (set `out='div zero'`).",
    lambda: check_var('out', str),
    hint="try:\n    n = int(input('Number: '))\n    r = 100 / n\nexcept ValueError:\n    out = 'bad input'\nexcept ZeroDivisionError:\n    out = 'div zero'"
)

# TASK 2
task(
    "Now write the same try/except but use a tuple to catch both exceptions in one block. Set `msg = 'error'` in the combined except.",
    lambda: check_var('msg', str, 'error'),
    hint="try:\n    n = int(input('Number: '))\n    r = 100 / n\nexcept (ValueError, ZeroDivisionError):\n    msg = 'error'"
)

# TASK 3
task(
    "Write a try that accesses a missing key in a dict `data = {'a':1}`. Catch KeyError (set `val='missing'`) and also catch a general Exception (set `val='other'`).",
    lambda: check_var('val', str, 'missing'),
    hint="data = {'a':1}\ntry:\n    x = data['b']\nexcept KeyError:\n    val = 'missing'\nexcept Exception:\n    val = 'other'"
)

# TASK 4
task(
    "Order matters: Write a try/except where the first except is `Exception` and the second is `ValueError`. The try should raise a ValueError. This will cause a mistake – after running, set `lesson = 'specific first'` to show you understand the ordering rule.",
    lambda: check_var('lesson', str, 'specific first'),
    hint="lesson = 'specific first'   # just acknowledge the rule"
)

print("\n" + "="*44)
print("🏆 L‑49 complete – Multiple")
print("exceptions, precise handling.")
print("="*44)