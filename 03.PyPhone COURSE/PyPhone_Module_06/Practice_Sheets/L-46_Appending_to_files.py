# =============================================
#  PyPhone Emperor · Module 6
#  PRACTICE L‑46  –  Appending to Files
#  Enterprise Coaching Engine
# =============================================
import sys, os

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

print("\n🎯 WELCOME TO L‑46 COACHING")
print("Append data without erasing the past.\n")

# Setup a fresh log file
LOG_FILE = "log.txt"
if os.path.exists(LOG_FILE):
    os.remove(LOG_FILE)
# Create initial content
with open(LOG_FILE, "w") as f:
    f.write("=== System Log ===\n")

# TASK 1
task(
    "Open 'log.txt' in append mode and add the line 'First entry\\n'.",
    lambda: "First entry" in open(LOG_FILE).read(),
    hint="with open('log.txt', 'a') as f:\n    f.write('First entry\\n')"
)

# TASK 2
task(
    "Now append a list of lines: ['Second\\n', 'Third\\n'] using .writelines().",
    lambda: "Second" in open(LOG_FILE).read() and "Third" in open(LOG_FILE).read(),
    hint="lines = ['Second\\n', 'Third\\n']\nwith open('log.txt', 'a') as f:\n    f.writelines(lines)"
)

# TASK 3
task(
    "Define a function `log_event(msg)` that appends a timestamped message to 'log.txt'. Then call it with 'User logged in'. Confirm the line appears in the file.",
    lambda: callable(globals().get('log_event')) and "User logged in" in open(LOG_FILE).read(),
    hint="from datetime import datetime\ndef log_event(msg):\n    ts = datetime.now().strftime('%H:%M:%S')\n    with open('log.txt','a') as f:\n        f.write(f'[{ts}] {msg}\\n')\nlog_event('User logged in')"
)

print("\n" + "="*44)
print("🏆 L‑46 complete – Append mode")
print("builds history without loss.")
print("="*44)