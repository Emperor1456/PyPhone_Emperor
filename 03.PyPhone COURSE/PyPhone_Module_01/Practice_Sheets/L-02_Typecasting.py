# =============================================
#  PyPhone Emperor · Module 1
#  PRACTICE L‑02  –  Typecasting
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

print("\n🎯 WELCOME TO L‑02 COACHING")
print("Complete each task by writing Python code.\n")

# TASK 1
task(
    "Convert the string '100' to an integer and store in variable 'num'.",
    lambda: check_var('num', int, 100),
    hint="num = int('100')"
)

# TASK 2
task(
    "Convert the string '3.14' to a float and store in 'pi'.",
    lambda: check_var('pi', float, 3.14),
    hint="pi = float('3.14')"
)

# TASK 3
task(
    "Take an integer variable 'age' = 18 and create a string 'age_str' from it.",
    lambda: check_var('age_str', str, '18'),
    hint="age_str = str(age)"
)

# TASK 4
task(
    "Create a variable 'raw' with the string '42'. Then create 'num2' by converting 'raw' to int.",
    lambda: check_var('num2', int, 42),
    hint="raw = '42'  then  num2 = int(raw)"
)

print("\n" + "="*44)
print("🏆 L‑02 complete – Typecasting mastered.")
print("="*44)