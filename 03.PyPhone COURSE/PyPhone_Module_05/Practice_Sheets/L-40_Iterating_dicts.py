# =============================================
#  PyPhone Emperor · Module 5
#  PRACTICE L‑40  –  Iterating Through Dicts
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

print("\n🎯 WELCOME TO L‑40 COACHING")
print("Loop over dictionaries like a pro.\n")

# TASK 1
task(
    "Create `scores = {'Ana':85, 'Bob':92, 'Emperor':78}`. Write a `for` loop that prints each key. Then set `done1 = True`.",
    lambda: check_var('done1', bool, True),
    hint="for k in scores:\n    print(k)\ndone1 = True"
)

# TASK 2
task(
    "Write a loop that prints each value in `scores`. Then set `done2 = True`.",
    lambda: check_var('done2', bool, True),
    hint="for v in scores.values():\n    print(v)\ndone2 = True"
)

# TASK 3
task(
    "Using `.items()`, create a new dictionary `high_scorers` containing only entries with score >= 80 from `scores`.",
    lambda: check_var('high_scorers', dict) and globals().get('high_scorers') == {'Ana':85, 'Bob':92},
    hint="high_scorers = {}\nfor k, v in scores.items():\n    if v >= 80:\n        high_scorers[k] = v"
)

# TASK 4
task(
    "Create a list `words = ['apple','banana','apple','cherry']`. Build a dictionary `count` that counts each word using a loop and `.get()`.",
    lambda: check_var('count', dict) and globals().get('count') == {'apple':2, 'banana':1, 'cherry':1},
    hint="count = {}\nfor w in words:\n    count[w] = count.get(w, 0) + 1"
)

print("\n" + "="*44)
print("🏆 L‑40 complete – Dict iteration")
print("is now second nature.")
print("="*44)