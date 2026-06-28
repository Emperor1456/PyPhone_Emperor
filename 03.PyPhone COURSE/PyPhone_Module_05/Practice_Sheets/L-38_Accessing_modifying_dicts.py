# =============================================
#  PyPhone Emperor · Module 5
#  PRACTICE L‑38  –  Accessing & Modifying Dicts
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

print("\n🎯 WELCOME TO L‑38 COACHING")
print("Add, update, remove keys safely.\n")

# TASK 1
task(
    "Start with `person = {'name': 'Emperor', 'age': 18}`. Add a new key 'city' with value 'Dhaka'.",
    lambda: check_var('person', dict) and globals().get('person') == {'name': 'Emperor', 'age': 18, 'city': 'Dhaka'},
    hint="person['city'] = 'Dhaka'"
)

# TASK 2
task(
    "Update `age` to 19 in `person`. Then store the updated dictionary back in `person` (it's already there).",
    lambda: check_var('person', dict) and globals().get('person').get('age') == 19,
    hint="person['age'] = 19"
)

# TASK 3
task(
    "Use `.update()` to change `age` to 20 and add a new key 'country'='BD' in one call.",
    lambda: check_var('person', dict) and globals().get('person').get('age') == 20 and globals().get('person').get('country') == 'BD',
    hint="person.update({'age': 20, 'country': 'BD'})"
)

# TASK 4
task(
    "Remove 'age' from `person` using `.pop()` and store its value in `removed_age`.",
    lambda: check_var('removed_age', int, 20) and 'age' not in globals().get('person', {}),
    hint="removed_age = person.pop('age')"
)

# TASK 5
task(
    "Check if 'phone' exists in `person` using `in`, and store the boolean result in `has_phone`.",
    lambda: check_var('has_phone', bool, False),
    hint="has_phone = 'phone' in person"
)

print("\n" + "="*44)
print("🏆 L‑38 complete – Modifying")
print("dictionaries is now routine.")
print("="*44)