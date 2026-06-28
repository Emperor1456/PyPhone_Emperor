# =============================================
#  PyPhone Emperor · Module 7
#  PRACTICE L‑52  –  `__init__` Constructor
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

print("\n🎯 WELCOME TO L‑52 COACHING")
print("Master the `__init__` constructor.\n")

# TASK 1
task(
    "Define a class `User` with `__init__(self, name, age)` that sets `self.name` and `self.age`.",
    lambda: callable(getattr(globals().get('User'), '__init__', None)),
    hint="class User:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age"
)

# TASK 2
task(
    "Create an instance `u1 = User('Emperor', 18)` and verify its attributes.",
    lambda: check_var('u1', object) and hasattr(globals().get('u1'), 'name') and globals()['u1'].name == 'Emperor' and globals()['u1'].age == 18,
    hint="u1 = User('Emperor', 18)"
)

# TASK 3
task(
    "Define a class `Product` with `__init__(self, name, price=0.0)` to set name and price. Then create `p = Product('Laptop', 799.99)`.",
    lambda: check_var('p', object) and hasattr(globals().get('p'), 'name') and globals()['p'].price == 799.99,
    hint="class Product:\n    def __init__(self, name, price=0.0):\n        self.name = name\n        self.price = price\n\np = Product('Laptop', 799.99)"
)

# TASK 4
task(
    "Create another instance `p2 = Product('Mouse')` (using default price) and check its price is 0.0.",
    lambda: check_var('p2', object) and globals().get('p2').price == 0.0,
    hint="p2 = Product('Mouse')"
)

# TASK 5
task(
    "Define a class `Group` with `__init__(self, members=None)` that sets `self.members = members if members is not None else []`. Then create `g = Group()` and append 'Emperor' to its members list.",
    lambda: check_var('g', object) and globals().get('g').members == ['Emperor'],
    hint="class Group:\n    def __init__(self, members=None):\n        self.members = members if members is not None else []\n\ng = Group()\ng.members.append('Emperor')"
)

print("\n" + "="*44)
print("🏆 L‑52 complete – `__init__`")
print("constructs your objects safely.")
print("="*44)