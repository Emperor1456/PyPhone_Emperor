# =============================================
#  PyPhone Emperor · Module 1
#  PRACTICE L‑11  –  Bitwise AND & OR
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

print("\n🎯 WELCOME TO L‑11 COACHING")
print("Bitwise AND & and OR |.\n")

# TASK 1
task(
    "Compute 5 & 3, store in 'and_result' (expect 1).",
    lambda: check_var('and_result', int, 1),
    hint="and_result = 5 & 3"
)

# TASK 2
task(
    "Compute 5 | 3, store in 'or_result' (expect 7).",
    lambda: check_var('or_result', int, 7),
    hint="or_result = 5 | 3"
)

# TASK 3
task(
    "Create permission flags: READ=4, WRITE=2, EXEC=1. Combine READ and EXEC, store in 'perm'.",
    lambda: check_var('perm', int, 5),
    hint="perm = READ | EXEC"
)

print("\n" + "="*44)
print("🏆 L‑11 complete – Bitwise gates open.")
print("="*44)