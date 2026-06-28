# =============================================
#  PyPhone Emperor · Module 1
#  PRACTICE L‑10  –  Compound Assignments (All)
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

print("\n🎯 WELCOME TO L‑10 COACHING")
print("All compound operators: *=, /=, //=, %=, **=.\n")

# TASK 1
task(
    "Start with n=5, multiply by 4 using *=, ensure n is 20.",
    lambda: check_var('n', int, 20),
    hint="n = 5  then  n *= 4"
)

# TASK 2
task(
    "Start with n=20, divide by 3 using /=, ensure n is approx 6.666...",
    lambda: check_var('n', float) and abs(globals()['n'] - 6.6666666667) < 0.1,
    hint="n /= 3"
)

# TASK 3
task(
    "Start with n=20, floor divide by 3 using //=, ensure n is 6.",
    lambda: check_var('n', int, 6),
    hint="n //= 3"
)

# TASK 4
task(
    "Start with n=17, modulus 5 using %=, ensure n is 2.",
    lambda: check_var('n', int, 2),
    hint="n %= 5"
)

# TASK 5
task(
    "Start with n=2, raise to power 5 using **=, ensure n is 32.",
    lambda: check_var('n', int, 32),
    hint="n **= 5"
)

print("\n" + "="*44)
print("🏆 L‑10 complete – Full compound toolkit.")
print("="*44)