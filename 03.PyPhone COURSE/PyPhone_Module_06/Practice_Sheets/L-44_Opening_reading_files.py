# =============================================
#  PyPhone Emperor · Module 6
#  PRACTICE L‑44  –  Opening & Reading Files
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

print("\n🎯 WELCOME TO L‑44 COACHING")
print("Read data from files safely.\n")

# Create a test file for the user
TEST_FILE = "test_read.txt"
if not os.path.exists(TEST_FILE):
    with open(TEST_FILE, "w") as f:
        f.write("Line 1\nLine 2\nLine 3\n")

# TASK 1
task(
    "Open 'test_read.txt' using `with` and read the entire content into a variable `content`.",
    lambda: check_var('content', str) and 'Line 1' in globals().get('content',''),
    hint="with open('test_read.txt','r') as f:\n    content = f.read()"
)

# TASK 2
task(
    "Open the same file and read all lines into a list `lines` using `.readlines()`. Then store the first line (with newline stripped) in `first_line`.",
    lambda: check_var('first_line', str, 'Line 1'),
    hint="with open('test_read.txt','r') as f:\n    lines = f.readlines()\nfirst_line = lines[0].strip()"
)

# TASK 3
task(
    "Open the file and iterate over it line by line. Count how many lines contain 'Line' and store the count in `line_count`.",
    lambda: check_var('line_count', int, 3),
    hint="line_count = 0\nwith open('test_read.txt','r') as f:\n    for line in f:\n        if 'Line' in line:\n            line_count += 1"
)

print("\n" + "="*44)
print("🏆 L‑44 complete – File reading")
print("is now a safe habit.")
print("="*44)