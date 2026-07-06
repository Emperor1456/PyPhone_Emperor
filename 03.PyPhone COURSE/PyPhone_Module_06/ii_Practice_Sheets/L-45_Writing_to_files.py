# =============================================
#  PyPhone Emperor · Module 6
#  PRACTICE L‑45  –  Writing to Files
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

print("\n🎯 WELCOME TO L‑45 COACHING")
print("Write data to files using 'w' mode.\n")

# Clean up any previous test file
WRITE_FILE = "output_test.txt"
if os.path.exists(WRITE_FILE):
    os.remove(WRITE_FILE)

# TASK 1
task(
    "Create a new file 'output_test.txt' and write the string 'Hello, Emperor!\\n' to it. Use mode 'w'.",
    lambda: os.path.exists(WRITE_FILE) and open(WRITE_FILE).read() == "Hello, Emperor!\n",
    hint="with open('output_test.txt', 'w') as f:\n    f.write('Hello, Emperor!\\n')"
)

# TASK 2
task(
    "Now write a list of lines: ['Line A\\n', 'Line B\\n', 'Line C\\n'] to the same file (overwriting previous content).",
    lambda: os.path.exists(WRITE_FILE) and open(WRITE_FILE).read() == "Line A\nLine B\nLine C\n",
    hint="lines = ['Line A\\n', 'Line B\\n', 'Line C\\n']\nwith open('output_test.txt', 'w') as f:\n    f.writelines(lines)"
)

# TASK 3
task(
    "Create a dictionary `sales = {'Jan':4500, 'Feb':5200}`. Write a CSV header 'Month,Sales' and then each row to 'sales.csv'.",
    lambda: os.path.exists("sales.csv") and "Month,Sales" in open("sales.csv").read(),
    hint="with open('sales.csv', 'w') as f:\n    f.write('Month,Sales\\n')\n    for m, s in sales.items():\n        f.write(f'{m},{s}\\n')"
)

print("\n" + "="*44)
print("🏆 L‑45 complete – Writing to")
print("files is now second nature.")
print("="*44)