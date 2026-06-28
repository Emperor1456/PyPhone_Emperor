# =============================================
#  PyPhone Emperor · Module 5
#  PRACTICE L‑41  –  Tuples
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

print("\n🎯 WELCOME TO L‑41 COACHING")
print("Tuples – immutable, ordered collections.\n")

# TASK 1
task(
    "Create a tuple `point` with two elements: 10 and 20.",
    lambda: check_var('point', tuple, (10,20)),
    hint="point = (10, 20)"
)

# TASK 2
task(
    "Create a single‑element tuple `single` containing the number 42 (remember the trailing comma).",
    lambda: check_var('single', tuple, (42,)),
    hint="single = (42,)"
)

# TASK 3
task(
    "Given `data = (100, 200, 300)`, extract the last element using negative indexing and store in `last`.",
    lambda: check_var('last', int, 300),
    hint="last = data[-1]"
)

# TASK 4
task(
    "Unpack the tuple `coords = (5,8)` into variables `x` and `y`.",
    lambda: check_var('x', int, 5) and check_var('y', int, 8),
    hint="x, y = coords"
)

# TASK 5
task(
    "Create a dictionary `locations` that uses a tuple (latitude, longitude) as a key. Add one entry: key=(40.7, -74.0) with value 'NYC'. Then store that value using the key in `city`.",
    lambda: check_var('city', str, 'NYC'),
    hint="locations = {(40.7, -74.0): 'NYC'}\ncity = locations[(40.7, -74.0)]"
)

print("\n" + "="*44)
print("🏆 L‑41 complete – Tuples")
print("are your fixed data holders.")
print("="*44)