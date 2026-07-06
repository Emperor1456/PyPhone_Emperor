# =============================================
#  PyPhone Emperor · Module 6
#  PRACTICE L‑50  –  `finally` & `else`
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

print("\n🎯 WELCOME TO L‑50 COACHING")
print("`else` and `finally` complete")
print("your error‑handling toolkit.\n")

# TASK 1
task(
    "Write try/except/else: try to do `x = 5`, except ValueError (won't happen), else set `success = True`.",
    lambda: check_var('success', bool, True),
    hint="try:\n    x = 5\nexcept ValueError:\n    pass\nelse:\n    success = True"
)

# TASK 2
task(
    "Write try/finally that sets `clean = True` in finally, regardless of a division error. First, set `clean = False`, then after try/finally, ensure `clean` is True.",
    lambda: check_var('clean', bool, True),
    hint="clean = False\ntry:\n    1/0\nexcept:\n    pass\nfinally:\n    clean = True"
)

# TASK 3
task(
    "Combine all: try to get a key from dict `d = {'a':1}` using key 'b'. Catch KeyError, set `status='key error'`. Else set `status='found'`. Finally set `done = True`. After running, `done` should be True and `status` should be 'key error'.",
    lambda: check_var('done', bool, True) and check_var('status', str, 'key error'),
    hint="d = {'a':1}\ndone = False\ntry:\n    val = d['b']\nexcept KeyError:\n    status = 'key error'\nelse:\n    status = 'found'\nfinally:\n    done = True"
)

print("\n" + "="*44)
print("🏆 L‑50 complete – `finally`")
print("and `else` seal the deal.")
print("="*44)