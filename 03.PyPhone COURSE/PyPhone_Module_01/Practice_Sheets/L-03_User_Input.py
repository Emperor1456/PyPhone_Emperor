# =============================================
#  PyPhone Emperor · Module 1
#  PRACTICE L‑03  –  User Input
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

print("\n🎯 WELCOME TO L‑03 COACHING")
print("You'll practice reading user input.\n")

# TASK 1
task(
    "Use input() to ask 'Enter your name: ' and store in 'name'.",
    lambda: check_var('name', str),
    hint="name = input('Enter your name: ')  (type a name when prompted)"
)

# TASK 2
task(
    "Now ask for age with input() and convert to int, store in 'age'.",
    lambda: check_var('age', int),
    hint="age = int(input('Your age: '))  (type a number)"
)

# TASK 3
task(
    "Ask for height in meters, convert to float, store in 'height'.",
    lambda: check_var('height', float),
    hint="height = float(input('Height: '))"
)

# TASK 4
task(
    "Create a variable 'year' that is age + 1 (use the age variable).",
    lambda: check_var('year', int),
    hint="year = age + 1"
)

print("\n" + "="*44)
print("🏆 L‑03 complete – Input handling ready.")
print("="*44)