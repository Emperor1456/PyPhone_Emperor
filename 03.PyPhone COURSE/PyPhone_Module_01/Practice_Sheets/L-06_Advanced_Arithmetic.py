# =============================================
#  PyPhone Emperor · Module 1
#  PRACTICE L‑06  –  Advanced Arithmetic
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

print("\n🎯 WELCOME TO L‑06 COACHING")
print("Floor division, modulus, exponentiation.\n")

# TASK 1
task(
    "Perform floor division of 17 by 5 and store the result in 'fd'.",
    lambda: check_var('fd', int, 3),
    hint="fd = 17 // 5"
)

# TASK 2
task(
    "Find the remainder of 17 divided by 5 and store in 'rem'.",
    lambda: check_var('rem', int, 2),
    hint="rem = 17 % 5"
)

# TASK 3
task(
    "Raise 2 to the power of 10 and store in 'power'.",
    lambda: check_var('power', int, 1024),
    hint="power = 2 ** 10"
)

# TASK 4
task(
    "Compute the square root of 25 using exponentiation, store in 'root'.",
    lambda: check_var('root', float, 5.0),
    hint="root = 25 ** 0.5"
)

print("\n" + "="*44)
print("🏆 L‑06 complete – Arithmetic tools sharp.")
print("="*44)