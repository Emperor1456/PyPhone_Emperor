# =============================================
#  PyPhone Emperor · Module 2
#  PRACTICE L‑17  –  Nested Conditionals
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

print("\n🎯 WELCOME TO L‑17 COACHING")
print("Nest `if` blocks to test")
print("conditions inside conditions.\n")

# TASK 1
task(
    "Set `is_logged_in = True` and `is_admin = False`. Write a nested `if` that sets `access = 'full'` only if both are True, else set `access = 'limited'` (outer True but inner False).",
    lambda: check_var('access', str, 'limited'),
    hint="if is_logged_in:\n    if is_admin:\n        access = 'full'\n    else:\n        access = 'limited'\nelse:\n    access = 'none'"
)

# TASK 2
task(
    "Given `age = 22`, `has_license = True`, and `is_banned = False`. Write a nested `if` that sets `can_drive` to True only if all three conditions are met; otherwise False. Use two levels: outer for age>=18, inner for has_license and not is_banned.",
    lambda: check_var('can_drive', bool, True),
    hint="if age >= 18:\n    if has_license and not is_banned:\n        can_drive = True\n    else:\n        can_drive = False\nelse:\n    can_drive = False"
)

# TASK 3
task(
    "Given `member = True`, `purchase = 150`. Write a nested `if` that sets `discount = 0.2` if member and purchase > 100; if member but purchase <= 100, discount = 0.1; if not member, discount = 0.0.",
    lambda: abs(globals().get('discount', 0) - 0.2) < 0.001,
    hint="if member:\n    if purchase > 100:\n        discount = 0.2\n    else:\n        discount = 0.1\nelse:\n    discount = 0.0"
)

print("\n" + "="*44)
print("🏆 L‑17 complete – Nested")
print("conditions feel natural now.")
print("="*44)