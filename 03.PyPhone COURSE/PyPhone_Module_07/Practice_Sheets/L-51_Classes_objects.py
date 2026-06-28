# =============================================
#  PyPhone Emperor · Module 7
#  PRACTICE L‑51  –  Classes & Objects
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

print("\n🎯 WELCOME TO L‑51 COACHING")
print("Create your first classes and objects.\n")

# TASK 1
task(
    "Define an empty class `User` with `pass`.",
    lambda: type(globals().get('User')) == type,
    hint="class User:\n    pass"
)

# TASK 2
task(
    "Create an instance of `User` and store it in `u1`.",
    lambda: check_var('u1', object),
    hint="u1 = User()"
)

# TASK 3
task(
    "Add an attribute `name` to `u1` with value 'Emperor'.",
    lambda: hasattr(globals().get('u1'), 'name') and globals()['u1'].name == 'Emperor',
    hint="u1.name = 'Emperor'"
)

# TASK 4
task(
    "Create another instance `u2` of `User` and set its `name` to 'Guest'.",
    lambda: hasattr(globals().get('u2'), 'name') and globals()['u2'].name == 'Guest',
    hint="u2 = User()\nu2.name = 'Guest'"
)

print("\n" + "="*44)
print("🏆 L‑51 complete – Classes and")
print("objects are now your blueprints.")
print("="*44)