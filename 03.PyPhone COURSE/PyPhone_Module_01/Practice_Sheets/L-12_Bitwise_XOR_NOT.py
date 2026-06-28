# =============================================
#  PyPhone Emperor · Module 1
#  PRACTICE L‑12  –  Bitwise XOR & NOT
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

print("\n🎯 WELCOME TO L‑12 COACHING")
print("Bitwise XOR ^ and NOT ~.\n")

# TASK 1
task(
    "Compute 12 ^ 10, store in 'xor_result' (expect 6).",
    lambda: check_var('xor_result', int, 6),
    hint="xor_result = 12 ^ 10"
)

# TASK 2
task(
    "Compute ~5, store in 'not_result' (expect -6).",
    lambda: check_var('not_result', int, -6),
    hint="not_result = ~5"
)

# TASK 3
task(
    "Toggle a flag: start with flag=0b1010, toggle the bit at position 1 (value 2) using XOR.",
    lambda: check_var('flag', int, 0b1000),
    hint="flag ^= 2"
)

print("\n" + "="*44)
print("🏆 L‑12 complete – XOR & NOT mastered.")
print("="*44)