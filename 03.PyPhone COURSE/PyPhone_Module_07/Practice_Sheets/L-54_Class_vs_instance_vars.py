# =============================================
#  PyPhone Emperor · Module 7
#  PRACTICE L‑54  –  Class vs Instance Variables
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

print("\n🎯 WELCOME TO L‑54 COACHING")
print("Understand class variables (shared)")
print("vs instance variables (unique).\n")

# TASK 1 – define a class with a class variable
task(
    "Define a class `Employee` with a class variable `company = 'PyPhone'` and `__init__(self, name)` that sets `self.name = name`.",
    lambda: type(globals().get('Employee')) == type and getattr(globals().get('Employee'), 'company', None) == 'PyPhone',
    hint="class Employee:\n    company = 'PyPhone'\n    def __init__(self, name):\n        self.name = name"
)

# TASK 2 – create instances and access class variable
task(
    "Create two instances `e1 = Employee('Emperor')` and `e2 = Employee('Guest')`. Then set `both_company = (e1.company, e2.company)` as a tuple.",
    lambda: check_var('both_company', tuple, ('PyPhone', 'PyPhone')),
    hint="e1 = Employee('Emperor')\ne2 = Employee('Guest')\nboth_company = (e1.company, e2.company)"
)

# TASK 3 – change class variable via class, affect all
task(
    "Change `Employee.company` to 'NewCorp'. Then set `updated = (e1.company, e2.company)`.",
    lambda: check_var('updated', tuple, ('NewCorp', 'NewCorp')),
    hint="Employee.company = 'NewCorp'\nupdated = (e1.company, e2.company)"
)

# TASK 4 – shadow class variable with instance variable
task(
    "Assign `e1.company = 'Freelance'` (this creates an instance variable). Then set `final = (e1.company, e2.company, Employee.company)`.",
    lambda: check_var('final', tuple, ('Freelance', 'NewCorp', 'NewCorp')),
    hint="e1.company = 'Freelance'\nfinal = (e1.company, e2.company, Employee.company)"
)

print("\n" + "="*44)
print("🏆 L‑54 complete – Class vs instance")
print("variables now crystal clear.")
print("="*44)