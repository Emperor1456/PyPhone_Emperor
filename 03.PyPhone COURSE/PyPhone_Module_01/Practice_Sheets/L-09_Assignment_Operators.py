# =============================================
#  PyPhone Emperor · Module 1
#  PRACTICE L‑09  –  Assignment Operators
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

print("\n🎯 WELCOME TO L‑09 COACHING")
print("Compound assignment: +=, -=, and swapping.\n")

# TASK 1
task(
    "Start with x = 10, then add 5 to x using +=, then ensure x is 15.",
    lambda: check_var('x', int, 15),
    hint="x = 10  then  x += 5"
)

# TASK 2
task(
    "Start with y = 20, then subtract 7 using -=, ensure y is 13.",
    lambda: check_var('y', int, 13),
    hint="y = 20  then  y -= 7"
)

# TASK 3
task(
    "Swap values of a=100 and b=200 in one line.",
    lambda: check_var('a', int, 200) and check_var('b', int, 100),
    hint="a, b = b, a"
)

print("\n" + "="*44)
print("🏆 L‑09 complete – Assignment fluent.")
print("="*44)