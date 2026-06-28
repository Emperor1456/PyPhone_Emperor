# =============================================
#  PyPhone Emperor · Module 2
#  PRACTICE L‑16  –  `if-elif-else` Chain
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

print("\n🎯 WELCOME TO L‑16 COACHING")
print("Build multi‑branch chains with")
print("`if-elif-else`.\n")

# TASK 1
task(
    "Start with `score = 82`. Use `if-elif-else` to set `grade` to 'A' (>=90), 'B' (>=80), 'C' (>=70), else 'F'.",
    lambda: check_var('grade', str, 'B'),
    hint="if score >= 90:\n    grade = 'A'\nelif score >= 80:\n    grade = 'B'\nelif score >= 70:\n    grade = 'C'\nelse:\n    grade = 'F'"
)

# TASK 2
task(
    "Given `quantity = 75`, use `if-elif-else` to set `price` to 8 (>=100), 9 (>=50), 10 (>=10), else 12.",
    lambda: check_var('price', int, 9),
    hint="if quantity >= 100:\n    price = 8\nelif quantity >= 50:\n    price = 9\nelif quantity >= 10:\n    price = 10\nelse:\n    price = 12"
)

# TASK 3
task(
    "Given `age = 65`, set `category` to 'Child' (<13), 'Teen' (13-19), 'Adult' (20-59), 'Senior' (>=60).",
    lambda: check_var('category', str, 'Senior'),
    hint="if age < 13:\n    category = 'Child'\nelif age <= 19:\n    category = 'Teen'\nelif age <= 59:\n    category = 'Adult'\nelse:\n    category = 'Senior'"
)

# TASK 4
task(
    "Given `income = 45000`, set `tax_rate` to 0.1 (<20000), 0.2 (<50000), 0.3 (<100000), else 0.4.",
    lambda: check_var('tax_rate', float, 0.2),
    hint="if income < 20000:\n    tax_rate = 0.1\nelif income < 50000:\n    tax_rate = 0.2\nelif income < 100000:\n    tax_rate = 0.3\nelse:\n    tax_rate = 0.4"
)

print("\n" + "="*44)
print("🏆 L‑16 complete – `if-elif-else`")
print("chains mastered.")
print("="*44)