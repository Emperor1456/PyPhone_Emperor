# =============================================
#  PyPhone Emperor · Module 2
#  PRACTICE L‑22  –  `pass` Statement
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

print("\n🎯 WELCOME TO L‑22 COACHING")
print("Use `pass` as a placeholder for")
print("empty blocks, classes, and stubs.\n")

# TASK 1
task(
    "Define an empty function `stub()` that does nothing, using `pass`. (Define the function in your code.)",
    lambda: callable(globals().get('stub')),
    hint="def stub():\n    pass"
)

# TASK 2
task(
    "Create an empty class `Placeholder` with `pass`.",
    lambda: type(globals().get('Placeholder')) == type,
    hint="class Placeholder:\n    pass"
)

# TASK 3
task(
    "Write an `if` statement with condition `True` and an empty body using `pass`. Then set a variable `check = 'done'` after the `if` block.",
    lambda: check_var('check', str, 'done'),
    hint="if True:\n    pass\ncheck = 'done'"
)

# TASK 4
task(
    "Write a `while` loop with condition `False` and an empty body using `pass`. Then set `loop_check = 'passed'` after the loop.",
    lambda: check_var('loop_check', str, 'passed'),
    hint="while False:\n    pass\nloop_check = 'passed'"
)

print("\n" + "="*44)
print("🏆 L‑22 complete – `pass` is")
print("your silent placeholder tool.")
print("="*44)