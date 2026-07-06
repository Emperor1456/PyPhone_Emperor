# =============================================
#  PyPhone Emperor · Module 4
#  PRACTICE L‑32  –  Default Parameters
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

print("\n🎯 WELCOME TO L‑32 COACHING")
print("Default parameters make functions")
print("flexible and backward‑compatible.\n")

# TASK 1
task(
    "Define a function `greet` with a default parameter `name='Guest'` that returns 'Hello, {name}!'.",
    lambda: callable(globals().get('greet')) and globals()['greet']() == 'Hello, Guest!' and globals()['greet']('Emperor') == 'Hello, Emperor!',
    hint="def greet(name='Guest'):\n    return f'Hello, {name}!'"
)

# TASK 2
task(
    "Define a function `power` with parameters `base` and `exponent=2` that returns base**exponent.",
    lambda: callable(globals().get('power')) and globals()['power'](5) == 25 and globals()['power'](2, 3) == 8,
    hint="def power(base, exponent=2):\n    return base ** exponent"
)

# TASK 3
task(
    "Define a function `add_item` that takes an item and a list (default None). If list is None, create an empty list. Append the item and return the list. (Solve the mutable default pitfall.)",
    lambda: callable(globals().get('add_item')) and globals()['add_item'](1) == [1] and globals()['add_item'](2) == [2],
    hint="def add_item(item, items=None):\n    if items is None:\n        items = []\n    items.append(item)\n    return items"
)

# TASK 4
task(
    "Define a function `create_user` with parameters `username`, `role='user'`, `active=True`. Return a dict with these keys and values.",
    lambda: callable(globals().get('create_user')) and globals()['create_user']('admin1', role='admin') == {'username': 'admin1', 'role': 'admin', 'active': True},
    hint="def create_user(username, role='user', active=True):\n    return {'username': username, 'role': role, 'active': active}"
)

print("\n" + "="*44)
print("🏆 L‑32 complete – Default")
print("parameters mastered safely.")
print("="*44)