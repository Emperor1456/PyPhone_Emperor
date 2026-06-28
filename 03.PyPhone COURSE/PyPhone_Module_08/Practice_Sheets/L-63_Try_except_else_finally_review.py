# =============================================
#  PyPhone Emperor · Module 8
#  PRACTICE L‑63  –  try-except-else-finally Review
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

print("\n🎯 WELCOME TO L‑63 COACHING")
print("Full exception structure mastery.\n")

# TASK 1
task(
    "Write try/except/else: try to do `x = 5`, except ValueError, else set `success = 'yes'`. Since no error occurs, success should be 'yes'.",
    lambda: check_var('success', str, 'yes'),
    hint="try:\n    x = 5\nexcept ValueError:\n    pass\nelse:\n    success = 'yes'"
)

# TASK 2
task(
    "Write try/finally: set `cleanup_done = False`. In try, raise ValueError. In except, set `error_seen = True`. In finally, set `cleanup_done = True`. Both should be True after execution.",
    lambda: check_var('error_seen', bool, True) and check_var('cleanup_done', bool, True),
    hint="cleanup_done = False\ntry:\n    raise ValueError()\nexcept ValueError:\n    error_seen = True\nfinally:\n    cleanup_done = True"
)

# TASK 3
task(
    "Show the danger of return in finally. Write a function `danger()` that tries to `return 'from try'`, but has `finally` that `return 'from finally'`. Call it and store result in `danger_result`.",
    lambda: check_var('danger_result', str, 'from finally'),
    hint="def danger():\n    try:\n        return 'from try'\n    finally:\n        return 'from finally'\n\ndanger_result = danger()"
)

# TASK 4
task(
    "Write a complete try/except/else/finally for a safe division. Try `10/2`, catch ZeroDivisionError and set `div_error = True`, else set `div_ok = True`, finally set `div_done = True`. Here div_ok should be True, div_error False, div_done True.",
    lambda: check_var('div_ok', bool, True) and check_var('div_error', bool, False) and check_var('div_done', bool, True),
    hint="div_error = False\ndiv_ok = False\ndiv_done = False\ntry:\n    10/2\nexcept ZeroDivisionError:\n    div_error = True\nelse:\n    div_ok = True\nfinally:\n    div_done = True"
)

print("\n" + "="*44)
print("🏆 L‑63 complete – Full exception")
print("structure now crystal clear.")
print("="*44)