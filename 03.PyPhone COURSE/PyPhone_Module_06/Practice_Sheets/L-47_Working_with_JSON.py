# =============================================
#  PyPhone Emperor · Module 6
#  PRACTICE L‑47  –  Working with JSON
#  Enterprise Coaching Engine
# =============================================
import sys, os, json

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

print("\n🎯 WELCOME TO L‑47 COACHING")
print("Read and write JSON, the data")
print("exchange format of the internet.\n")

# Clean up test file
JSON_FILE = "test_user.json"
if os.path.exists(JSON_FILE):
    os.remove(JSON_FILE)

# TASK 1
task(
    "Create a dict `user` with keys 'name'='Emperor', 'age'=18, 'active'=True. Write it to 'test_user.json' using `json.dump` with `indent=4`.",
    lambda: os.path.exists(JSON_FILE) and json.load(open(JSON_FILE)) == {"name":"Emperor","age":18,"active":True},
    hint="import json\nuser = {'name':'Emperor','age':18,'active':True}\nwith open('test_user.json','w') as f:\n    json.dump(user, f, indent=4)"
)

# TASK 2
task(
    "Now read the JSON file back into a variable `loaded_user` using `json.load`.",
    lambda: check_var('loaded_user', dict) and globals().get('loaded_user') == {"name":"Emperor","age":18,"active":True},
    hint="with open('test_user.json','r') as f:\n    loaded_user = json.load(f)"
)

# TASK 3
task(
    "Convert the `loaded_user` dict to a JSON string using `json.dumps` and store in `json_str`. Then verify it contains 'Emperor'.",
    lambda: check_var('json_str', str) and "Emperor" in globals().get('json_str',''),
    hint="json_str = json.dumps(loaded_user, indent=4)"
)

print("\n" + "="*44)
print("🏆 L‑47 complete – JSON is")
print("now your data interchange tool.")
print("="*44)