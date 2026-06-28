# =============================================
#  PyPhone Emperor · Module 1
#  PRACTICE L‑05  –  Escape Sequences (Continued)
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

print("\n🎯 WELCOME TO L‑05 COACHING")
print("Quotes, backslashes, and raw strings.\n")

# TASK 1
task(
    "Create a string 'quote1' that contains double quotes inside: He said, \"Hello\".",
    lambda: check_var('quote1', str) and '"' in globals()['quote1'],
    hint="quote1 = 'He said, \"Hello\"'"
)

# TASK 2
task(
    "Create a string 'quote2' that contains a single quote inside: It's fine.",
    lambda: check_var('quote2', str) and "'" in globals()['quote2'],
    hint="quote2 = \"It's fine\""
)

# TASK 3
task(
    "Create a string 'filepath' with backslashes: C:\\Users\\Emperor.",
    lambda: check_var('filepath', str) and '\\' in globals()['filepath'],
    hint="filepath = 'C:\\\\Users\\\\Emperor'"
)

# TASK 4
task(
    "Create a raw string 'raw' that contains the literal text '\\n\\t' without newline/tab.",
    lambda: check_var('raw', str) and '\\n' in globals()['raw'],
    hint="raw = r'\\n\\t'"
)

print("\n" + "="*44)
print("🏆 L‑05 complete – Escape mastery.")
print("="*44)