# =============================================
#  PyPhone Emperor · Module 2
#  PRACTICE L‑18  –  `match-case`
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

print("\n🎯 WELCOME TO L‑18 COACHING")
print("Use `match-case` to branch on")
print("values and patterns.\n")

# TASK 1
task(
    "Given `cmd = 'stop'`, use `match` to set `action` to 'Engine stopped' for 'stop', 'Engine started' for 'start', else 'Unknown'.",
    lambda: check_var('action', str, 'Engine stopped'),
    hint="match cmd:\n    case 'start': action = 'Engine started'\n    case 'stop': action = 'Engine stopped'\n    case _: action = 'Unknown'"
)

# TASK 2
task(
    "Given `point = (0, 5)`, use `match` to set `where` to 'Origin' for (0,0), 'Y-axis' for (0, y), 'X-axis' for (x, 0), else 'Quadrant'.",
    lambda: check_var('where', str, 'Y-axis'),
    hint="match point:\n    case (0,0): where = 'Origin'\n    case (0, y): where = 'Y-axis'\n    case (x, 0): where = 'X-axis'\n    case _: where = 'Quadrant'"
)

# TASK 3
task(
    "Given `value = -5`, use `match` with guard to set `sign` to 'Negative' if x<0, 'Zero' if x==0, 'Positive' if x>0.",
    lambda: check_var('sign', str, 'Negative'),
    hint="match value:\n    case x if x < 0: sign = 'Negative'\n    case x if x == 0: sign = 'Zero'\n    case x if x > 0: sign = 'Positive'"
)

print("\n" + "="*44)
print("🏆 L‑18 complete – `match-case`")
print("is your new branching tool.")
print("="*44)