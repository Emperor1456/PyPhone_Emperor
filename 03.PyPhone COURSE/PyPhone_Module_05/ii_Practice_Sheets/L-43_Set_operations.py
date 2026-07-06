# =============================================
#  PyPhone Emperor · Module 5
#  PRACTICE L‑43  –  Set Operations
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

print("\n🎯 WELCOME TO L‑43 COACHING")
print("Union, intersection, difference –")
print("set operations made easy.\n")

# TASK 1
task(
    "Create set `a = {1,2,3}` and `b = {3,4,5}`. Compute the union using `|` and store in `union_set`.",
    lambda: check_var('union_set', set, {1,2,3,4,5}),
    hint="union_set = a | b"
)

# TASK 2
task(
    "Compute the intersection of `a` and `b` using `&` and store in `inter_set`.",
    lambda: check_var('inter_set', set, {3}),
    hint="inter_set = a & b"
)

# TASK 3
task(
    "Compute the difference `a - b` (elements in `a` but not `b`) and store in `diff_set`.",
    lambda: check_var('diff_set', set, {1,2}),
    hint="diff_set = a - b"
)

# TASK 4
task(
    "Compute the symmetric difference of `a` and `b` using `^` and store in `sym_set`.",
    lambda: check_var('sym_set', set, {1,2,4,5}),
    hint="sym_set = a ^ b"
)

# TASK 5
task(
    "Check if `{1,2}` is a subset of `{1,2,3}` and store the boolean result in `is_sub`.",
    lambda: check_var('is_sub', bool, True),
    hint="is_sub = {1,2}.issubset({1,2,3})"
)

print("\n" + "="*44)
print("🏆 L‑43 complete – Set operations")
print("are now in your mathematical toolkit.")
print("="*44)