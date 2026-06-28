# =============================================
#  PyPhone Emperor · Module 8
#  PRACTICE L‑65  –  Virtual Environments in Termux
#  Enterprise Coaching Engine
# =============================================
import sys, os, subprocess

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

print("\n🎯 WELCOME TO L‑65 COACHING")
print("Create and use virtual environments.\n")
print("(This practice simulates commands;")
print("you'll run the real ones in Termux.)\n")

# TASK 1
task(
    "Write the bash command (as a string) to create a virtual environment named '.venv' in the current folder. Store it in `create_cmd`.",
    lambda: check_var('create_cmd', str) and 'venv' in globals()['create_cmd'] and '.venv' in globals()['create_cmd'],
    hint="create_cmd = 'python -m venv .venv'"
)

# TASK 2
task(
    "Write the bash command to activate the virtual environment (on Linux/Termux). Store in `activate_cmd`.",
    lambda: check_var('activate_cmd', str) and 'source' in globals()['activate_cmd'] and 'activate' in globals()['activate_cmd'],
    hint="activate_cmd = 'source .venv/bin/activate'"
)

# TASK 3
task(
    "Write the bash command to deactivate the virtual environment. Store in `deactivate_cmd`.",
    lambda: check_var('deactivate_cmd', str) and 'deactivate' in globals()['deactivate_cmd'],
    hint="deactivate_cmd = 'deactivate'"
)

# TASK 4
task(
    "Why is a virtual environment important? Write a one‑sentence string in `reason` about isolation or dependency conflicts.",
    lambda: check_var('reason', str) and len(globals()['reason']) > 20,
    hint="reason = 'It isolates dependencies per project to avoid conflicts.'"
)

print("\n" + "="*44)
print("🏆 L‑65 complete – Virtual environments")
print("keep your projects clean.")
print("="*44)