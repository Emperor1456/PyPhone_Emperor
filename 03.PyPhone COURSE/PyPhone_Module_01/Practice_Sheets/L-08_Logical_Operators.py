# =============================================
#  PyPhone Emperor · Module 1
#  PRACTICE L‑08  –  Logical Operators
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

print("\n🎯 WELCOME TO L‑08 COACHING")
print("Combine conditions with and, or, not.\n")

# TASK 1
task(
    "Use 'and' to check if (10 > 5) AND (5 > 2), store in 'a'.",
    lambda: check_var('a', bool, True),
    hint="a = (10 > 5) and (5 > 2)"
)

# TASK 2
task(
    "Use 'or' to check if (10 < 5) OR (5 > 2), store in 'b'.",
    lambda: check_var('b', bool, True),
    hint="b = (10 < 5) or (5 > 2)"
)

# TASK 3
task(
    "Use 'not' to reverse the result of (10 == 10), store in 'c'.",
    lambda: check_var('c', bool, False),
    hint="c = not (10 == 10)"
)

# TASK 4
task(
    "Create a variable 'can_drive' that is True if age >= 18 AND has_license is True.",
    lambda: check_var('can_drive', bool, False),
    hint="Define age=16, has_license=True, then can_drive = (age>=18) and has_license"
)

print("\n" + "="*44)
print("🏆 L‑08 complete – Logic gates opened.")
print("="*44)