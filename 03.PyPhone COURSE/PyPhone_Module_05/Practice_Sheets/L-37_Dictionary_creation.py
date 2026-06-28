# =============================================
#  PyPhone Emperor · Module 5
#  PRACTICE L‑37  –  Dictionary Creation
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

print("\n🎯 WELCOME TO L‑37 COACHING")
print("Create dictionaries with")
print("key‑value pairs.\n")

# TASK 1
task(
    "Create an empty dictionary called `empty`.",
    lambda: check_var('empty', dict, {}),
    hint="empty = {}"
)

# TASK 2
task(
    "Create a dict `user` with keys 'name'='Emperor', 'age'=18, 'active'=True.",
    lambda: check_var('user', dict) and globals().get('user') == {'name': 'Emperor', 'age': 18, 'active': True},
    hint="user = {'name': 'Emperor', 'age': 18, 'active': True}"
)

# TASK 3
task(
    "Create a dict `config` with 'host'='localhost', 'port'=8080, 'debug'=False using the dict() constructor.",
    lambda: check_var('config', dict) and globals().get('config') == {'host': 'localhost', 'port': 8080, 'debug': False},
    hint="config = dict(host='localhost', port=8080, debug=False)"
)

# TASK 4
task(
    "From `user`, access the name using bracket notation and store in `user_name`.",
    lambda: check_var('user_name', str, 'Emperor'),
    hint="user_name = user['name']"
)

# TASK 5
task(
    "Use `.get()` to safely retrieve the key 'phone' from `user`, defaulting to 'N/A'. Store in `phone`.",
    lambda: check_var('phone', str, 'N/A'),
    hint="phone = user.get('phone', 'N/A')"
)

print("\n" + "="*44)
print("🏆 L‑37 complete – Dictionaries")
print("now hold your structured data.")
print("="*44)