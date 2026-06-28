# =============================================
#  PyPhone Emperor · Module 1
#  PRACTICE L‑13  –  Bitwise Shifts
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

print("\n🎯 WELCOME TO L‑13 COACHING")
print("Left shift << and right shift >>.\n")

# TASK 1
task(
    "Compute 1 << 5, store in 'left_shift' (expect 32).",
    lambda: check_var('left_shift', int, 32),
    hint="left_shift = 1 << 5"
)

# TASK 2
task(
    "Compute 64 >> 2, store in 'right_shift' (expect 16).",
    lambda: check_var('right_shift', int, 16),
    hint="right_shift = 64 >> 2"
)

# TASK 3
task(
    "Pack RGB: red=100, green=150, blue=200 into a single integer using shifts and OR.",
    lambda: check_var('packed', int, (100<<16)|(150<<8)|200),
    hint="packed = (red << 16) | (green << 8) | blue"
)

print("\n" + "="*44)
print("🏆 L‑13 complete – Shifts locked.")
print("="*44)