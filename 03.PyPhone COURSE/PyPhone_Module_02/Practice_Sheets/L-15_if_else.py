# =============================================
#  PyPhone Emperor · Module 2
#  PRACTICE L‑15  –  `if-else`
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

print("\n🎯 WELCOME TO L‑15 COACHING")
print("You'll write `if-else` blocks that")
print("handle both true and false paths.\n")

# TASK 1
task(
    "Set `age = 16`. Write an `if-else` that sets `status` to 'adult' if age >= 18, else 'minor'.",
    lambda: check_var('status', str, 'minor'),
    hint="status = 'adult' if age >= 18 else 'minor'"
)

# TASK 2
task(
    "Start with `balance = 300`, `withdraw = 500`. Use `if-else` to subtract only if enough funds; otherwise set `message` to 'Insufficient'.",
    lambda: check_var('message', str, 'Insufficient'),
    hint="if balance >= withdraw:\n    balance -= withdraw\nelse:\n    message = 'Insufficient'"
)

# TASK 3
task(
    "Define `score = 65`. Write an `if-else` that sets `result` to 'Pass' if score >= 60, else 'Fail'.",
    lambda: check_var('result', str, 'Pass'),
    hint="result = 'Pass' if score >= 60 else 'Fail'"
)

# TASK 4
task(
    "Create `temp = 22` and `is_raining = True`. Write an `if-else` that sets `activity` to 'cinema' if raining or temp < 15, else 'park'.",
    lambda: check_var('activity', str, 'cinema'),
    hint="if is_raining or temp < 15:\n    activity = 'cinema'\nelse:\n    activity = 'park'"
)

print("\n" + "="*44)
print("🏆 L‑15 complete – `if-else`")
print("decisions are now second nature.")
print("="*44)