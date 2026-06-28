# =============================================
#  PyPhone Emperor · Module 5
#  PRACTICE L‑39  –  Dictionary Methods
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

print("\n🎯 WELCOME TO L‑39 COACHING")
print("Extract keys, values, copy and")
print("set defaults.\n")

# TASK 1
task(
    "Create `user = {'name':'Emperor','age':18}`. Extract keys as a list and store in `keys_list`.",
    lambda: check_var('keys_list', list) and sorted(globals()['keys_list']) == ['age','name'],
    hint="keys_list = list(user.keys())"
)

# TASK 2
task(
    "Extract values as a list and store in `values_list`.",
    lambda: check_var('values_list', list) and sorted(globals()['values_list']) == [18,'Emperor'],
    hint="values_list = list(user.values())"
)

# TASK 3
task(
    "Create a shallow copy of `user` into `copy_user`. Then modify `copy_user` (add key 'test') to prove they are independent.",
    lambda: 'test' in globals().get('copy_user', {}) and 'test' not in globals().get('user', {}),
    hint="copy_user = user.copy()\ncopy_user['test'] = 1"
)

# TASK 4
task(
    "Using `.setdefault()`, ensure the key 'score' exists with default 0. Then store its value in `score`.",
    lambda: check_var('score', int, 0) and globals().get('user', {}).get('score') == 0,
    hint="score = user.setdefault('score', 0)"
)

# TASK 5
task(
    "Clear the `user` dictionary using `.clear()`. It should become an empty dict.",
    lambda: check_var('user', dict, {}),
    hint="user.clear()"
)

print("\n" + "="*44)
print("🏆 L‑39 complete – Dictionary")
print("methods are now your toolkit.")
print("="*44)