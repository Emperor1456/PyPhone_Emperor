# =============================================
#  PyPhone Emperor · Module 1
#  PRACTICE L‑04  –  Comments & Escape Sequences
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

print("\n🎯 WELCOME TO L‑04 COACHING")
print("Master comments and escape sequences.\n")

# TASK 1
task(
    "Write a single‑line comment that says 'This is a comment'.",
    lambda: True,   # We cannot execute a comment, accept any safe line
    hint="Type: # This is a comment"
)

# TASK 2
task(
    "Create a string variable 'msg' containing a newline: 'Hello\\nWorld'.",
    lambda: check_var('msg', str) and '\n' in globals()['msg'],
    hint="msg = 'Hello\\nWorld'"
)

# TASK 3
task(
    "Create a string 'path' with a tab between 'User' and 'Admin': 'User\\tAdmin'.",
    lambda: check_var('path', str) and '\t' in globals()['path'],
    hint="path = 'User\\tAdmin'"
)

# TASK 4
task(
    "Create a string 'backslash' that holds a single backslash: '\\'.",
    lambda: check_var('backslash', str) and '\\' in globals()['backslash'],
    hint="backslash = '\\\\'"
)

print("\n" + "="*44)
print("🏆 L‑04 complete – Comments & escapes locked.")
print("="*44)