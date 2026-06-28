# =============================================
#  PyPhone Emperor · Module 1
#  PRACTICE L‑07  –  Comparison Operators
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

print("\n🎯 WELCOME TO L‑07 COACHING")
print("Six comparison operators – True/False.\n")

# TASK 1
task(
    "Check if 42 is equal to 42, store result in 'eq'.",
    lambda: check_var('eq', bool, True),
    hint="eq = (42 == 42)"
)

# TASK 2
task(
    "Check if 'apple' is less than 'banana', store in 'less'.",
    lambda: check_var('less', bool, True),
    hint="less = ('apple' < 'banana')"
)

# TASK 3
task(
    "Check if 10 is NOT equal to 5, store in 'neq'.",
    lambda: check_var('neq', bool, True),
    hint="neq = (10 != 5)"
)

# TASK 4
task(
    "Using chained comparison, check if 15 is between 10 and 20, store in 'mid'.",
    lambda: check_var('mid', bool, True),
    hint="mid = (10 < 15 < 20)"
)

print("\n" + "="*44)
print("🏆 L‑07 complete – Comparisons sharp.")
print("="*44)