# =============================================
#  PyPhone Emperor · Module 2
#  PRACTICE L‑14  –  Basic `if` Statement
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

print("\n🎯 WELCOME TO L‑14 COACHING")
print("You'll write `if` statements that")
print("control the flow of your program.\n")

# TASK 1
task(
    "Set `age = 20`. Then write an `if` that changes `status` to 'adult' when age >= 18.",
    lambda: check_var('status', str, 'adult'),
    hint="status = 'child'\nif age >= 18:\n    status = 'adult'"
)

# TASK 2
task(
    "Start with `balance = 500`, `withdraw = 300`. Write an `if` that subtracts withdraw from balance only if balance >= withdraw.",
    lambda: check_var('balance', int, 200),
    hint="if balance >= withdraw:\n    balance -= withdraw"
)

# TASK 3
task(
    "Define `x = 5`. Write an `if` that sets `y = 10` when x > 10. Then check that y remains unchanged (i.e., y should not exist).",
    lambda: 'y' not in globals(),
    hint="if x > 10:\n    y = 10\n(no else, so y is never created)"
)

# TASK 4
task(
    "Create `temp = 25` and `sunny = True`. Write an `if` with `and` that sets `activity = 'beach'` when temp > 20 and sunny is True.",
    lambda: check_var('activity', str, 'beach'),
    hint="if temp > 20 and sunny:\n    activity = 'beach'"
)

print("\n" + "="*44)
print("🏆 L‑14 complete – `if` statements")
print("are now in your toolbox.")
print("="*44)